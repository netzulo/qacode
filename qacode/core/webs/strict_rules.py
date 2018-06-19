# -*- coding: utf-8 -*-
"""TODO: doc module"""


from qacode.core.enums.enum_base import EnumBase
from qacode.core.exceptions.core_exception import CoreException
from qacode.core.webs.css_properties import CssProperty
from qacode.core.webs.html_attrs import HtmlAttr
from qacode.core.webs.html_tags import HtmlTag


class StrictRule(object):
    """Strict Rule for an element"""

    name = None
    enum_type = None
    strict_type = None
    severity = None
    strict_log = None

    def __init__(self, name, strict_type, severity):
        """Class to allows include validation checks when loading elements
            using qacode library through selenium core

        Arguments:
            strict_type {StrictType} -- type of rule
            severity {StrictSeverity} -- severity of rule
                (for logging messages)
        """
        if name is None:
            raise CoreException(
                message="bad param 'name' can't be None")
        if isinstance(name, (HtmlTag, HtmlAttr, CssProperty)):
            self.name = name.value
        else:
            self.name = name.lower()
        if not isinstance(strict_type, StrictType):
            raise CoreException(
                message="bad param 'strict_type' isn't instance of StrictType")
        self.strict_type = strict_type
        if not isinstance(severity, StrictSeverity):
            raise CoreException(
                message="bad param 'severity' isnt instance of StrictSeverity")
        self.severity = severity

        if strict_type == StrictType.TAG:
            if HtmlTag.has_property(self.name):
                self.enum_type = HtmlTag(self.name)
        elif strict_type == StrictType.HTML_ATTR:
            if HtmlAttr.has_property(self.name):
                self.enum_type = HtmlAttr(self.name)
        elif strict_type == StrictType.CSS_PROP:
            if CssProperty.has_property(self.name):
                self.enum_type = CssProperty(self.name)
        elif strict_type == StrictType.JS_EVENT:
            raise NotImplementedError("Open an issue on github if raise here")
        elif strict_type == StrictType.BEHAVIOUR:
            raise NotImplementedError("Open an issue on github if raise here")
        elif strict_type == StrictType.USABILITY:
            raise NotImplementedError("Open an issue on github if raise here")
        elif strict_type == StrictType.SEO:
            raise NotImplementedError("Open an issue on github if raise here")
        else:
            raise CoreException(
                message="bad param 'strict_type', invalid value")


class StrictType(EnumBase):
    """Just message type enum for warning and errors on control form class
        or inherits
    """

    TAG = 'tag'
    HTML_ATTR = 'html_attr'
    CSS_PROP = 'css_prop'
    JS_EVENT = 'js_event'
    BEHAVIOUR = 'behaviour'
    USABILITY = 'usability'
    SEO = 'seo'


class StrictSeverity(EnumBase):
    """Integer type enum to indicates severity at apply StrictRule"""

    LOW = "low"
    MEDIUM = "medium"
    HIGHT = "hight"
