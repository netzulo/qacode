# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_form"""


from qacode.core.exceptions.control_exception import ControlException
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.loggers import logger_messages as MSG
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.controls.control_form import ControlForm
from selenium.common.exceptions import WebDriverException


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
        strict_rules = kwargs.get("strict_rules")
        if not bool(strict_rules):
            strict_rules.append(
                {"tag": "table", "type": "tag", "severity": "hight"})
        super(ControlTable, self).__init__(bot, **kwargs)
        if not self.IS_TABLE and self.tag is not None:
            raise ControlException(msg=MSG.CT_BADTAG)
        self.bot.log.debug(MSG.CT_LOADED)

    def __load_table__(self, element=None):
        """Allow to load all TR > TD items from a TABLE element

        Before structure some checks are necessary for some children elements:
            caption {ControlBase}-- optional <caption> element

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
        self.tbodies = self.__try__("find_children", "tbodies")
        is_html5 = False
        if bool(self.tbodies):
            is_html5 = True
            self.caption = self.__try__("find_child", "caption")
            self.thead = self.__try__("find_child", "thead")
            self.tfoot = self.__try__("find_child", "tfoot")
        # Load column headers
        if not is_html5:
            columns = self._table.find_children("tr :not(td)")  # noqa
            for column in columns:
                column.name = column.text
            rows = []
            ctls_rows = self._table.find_children("tr")
            for index, ctl_row in enumerate(ctls_rows):
                if index == 0:
                    rows.append(self.__get_row__(ctl_row, "th"))
                else:
                    rows.append(self.__get_row__(ctl_row, "td"))
            self._rows = rows
        else:
            # is_hmtl5==True
            # raise NotImplementedError("TODO: WIP zone")
            pass
        # raise NotImplementedError("TODO: WIP zone")

    def __get_row__(self, ctl_row, selector):
        """WARNING: this method just can be used from __load_table__"""
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
        if value is None or not isinstance(value, ControlBase):
            raise ControlException("Can't set not 'Control' instance")
        self.__load_table__(element=value)

    @property
    def rows(self):
        """GETTER for 'rows' property"""
        return self._rows
