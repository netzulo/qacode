# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_form"""


from qacode.core.exceptions.control_exception import ControlException
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.loggers import logger_messages as MSG
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.controls.control_form import ControlForm
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.remote.webelement import WebElement


class ControlTable(ControlForm):
    """TODO: doc class"""

    _table = None
    _rows = None

    # public properties

    caption = None
    thead = None
    tfoot = None
    tbodies = None

    def __init__(self, bot, **kwargs):
        """Instance of ControlForm. Load properties from settings dict.
            Some elements need to search False to be search at future
        """
        kwargs.update({"instance": "ControlTable"})
        strict_rules = kwargs.get("strict_rules") or []
        if not bool(strict_rules):
            strict_rules.append(
                {"tag": "table", "type": "tag", "severity": "hight"})
            kwargs.update({"strict_rules": strict_rules})
        super(ControlTable, self).__init__(bot, **kwargs)
        if not self.IS_TABLE and self.tag is not None:
            raise ControlException(msg=MSG.CT_BADTAG)
        self.bot.log.debug(MSG.CT_LOADED)

    def __load_table__(self, element=None):
        """Allow to load all TR > TD items from a TABLE element

        Before structure some checks are necessary for some children elements:
            tbody {ControlBase}-- required 1 or more <tbody> elements
            caption {ControlBase}-- optional <caption> element if tbody found
            thead {ControlBase}-- optional <thead> element if tbody found
            tfoot {ControlBase}-- optional <tfoot> element if tbody found

        Examples:
            Use case 1. TABLE > (TR > TH)+(TR > TD)
            Use case 2. TABLE > (THEAD > (TR > TH))+(TBODY > (TR > TH))
        """
        if element is None:
            element = self.element
        self._table = ControlBase(self.bot, **{
            "selector": self.selector,
            "element": element})
        # Preload
        self.tbodies = self.__try__("find_children", "tbody")
        if bool(self.tbodies):
            self._rows = self.__load_table_html5__()
        else:
            self._rows = self.__load_table_html4__()

    def __load_table_html4__(self):
        """Allow to load table with this structure
            TABLE > (TR > TH)+(TR > TD)
        """
        rows = []
        ctls_rows = self._table.find_children("tr")
        for index, ctl_row in enumerate(ctls_rows):
            if index == 0:
                rows.append(self.__get_row__(ctl_row, "th"))
            else:
                rows.append(self.__get_row__(ctl_row, "td"))
        return rows

    def __load_table_html5__(self):
        """Allow to load table with this structure
            TABLE > (THEAD > (TR > TH))+(TBODY > (TR > TH))
        """
        self.caption = self.__try__("find_child", "caption")
        self.thead = self.__try__("find_child", "thead")
        self.tfoot = self.__try__("find_child", "tfoot")
        if len(self.tbodies) > 1:
            raise ControlException(MSG.CT_TBL2ORMORETBODIES)
        rows = []
        if self.thead is not None:
            rows.append(self.__get_row__(self.thead.find_child("tr"), "th"))
        for ctl_row in self.tbodies[0].find_children("tr"):
            rows.append(self.__get_row__(ctl_row, "td"))
        return rows

    def __get_row__(self, ctl_row, selector):
        """Allow to get cells of a <TR> element
            WARNING: this method just can be used from __load_table__
        """
        row = []
        for cell in ctl_row.find_children(selector):
            text = cell.get_text()
            cell.settings.update({"name": text})
            cell.name = text
            row.append(cell)
        return row

    def __try__(self, method, selector):
        """Allow to exec some method to handle exception"""
        try:
            return getattr(self._table, method)(selector)
        except (ControlException, CoreException, WebDriverException):
            self.bot.log.debug(MSG.CT_TBLNOTCHILD.format(selector))
            return None

    def __check_reload__form__(self):
        """Allow to check before methods calls to ensure
            if it's neccessary reload element properties
        """
        super(ControlTable, self).__check_reload__form__()
        reload_needed = not self.element or not self.table
        if reload_needed:
            self.reload(**self.settings)
        if not self.IS_TABLE and self.tag is not None:
            raise ControlException(msg=MSG.CT_BADTAG)

    def reload(self, **kwargs):
        """Reload 'self.settings' property:dict and call to instance
            logic with new configuration
        """
        super(ControlTable, self).reload(**kwargs)
        self.__load_table__(element=self.element)

    @property
    def table(self):
        """GETTER for 'table' property"""
        return self._table

    @table.setter
    def table(self, value):
        """SETTER for 'table' property"""
        if value is None or not isinstance(value, WebElement):
            raise ControlException("Can't set not 'WebElement' instance")
        self.__load_table__(element=value)

    @property
    def rows(self):
        """GETTER for 'rows' property"""
        self.__check_reload__form__()
        return self._rows
