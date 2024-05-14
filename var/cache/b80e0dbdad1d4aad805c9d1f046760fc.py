# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/Products.CMFPlone-6.0.11-py3.9.egg/Products/CMFPlone/controlpanel/browser/prefsmaintemplate.pt'

__tokens = {256: ("python:request.set('disable_border',1)", 6, 43), 345: (" python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel'", 7, 49), 485: ("e python:request.set('disable_plone.leftcolumn', ", 8, 54), 591: ("wo python:request.set('disable_plone.rightcolumn'", 9, 53), 1074: ("python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", 21, 46), 1198: (" python:controlPanel.getGroups('site'", 22, 39), 1278: ('l controlPanel/site_u', 23, 40), 1345: ('rl request/', 24, 42), 1496: ('string:$portal_url/@@overview-controlpanel', 27, 49), 1573: ("nav-link ${python:'active' if overview_url in current_url else ''}", 28, 32), 1584: ("python:'active' if overview_url in current_url else ''", 28, 43), 1667: ('${overview_url}', 28, 126), 1669: ('overview_url', 28, 128), 1792: ('groups', 30, 49), 1850: ("python:controlPanel.enumConfiglets(group=group['id'])", 31, 49), 1949: (" python:'active' if bool([c for c in configlets if current_url.startswith(c['url'])]) else 'inactive", 32, 44), 2093: ('python:configlets and controlPanel.maySeeSomeConfiglets', 33, 41), 2237: ('nav-link dropdown-toggle ${active}', 35, 34), 2264: ('active', 35, 61), 2344: ('${group/title}', 35, 141), 2346: ('group/title', 35, 143), 2474: ('configlets', 37, 58), 2534: ('configlet/visible', 38, 47), 2608: ("python:'http' in configlet['icon']", 39, 54), 2738: ('${configlet/url}', 41, 39), 2740: ('configlet/url', 41, 41), 2809: ('icon_url', 42, 52), 2938: ('configlet/icon', 44, 56), 3009: (' configlet/titl', 45, 55), 3143: ('not: icon_url', 47, 57), 3223: ("python:icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])", 48, 65), 3347: ('${configlet/title}', 49, 32), 3349: ('configlet/title', 49, 34), 3694: ('nothing', 59, 82), 898: ('context/@@main_template/macros/content', 17, 42), 898: ('context/@@main_template/macros/content', 17, 42), 85: ('context/@@main_template/macros/master', 2, 30), 85: ('context/@@main_template/macros/master', 2, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_140362872270464 = {'src': '', 'alt': '', 'class': 'icon', }
_static_140362873230288 = {'class': 'dropdown-item', 'href': '${configlet/url}', }
_static_140362873233024 = {'class': 'dropdown-menu', }
_static_140362872276976 = {'class': 'nav-link dropdown-toggle ${active}', 'data-bs-toggle': 'dropdown', 'href': '#', 'role': 'button', 'aria-expanded': 'false', }
_static_140362872320448 = {'class': 'nav-item dropdown', }
_static_140362872320352 = {'class': "nav-link ${python:'active' if overview_url in current_url else ''}", 'aria-current': 'page', 'href': '${overview_url}', }
_static_140362872386128 = {'class': 'nav-item', }
_static_140362872389056 = {'class': 'nav nav-tabs', }
_static_140362873010544 = {'class': 'mb-3', }
_static_140362873008624 = 'content'
_static_140362943564240 = __C2ZContextWrapper
_static_140362943564528 = __compile_zt_expr
_static_140362872912960 = 'master'
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

    def render_master(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_prefs_configlet_main = econtext['__slot_prefs_configlet_main'].pop()
        except:
            __slot_prefs_configlet_main = None

        try:
            __slot_prefs_configlet_wrapper = econtext['__slot_prefs_configlet_wrapper'].pop()
        except:
            __slot_prefs_configlet_wrapper = None

        try:
            __slot_top_slot = econtext['__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            __slot_prefs_configlet_content = econtext['__slot_prefs_configlet_content'].pop()
        except:
            __slot_prefs_configlet_content = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872911520
            __attrs_140362872911520 = _static_140362943909360
            __previous_i18n_domain_140362872911808 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872911904
            __attrs_140362872911904 = _static_140362943909360
            __backup_macroname_140362918786816 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fa8c72dfc40> name=None at 7fa8c72df250> -> __value
            __value = _static_140362872912960
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872910224
                __attrs_140362872910224 = _static_140362943909360
                __append('\n        ')
                if (__slot_top_slot is None):

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872913536
                    __attrs_140362872913536 = _static_140362943909360
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872982304
                    __attrs_140362872982304 = _static_140362943909360
                    __backup_dummy_140362873135840 = get('dummy', __marker)

                    # <Value "python:request.set('disable_border',1)" (6:43)> -> __value
                    __token = 256
                    try:
                        __zt_tmp = __attrs_140362872982304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140362943564528('python', "request.set('disable_border',1)", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    econtext['dummy'] = __value
                    __backup_controlPanel_140362873334464 = get('controlPanel', __marker)

                    # <Value "python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')" (7:49)> -> __value
                    __token = 345
                    try:
                        __zt_tmp = __attrs_140362872982304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140362943564528('python', "modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    econtext['controlPanel'] = __value
                    __backup_disable_column_one_140362873334080 = get('disable_column_one', __marker)

                    # <Value "python:request.set('disable_plone.leftcolumn', 1)" (8:54)> -> __value
                    __token = 485
                    try:
                        __zt_tmp = __attrs_140362872982304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140362943564528('python', "request.set('disable_plone.leftcolumn', 1)", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    econtext['disable_column_one'] = __value
                    __backup_disable_column_two_140362873331872 = get('disable_column_two', __marker)

                    # <Value "python:request.set('disable_plone.rightcolumn',1)" (9:53)> -> __value
                    __token = 591
                    try:
                        __zt_tmp = __attrs_140362872982304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140362943564528('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    econtext['disable_column_two'] = __value
                    if (__backup_disable_column_two_140362873331872 is __marker):
                        del econtext['disable_column_two']
                    else:
                        econtext['disable_column_two'] = __backup_disable_column_two_140362873331872
                    if (__backup_disable_column_one_140362873334080 is __marker):
                        del econtext['disable_column_one']
                    else:
                        econtext['disable_column_one'] = __backup_disable_column_one_140362873334080
                    if (__backup_controlPanel_140362873334464 is __marker):
                        del econtext['controlPanel']
                    else:
                        econtext['controlPanel'] = __backup_controlPanel_140362873334464
                    if (__backup_dummy_140362873135840 is __marker):
                        del econtext['dummy']
                    else:
                        econtext['dummy'] = __backup_dummy_140362873135840
                    __append('\n        ')
                else:
                    __slot_top_slot(__stream, econtext.copy(), rcontext)
                __append('\n    ')
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_content(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872912384
                __attrs_140362872912384 = _static_140362943909360
                __append('\n        ')
                if (__slot_prefs_configlet_wrapper is None):

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872981392
                    __attrs_140362872981392 = _static_140362943909360
                    __append('\n          ')
                    if (__slot_prefs_configlet_content is None):

                        # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872980192
                        __attrs_140362872980192 = _static_140362943909360
                        __append('\n\n            ')

                        # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873012128
                        __attrs_140362873012128 = _static_140362943909360
                        __backup_macroname_140362919099712 = get('macroname', __marker)

                        # <Static value=<ast.Constant object at 0x7fa8c72f71f0> name=None at 7fa8c72f7220> -> __value
                        __value = _static_140362873008624
                        econtext['macroname'] = __value

                        def __fill_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                            getname = econtext.get_name
                            get = econtext.get

                            # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873008240
                            __attrs_140362873008240 = _static_140362943909360
                            __append('\n\n                ')

                            # <Static value=<ast.Dict object at 0x7fa8c72f7970> name=None at 7fa8c72f7910> -> __attrs_140362873009536
                            __attrs_140362873009536 = _static_140362873010544
                            __backup_controlPanel_140362873129328 = get('controlPanel', __marker)

                            # <Value "python:modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')" (21:46)> -> __value
                            __token = 1074
                            try:
                                __zt_tmp = __attrs_140362873009536
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140362943564528('python', "modules['Products.CMFCore.utils'].getToolByName(here, 'portal_controlpanel')", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                            econtext['controlPanel'] = __value
                            __backup_groups_140362873079024 = get('groups', __marker)

                            # <Value "python:controlPanel.getGroups('site')" (22:39)> -> __value
                            __token = 1198
                            try:
                                __zt_tmp = __attrs_140362873009536
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140362943564528('python', "controlPanel.getGroups('site')", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                            econtext['groups'] = __value
                            __backup_site_url_140362873089184 = get('site_url', __marker)

                            # <Value 'controlPanel/site_url' (23:40)> -> __value
                            __token = 1278
                            try:
                                __zt_tmp = __attrs_140362873009536
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140362943564528('path', 'controlPanel/site_url', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                            econtext['site_url'] = __value
                            __backup_current_url_140362873137232 = get('current_url', __marker)

                            # <Value 'request/URL' (24:42)> -> __value
                            __token = 1345
                            try:
                                __zt_tmp = __attrs_140362873009536
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140362943564528('path', 'request/URL', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                            econtext['current_url'] = __value

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="mb-3">\n                  ')

                            # <Static value=<ast.Dict object at 0x7fa8c725fdc0> name=None at 7fa8c725fd90> -> __attrs_140362872388672
                            __attrs_140362872388672 = _static_140362872389056

                            # <ul ... (0:0)
                            # --------------------------------------------------------
                            __append('<ul class="nav nav-tabs">\n                    ')

                            # <Static value=<ast.Dict object at 0x7fa8c725f250> name=None at 7fa8c725f0a0> -> __attrs_140362872387088
                            __attrs_140362872387088 = _static_140362872386128
                            __backup_overview_url_140362873063072 = get('overview_url', __marker)

                            # <Value 'string:$portal_url/@@overview-controlpanel' (27:49)> -> __value
                            __token = 1496
                            try:
                                __zt_tmp = __attrs_140362872387088
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140362943564528('string', '$portal_url/@@overview-controlpanel', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                            econtext['overview_url'] = __value

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append('<li class="nav-item">\n                      ')

                            # <Static value=<ast.Dict object at 0x7fa8c724f160> name=None at 7fa8c724f610> -> __attrs_140362872324000
                            __attrs_140362872324000 = _static_140362872320352

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a')

                            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872321504
                            __default_140362872321504 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution "nav-link ${python:'active' if overview_url in current_url else ''}" (28:32)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c724f670> -> __attr_class
                            __token = 1573
                            __token = 1584
                            try:
                                __zt_tmp = __attrs_140362872324000
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_class = _static_140362943564528('python', "'active' if overview_url in current_url else ''", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_class = ('%s%s' % ('nav-link ', (__attr_class if (__attr_class is not None) else ''), ))
                            if (__attr_class is None):
                                pass
                            else:
                                if (__attr_class is _DEFAULT_MARKER):
                                    __attr_class = None
                                else:
                                    __tt = type(__attr_class)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_class = str(__attr_class)
                                    else:
                                        if (__tt is bytes):
                                            __attr_class = decode(__attr_class)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_class = __attr_class.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_class)
                                                    __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                                else:
                                                    __attr_class = __attr_class()
                            if (__attr_class is not None):
                                __append((' class="%s"' % __attr_class))
                            __append(' aria-current="page"')

                            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872322464
                            __default_140362872322464 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${overview_url}' (28:126)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c724fb20> -> __attr_href
                            __token = 1667
                            __token = 1669
                            try:
                                __zt_tmp = __attrs_140362872324000
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_140362943564528('path', 'overview_url', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_href = __attr_href
                            if (__attr_href is None):
                                pass
                            else:
                                if (__attr_href is _DEFAULT_MARKER):
                                    __attr_href = None
                                else:
                                    __tt = type(__attr_href)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_href = str(__attr_href)
                                    else:
                                        if (__tt is bytes):
                                            __attr_href = decode(__attr_href)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_href = __attr_href.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_href)
                                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                                else:
                                                    __attr_href = __attr_href()
                            if (__attr_href is not None):
                                __append((' href="%s"' % __attr_href))
                            __append('>')
                            __stream_140362872387760 = []
                            __append_140362872387760 = __stream_140362872387760.append
                            __append_140362872387760('Site Setup')
                            __msgid_140362872387760 = __re_whitespace(''.join(__stream_140362872387760)).strip()
                            if __msgid_140362872387760:
                                __append(translate(__msgid_140362872387760, mapping=None, default=__msgid_140362872387760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</a>\n                    </li>')
                            if (__backup_overview_url_140362873063072 is __marker):
                                del econtext['overview_url']
                            else:
                                econtext['overview_url'] = __backup_overview_url_140362873063072
                            __append('\n                    ')

                            # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872320832
                            __attrs_140362872320832 = _static_140362943909360
                            __backup_group_140362883150800 = get('group', __marker)

                            # <Value 'groups' (30:49)> -> __iterator
                            __token = 1792
                            try:
                                __zt_tmp = __attrs_140362872320832
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __iterator = _static_140362943564528('path', 'groups', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                            (__iterator, ____index_140362872321408, ) = getname('repeat')('group', __iterator)
                            econtext['group'] = None
                            for __item in __iterator:
                                econtext['group'] = __item
                                __append('\n                      ')

                                # <Static value=<ast.Dict object at 0x7fa8c724f1c0> name=None at 7fa8c724f430> -> __attrs_140362872276112
                                __attrs_140362872276112 = _static_140362872320448
                                __backup_configlets_140362873331968 = get('configlets', __marker)

                                # <Value "python:controlPanel.enumConfiglets(group=group['id'])" (31:49)> -> __value
                                __token = 1850
                                try:
                                    __zt_tmp = __attrs_140362872276112
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_140362943564528('python', "controlPanel.enumConfiglets(group=group['id'])", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                econtext['configlets'] = __value
                                __backup_active_140362883010816 = get('active', __marker)

                                # <Value "python:'active' if bool([c for c in configlets if current_url.startswith(c['url'])]) else 'inactive'" (32:44)> -> __value
                                __token = 1949
                                try:
                                    __zt_tmp = __attrs_140362872276112
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __value = _static_140362943564528('python', "'active' if bool([c for c in configlets if current_url.startswith(c['url'])]) else 'inactive'", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                econtext['active'] = __value

                                # <Value 'python:configlets and controlPanel.maySeeSomeConfiglets' (33:41)> -> __condition
                                __token = 2093
                                try:
                                    __zt_tmp = __attrs_140362872276112
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140362943564528('python', 'configlets and controlPanel.maySeeSomeConfiglets', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                if __condition:

                                    # <li ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<li class="nav-item dropdown">\n                        ')

                                    # <Static value=<ast.Dict object at 0x7fa8c72447f0> name=None at 7fa8c7244250> -> __attrs_140362872277168
                                    __attrs_140362872277168 = _static_140362872276976

                                    # <a ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<a')

                                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872275008
                                    __default_140362872275008 = _DEFAULT_MARKER

                                    # <Interpolation value=<Substitution 'nav-link dropdown-toggle ${active}' (35:34)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c7244220> -> __attr_class
                                    __token = 2237
                                    __token = 2264
                                    try:
                                        __zt_tmp = __attrs_140362872277168
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_class = _static_140362943564528('path', 'active', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_class = ('%s%s' % ('nav-link dropdown-toggle ', (__attr_class if (__attr_class is not None) else ''), ))
                                    if (__attr_class is None):
                                        pass
                                    else:
                                        if (__attr_class is _DEFAULT_MARKER):
                                            __attr_class = None
                                        else:
                                            __tt = type(__attr_class)
                                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                __attr_class = str(__attr_class)
                                            else:
                                                if (__tt is bytes):
                                                    __attr_class = decode(__attr_class)
                                                else:
                                                    if (__tt is not str):
                                                        try:
                                                            __attr_class = __attr_class.__html__
                                                        except get('AttributeError', AttributeError):
                                                            __converted = convert(__attr_class)
                                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                                        else:
                                                            __attr_class = __attr_class()
                                    if (__attr_class is not None):
                                        __append((' class="%s"' % __attr_class))
                                    __append(' data-bs-toggle="dropdown" href="#" role="button" aria-expanded="false">')

                                    # <Interpolation value=<Substitution '${group/title}' (35:141)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c7244700> -> __content_140363024536688
                                    __token = 2344
                                    __token = 2346
                                    try:
                                        __zt_tmp = __attrs_140362872277168
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __content_140363024536688 = _static_140362943564528('path', 'group/title', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
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
                                    __append('</a>\n                          ')

                                    # <Static value=<ast.Dict object at 0x7fa8c732de80> name=None at 7fa8c732d9d0> -> __attrs_140362873231728
                                    __attrs_140362873231728 = _static_140362873233024

                                    # <ul ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<ul class="dropdown-menu">\n                          ')

                                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873230144
                                    __attrs_140362873230144 = _static_140362943909360
                                    __backup_configlet_140362883094512 = get('configlet', __marker)

                                    # <Value 'configlets' (37:58)> -> __iterator
                                    __token = 2474
                                    try:
                                        __zt_tmp = __attrs_140362873230144
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __iterator = _static_140362943564528('path', 'configlets', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                    (__iterator, ____index_140362873232832, ) = getname('repeat')('configlet', __iterator)
                                    econtext['configlet'] = None
                                    for __item in __iterator:
                                        econtext['configlet'] = __item
                                        __append('\n                            ')

                                        # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873232640
                                        __attrs_140362873232640 = _static_140362943909360

                                        # <Value 'configlet/visible' (38:47)> -> __condition
                                        __token = 2534
                                        try:
                                            __zt_tmp = __attrs_140362873232640
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __condition = _static_140362943564528('path', 'configlet/visible', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                        if __condition:

                                            # <li ... (0:0)
                                            # --------------------------------------------------------
                                            __append('<li>\n                              ')

                                            # <Static value=<ast.Dict object at 0x7fa8c732d3d0> name=None at 7fa8c732d0d0> -> __attrs_140362872267680
                                            __attrs_140362872267680 = _static_140362873230288
                                            __backup_icon_url_140362873786624 = get('icon_url', __marker)

                                            # <Value "python:'http' in configlet['icon']" (39:54)> -> __value
                                            __token = 2608
                                            try:
                                                __zt_tmp = __attrs_140362872267680
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __value = _static_140362943564528('python', "'http' in configlet['icon']", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                            econtext['icon_url'] = __value

                                            # <a ... (0:0)
                                            # --------------------------------------------------------
                                            __append('<a class="dropdown-item"')

                                            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872268448
                                            __default_140362872268448 = _DEFAULT_MARKER

                                            # <Interpolation value=<Substitution '${configlet/url}' (41:39)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c7242490> -> __attr_href
                                            __token = 2738
                                            __token = 2740
                                            try:
                                                __zt_tmp = __attrs_140362872267680
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __attr_href = _static_140362943564528('path', 'configlet/url', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                                            __attr_href = __attr_href
                                            if (__attr_href is None):
                                                pass
                                            else:
                                                if (__attr_href is _DEFAULT_MARKER):
                                                    __attr_href = None
                                                else:
                                                    __tt = type(__attr_href)
                                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                                        __attr_href = str(__attr_href)
                                                    else:
                                                        if (__tt is bytes):
                                                            __attr_href = decode(__attr_href)
                                                        else:
                                                            if (__tt is not str):
                                                                try:
                                                                    __attr_href = __attr_href.__html__
                                                                except get('AttributeError', AttributeError):
                                                                    __converted = convert(__attr_href)
                                                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                                                else:
                                                                    __attr_href = __attr_href()
                                            if (__attr_href is not None):
                                                __append((' href="%s"' % __attr_href))
                                            __append('>\n                                ')

                                            # <Static value=<ast.Dict object at 0x7fa8c7242e80> name=None at 7fa8c72427c0> -> __attrs_140362872269024
                                            __attrs_140362872269024 = _static_140362872270464

                                            # <Value 'icon_url' (42:52)> -> __condition
                                            __token = 2809
                                            try:
                                                __zt_tmp = __attrs_140362872269024
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __condition = _static_140362943564528('path', 'icon_url', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                            if __condition:

                                                # <img ... (0:0)
                                                # --------------------------------------------------------
                                                __append('<img')

                                                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872269216
                                                __default_140362872269216 = _DEFAULT_MARKER

                                                # <Substitution 'configlet/icon' (44:56)> -> __attr_src
                                                __token = 2938
                                                try:
                                                    __zt_tmp = __attrs_140362872269024
                                                except get('NameError', NameError):
                                                    __zt_tmp = None

                                                __attr_src = _static_140362943564528('path', 'configlet/icon', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                                __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                                                if (__attr_src is not None):
                                                    __append((' src="%s"' % __attr_src))

                                                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872269840
                                                __default_140362872269840 = _DEFAULT_MARKER

                                                # <Translate msgid=None node=<Substitution 'configlet/title' (45:55)> at 7fa8c7242280> -> __attr_alt

                                                # <Substitution 'configlet/title' (45:55)> -> __attr_alt
                                                __token = 3009
                                                try:
                                                    __zt_tmp = __attrs_140362872269024
                                                except get('NameError', NameError):
                                                    __zt_tmp = None

                                                __attr_alt = _static_140362943564528('path', 'configlet/title', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                                __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                                                __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                                if (__attr_alt is not None):
                                                    __append((' alt="%s"' % __attr_alt))
                                                __append(' class="icon">')
                                            __append('\n                                ')

                                            # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872289216
                                            __attrs_140362872289216 = _static_140362943909360

                                            # <Value 'not: icon_url' (47:57)> -> __condition
                                            __token = 3143
                                            try:
                                                __zt_tmp = __attrs_140362872289216
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __condition = _static_140362943564528('not', ' icon_url', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                            if __condition:

                                                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872287584
                                                __default_140362872287584 = _DEFAULT_MARKER

                                                # <Value "python:icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])" (48:65)> -> __cache_140362872287344
                                                __token = 3223
                                                try:
                                                    __zt_tmp = __attrs_140362872289216
                                                except get('NameError', NameError):
                                                    __zt_tmp = None

                                                __cache_140362872287344 = _static_140362943564528('python', "icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                                                # <BinOp left=<Value "python:icons.tag(configlet['icon'] or 'plone-controlpanel', tag_alt=configlet['title'])" (48:65)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c7247940> -> __condition
                                                __expression = __cache_140362872287344

                                                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                                                __value = _DEFAULT_MARKER
                                                __condition = (__expression is __value)
                                                if __condition:
                                                    pass
                                                else:
                                                    __content = __cache_140362872287344
                                                    __content = __convert(__content)
                                                    if (__content is not None):
                                                        __append(__content)

                                            # <Interpolation value=<Substitution '\n                                ${configlet/title}\n                              ' (48:156)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c7247400> -> __content_140363024536688
                                            __token = 3347
                                            __token = 3349
                                            try:
                                                __zt_tmp = __attrs_140362872267680
                                            except get('NameError', NameError):
                                                __zt_tmp = None

                                            __content_140363024536688 = _static_140362943564528('path', 'configlet/title', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                                            __content_140363024536688 = __quote(__content_140363024536688, '\x00', '&#0;', None, None)
                                            __content_140363024536688 = ('%s%s%s' % ('\n                                ', (__content_140363024536688 if (__content_140363024536688 is not None) else ''), '\n                              ', ))
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
                                            __append('</a>')
                                            if (__backup_icon_url_140362873786624 is __marker):
                                                del econtext['icon_url']
                                            else:
                                                econtext['icon_url'] = __backup_icon_url_140362873786624
                                            __append('\n                            </li>')
                                        __append('\n                          ')
                                        ____index_140362873232832 -= 1
                                        if (____index_140362873232832 > 0):
                                            __append('')
                                    if (__backup_configlet_140362883094512 is __marker):
                                        del econtext['configlet']
                                    else:
                                        econtext['configlet'] = __backup_configlet_140362883094512
                                    __append('\n                        </ul>\n                      </li>')
                                if (__backup_active_140362883010816 is __marker):
                                    del econtext['active']
                                else:
                                    econtext['active'] = __backup_active_140362883010816
                                if (__backup_configlets_140362873331968 is __marker):
                                    del econtext['configlets']
                                else:
                                    econtext['configlets'] = __backup_configlets_140362873331968
                                __append('\n                    ')
                                ____index_140362872321408 -= 1
                                if (____index_140362872321408 > 0):
                                    __append('')
                            if (__backup_group_140362883150800 is __marker):
                                del econtext['group']
                            else:
                                econtext['group'] = __backup_group_140362883150800
                            __append('\n                  </ul>\n                </div>')
                            if (__backup_current_url_140362873137232 is __marker):
                                del econtext['current_url']
                            else:
                                econtext['current_url'] = __backup_current_url_140362873137232
                            if (__backup_site_url_140362873089184 is __marker):
                                del econtext['site_url']
                            else:
                                econtext['site_url'] = __backup_site_url_140362873089184
                            if (__backup_groups_140362873079024 is __marker):
                                del econtext['groups']
                            else:
                                econtext['groups'] = __backup_groups_140362873079024
                            if (__backup_controlPanel_140362873129328 is __marker):
                                del econtext['controlPanel']
                            else:
                                econtext['controlPanel'] = __backup_controlPanel_140362873129328
                            __append('\n\n                ')
                            if (__slot_prefs_configlet_main is None):

                                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873231632
                                __attrs_140362873231632 = _static_140362943909360

                                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873232304
                                __default_140362873232304 = _DEFAULT_MARKER

                                # <Value 'nothing' (59:82)> -> __cache_140362872322080
                                __token = 3694
                                try:
                                    __zt_tmp = __attrs_140362873231632
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140362872322080 = _static_140362943564528('path', 'nothing', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                                # <BinOp left=<Value 'nothing' (59:82)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c724f190> -> __condition
                                __expression = __cache_140362872322080

                                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append('\n                  Page body text\n                ')
                                else:
                                    __content = __cache_140362872322080
                                    __content = __quote(__content, None, '\xad', None, None)
                                    if (__content is not None):
                                        __append(__content)
                            else:
                                __slot_prefs_configlet_main(__stream, econtext.copy(), rcontext)
                            __append('\n\n              ')
                        _slots = econtext['__slot_main'] = _deque((__fill_main, ))

                        # <Value 'context/@@main_template/macros/content' (17:42)> -> __macro
                        __token = 898
                        try:
                            __zt_tmp = __attrs_140362873012128
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __macro = _static_140362943564528('path', 'context/@@main_template/macros/content', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                        __token = 898
                        __m = __macro.include
                        __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                        econtext.update(rcontext)
                        if (__backup_macroname_140362919099712 is __marker):
                            del econtext['macroname']
                        else:
                            econtext['macroname'] = __backup_macroname_140362919099712
                        __append('\n\n          ')
                    else:
                        __slot_prefs_configlet_content(__stream, econtext.copy(), rcontext)
                    __append('\n        ')
                else:
                    __slot_prefs_configlet_wrapper(__stream, econtext.copy(), rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content'] = _deque((__fill_content, ))

            # <Value 'context/@@main_template/macros/master' (2:30)> -> __macro
            __token = 85
            try:
                __zt_tmp = __attrs_140362872911904
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140362943564528('path', 'context/@@main_template/macros/master', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __token = 85
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140362918786816 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140362918786816
            __append('\n')
            __i18n_domain = __previous_i18n_domain_140362872911808
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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
            __token = None
            render_master(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_master': render_master, 'render': render, }