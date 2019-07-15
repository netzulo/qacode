# -*- coding: utf-8 -*-
"""Module related with all logging messages"""

# Commons
NOT_IMPLEMENTED = "Open an issue on github if raise here"  # noqa:E501
BAD_PARAM = "ctl_form | bad param '{}', invalid value"  # noqa:E501
# ControlBase
CB_SETTINGS_LOADING = "ctl | load_settings_keys: loading keys..."  # noqa:E501
CB_SETTINGS_LOADED = "ctl | load_settings_keys: loaded keys"  # noqa:E501
CB_SEARCH_DISABLED = "ctl | _load_search: Disabled element search"  # noqa:E501
CB_SEARCH_LOADING = "ctl | _load_search: searching element..."  # noqa:E501
CB_SEARCH_WAITING = "ctl | _load_search: waiting for element..."  # noqa:E501
CB_SEARCH_FOUND = "ctl | _load_search: element found!"  # noqa:E501
CB_SEARCH_FOUND_CHILD = "ctl | _load_search: element child found!"  # noqa:E501
CB_PROP_DISABLED = "ctl | _load_properties: disabled loading for properties"  # noqa:E501
CB_PROP_LOADING = "ctl | _load_properties: loading properties..."  # noqa:E501
CB_PROP_LOADED = "ctl | _load_properties: loaded properties"  # noqa:E501
CB_FINDCHILD_LOADING = "ctl | find_child: searching for selector='{}'"  # noqa:E501
CB_FINDCHILD_LOADED = "ctl | find_child: child element found"  # noqa:E501
CB_GETTAG_LOADING = "ctl | get_tag: searching for tag"  # noqa:E501
CB_GETTAG_LOADED = "ctl | get_tag: found same tag='{}'"  # noqa:E501
CB_TYPETEXT_LOADING = "ctl | type_text: typing text='{}'"  # noqa:E501
CB_CLEAR_LOADING = "ctl | clear: clearing text..."  # noqa:E501
CB_CLEAR_LOADED = "ctl | clear: cleared text"  # noqa:E501
CB_CLICK_LOADING = "ctl | click: clicking element..."  # noqa:E501
CB_CLICK_RETRY = "ctl | click: retry clicking element..."  # noqa:E501
CB_CLICK_LOADED = "ctl | click: clicked!"  # noqa:E501
CB_GETTEXT_LOADING = "ctl | get_text: obtaining text..."  # noqa:E501
CB_GETTEXT_FAILED = "ctl | get_text: failed at obtain text"  # noqa:E501
CB_GETTEXT_LOADED = "ctl | get_text: text obtained, text='{}'"  # noqa:E501
CB_GETATTRS_LOADING = "ctl | get_attrs: obtaining attrs..."  # noqa:E501
CB_GETATTRVALUE_LOADING = "ctl | get_attr_value: obtaining value for attr_name='{}'"  # noqa:E501
CB_GETATTRVALUE_LOADED = "ctl | get_attr_value: obtained attr_name='{}', value='{}'"  # noqa:E501
CB_GETATTRVALUE_FAILED = "ctl | get_attr_value: fail at obtain value"  # noqa:E501
CB_SETCSSRULE_LOADING = "ctl | set_css_value: setting new CSS rule, prop_name='{}', prop_value='{}'"  # noqa:E501
CB_SETCSSRULE_FAILED = "ctl | set_css_value: failed at set CSS rule"  # noqa:E501
CB_GETCSSRULE_LOADING = "ctl | get_css_value: obtaining css_value..."  # noqa:E501
CB_GETCSSRULE_LOADED = "ctl | get_css_value: css_value='{}'"  # noqa:E501
CB_RELOAD_LOADING = "{} | reload: reloading control..."  # noqa:E501
CB_RELOAD_LOADED = "{} | reload: reloaded control"  # noqa:E501
# ControlForm
CF_RULES_LOADING = "ctl_form | loading rules..."  # noqa:E501
CF_RULES_DISABLED = "ctl_form | disabled rules functionality for this control"  # noqa:E501
CF_RULES_PARSING = "ctl_form | parsing rules..."  # noqa:E501
CF_RULES_PARSED = "ctl_form | parsed rules"  # noqa:E501
CF_RULES_APPLYING = "ctl_form | applying rules..."  # noqa:E501
CF_RULES_APPLIED = "ctl_form | applied rules"  # noqa:E501
CF_RULES_APPLYING_TAG = "ctl_form | applying tag rule..."  # noqa:E501
CF_RULES_APPLIED_TAG = "ctl_form | applied tag rule"  # noqa:E501
CF_RELOAD_LOADED = "ctl_form | reload: reloaded ctl"  # noqa:E501
CF_BADTAG = "ctl_form | This tag can't be loaded due a check, element must contains tag equals to validation rule tag type"  # noqa:E501
# ControlDropdown
CDD_SELECT_LOADING = "ctl_dd | select: selecting..."  # noqa:E501
CDD_SELECT_LOADED = "ctl_dd | select: selected"  # noqa:E501
CDD_SELECT_LOADING = "ctl_dd | deselect: deselecting..."  # noqa:E501
CDD_DESESELECT_LOADED = "ctl_dd | select: deselected"  # noqa:E501
CDD_DESELECTALL_LOADING = "ctl_dd | dropdown_select: deselecting all..."  # noqa:E501
CDD_DESELECTALL_LOADED = "ctl_dd | dropdown_select: deselected all"  # noqa:E501
CDD_BADTAG = "ctl_dd | Can't use this for not <select> tag element"  # noqa:E501
CDD_BADPARAMS = "ctl_dd | Can't use this function with all flags with True values"  # noqa:E501
CDD_BADINDEXTYPE = "ctl_dd | index must be an int value"  # noqa:E501
# ControlTable
CT_BADTAG = "ctl_tb | Can't use this for not <table> tag element"  # noqa:E501
CT_LOADED = "ctl_tb | ctl.table property for <table>"  # noqa:E501
CT_TBLNOTCHILD = "ctl_tb | this table haven't got '{}' selector"  # noqa:E501
