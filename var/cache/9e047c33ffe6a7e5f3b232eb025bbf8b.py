# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/Products.CMFPlone-6.0.11-py3.9.egg/Products/CMFPlone/controlpanel/browser/overview.pt'

__tokens = {421: ("python:request.set('disable_plone.leftcolumn',1)", 12, 47), 517: (" python:request.set('disable_plone.rightcolumn',1", 13, 46), 979: ('view/upgrade_warning', 26, 23), 1261: ('string:${context/portal_url}/@@plone-upgrade', 34, 35), 1644: ('view/mailhost_warning', 46, 23), 2215: ('string:${portal_url}/@@mail-controlpanel', 57, 39), 2449: ('view/timezone_warning', 66, 23), 2982: ('string:${portal_url}/@@dateandtime-controlpanel', 78, 39), 3241: ('not:view/pil', 87, 23), 3522: ('view/categories', 96, 37), 3574: ("python:view.sublists(category.get('id'))", 97, 34), 3680: ('sublist', 98, 63), 3724: ('category/title', 99, 34), 3823: ('sublist', 102, 40), 3978: ('sublist', 105, 29), 4032: ('sublist', 106, 44), 4092: ('action/visible', 107, 50), 4244: ('action/icon', 109, 37), 4297: (" python:'http' in action['icon'", 110, 40), 4372: ('action/url', 111, 41), 4466: ('icon_url', 113, 42), 4571: ('action/icon', 115, 44), 4627: (' action/titl', 116, 43), 4736: ('not: icon_url', 118, 47), 4798: ("python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')", 119, 47), 4976: ('action/title', 121, 38), 5339: ('not:sublist', 133, 31), 5702: ('view/version_overview', 145, 41), 5751: ('version', 146, 25), 5842: ('view/server_info', 148, 42), 5898: (' server_info/wsg', 149, 38), 6042: ('has_wsgi', 152, 51), 6113: ('not:has_wsgi', 153, 51), 6246: ('${server_info/server_name}', 157, 18), 6248: ('server_info/server_name', 157, 20), 6298: ('${server_info/version}', 158, 18), 6300: ('server_info/version', 158, 20), 6397: ('not:view/is_dev_mode', 163, 22), 6969: ('view/is_dev_mode', 175, 22), 261: ('here/prefs_main_template/macros/master', 6, 23), 261: ('here/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_140362873170720 = {'class': '', }
_static_140362873164320 = {'class': '', }
_static_140362873114144 = {'class': 'controlPanelSectionFooter', }
_static_140362873129376 = {'class': 'discreet', }
_static_140362873146288 = {'class': 'text-decoration-none text-center ', }
_static_140362873138480 = {'src': '', 'alt': '', 'class': 'icon', }
_static_140362873136512 = {'class': 'mb-3', }
_static_140362873130432 = {'href': '', 'class': 'd-block text-dark text-center py-4 rounded btn btn-light h-100', }
_static_140362873128368 = {'class': 'col mb-4', }
_static_140362873125472 = {'class': 'configlets row row-cols-3 row-cols-sm-4 row-cols-lg-6 row-cols-xl-8 list-unstyled list w-100', }
_static_140362873123936 = {'class': 'row', }
_static_140362873122576 = {'class': '', }
_static_140362873120416 = {'class': 'controlPanelSection mb-4', }
_static_140362873097040 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_140362873097808 = {'href': '', }
_static_140362873081760 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_140362873088176 = {'href': '', }
_static_140362873076608 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_140362873077664 = {'href': '#', 'title': 'Go to the upgrade page', }
_static_140362873073568 = {'class': 'alert alert-warning mb-5', 'role': 'status', }
_static_140362873072272 = {'class': 'lead', }
_static_140362873070928 = {'class': 'documentFirstHeading', }
_static_140362873064176 = {'class': 'controlPanel controlPanelOverview', }
_static_140362943564240 = __C2ZContextWrapper
_static_140362943564528 = __compile_zt_expr
_static_140362873335040 = 'master'
_static_140362943909360 = {}

import re
import functools
from itertools import chain as __chain
from sys import intern
__default = intern('__default__')
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(modules, nothing, tales, zope_version_5_9_0_):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        on_error_handler = econtext['__on_error_handler']
        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873335376
            __attrs_140362873335376 = _static_140362943909360
            __previous_i18n_domain_140362873335520 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140362925173376 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fa8c7346d00> name=None at 7fa8c7346d30> -> __value
            __value = _static_140362873335040
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873062976
                __attrs_140362873062976 = _static_140362943909360
                __backup_disable_column_one_140362873335616 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn',1)" (12:47)> -> __value
                __token = 421
                try:
                    __zt_tmp = __attrs_140362873062976
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140362943564528('python', "request.set('disable_plone.leftcolumn',1)", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_140362873061488 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn',1)" (13:46)> -> __value
                __token = 517
                try:
                    __zt_tmp = __attrs_140362873062976
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140362943564528('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_140362873061488 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_140362873061488
                if (__backup_disable_column_one_140362873335616 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_140362873335616
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fa8c7304af0> name=None at 7fa8c7304940> -> __attrs_140362873064512
                __attrs_140362873064512 = _static_140362873064176

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="controlPanel controlPanelOverview">\n  ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873069776
                __attrs_140362873069776 = _static_140362943909360

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n    ')

                # <Static value=<ast.Dict object at 0x7fa8c7306550> name=None at 7fa8c73063d0> -> __attrs_140362873071264
                __attrs_140362873071264 = _static_140362873070928

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_140362873070400 = []
                __append_140362873070400 = __stream_140362873070400.append
                __append_140362873070400('Site Setup')
                __msgid_140362873070400 = __re_whitespace(''.join(__stream_140362873070400)).strip()
                if __msgid_140362873070400:
                    __append(translate(__msgid_140362873070400, mapping=None, default=__msgid_140362873070400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n    ')

                # <Static value=<ast.Dict object at 0x7fa8c7306a90> name=None at 7fa8c7306ac0> -> __attrs_140362873072656
                __attrs_140362873072656 = _static_140362873072272

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_140362873071792 = []
                __append_140362873071792 = __stream_140362873071792.append
                __append_140362873071792('\n        Configuration area for Plone and add-on Products.\n    ')
                __msgid_140362873071792 = __re_whitespace(''.join(__stream_140362873071792)).strip()
                if 'description_control_panel':
                    __append(translate('description_control_panel', mapping=None, default=__msgid_140362873071792, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  </header>\n  ')

                # <Static value=<ast.Dict object at 0x7fa8c7306fa0> name=None at 7fa8c7306fd0> -> __attrs_140362873074112
                __attrs_140362873074112 = _static_140362873073568

                # <Value 'view/upgrade_warning' (26:23)> -> __condition
                __token = 979
                try:
                    __zt_tmp = __attrs_140362873074112
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140362943564528('path', 'view/upgrade_warning', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873075360
                    __attrs_140362873075360 = _static_140362943909360

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_140362873074880 = []
                    __append_140362873074880 = __stream_140362873074880.append
                    __append_140362873074880('\n          Warning\n      ')
                    __msgid_140362873074880 = __re_whitespace(''.join(__stream_140362873074880)).strip()
                    if __msgid_140362873074880:
                        __append(translate(__msgid_140362873074880, mapping=None, default=__msgid_140362873074880, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873076272
                    __attrs_140362873076272 = _static_140362943909360
                    __stream_140362873218208_link_continue_with_the_upgrade = ''
                    __stream_140362873075888 = []
                    __append_140362873075888 = __stream_140362873075888.append
                    __append_140362873075888('\n          The site configuration is outdated and needs to be\n          upgraded. Please\n          ')
                    __stream_140362873218208_link_continue_with_the_upgrade = []
                    __append_140362873218208_link_continue_with_the_upgrade = __stream_140362873218208_link_continue_with_the_upgrade.append

                    # <Static value=<ast.Dict object at 0x7fa8c7307fa0> name=None at 7fa8c7307fd0> -> __attrs_140362873078640
                    __attrs_140362873078640 = _static_140362873077664

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140362873218208_link_continue_with_the_upgrade('<a')

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873077136
                    __default_140362873077136 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/portal_url}/@@plone-upgrade' (34:35)> -> __attr_href
                    __token = 1261
                    try:
                        __zt_tmp = __attrs_140362873078640
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140362943564528('string', '${context/portal_url}/@@plone-upgrade', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140362873218208_link_continue_with_the_upgrade((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873078112
                    __default_140362873078112 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x7fa8c7308040> at 7fa8c73080d0> -> __attr_title
                    __attr_title = 'Go to the upgrade page'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append_140362873218208_link_continue_with_the_upgrade((' title="%s"' % __attr_title))
                    __append_140362873218208_link_continue_with_the_upgrade('>')
                    __stream_140362873076848 = []
                    __append_140362873076848 = __stream_140362873076848.append
                    __append_140362873076848('\n            continue with the upgrade\n          ')
                    __msgid_140362873076848 = __re_whitespace(''.join(__stream_140362873076848)).strip()
                    if __msgid_140362873076848:
                        __append_140362873218208_link_continue_with_the_upgrade(translate(__msgid_140362873076848, mapping=None, default=__msgid_140362873076848, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_140362873218208_link_continue_with_the_upgrade('</a>')
                    __append_140362873075888('${link_continue_with_the_upgrade}')
                    __stream_140362873218208_link_continue_with_the_upgrade = ''.join(__stream_140362873218208_link_continue_with_the_upgrade)
                    __append_140362873075888('.\n      ')
                    __msgid_140362873075888 = __re_whitespace(''.join(__stream_140362873075888)).strip()
                    if __msgid_140362873075888:
                        __append(translate(__msgid_140362873075888, mapping={'link_continue_with_the_upgrade': __stream_140362873218208_link_continue_with_the_upgrade, }, default=__msgid_140362873075888, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa8c7307b80> name=None at 7fa8c7307d30> -> __attrs_140362873079792
                __attrs_140362873079792 = _static_140362873076608

                # <Value 'view/mailhost_warning' (46:23)> -> __condition
                __token = 1644
                try:
                    __zt_tmp = __attrs_140362873079792
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140362943564528('path', 'view/mailhost_warning', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873081040
                    __attrs_140362873081040 = _static_140362943909360

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_140362873080560 = []
                    __append_140362873080560 = __stream_140362873080560.append
                    __append_140362873080560('\n          Warning\n      ')
                    __msgid_140362873080560 = __re_whitespace(''.join(__stream_140362873080560)).strip()
                    if __msgid_140362873080560:
                        __append(translate(__msgid_140362873080560, mapping=None, default=__msgid_140362873080560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873086064
                    __attrs_140362873086064 = _static_140362943909360
                    __stream_140362873218208_label_mail_control_panel_link = ''
                    __stream_140362873081520 = []
                    __append_140362873081520 = __stream_140362873081520.append
                    __append_140362873081520("\n          You have not configured a mail host or a site 'From'\n          address, various features including contact forms, email\n          notification and password reset will not work. Go to the\n          ")
                    __stream_140362873218208_label_mail_control_panel_link = []
                    __append_140362873218208_label_mail_control_panel_link = __stream_140362873218208_label_mail_control_panel_link.append

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873086928
                    __attrs_140362873086928 = _static_140362943909360
                    __append_140362873218208_label_mail_control_panel_link('\n              ')

                    # <Static value=<ast.Dict object at 0x7fa8c730a8b0> name=None at 7fa8c730a8e0> -> __attrs_140362873088848
                    __attrs_140362873088848 = _static_140362873088176

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140362873218208_label_mail_control_panel_link('<a')

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873088320
                    __default_140362873088320 = _DEFAULT_MARKER

                    # <Substitution 'string:${portal_url}/@@mail-controlpanel' (57:39)> -> __attr_href
                    __token = 2215
                    try:
                        __zt_tmp = __attrs_140362873088848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140362943564528('string', '${portal_url}/@@mail-controlpanel', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140362873218208_label_mail_control_panel_link((' href="%s"' % __attr_href))
                    __append_140362873218208_label_mail_control_panel_link(' >')
                    __stream_140362873087648 = []
                    __append_140362873087648 = __stream_140362873087648.append
                    __append_140362873087648('Mail control panel')
                    __msgid_140362873087648 = __re_whitespace(''.join(__stream_140362873087648)).strip()
                    if 'text_no_mailhost_configured_control_panel_link':
                        __append_140362873218208_label_mail_control_panel_link(translate('text_no_mailhost_configured_control_panel_link', mapping=None, default=__msgid_140362873087648, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_140362873218208_label_mail_control_panel_link('</a>\n          ')
                    __append_140362873081520('${label_mail_control_panel_link}')
                    __stream_140362873218208_label_mail_control_panel_link = ''.join(__stream_140362873218208_label_mail_control_panel_link)
                    __append_140362873081520('\n          to fix this.\n      ')
                    __msgid_140362873081520 = __re_whitespace(''.join(__stream_140362873081520)).strip()
                    if 'text_no_mailhost_configured':
                        __append(translate('text_no_mailhost_configured', mapping={'label_mail_control_panel_link': __stream_140362873218208_label_mail_control_panel_link, }, default=__msgid_140362873081520, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa8c7308fa0> name=None at 7fa8c7308f10> -> __attrs_140362873089472
                __attrs_140362873089472 = _static_140362873081760

                # <Value 'view/timezone_warning' (66:23)> -> __condition
                __token = 2449
                try:
                    __zt_tmp = __attrs_140362873089472
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140362943564528('path', 'view/timezone_warning', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873094880
                    __attrs_140362873094880 = _static_140362943909360

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_140362873094400 = []
                    __append_140362873094400 = __stream_140362873094400.append
                    __append_140362873094400('\n          Warning\n      ')
                    __msgid_140362873094400 = __re_whitespace(''.join(__stream_140362873094400)).strip()
                    if __msgid_140362873094400:
                        __append(translate(__msgid_140362873094400, mapping=None, default=__msgid_140362873094400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873095744
                    __attrs_140362873095744 = _static_140362943909360
                    __stream_140362873218208_label_mail_event_settings_link = ''
                    __stream_140362873095360 = []
                    __append_140362873095360 = __stream_140362873095360.append
                    __append_140362873095360('\n\n          You have not set the portal timezone. Date/Time handling will not\n          work properly for timezone aware date/time values.\n          Go to the\n          ')
                    __stream_140362873218208_label_mail_event_settings_link = []
                    __append_140362873218208_label_mail_event_settings_link = __stream_140362873218208_label_mail_event_settings_link.append

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873096608
                    __attrs_140362873096608 = _static_140362943909360
                    __append_140362873218208_label_mail_event_settings_link('\n              ')

                    # <Static value=<ast.Dict object at 0x7fa8c730ce50> name=None at 7fa8c730ce80> -> __attrs_140362873110832
                    __attrs_140362873110832 = _static_140362873097808

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140362873218208_label_mail_event_settings_link('<a')

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873097952
                    __default_140362873097952 = _DEFAULT_MARKER

                    # <Substitution 'string:${portal_url}/@@dateandtime-controlpanel' (78:39)> -> __attr_href
                    __token = 2982
                    try:
                        __zt_tmp = __attrs_140362873110832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140362943564528('string', '${portal_url}/@@dateandtime-controlpanel', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140362873218208_label_mail_event_settings_link((' href="%s"' % __attr_href))
                    __append_140362873218208_label_mail_event_settings_link(' >')
                    __stream_140362873097280 = []
                    __append_140362873097280 = __stream_140362873097280.append
                    __append_140362873097280('Date and Time Settings control panel')
                    __msgid_140362873097280 = __re_whitespace(''.join(__stream_140362873097280)).strip()
                    if 'text_no_timezone_configured_control_panel_link':
                        __append_140362873218208_label_mail_event_settings_link(translate('text_no_timezone_configured_control_panel_link', mapping=None, default=__msgid_140362873097280, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append_140362873218208_label_mail_event_settings_link('</a>\n          ')
                    __append_140362873095360('${label_mail_event_settings_link}')
                    __stream_140362873218208_label_mail_event_settings_link = ''.join(__stream_140362873218208_label_mail_event_settings_link)
                    __append_140362873095360('\n          to fix this.\n      ')
                    __msgid_140362873095360 = __re_whitespace(''.join(__stream_140362873095360)).strip()
                    if 'text_no_timezone_configured':
                        __append(translate('text_no_timezone_configured', mapping={'label_mail_event_settings_link': __stream_140362873218208_label_mail_event_settings_link, }, default=__msgid_140362873095360, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa8c730cb50> name=None at 7fa8c730cd00> -> __attrs_140362873111456
                __attrs_140362873111456 = _static_140362873097040

                # <Value 'not:view/pil' (87:23)> -> __condition
                __token = 3241
                try:
                    __zt_tmp = __attrs_140362873111456
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140362943564528('not', 'view/pil', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="alert alert-warning mb-5" role="status">\n      ')

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873112704
                    __attrs_140362873112704 = _static_140362943909360

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_140362873112224 = []
                    __append_140362873112224 = __stream_140362873112224.append
                    __append_140362873112224('\n          Warning\n      ')
                    __msgid_140362873112224 = __re_whitespace(''.join(__stream_140362873112224)).strip()
                    if __msgid_140362873112224:
                        __append(translate(__msgid_140362873112224, mapping=None, default=__msgid_140362873112224, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n      ')

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873113568
                    __attrs_140362873113568 = _static_140362943909360
                    __stream_140362873113184 = []
                    __append_140362873113184 = __stream_140362873113184.append
                    __append_140362873113184('\n          PIL is not installed properly, image scaling will not work.\n      ')
                    __msgid_140362873113184 = __re_whitespace(''.join(__stream_140362873113184)).strip()
                    if 'text_no_pil_installed':
                        __append(translate('text_no_pil_installed', mapping=None, default=__msgid_140362873113184, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n  </div>')
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873113952
                __attrs_140362873113952 = _static_140362943909360
                __backup_category_140362873063168 = get('category', __marker)

                # <Value 'view/categories' (96:37)> -> __iterator
                __token = 3522
                try:
                    __zt_tmp = __attrs_140362873113952
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140362943564528('path', 'view/categories', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                (__iterator, ____index_140362873114192, ) = getname('repeat')('category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873119168
                    __attrs_140362873119168 = _static_140362943909360
                    __backup_sublist_140362873064944 = get('sublist', __marker)

                    # <Value "python:view.sublists(category.get('id'))" (97:34)> -> __value
                    __token = 3574
                    try:
                        __zt_tmp = __attrs_140362873119168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140362943564528('python', "view.sublists(category.get('id'))", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    econtext['sublist'] = __value
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7fa8c73126a0> name=None at 7fa8c73124f0> -> __attrs_140362873120752
                    __attrs_140362873120752 = _static_140362873120416

                    # <Value 'sublist' (98:63)> -> __condition
                    __token = 3680
                    try:
                        __zt_tmp = __attrs_140362873120752
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140362943564528('path', 'sublist', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    if __condition:

                        # <section ... (0:0)
                        # --------------------------------------------------------
                        __append('<section class="controlPanelSection mb-4">\n        ')

                        # <Static value=<ast.Dict object at 0x7fa8c7312f10> name=None at 7fa8c7312f40> -> __attrs_140362873123024
                        __attrs_140362873123024 = _static_140362873122576

                        # <h3 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h3 class="">')

                        # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873122000
                        __default_140362873122000 = _DEFAULT_MARKER

                        # <Value 'category/title' (99:34)> -> __cache_140362873121520
                        __token = 3724
                        try:
                            __zt_tmp = __attrs_140362873123024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140362873121520 = _static_140362943564528('path', 'category/title', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                        # <BinOp left=<Value 'category/title' (99:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c7312bb0> -> __condition
                        __expression = __cache_140362873121520

                        # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Category')
                        else:
                            __content = __cache_140362873121520
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</h3>\n\n        ')

                        # <Static value=<ast.Dict object at 0x7fa8c7313460> name=None at 7fa8c7313490> -> __attrs_140362873124320
                        __attrs_140362873124320 = _static_140362873123936

                        # <Value 'sublist' (102:40)> -> __condition
                        __token = 3823
                        try:
                            __zt_tmp = __attrs_140362873124320
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140362943564528('path', 'sublist', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                        if __condition:

                            # <nav ... (0:0)
                            # --------------------------------------------------------
                            __append('<nav class="row">\n\n          ')

                            # <Static value=<ast.Dict object at 0x7fa8c7313a60> name=None at 7fa8c7313a90> -> __attrs_140362873125904
                            __attrs_140362873125904 = _static_140362873125472

                            # <Value 'sublist' (105:29)> -> __condition
                            __token = 3978
                            try:
                                __zt_tmp = __attrs_140362873125904
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140362943564528('path', 'sublist', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                            if __condition:

                                # <ul ... (0:0)
                                # --------------------------------------------------------
                                __append('<ul class="configlets row row-cols-3 row-cols-sm-4 row-cols-lg-6 row-cols-xl-8 list-unstyled list w-100">\n            ')

                                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873127120
                                __attrs_140362873127120 = _static_140362943909360
                                __backup_action_140362873126096 = get('action', __marker)

                                # <Value 'sublist' (106:44)> -> __iterator
                                __token = 4032
                                try:
                                    __zt_tmp = __attrs_140362873127120
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __iterator = _static_140362943564528('path', 'sublist', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                (__iterator, ____index_140362873127456, ) = getname('repeat')('action', __iterator)
                                econtext['action'] = None
                                for __item in __iterator:
                                    econtext['action'] = __item
                                    __append('\n              ')

                                    # <Static value=<ast.Dict object at 0x7fa8c73145b0> name=None at 7fa8c73145e0> -> __attrs_140362873128752
                                    __attrs_140362873128752 = _static_140362873128368

                                    # <Value 'action/visible' (107:50)> -> __condition
                                    __token = 4092
                                    try:
                                        __zt_tmp = __attrs_140362873128752
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_140362943564528('path', 'action/visible', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                    if __condition:

                                        # <li ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<li class="col mb-4">\n                ')

                                        # <Static value=<ast.Dict object at 0x7fa8c7314dc0> name=None at 7fa8c7314df0> -> __attrs_140362873130912
                                        __attrs_140362873130912 = _static_140362873130432
                                        __backup_icon_140362873127360 = get('icon', __marker)

                                        # <Value 'action/icon' (109:37)> -> __value
                                        __token = 4244
                                        try:
                                            __zt_tmp = __attrs_140362873130912
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __value = _static_140362943564528('path', 'action/icon', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                        econtext['icon'] = __value
                                        __backup_icon_url_140362873128944 = get('icon_url', __marker)

                                        # <Value "python:'http' in action['icon']" (110:40)> -> __value
                                        __token = 4297
                                        try:
                                            __zt_tmp = __attrs_140362873130912
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __value = _static_140362943564528('python', "'http' in action['icon']", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                        econtext['icon_url'] = __value

                                        # <a ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<a')

                                        # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873130000
                                        __default_140362873130000 = _DEFAULT_MARKER

                                        # <Substitution 'action/url' (111:41)> -> __attr_href
                                        __token = 4372
                                        try:
                                            __zt_tmp = __attrs_140362873130912
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __attr_href = _static_140362943564528('path', 'action/url', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                                        if (__attr_href is not None):
                                            __append((' href="%s"' % __attr_href))
                                        __append(' class="d-block text-dark text-center py-4 rounded btn btn-light h-100">\n                    ')

                                        # <Static value=<ast.Dict object at 0x7fa8c7316580> name=None at 7fa8c73165b0> -> __attrs_140362873136896
                                        __attrs_140362873136896 = _static_140362873136512

                                        # <div ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<div class="mb-3">\n                      ')

                                        # <Static value=<ast.Dict object at 0x7fa8c7316d30> name=None at 7fa8c7316970> -> __attrs_140362873143408
                                        __attrs_140362873143408 = _static_140362873138480

                                        # <Value 'icon_url' (113:42)> -> __condition
                                        __token = 4466
                                        try:
                                            __zt_tmp = __attrs_140362873143408
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_140362943564528('path', 'icon_url', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                        if __condition:

                                            # <img ... (0:0)
                                            # --------------------------------------------------------
                                            __append('<img')

                                            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873138576
                                            __default_140362873138576 = _DEFAULT_MARKER

                                            # <Substitution 'action/icon' (115:44)> -> __attr_src
                                            __token = 4571
                                            try:
                                                __zt_tmp = __attrs_140362873143408
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_src = _static_140362943564528('path', 'action/icon', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                            __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                                            if (__attr_src is not None):
                                                __append((' src="%s"' % __attr_src))

                                            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873138672
                                            __default_140362873138672 = _DEFAULT_MARKER

                                            # <Translate msgid=None node=<Substitution 'action/title' (116:43)> at 7fa8c73169a0> -> __attr_alt

                                            # <Substitution 'action/title' (116:43)> -> __attr_alt
                                            __token = 4627
                                            try:
                                                __zt_tmp = __attrs_140362873143408
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_alt = _static_140362943564528('path', 'action/title', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                            __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                            if (__attr_alt is not None):
                                                __append((' alt="%s"' % __attr_alt))
                                            __append(' class="icon">')
                                        __append('\n                      ')

                                        # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873144896
                                        __attrs_140362873144896 = _static_140362943909360

                                        # <Value 'not: icon_url' (118:47)> -> __condition
                                        __token = 4736
                                        try:
                                            __zt_tmp = __attrs_140362873144896
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_140362943564528('not', ' icon_url', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                        if __condition:

                                            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873144704
                                            __default_140362873144704 = _DEFAULT_MARKER

                                            # <Value "python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')" (119:47)> -> __cache_140362873144224
                                            __token = 4798
                                            try:
                                                __zt_tmp = __attrs_140362873144896
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __cache_140362873144224 = _static_140362943564528('python', "icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                                            # <BinOp left=<Value "python:icons.tag(action['icon'] or 'plone-controlpanel', tag_alt=action['title'], tag_class='overview-icon')" (119:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c7318460> -> __condition
                                            __expression = __cache_140362873144224

                                            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                                            __value = _DEFAULT_MARKER
                                            __condition = (__expression is __value)
                                            if __condition:
                                                pass
                                            else:
                                                __content = __cache_140362873144224
                                                __content = __convert(__content)
                                                if (__content is not None):
                                                    __append(__content)
                                        __append('\n                    </div>\n                    ')

                                        # <Static value=<ast.Dict object at 0x7fa8c7318bb0> name=None at 7fa8c7318a00> -> __attrs_140362873146624
                                        __attrs_140362873146624 = _static_140362873146288

                                        # <div ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<div class="text-decoration-none text-center ">')

                                        # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873145664
                                        __default_140362873145664 = _DEFAULT_MARKER

                                        # <Value 'action/title' (121:38)> -> __cache_140362873144032
                                        __token = 4976
                                        try:
                                            __zt_tmp = __attrs_140362873146624
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __cache_140362873144032 = _static_140362943564528('path', 'action/title', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                                        # <BinOp left=<Value 'action/title' (121:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c7318820> -> __condition
                                        __expression = __cache_140362873144032

                                        # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                                        __value = _DEFAULT_MARKER
                                        __condition = (__expression is __value)
                                        if __condition:
                                            __append('\n                        Title\n                    ')
                                        else:
                                            __content = __cache_140362873144032
                                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                            __content = __quote(__content, None, '\xad', None, None)
                                            if (__content is not None):
                                                __append(__content)
                                        __append('</div>\n                </a>')
                                        if (__backup_icon_url_140362873128944 is __marker):
                                            del econtext['icon_url']
                                        else:
                                            econtext['icon_url'] = __backup_icon_url_140362873128944
                                        if (__backup_icon_140362873127360 is __marker):
                                            del econtext['icon']
                                        else:
                                            econtext['icon'] = __backup_icon_140362873127360
                                        __append('\n              </li>')
                                    __append('\n            ')
                                    ____index_140362873127456 -= 1
                                    if (____index_140362873127456 > 0):
                                        __append('')
                                if (__backup_action_140362873126096 is __marker):
                                    del econtext['action']
                                else:
                                    econtext['action'] = __backup_action_140362873126096
                                __append('\n            </ul>')
                            __append('\n          </nav>')
                        __append('\n\n          ')

                        # <Static value=<ast.Dict object at 0x7fa8c73149a0> name=None at 7fa8c73161f0> -> __attrs_140362873147200
                        __attrs_140362873147200 = _static_140362873129376

                        # <Value 'not:sublist' (133:31)> -> __condition
                        __token = 5339
                        try:
                            __zt_tmp = __attrs_140362873147200
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140362943564528('not', 'sublist', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="discreet">')
                            __stream_140362873126864 = []
                            __append_140362873126864 = __stream_140362873126864.append
                            __append_140362873126864('\n              No preference panels available.\n          ')
                            __msgid_140362873126864 = __re_whitespace(''.join(__stream_140362873126864)).strip()
                            if 'label_no_prefs_panels_available':
                                __append(translate('label_no_prefs_panels_available', mapping=None, default=__msgid_140362873126864, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</div>')
                        __append('\n\n      </section>')
                    __append('\n    ')
                    if (__backup_sublist_140362873064944 is __marker):
                        del econtext['sublist']
                    else:
                        econtext['sublist'] = __backup_sublist_140362873064944
                    __append('\n  ')
                    ____index_140362873114192 -= 1
                    if (____index_140362873114192 > 0):
                        __append('')
                if (__backup_category_140362873063168 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_140362873063168
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa8c7310e20> name=None at 7fa8c7310b20> -> __attrs_140362873151936
                __attrs_140362873151936 = _static_140362873114144

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="controlPanelSectionFooter">\n    ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873152992
                __attrs_140362873152992 = _static_140362943909360

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2>')
                __stream_140362873152512 = []
                __append_140362873152512 = __stream_140362873152512.append
                __append_140362873152512('Version Overview')
                __msgid_140362873152512 = __re_whitespace(''.join(__stream_140362873152512)).strip()
                if 'heading_version_overview':
                    __append(translate('heading_version_overview', mapping=None, default=__msgid_140362873152512, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h2>\n    ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873153856
                __attrs_140362873153856 = _static_140362943909360

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul>\n      ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873154720
                __attrs_140362873154720 = _static_140362943909360
                __backup_version_140362873070112 = get('version', __marker)

                # <Value 'view/version_overview' (145:41)> -> __iterator
                __token = 5702
                try:
                    __zt_tmp = __attrs_140362873154720
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140362943564528('path', 'view/version_overview', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                (__iterator, ____index_140362873154960, ) = getname('repeat')('version', __iterator)
                econtext['version'] = None
                for __item in __iterator:
                    econtext['version'] = __item
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873156608
                    __attrs_140362873156608 = _static_140362943909360

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li>')

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873156032
                    __default_140362873156032 = _DEFAULT_MARKER

                    # <Value 'version' (146:25)> -> __cache_140362873155488
                    __token = 5751
                    try:
                        __zt_tmp = __attrs_140362873156608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140362873155488 = _static_140362943564528('path', 'version', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                    # <BinOp left=<Value 'version' (146:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c731b0a0> -> __condition
                    __expression = __cache_140362873155488

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Version')
                    else:
                        __content = __cache_140362873155488
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</li>\n      ')
                    ____index_140362873154960 -= 1
                    if (____index_140362873154960 > 0):
                        __append('')
                if (__backup_version_140362873070112 is __marker):
                    del econtext['version']
                else:
                    econtext['version'] = __backup_version_140362873070112
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873156992
                __attrs_140362873156992 = _static_140362943909360
                __backup_server_info_140362873075696 = get('server_info', __marker)

                # <Value 'view/server_info' (148:42)> -> __value
                __token = 5842
                try:
                    __zt_tmp = __attrs_140362873156992
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140362943564528('path', 'view/server_info', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                econtext['server_info'] = __value
                __backup_has_wsgi_140362873078880 = get('has_wsgi', __marker)

                # <Value 'server_info/wsgi' (149:38)> -> __value
                __token = 5898
                try:
                    __zt_tmp = __attrs_140362873156992
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140362943564528('path', 'server_info/wsgi', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                econtext['has_wsgi'] = __value
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873158336
                __attrs_140362873158336 = _static_140362943909360

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>\n            ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873159296
                __attrs_140362873159296 = _static_140362943909360
                __stream_140362873158912 = []
                __append_140362873158912 = __stream_140362873158912.append
                __append_140362873158912('WSGI:')
                __msgid_140362873158912 = __re_whitespace(''.join(__stream_140362873158912)).strip()
                if __msgid_140362873158912:
                    __append(translate(__msgid_140362873158912, mapping=None, default=__msgid_140362873158912, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873164128
                __attrs_140362873164128 = _static_140362943909360

                # <Value 'has_wsgi' (152:51)> -> __condition
                __token = 6042
                try:
                    __zt_tmp = __attrs_140362873164128
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140362943564528('path', 'has_wsgi', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_140362873159008 = []
                    __append_140362873159008 = __stream_140362873159008.append
                    __append_140362873159008('On')
                    __msgid_140362873159008 = __re_whitespace(''.join(__stream_140362873159008)).strip()
                    if __msgid_140362873159008:
                        __append(translate(__msgid_140362873159008, mapping=None, default=__msgid_140362873159008, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873165280
                __attrs_140362873165280 = _static_140362943909360

                # <Value 'not:has_wsgi' (153:51)> -> __condition
                __token = 6113
                try:
                    __zt_tmp = __attrs_140362873165280
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140362943564528('not', 'has_wsgi', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_140362873164800 = []
                    __append_140362873164800 = __stream_140362873164800.append
                    __append_140362873164800('Off')
                    __msgid_140362873164800 = __re_whitespace(''.join(__stream_140362873164800)).strip()
                    if __msgid_140362873164800:
                        __append(translate(__msgid_140362873164800, mapping=None, default=__msgid_140362873164800, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>')
                __append('\n          </li>\n          ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873166240
                __attrs_140362873166240 = _static_140362943909360

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li>\n            ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873167200
                __attrs_140362873167200 = _static_140362943909360
                __stream_140362873166816 = []
                __append_140362873166816 = __stream_140362873166816.append
                __append_140362873166816('Server:')
                __msgid_140362873166816 = __re_whitespace(''.join(__stream_140362873166816)).strip()
                if __msgid_140362873166816:
                    __append(translate(__msgid_140362873166816, mapping=None, default=__msgid_140362873166816, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873167776
                __attrs_140362873167776 = _static_140362943909360

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Interpolation value=<Substitution '${server_info/server_name}' (157:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c731e130> -> __content_140363024536688
                __token = 6246
                __token = 6248
                try:
                    __zt_tmp = __attrs_140362873167776
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140363024536688 = _static_140362943564528('path', 'server_info/server_name', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __content_140363024536688 = __quote(__content_140363024536688, '\x00', '&#0;', None, None)
                __content_140363024536688 = __content_140363024536688
                if (__content_140363024536688 is None):
                    pass
                else:
                    if (__content_140363024536688 is None):
                        __content_140363024536688 = None
                    else:
                        __tt = type(__content_140363024536688)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140363024536688 = str(__content_140363024536688)
                        else:
                            if (__tt is bytes):
                                __content_140363024536688 = decode(__content_140363024536688)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140363024536688 = __content_140363024536688.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140363024536688)
                                        __content_140363024536688 = (str(__content_140363024536688) if (__content_140363024536688 is __converted) else __converted)
                                    else:
                                        __content_140363024536688 = __content_140363024536688()
                if (__content_140363024536688 is not None):
                    __append(__content_140363024536688)
                __append('</span>\n            ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873168752
                __attrs_140362873168752 = _static_140362943909360

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>')

                # <Interpolation value=<Substitution '${server_info/version}' (158:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c731e490> -> __content_140363024536688
                __token = 6298
                __token = 6300
                try:
                    __zt_tmp = __attrs_140362873168752
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140363024536688 = _static_140362943564528('path', 'server_info/version', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __content_140363024536688 = __quote(__content_140363024536688, '\x00', '&#0;', None, None)
                __content_140363024536688 = __content_140363024536688
                if (__content_140363024536688 is None):
                    pass
                else:
                    if (__content_140363024536688 is None):
                        __content_140363024536688 = None
                    else:
                        __tt = type(__content_140363024536688)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140363024536688 = str(__content_140363024536688)
                        else:
                            if (__tt is bytes):
                                __content_140363024536688 = decode(__content_140363024536688)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140363024536688 = __content_140363024536688.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140363024536688)
                                        __content_140363024536688 = (str(__content_140363024536688) if (__content_140363024536688 is __converted) else __converted)
                                    else:
                                        __content_140363024536688 = __content_140363024536688()
                if (__content_140363024536688 is not None):
                    __append(__content_140363024536688)
                __append('</span>\n          </li>\n      ')
                if (__backup_has_wsgi_140362873078880 is __marker):
                    del econtext['has_wsgi']
                else:
                    econtext['has_wsgi'] = __backup_has_wsgi_140362873078880
                if (__backup_server_info_140362873075696 is __marker):
                    del econtext['server_info']
                else:
                    econtext['server_info'] = __backup_server_info_140362873075696
                __append('\n    </ul>\n\n    ')

                # <Static value=<ast.Dict object at 0x7fa8c731d220> name=None at 7fa8c731da00> -> __attrs_140362873169568
                __attrs_140362873169568 = _static_140362873164320

                # <Value 'not:view/is_dev_mode' (163:22)> -> __condition
                __token = 6397
                try:
                    __zt_tmp = __attrs_140362873169568
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140362943564528('not', 'view/is_dev_mode', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="">')
                    __stream_140362873154432 = []
                    __append_140362873154432 = __stream_140362873154432.append
                    __append_140362873154432('\n      You are running in "production mode". This is the preferred mode of\n      operation for a live Plone site, but means that some\n      configuration changes will not take effect until your server is\n      restarted or a product refreshed. If this is a development instance,\n      and you want to enable debug mode, stop the server, set \'debug-mode=on\'\n      in your buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_140362873154432 = __re_whitespace(''.join(__stream_140362873154432)).strip()
                    if 'description_production_mode':
                        __append(translate('description_production_mode', mapping=None, default=__msgid_140362873154432, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7fa8c731eb20> name=None at 7fa8c731eb50> -> __attrs_140362873171104
                __attrs_140362873171104 = _static_140362873170720

                # <Value 'view/is_dev_mode' (175:22)> -> __condition
                __token = 6969
                try:
                    __zt_tmp = __attrs_140362873171104
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140362943564528('path', 'view/is_dev_mode', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="">')
                    __stream_140362873170240 = []
                    __append_140362873170240 = __stream_140362873170240.append
                    __append_140362873170240('\n      You are running in "debug mode". This mode is intended for sites that\n      are under development. This allows many configuration changes to be\n      immediately visible, but will make your site run more slowly. To turn\n      off debug mode, stop the server, set \'debug-mode=off\' in your\n      buildout.cfg, re-run bin/buildout and then restart the server\n      process.\n    ')
                    __msgid_140362873170240 = __re_whitespace(''.join(__stream_140362873170240)).strip()
                    if 'description_debug_mode':
                        __append(translate('description_debug_mode', mapping=None, default=__msgid_140362873170240, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</p>')
                __append('\n  </section>\n\n</div>')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'here/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140362873335376
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140362943564528('path', 'here/prefs_main_template/macros/master', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140362925173376 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140362925173376
            __i18n_domain = __previous_i18n_domain_140362873335520
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }