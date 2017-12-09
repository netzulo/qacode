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
        HtmlTag.TAG_FIELDSET.valueT
    ]

    #TODO: follow instructions on #63
    def __init__(self, bot, selector='', locator=By.CSS_SELECTOR,
                 element=None, search=True, strict_mode=False):
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

        :args:
            strict_mode: allows to raise validation when
             warning it's received
        """
        super(ControlForm, self).__init__(
            bot,
            selector=selector,
            locator=locator,
            element=element,
            search=search)
        if search:
            self._validate_tag(strict_mode=strict_mode)

    def _validate_tag(self, strict_mode=False):
        """
        Validate self.tag property is in valid_tags array
         and load by tag each validation
        :args:
            strict_mode: allows to raise validation when
             warning it's received
        """
        msg_err_tag = "Tag invalid for ControlForm class: tag={}"
        if self.tag not in self.VALID_TAGS:
            raise ControlException(
                message=msg_err_tag.format(self.tag))
        if self.tag == HtmlTag.TAG_LABEL.value:
            self._tag_label(strict_mode=strict_mode)
        if self.tag == HtmlTag.TAG_INPUT.value:
            # TODO: self._tag_input(strict_mode=strict_mode)
            pass
        if self.tag == HtmlTag.TAG_BUTTON.value:
            # TODO: self._tag_button(strict_mode=strict_mode)
            pass


    def _tag_label(self, strict_mode=False):
        """
        Initialize ControlForm with tag <label>
         must validate attrs= id, class, for
         error: if not exist element with id for for attr value HTML warn
         warn: if not have css property cursor:default usability warn
        :args:
            strict_mode: allows to raise validation when
             warning it's received
        :return:
            True if validation ok or if strict_mode and have warnings
            False if validation have error
        """
        raise NotImplementedError("Must code more here...")
