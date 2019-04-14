# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_form"""


from qacode.core.exceptions.control_exception import ControlException
from qacode.core.loggers import logger_messages as MSG
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.controls.control_form import ControlForm


class ControlTable(ControlForm):
    """TODO: doc class"""

    _table = None

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
        self.bot.log.debug(MSG.CDD_LOADED)

    def __load_table__(self, element=None):
        """Allow to load all TR > TD items from a TABLE element

        Examples:
            Use case 1. TABLE > (TR > TH)+(TR > TD)
            Use case 2. TABLE > (THEAD > (TR > TH))+(TBODY > (TR > TH))
        """
        if element is None:
            element = self.element
        self._table = ControlBase(self.bot, **{
            "selector": self.selector,
            "element": element})
        # Load rows
        # thead = self._table.find_child("thead")
        # tbody = self._table.find_child("tbody")
        # Load columns
        # Load cells
        # raise NotImplementedError("TODO: WIP zone")

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
