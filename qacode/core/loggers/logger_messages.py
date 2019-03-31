# -*- coding: utf-8 -*-
"""Module related with all logging messages"""


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
CF_STRICT_LOADING = "ctl_form | _load_strict: loading strict_rules..."  # noqa:E501
CF_STRICT_DISABLED = "ctl_form | _load_strict: disabled loading StrictRules"  # noqa:E501
CF_STRICT_LOADED = "ctl_form | _load_strict: loaded strict_rules"  # noqa:E501
CF_ADDRULES_BASE_ADDING = "ctl_form | add_rules: adding base list of strict_rules..."  # noqa:E501
CF_ADDRULES_BASE_ADDED = "ctl_form | add_rules: added base list of strict_rules"  # noqa:E501
CF_ADDRULES_TYPED_ADDING = "ctl_form | add_rules: adding typed list of strict_rules..."  # noqa:E501
CF_ADDRULES_TYPED_ADDED = "ctl_form | add_rules: added typed list of strict_rules"  # noqa:E501
CF_NOT_IMPLEMENTED_TYPES = "ctl_form | Open an issue on github if raise here"  # noqa:E501
CF_STRICTTAG_LOADING = "ctl_form | load_strict_tag: loading strict_tags..."  # noqa:E501
CF_STRICTTAG_NOTAGS = "ctl_form | load_strict_tag: 0 strict_tags"  # noqa:E501
CF_STRICTTAG_SOMUCHTAGS = "ctl_form | load_strict_tag: more than 1 strict_tag"  # noqa:E501
CF_STRICTTAG_LOADED = "ctl_form | load_strict_tag: loaded"  # noqa:E501
CF_STRICTTAG_RAISES = "Validation raises for strict_tag for this element: strict_tag={}"  # noqa:E501
CF_STRICTTAG_NOT_LOADED = "ctl_form | load_strict_tag: not loaded"  # noqa:E501
CF_STRICTATTRS_LOADING = "ctl_form | load_strict_attrs: loading strict_attrs..."  # noqa:E501
CF_STRICTATTRS_NOT_LOADED = "ctl_form | load_strict_attrs: not loaded strict_attrs"  # noqa:E501
CF_STRICTATTRS_ERROR = "ctl_form | load_strict_attrs: not loaded strict_attrs with enabled strict_mode"  # noqa:E501
CF_STRICTATTRS_LOADED = "ctl_form | load_strict_attrs: loaded strict_attrs"  # noqa:E501
CF_STRICTCSS_LOADING = "ctl_form | load_strict_css_props: loading..."  # noqa:E501
CF_STRICTCSS_LOADED = "ctl_form | load_strict_css_props: loaded"  # noqa:E501
CF_STRICTCSS_NOT_LOADED = "ctl_form | load_strict_css_props: not loaded strict_attrs"  # noqa:E501
CF_STRICTCSS_ERROR = "ctl_form | load_strict_css_props: not loaded strict_css_props with enabled strict_mode"  # noqa:E501
CF_PARSERULES_LOADING = "ctl_form | parse_rules: parsing..."  # noqa:E501
CF_PARSERULES_LOADED = "ctl_form | parse_rules: parsed"  # noqa:E501
CF_RELOAD_LOADED = "ctl_form | reload: reloaded ctl"  # noqa:E501
CF_STRICT_ATTRS_RAISES = "Validation raises for strict_attrs for this element: control={}, strict_attrs=[{}]"  # noqa:E501
CF_DROPDOWNSELECT_LOADING = "ctl_form | dropdown_select: selecting..."  # noqa:E501
CF_DROPDOWNSELECT_LOADED = "ctl_form | dropdown_select: selected"  # noqa:E501
CF_DROPDOWNDESELECT_LOADING = "ctl_form | dropdown_select: deselecting..."  # noqa:E501
CF_DROPDOWNDESELECT_LOADED = "ctl_form | dropdown_select: deselected"  # noqa:E501
CF_DROPDOWNDESELECTALL_LOADING = "ctl_form | dropdown_select: deselecting all..."  # noqa:E501
CF_DROPDOWNDESELECTALL_LOADED = "ctl_form | dropdown_select: deselected all"  # noqa:E501
CF_DROPDOWN_LOADED = "ctl_form | ctl.dropdown property for <select>"  # noqa:E501
