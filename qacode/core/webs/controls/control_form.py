# -*- coding: utf-8 -*-
# pylint: disable=too-many-arguments
""""TODO: doc module"""


from selenium.webdriver.common.by import By
from qacode.core.exceptions.control_exception import ControlException
from qacode.core.webs.controls.control_base import ControlBase
from qacode.core.webs.html_tags import HtmlTag


class ControlForm(ControlBase):
    """Requirements: #63"""

    VALID_TAGS = [
        HtmlTag.TAG_LABEL.value,
        HtmlTag.TAG_INPUT.value,
        HtmlTag.TAG_SELECT.value,
        HtmlTag.TAG_TEXTAREA.value,
        HtmlTag.TAG_DATALIST.value,
        HtmlTag.TAG_OUTPUT.value,
        HtmlTag.TAG_FORM.value,
        HtmlTag.TAG_LEGEND.value,
        HtmlTag.TAG_FIELDSE.valueT
    ]

    #TODO: follow instructions on #63
    def __init__(self, bot, selector='', locator=By.CSS_SELECTOR,
                 element=None, search=True):
        """
        Apply for elements tagged with
        <label> : must validate attrs= id, class, for
        <input> : must validate attrs= id, class
        <select> + <option> : must validate attrs= id, class
        <textarea> : must validate attrs= id, class
        <datalist> + <option> : must validate attrs= id, class
        <output> : must validate attrs= id, class
        Apply also on parent elements
        <form> : must validate attrs= id, class
        <legend> : must validate attrs= id, class
        <fieldset> : must validate attrs= id, class
        """
        super(ControlForm, self).__init__(
            bot,
            selector=selector,
            locator=locator,
            element=element,
            search=search)
        if search:
            if self.tag in self.VALID_TAGS:
                raise NotImplementedError("Still not working, see #63")
