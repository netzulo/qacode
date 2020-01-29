# -*- coding: utf-8 -*-
"""Package module qacode.core.webs.control_dropdown"""


from qacode.core.exceptions.control_exception import ControlException
from qacode.core.loggers import logger_messages as MSG
from qacode.core.webs.controls.control_base import ControlBase
from selenium.webdriver.support.ui import Select


class ControlDropdown(ControlBase):
    """TODO: doc class"""

    def __init__(self, bot, **kwargs):
        """Instance of ControlDropdown. Load properties from settings dict.
            Some elements need to search False to be search at future
        """
        super(ControlDropdown, self).__init__(bot, **kwargs)
        self._dropdown = None

    def __load__(self, **kwargs):
        """Allow to reinstance control properties"""
        super(ControlDropdown, self).__load__(**kwargs)
        if self._on_instance_search:
            self._dropdown = Select(self._element)

    def __check_dropdown__(self, text, by_value=False, by_index=False):
        """Internal funcionality for select/deselect methods"""
        if not self._element or not self._dropdown:
            self.reload(**self._settings)
        if self._dropdown is None:
            raise ControlException(MSG.CDD_BADTAG, info_bot=self._info_bot)
        if by_value and by_index:
            raise ControlException(MSG.CDD_BADPARAMS, info_bot=self._info_bot)
        if by_index and not isinstance(text, int):
            raise ControlException(
                MSG.CDD_BADINDEXTYPE, info_bot=self._info_bot)

    def reload(self, **kwargs):
        """Reload 'self.settings' property:dict and call to instance
            logic with new configuration
        """
        super(ControlDropdown, self).reload(**kwargs)
        self._dropdown = Select(self.element)

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

    @property
    def dropdown(self):
        """GET for _dropdown attribute"""
        return self._dropdown

    @dropdown.setter
    def dropdown(self, value):
        """SET for _dropdown attribute"""
        # if not isinstance(value, Select):
        #    raise ControlException("Dropdown must be a type == Select")
        self._dropdown = value
