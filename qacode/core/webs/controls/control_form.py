# -*- coding: utf-8 -*-
# pylint: disable=too-many-arguments
""""TODO: doc module"""


from enum import Enum
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
        HtmlTag.TAG_FIELDSET.value
    ]

    # TODO: follow instructions on #63
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
        msg_not_found_for = "Element '{}' not found for '{}' attr 'for' value"
        msg_not_attr = "Element '{}', not attr '{}' detected"
        msg_not_css = "Element '{}', not css '{}' with value '{}' detected"
        msg = "**{}** {}: {}"
        if strict_mode:
            msg.format('ERROR', '{}', '{}')
        else:
            msg.format('WARN', '{}', '{}')
        # load attrs
        self.attr_for = self.get_attr_value('for')
        self.attr_name = self.get_attr_value('name')
        # load css
        # TODO: will fail, NotImplemented
        self.css_cursor = self.get_css_value('cursor')
        # warnings and errors
        self._log_rule('name', msg.format(
            MessageType.USABILITY,
            msg_not_attr.format(self.selector, 'name')))

        is_for_attr = self._log_rule('for', msg.format(
            MessageType.BEHAVIOUR,
            msg_not_attr.format(self.selector, 'for')))
        if is_for_attr:
            try:
                selector_id = '#{}'.format(self.attr_for)
                ControlBase(self.bot, selector=selector_id)
            except Exception:
                raise ControlException(
                    message=msg_not_found_for.format(
                        selector_id, self.selector))
        if self.css_cursor is None or self.css_cursor != 'default':
            self._log_rule('cursor', msg.format(
                MessageType.USABILITY,
                msg_not_css.format(self.selector, 'cursor', 'default')))

    def _log_rule(self, attr, msg, strict_mode=False):
        """
        Log to logger by strict_mode type
        :return:
            returns is_attr variable value
        """
        is_attr = False
        if attr is None or attr == '':
            if strict_mode:
                self.bot.log.error(msg)
            else:
                self.bot.log.warning(msg)
        else:
            self.bot.log.info(
                "ControlForm, attr found : {}".format(attr))
            is_attr = True
        return is_attr


class MessageType(Enum):
    """
    Just message type enum for warning and errors
     on control form class
    """

    BEHAVIOUR = 'BEHAVIOUR'
    USABILITY = 'USABILITY'
    SEO = 'SEO'

    @classmethod
    def get_attr(cls):
        """return enum values"""
        return [item.value for item in MessageType]

    @classmethod
    def has_attr(cls, value):
        """returns True if enum have value"""
        return any(value == item.value for item in cls)
