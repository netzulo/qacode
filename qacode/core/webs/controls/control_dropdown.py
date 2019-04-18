# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_form"""


from qacode.core.exceptions.control_exception import ControlException
from qacode.core.loggers import logger_messages as MSG
from qacode.core.webs.controls.control_form import ControlForm
from selenium.webdriver.support.ui import Select


class ControlDropdown(ControlForm):
    """TODO: doc class"""

    dropdown = None

    def __init__(self, bot, **kwargs):
        """Instance of ControlForm. Load properties from settings dict.
            Some elements need to search False to be search at future
        """
        kwargs.update({"instance": "ControlDropdown"})
        strict_rules = kwargs.get("strict_rules") or []
        if not bool(strict_rules):
            strict_rules.append(
                {"tag": "select", "type": "tag", "severity": "hight"})
            kwargs.update({"strict_rules": strict_rules})
        super(ControlDropdown, self).__init__(bot, **kwargs)
        if not self.IS_DROPDOWN and self.tag is not None:
            raise ControlException(msg=MSG.CDD_BADTAG)
        self.bot.log.debug(MSG.CDD_LOADED)

    def __check_reload__form__(self):
        """Allow to check before methods calls to ensure
            if it's neccessary reload element properties
        """
        super(ControlDropdown, self).__check_reload__form__()
        reload_needed = not self.element or not self.dropdown
        if reload_needed:
            self.reload(**self.settings)

    def reload(self, **kwargs):
        """Reload 'self.settings' property:dict and call to instance
            logic with new configuration
        """
        super(ControlDropdown, self).reload(**kwargs)
        self.dropdown = Select(self.element)

    def __check_dropdown__(self, text, by_value=False, by_index=False):
        """Internal funcionality for select/deselect methods"""
        self.__check_reload__form__()
        if self.dropdown is None:
            raise ControlException(msg=MSG.CDD_BADTAG)
        if by_value and by_index:
            raise ControlException(msg=MSG.CDD_BADPARAMS)
        if by_index and not isinstance(text, int):
            raise ControlException(msg=MSG.CDD_BADINDEXTYPE)

    def select(self, text, by_value=False, by_index=False):
        """The Select class only works with tags which have select tags.
            Using the Index of Dropdown (int)
            Using the Value of Dropdown (str)
            Using the Text of Dropdown (str)

        Arguments:
            text {str|int} -- Probably the easiest way of doing it. You
                have to match the text which is displayed in the drop down.

        Keyword Arguments:
            by_value {bool} -- We can use to select an option using the
                value attribute. (default: {False})
            by_index {bool} -- We can use to select an option using the
                index attribute. (default: {False})

        Raises:
            ControlException -- if tag is not 'select'
            ControlException -- if all flags are 'True'
        """
        self.__check_dropdown__(
            text, by_value=by_value, by_index=by_index)
        self.bot.log.debug(MSG.CDD_SELECT_LOADING)
        if by_value:
            self.dropdown.select_by_value(text)
        elif by_index:
            self.dropdown.select_by_index(int(text))
        else:
            self.dropdown.select_by_visible_text(text)
        self.bot.log.debug(MSG.CDD_SELECT_LOADED)

    def deselect(self, text, by_value=False, by_index=False):
        """The Select class only works with tags which have select tags.
            Using the Index of Dropdown (int)
            Using the Value of Dropdown (str)
            Using the Text of Dropdown (str)

        Arguments:
            text {str|int} -- Probably the easiest way of doing it. You
                have to match the text which is displayed in the drop down.

        Keyword Arguments:
            by_value {bool} -- We can use to select an option using the
                value attribute. (default: {False})
            by_index {bool} -- We can use to select an option using the
                index attribute. (default: {False})

        Raises:
            ControlException -- if tag is not 'select'
            ControlException -- if all flags are 'True'
        """
        self.bot.log.debug(MSG.CDD_SELECT_LOADING)
        self.__check_dropdown__(
            text, by_value=by_value, by_index=by_index)
        if by_value:
            self.dropdown.deselect_by_value(text)
        elif by_index:
            self.dropdown.deselect_by_index(int(text))
        else:
            self.dropdown.deselect_by_visible_text(text)
        self.bot.log.debug(MSG.CDD_DESELECTALL_LOADING)

    def deselect_all(self):
        """The Select class only works with tags which have select
            tags with multiple="multiple" attribute.

        Raises:
            ControlException -- if tag is not 'select'
        """
        self.bot.log.debug(MSG.CDD_DESELECTALL_LOADING)
        self.__check_dropdown__('')
        self.dropdown.deselect_all()
        self.bot.log.debug(MSG.CDD_DESELECTALL_LOADED)
