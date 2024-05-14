# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.contentmenu-3.0.4-py3.9.egg/plone/app/contentmenu/contentmenu.pt'

__tokens = {64: ('view/menu', 2, 31), 106: (" python:context.restrictedTraverse('@@iconresolver'", 3, 31), 196: ('s view/toolbar_positi', 4, 36), 282: ('view/available', 6, 35), 374: ('menu', 9, 30), 426: ('menuItem/submenu', 11, 23), 469: (' menuItem/extra/i', 12, 25), 522: ("${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}", 14, 17), 524: ('menuItem/extra/li_class|nothing', 14, 19), 559: ("python:'dropend' if (submenu and toolbar_pos == 'side') else ''", 14, 54), 639: ('${menuItem/extra/id}', 15, 14), 641: ('menuItem/extra/id', 15, 16), 987: ('menuItem/extra/class | nothing', 24, 25), 1043: (" python:'label-%s' % state_class if state_class else '", 25, 24), 688: ("${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}", 18, 18), 690: ("python:'nav-link dropdown-toggle' if submenu else 'nav-link'", 18, 20), 779: ("${python:'false' if submenu else ''}", 19, 26), 781: ("python:'false' if submenu else ''", 19, 28), 1159: ("python:menuItem['action'] or 'javascript:void(0)'", 28, 18), 896: ("${python: 'dropdown' if submenu else ''}", 22, 27), 898: ("python: 'dropdown' if submenu else ''", 22, 29), 1228: (" python:'cursor: default;; pointer-events: none' if not menuItem['action'] else No", 29, 18), 1330: ('le menuItem/descript', 30, 16), 1458: ("python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')", 35, 43), 1630: ('menuItem/title', 38, 31), 1766: ('${state_class}', 43, 25), 1768: ('state_class', 43, 27), 1813: ('menuItem/extra/stateTitle | nothing', 44, 31), 2042: ('submenu | nothing', 54, 27), 2141: ('${menuItem/title}', 58, 14), 2143: ('menuItem/title', 58, 16), 2211: ("python:toolbar_pos == 'top'", 59, 52), 2357: ('menuItem/extra/class | nothing', 62, 36), 2424: (" python:'label-%s' % state_class if state_class else '", 63, 35), 2515: ('e menuItem/extra/stateTitle|nothi', 64, 34), 2613: ('state_title', 66, 37), 2270: ('${state_class}', 60, 29), 2272: ('state_class', 60, 31), 2660: ('${state_title}', 68, 16), 2662: ('state_title', 68, 18), 2810: ('submenu', 73, 38), 2889: ('subMenuItem/extra/class | string:', 75, 37), 3034: ('subMenuItem/extra/separator|nothing', 78, 43), 3144: ('not:subMenuItem/action', 80, 43), 3263: ('is_separator', 83, 35), 3343: ('subMenuItem/title', 85, 48), 3613: ('not:is_separator', 92, 37), 3537: ('nav-link dropdown-item ${extra_class}', 91, 29), 3562: ('extra_class', 91, 54), 3700: ("python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", 94, 51), 3845: ('subMenuItem/title', 95, 48), 4163: ('subMenuItem/action', 104, 32), 4066: ('nav-link dropdown-item ${extra_class}', 102, 24), 4091: ('extra_class', 102, 49), 4241: ('subMenuItem/action', 106, 24), 4285: (' subMenuItem/descriptio', 107, 24), 4331: ('d subMenuItem/extra/id | nothi', 108, 20), 4402: ('al subMenuItem/extra/modal | noth', 109, 37), 4566: ("python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", 114, 49), 4710: ('subMenuItem/title', 116, 46), 4927: ('not:subMenuItem/action', 122, 37), 4874: ('${extra_class}', 121, 29), 4876: ('extra_class', 121, 31), 5017: ('subMenuItem/extra/id | nothing', 124, 27), 5134: ("python:'active' in extra_class", 127, 43), 5217: ("python:icons.tag('check')", 128, 51), 5312: ('subMenuItem/title', 130, 47)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355448967472 = {'class': '${extra_class}', 'id': 'subMenuItem/extra/id | nothing', }
_static_140355449041920 = {'class': 'nav-link dropdown-item ${extra_class}', 'href': '#', 'title': 'subMenuItem/description', 'id': 'subMenuItem/extra/id | nothing', 'data-pat-plone-modal': 'subMenuItem/extra/modal | nothing', }
_static_140355492174720 = {'class': 'nav-link dropdown-item ${extra_class}', }
_static_140355492175776 = {'class': 'dropdown-header', }
_static_140355448785504 = {'class': '${state_class}', }
_static_140355479784560 = {'class': 'dropdown-header', }
_static_140355479782592 = {'class': 'dropdown-menu', }
_static_140355479784416 = {'class': '${state_class}', }
_static_140355449495408 = {'class': 'toolbar-label', }
_static_140355469362272 = {'class': "${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}", 'aria-expanded': "${python:'false' if submenu else ''}", 'href': '#', 'data-bs-offset': '0,0', 'data-bs-toggle': "${python: 'dropdown' if submenu else ''}", 'style': "python:'cursor: default; pointer-events: none' if not menuItem['action'] else None", 'title': 'menuItem/description', }
_static_140355449231104 = {'class': "${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}", 'id': '${menuItem/extra/id}', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355540704128 = {}

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

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355480696000
            __attrs_140355480696000 = _static_140355540704128
            __backup_menu_140355449015840 = get('menu', __marker)

            # <Value 'view/menu' (2:31)> -> __value
            __token = 64
            try:
                __zt_tmp = __attrs_140355480696000
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/menu', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['menu'] = __value
            __backup_icons_140355449430176 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (3:31)> -> __value
            __token = 106
            try:
                __zt_tmp = __attrs_140355480696000
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_toolbar_pos_140355449401408 = get('toolbar_pos', __marker)

            # <Value 'view/toolbar_position' (4:36)> -> __value
            __token = 196
            try:
                __zt_tmp = __attrs_140355480696000
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/toolbar_position', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['toolbar_pos'] = __value

            # <Value 'view/available' (6:35)> -> __condition
            __token = 282
            try:
                __zt_tmp = __attrs_140355480696000
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'view/available', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140355481087712 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449231536
                __attrs_140355449231536 = _static_140355540704128
                __backup_menuItem_140355449698432 = get('menuItem', __marker)

                # <Value 'menu' (9:30)> -> __iterator
                __token = 374
                try:
                    __zt_tmp = __attrs_140355449231536
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140355540363392('path', 'menu', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                (__iterator, ____index_140355449233168, ) = getname('repeat')('menuItem', __iterator)
                econtext['menuItem'] = None
                for __item in __iterator:
                    econtext['menuItem'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449229904
                    __attrs_140355449229904 = _static_140355540704128
                    __backup_submenu_140355449015936 = get('submenu', __marker)

                    # <Value 'menuItem/submenu' (11:23)> -> __value
                    __token = 426
                    try:
                        __zt_tmp = __attrs_140355449229904
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'menuItem/submenu', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['submenu'] = __value
                    __backup_identifier_140355479783888 = get('identifier', __marker)

                    # <Value 'menuItem/extra/id' (12:25)> -> __value
                    __token = 469
                    try:
                        __zt_tmp = __attrs_140355449229904
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'menuItem/extra/id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['identifier'] = __value
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7fa70cb19700> name=None at 7fa70cb19430> -> __attrs_140355448975072
                    __attrs_140355448975072 = _static_140355449231104

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448975216
                    __default_140355448975216 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${menuItem/extra/li_class|nothing} ${python:'dropend' if (submenu and toolbar_pos == 'side') else ''}" (14:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cadab80> -> __attr_class
                    __token = 522
                    __token = 524
                    try:
                        __zt_tmp = __attrs_140355448975072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140355540363392('path', 'menuItem/extra/li_class|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __token = 559
                    try:
                        __zt_tmp = __attrs_140355448975072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class_557 = _static_140355540363392('python', "'dropend' if (submenu and toolbar_pos == 'side') else ''", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_class_557 = __quote(__attr_class_557, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s%s' % ((__attr_class if (__attr_class is not None) else ''), ' ', (__attr_class_557 if (__attr_class_557 is not None) else ''), ))
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

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448974160
                    __default_140355448974160 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${menuItem/extra/id}' (15:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cada610> -> __attr_id
                    __token = 639
                    __token = 641
                    try:
                        __zt_tmp = __attrs_140355448975072
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140355540363392('path', 'menuItem/extra/id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_id = __attr_id
                    if (__attr_id is None):
                        pass
                    else:
                        if (__attr_id is _DEFAULT_MARKER):
                            __attr_id = None
                        else:
                            __tt = type(__attr_id)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_id = str(__attr_id)
                            else:
                                if (__tt is bytes):
                                    __attr_id = decode(__attr_id)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_id = __attr_id.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_id)
                                            __attr_id = (str(__attr_id) if (__attr_id is __converted) else __converted)
                                        else:
                                            __attr_id = __attr_id()
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append(' >\n\n        ')

                    # <Static value=<ast.Dict object at 0x7fa70de4c460> name=None at 7fa70de4c4c0> -> __attrs_140355482521408
                    __attrs_140355482521408 = _static_140355469362272
                    __backup_state_class_140355449233216 = get('state_class', __marker)

                    # <Value 'menuItem/extra/class | nothing' (24:25)> -> __value
                    __token = 987
                    try:
                        __zt_tmp = __attrs_140355482521408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'menuItem/extra/class | nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['state_class'] = __value
                    __backup_state_class_140355449232976 = get('state_class', __marker)

                    # <Value "python:'label-%s' % state_class if state_class else ''" (25:24)> -> __value
                    __token = 1043
                    try:
                        __zt_tmp = __attrs_140355482521408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('python', "'label-%s' % state_class if state_class else ''", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['state_class'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448971328
                    __default_140355448971328 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:'nav-link dropdown-toggle' if submenu else 'nav-link'}" (18:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cada4c0> -> __attr_class
                    __token = 688
                    __token = 690
                    try:
                        __zt_tmp = __attrs_140355482521408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140355540363392('python', "'nav-link dropdown-toggle' if submenu else 'nav-link'", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = __attr_class
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

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355482518816
                    __default_140355482518816 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:'false' if submenu else ''}" (19:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cada190> -> __attr_aria_expanded
                    __token = 779
                    __token = 781
                    try:
                        __zt_tmp = __attrs_140355482521408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_aria_expanded = _static_140355540363392('python', "'false' if submenu else ''", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_aria_expanded = __quote(__attr_aria_expanded, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_aria_expanded = __attr_aria_expanded
                    if (__attr_aria_expanded is None):
                        pass
                    else:
                        if (__attr_aria_expanded is _DEFAULT_MARKER):
                            __attr_aria_expanded = None
                        else:
                            __tt = type(__attr_aria_expanded)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_aria_expanded = str(__attr_aria_expanded)
                            else:
                                if (__tt is bytes):
                                    __attr_aria_expanded = decode(__attr_aria_expanded)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_aria_expanded = __attr_aria_expanded.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_aria_expanded)
                                            __attr_aria_expanded = (str(__attr_aria_expanded) if (__attr_aria_expanded is __converted) else __converted)
                                        else:
                                            __attr_aria_expanded = __attr_aria_expanded()
                    if (__attr_aria_expanded is not None):
                        __append((' aria-expanded="%s"' % __attr_aria_expanded))

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355482520640
                    __default_140355482520640 = _DEFAULT_MARKER

                    # <Substitution "python:menuItem['action'] or 'javascript:void(0)'" (28:18)> -> __attr_href
                    __token = 1159
                    try:
                        __zt_tmp = __attrs_140355482521408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140355540363392('python', "menuItem['action'] or 'javascript:void(0)'", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' data-bs-offset="0,0"')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355482520928
                    __default_140355482520928 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python: 'dropdown' if submenu else ''}" (22:27)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70ead87f0> -> __attr_data_bs_toggle
                    __token = 896
                    __token = 898
                    try:
                        __zt_tmp = __attrs_140355482521408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_data_bs_toggle = _static_140355540363392('python', " 'dropdown' if submenu else ''", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_data_bs_toggle = __quote(__attr_data_bs_toggle, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_data_bs_toggle = __attr_data_bs_toggle
                    if (__attr_data_bs_toggle is None):
                        pass
                    else:
                        if (__attr_data_bs_toggle is _DEFAULT_MARKER):
                            __attr_data_bs_toggle = None
                        else:
                            __tt = type(__attr_data_bs_toggle)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_data_bs_toggle = str(__attr_data_bs_toggle)
                            else:
                                if (__tt is bytes):
                                    __attr_data_bs_toggle = decode(__attr_data_bs_toggle)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_data_bs_toggle = __attr_data_bs_toggle.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_data_bs_toggle)
                                            __attr_data_bs_toggle = (str(__attr_data_bs_toggle) if (__attr_data_bs_toggle is __converted) else __converted)
                                        else:
                                            __attr_data_bs_toggle = __attr_data_bs_toggle()
                    if (__attr_data_bs_toggle is not None):
                        __append((' data-bs-toggle="%s"' % __attr_data_bs_toggle))

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355482518096
                    __default_140355482518096 = _DEFAULT_MARKER

                    # <Substitution "python:'cursor: default; pointer-events: none' if not menuItem['action'] else None" (29:18)> -> __attr_style
                    __token = 1228
                    try:
                        __zt_tmp = __attrs_140355482521408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_style = _static_140355540363392('python', "'cursor: default; pointer-events: none' if not menuItem['action'] else None", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_style is not None):
                        __append((' style="%s"' % __attr_style))

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355482521072
                    __default_140355482521072 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<Substitution 'menuItem/description' (30:16)> at 7fa70ead8b20> -> __attr_title

                    # <Substitution 'menuItem/description' (30:16)> -> __attr_title
                    __token = 1330
                    try:
                        __zt_tmp = __attrs_140355482521408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140355540363392('path', 'menuItem/description', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' >\n\n          ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449492048
                    __attrs_140355449492048 = _static_140355540704128

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449493920
                    __default_140355449493920 = _DEFAULT_MARKER

                    # <Value "python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')" (35:43)> -> __cache_140355449491904
                    __token = 1458
                    try:
                        __zt_tmp = __attrs_140355449492048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355449491904 = _static_140355540363392('python', "icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag(menuItem.get('icon','') and menuItem['icon'] or 'toolbar-action', tag_class='')" (35:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb59d00> -> __condition
                    __expression = __cache_140355449491904

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355449491904
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x7fa70cb59f70> name=None at 7fa70cb59c40> -> __attrs_140355449610784
                    __attrs_140355449610784 = _static_140355449495408

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="toolbar-label">\n            ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449611408
                    __attrs_140355449611408 = _static_140355540704128

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449611120
                    __default_140355449611120 = _DEFAULT_MARKER

                    # <Value 'menuItem/title' (38:31)> -> __cache_140355449613520
                    __token = 1630
                    try:
                        __zt_tmp = __attrs_140355449611408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355449613520 = _static_140355540363392('path', 'menuItem/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'menuItem/title' (38:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb76c70> -> __condition
                    __expression = __cache_140355449613520

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span >\n              Menu Title\n            </span>')
                    else:
                        __content = __cache_140355449613520
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7fa70e83cbe0> name=None at 7fa70cb76a60> -> __attrs_140355479782208
                    __attrs_140355479782208 = _static_140355479784416

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355479783600
                    __default_140355479783600 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${state_class}' (43:25)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cadafa0> -> __attr_class
                    __token = 1766
                    __token = 1768
                    try:
                        __zt_tmp = __attrs_140355479782208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140355540363392('path', 'state_class', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = __attr_class
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
                    __append(' >')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449611456
                    __default_140355449611456 = _DEFAULT_MARKER

                    # <Value 'menuItem/extra/stateTitle | nothing' (44:31)> -> __cache_140355449613904
                    __token = 1813
                    try:
                        __zt_tmp = __attrs_140355479782208
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355449613904 = _static_140355540363392('path', 'menuItem/extra/stateTitle | nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'menuItem/extra/stateTitle | nothing' (44:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb76790> -> __condition
                    __expression = __cache_140355449613904

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                State title\n            ')
                    else:
                        __content = __cache_140355449613904
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n          </span>\n\n        </a>')
                    if (__backup_state_class_140355449232976 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_140355449232976
                    if (__backup_state_class_140355449233216 is __marker):
                        del econtext['state_class']
                    else:
                        econtext['state_class'] = __backup_state_class_140355449233216
                    __append('\n\n        ')

                    # <Static value=<ast.Dict object at 0x7fa70e83c4c0> name=None at 7fa70e83c4f0> -> __attrs_140355479783648
                    __attrs_140355479783648 = _static_140355479782592

                    # <Value 'submenu | nothing' (54:27)> -> __condition
                    __token = 2042
                    try:
                        __zt_tmp = __attrs_140355479783648
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('path', 'submenu | nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:

                        # <ul ... (0:0)
                        # --------------------------------------------------------
                        __append('<ul class="dropdown-menu" >\n          ')

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355479784848
                        __attrs_140355479784848 = _static_140355540704128

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n            ')

                        # <Static value=<ast.Dict object at 0x7fa70e83cc70> name=None at 7fa70e83c910> -> __attrs_140355448784400
                        __attrs_140355448784400 = _static_140355479784560

                        # <h6 ... (0:0)
                        # --------------------------------------------------------
                        __append('<h6 class="dropdown-header">')

                        # <Interpolation value=<Substitution '\n              ${menuItem/title}\n              ' (57:40)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70caac580> -> __content_140355621335664
                        __token = 2141
                        __token = 2143
                        try:
                            __zt_tmp = __attrs_140355448784400
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_140355621335664 = _static_140355540363392('path', 'menuItem/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        __content_140355621335664 = __quote(__content_140355621335664, '\x00', '&#0;', None, None)
                        __content_140355621335664 = ('%s%s%s' % ('\n              ', (__content_140355621335664 if (__content_140355621335664 is not None) else ''), '\n              ', ))
                        if (__content_140355621335664 is None):
                            pass
                        else:
                            if (__content_140355621335664 is None):
                                __content_140355621335664 = None
                            else:
                                __tt = type(__content_140355621335664)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __content_140355621335664 = str(__content_140355621335664)
                                else:
                                    if (__tt is bytes):
                                        __content_140355621335664 = decode(__content_140355621335664)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __content_140355621335664 = __content_140355621335664.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__content_140355621335664)
                                                __content_140355621335664 = (str(__content_140355621335664) if (__content_140355621335664 is __converted) else __converted)
                                            else:
                                                __content_140355621335664 = __content_140355621335664()
                        if (__content_140355621335664 is not None):
                            __append(__content_140355621335664)

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448783440
                        __attrs_140355448783440 = _static_140355540704128

                        # <Value "python:toolbar_pos == 'top'" (59:52)> -> __condition
                        __token = 2211
                        try:
                            __zt_tmp = __attrs_140355448783440
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140355540363392('python', "toolbar_pos == 'top'", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        if __condition:
                            __append('\n                ')

                            # <Static value=<ast.Dict object at 0x7fa70caaca60> name=None at 7fa70caacfa0> -> __attrs_140355448786080
                            __attrs_140355448786080 = _static_140355448785504
                            __backup_state_class_140355492174672 = get('state_class', __marker)

                            # <Value 'menuItem/extra/class | nothing' (62:36)> -> __value
                            __token = 2357
                            try:
                                __zt_tmp = __attrs_140355448786080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140355540363392('path', 'menuItem/extra/class | nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            econtext['state_class'] = __value
                            __backup_state_class_140355492172416 = get('state_class', __marker)

                            # <Value "python:'label-%s' % state_class if state_class else ''" (63:35)> -> __value
                            __token = 2424
                            try:
                                __zt_tmp = __attrs_140355448786080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140355540363392('python', "'label-%s' % state_class if state_class else ''", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            econtext['state_class'] = __value
                            __backup_state_title_140355492174864 = get('state_title', __marker)

                            # <Value 'menuItem/extra/stateTitle|nothing' (64:34)> -> __value
                            __token = 2515
                            try:
                                __zt_tmp = __attrs_140355448786080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140355540363392('path', 'menuItem/extra/stateTitle|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            econtext['state_title'] = __value

                            # <Value 'state_title' (66:37)> -> __condition
                            __token = 2613
                            try:
                                __zt_tmp = __attrs_140355448786080
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140355540363392('path', 'state_title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span')

                                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448785024
                                __default_140355448785024 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution '${state_class}' (60:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70caacd30> -> __attr_class
                                __token = 2270
                                __token = 2272
                                try:
                                    __zt_tmp = __attrs_140355448786080
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140355540363392('path', 'state_class', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_class = __attr_class
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
                                __append(' >')

                                # <Interpolation value=<Substitution '\n                ${state_title}\n                ' (67:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70eaf70d0> -> __content_140355621335664
                                __token = 2660
                                __token = 2662
                                try:
                                    __zt_tmp = __attrs_140355448786080
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_140355621335664 = _static_140355540363392('path', 'state_title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                __content_140355621335664 = __quote(__content_140355621335664, '\x00', '&#0;', None, None)
                                __content_140355621335664 = ('%s%s%s' % ('\n                ', (__content_140355621335664 if (__content_140355621335664 is not None) else ''), '\n                ', ))
                                if (__content_140355621335664 is None):
                                    pass
                                else:
                                    if (__content_140355621335664 is None):
                                        __content_140355621335664 = None
                                    else:
                                        __tt = type(__content_140355621335664)
                                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                                            __content_140355621335664 = str(__content_140355621335664)
                                        else:
                                            if (__tt is bytes):
                                                __content_140355621335664 = decode(__content_140355621335664)
                                            else:
                                                if (__tt is not str):
                                                    try:
                                                        __content_140355621335664 = __content_140355621335664.__html__
                                                    except get('AttributeError', AttributeError):
                                                        __converted = convert(__content_140355621335664)
                                                        __content_140355621335664 = (str(__content_140355621335664) if (__content_140355621335664 is __converted) else __converted)
                                                    else:
                                                        __content_140355621335664 = __content_140355621335664()
                                if (__content_140355621335664 is not None):
                                    __append(__content_140355621335664)
                                __append('</span>')
                            if (__backup_state_title_140355492174864 is __marker):
                                del econtext['state_title']
                            else:
                                econtext['state_title'] = __backup_state_title_140355492174864
                            if (__backup_state_class_140355492172416 is __marker):
                                del econtext['state_class']
                            else:
                                econtext['state_class'] = __backup_state_class_140355492172416
                            if (__backup_state_class_140355492174672 is __marker):
                                del econtext['state_class']
                            else:
                                econtext['state_class'] = __backup_state_class_140355492174672
                            __append('\n              ')
                        __append('\n            </h6>\n          </li>\n          ')

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355482646320
                        __attrs_140355482646320 = _static_140355540704128
                        __backup_subMenuItem_140355449430320 = get('subMenuItem', __marker)

                        # <Value 'submenu' (73:38)> -> __iterator
                        __token = 2810
                        try:
                            __zt_tmp = __attrs_140355482646320
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140355540363392('path', 'submenu', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        (__iterator, ____index_140355482646608, ) = getname('repeat')('subMenuItem', __iterator)
                        econtext['subMenuItem'] = None
                        for __item in __iterator:
                            econtext['subMenuItem'] = __item

                            # <li ... (0:0)
                            # --------------------------------------------------------
                            __append('<li>\n            ')

                            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355482645072
                            __attrs_140355482645072 = _static_140355540704128
                            __backup_extra_class_140355449459280 = get('extra_class', __marker)

                            # <Value 'subMenuItem/extra/class | string:' (75:37)> -> __value
                            __token = 2889
                            try:
                                __zt_tmp = __attrs_140355482645072
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140355540363392('path', 'subMenuItem/extra/class | string:', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            econtext['extra_class'] = __value
                            __append('\n              ')

                            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355482648336
                            __attrs_140355482648336 = _static_140355540704128
                            __backup_is_separator_140355479783264 = get('is_separator', __marker)

                            # <Value 'subMenuItem/extra/separator|nothing' (78:43)> -> __value
                            __token = 3034
                            try:
                                __zt_tmp = __attrs_140355482648336
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __value = _static_140355540363392('path', 'subMenuItem/extra/separator|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            econtext['is_separator'] = __value

                            # <Value 'not:subMenuItem/action' (80:43)> -> __condition
                            __token = 3144
                            try:
                                __zt_tmp = __attrs_140355482648336
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140355540363392('not', 'subMenuItem/action', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            if __condition:
                                __append('\n                ')

                                # <Static value=<ast.Dict object at 0x7fa70f40dfa0> name=None at 7fa70f40dfd0> -> __attrs_140355492174240
                                __attrs_140355492174240 = _static_140355492175776

                                # <Value 'is_separator' (83:35)> -> __condition
                                __token = 3263
                                try:
                                    __zt_tmp = __attrs_140355492174240
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140355540363392('path', 'is_separator', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                if __condition:

                                    # <h6 ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<h6 class="dropdown-header" >\n                  ')

                                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355492172224
                                    __attrs_140355492172224 = _static_140355540704128

                                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355492172368
                                    __default_140355492172368 = _DEFAULT_MARKER

                                    # <Value 'subMenuItem/title' (85:48)> -> __cache_140355492172512
                                    __token = 3343
                                    try:
                                        __zt_tmp = __attrs_140355492172224
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140355492172512 = _static_140355540363392('path', 'subMenuItem/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                                    # <BinOp left=<Value 'subMenuItem/title' (85:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70f40d5e0> -> __condition
                                    __expression = __cache_140355492172512

                                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        __append('\n                    Title\n                  ')
                                    else:
                                        __content = __cache_140355492172512
                                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                </h6>')
                                __append('\n                ')

                                # <Static value=<ast.Dict object at 0x7fa70f40db80> name=None at 7fa70f40d070> -> __attrs_140355449041392
                                __attrs_140355449041392 = _static_140355492174720

                                # <Value 'not:is_separator' (92:37)> -> __condition
                                __token = 3613
                                try:
                                    __zt_tmp = __attrs_140355449041392
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140355540363392('not', 'is_separator', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                if __condition:

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<span')

                                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355492173376
                                    __default_140355492173376 = _DEFAULT_MARKER

                                    # <Interpolation value=<Substitution 'nav-link dropdown-item ${extra_class}' (91:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70f40d100> -> __attr_class
                                    __token = 3537
                                    __token = 3562
                                    try:
                                        __zt_tmp = __attrs_140355449041392
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_class = _static_140355540363392('path', 'extra_class', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_class = ('%s%s' % ('nav-link dropdown-item ', (__attr_class if (__attr_class is not None) else ''), ))
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
                                    __append(' >\n                  ')

                                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449044608
                                    __attrs_140355449044608 = _static_140355540704128

                                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449044320
                                    __default_140355449044320 = _DEFAULT_MARKER

                                    # <Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (94:51)> -> __cache_140355449042976
                                    __token = 3700
                                    try:
                                        __zt_tmp = __attrs_140355449044608
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140355449042976 = _static_140355540363392('python', "icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                                    # <BinOp left=<Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (94:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70caebd30> -> __condition
                                    __expression = __cache_140355449042976

                                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        pass
                                    else:
                                        __content = __cache_140355449042976
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                  ')

                                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449042832
                                    __attrs_140355449042832 = _static_140355540704128

                                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449043648
                                    __default_140355449043648 = _DEFAULT_MARKER

                                    # <Value 'subMenuItem/title' (95:48)> -> __cache_140355449042112
                                    __token = 3845
                                    try:
                                        __zt_tmp = __attrs_140355449042832
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140355449042112 = _static_140355540363392('path', 'subMenuItem/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                                    # <BinOp left=<Value 'subMenuItem/title' (95:48)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70caebeb0> -> __condition
                                    __expression = __cache_140355449042112

                                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:
                                        __append('\n                    Title\n                  ')
                                    else:
                                        __content = __cache_140355449042112
                                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                </span>')
                                __append('\n              ')
                            if (__backup_is_separator_140355479783264 is __marker):
                                del econtext['is_separator']
                            else:
                                econtext['is_separator'] = __backup_is_separator_140355479783264
                            __append('\n              ')

                            # <Static value=<ast.Dict object at 0x7fa70caeb400> name=None at 7fa70caeb5e0> -> __attrs_140355449073616
                            __attrs_140355449073616 = _static_140355449041920

                            # <Value 'subMenuItem/action' (104:32)> -> __condition
                            __token = 4163
                            try:
                                __zt_tmp = __attrs_140355449073616
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140355540363392('path', 'subMenuItem/action', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            if __condition:

                                # <a ... (0:0)
                                # --------------------------------------------------------
                                __append('<a')

                                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355482646128
                                __default_140355482646128 = _DEFAULT_MARKER

                                # <Interpolation value=<Substitution 'nav-link dropdown-item ${extra_class}' (102:24)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70caeb670> -> __attr_class
                                __token = 4066
                                __token = 4091
                                try:
                                    __zt_tmp = __attrs_140355449073616
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_class = _static_140355540363392('path', 'extra_class', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_class = ('%s%s' % ('nav-link dropdown-item ', (__attr_class if (__attr_class is not None) else ''), ))
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

                                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449070496
                                __default_140355449070496 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/action' (106:24)> -> __attr_href
                                __token = 4241
                                try:
                                    __zt_tmp = __attrs_140355449073616
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_href = _static_140355540363392('path', 'subMenuItem/action', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                                if (__attr_href is not None):
                                    __append((' href="%s"' % __attr_href))

                                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449071360
                                __default_140355449071360 = _DEFAULT_MARKER

                                # <Translate msgid=None node=<Substitution 'subMenuItem/description' (107:24)> at 7fa70caf2490> -> __attr_title

                                # <Substitution 'subMenuItem/description' (107:24)> -> __attr_title
                                __token = 4285
                                try:
                                    __zt_tmp = __attrs_140355449073616
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_title = _static_140355540363392('path', 'subMenuItem/description', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                if (__attr_title is not None):
                                    __append((' title="%s"' % __attr_title))

                                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449070784
                                __default_140355449070784 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/extra/id | nothing' (108:20)> -> __attr_id
                                __token = 4331
                                try:
                                    __zt_tmp = __attrs_140355449073616
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_id = _static_140355540363392('path', 'subMenuItem/extra/id | nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_id is not None):
                                    __append((' id="%s"' % __attr_id))

                                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449073232
                                __default_140355449073232 = _DEFAULT_MARKER

                                # <Substitution 'subMenuItem/extra/modal | nothing' (109:37)> -> __attr_data_pat_plone_modal
                                __token = 4402
                                try:
                                    __zt_tmp = __attrs_140355449073616
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __attr_data_pat_plone_modal = _static_140355540363392('path', 'subMenuItem/extra/modal | nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                __attr_data_pat_plone_modal = __quote(__attr_data_pat_plone_modal, '"', '&quot;', None, _DEFAULT_MARKER)
                                if (__attr_data_pat_plone_modal is not None):
                                    __append((' data-pat-plone-modal="%s"' % __attr_data_pat_plone_modal))
                                __append(' >\n\n                ')

                                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448970496
                                __attrs_140355448970496 = _static_140355540704128

                                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449071744
                                __default_140355449071744 = _DEFAULT_MARKER

                                # <Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (114:49)> -> __cache_140355449073136
                                __token = 4566
                                try:
                                    __zt_tmp = __attrs_140355448970496
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140355449073136 = _static_140355540363392('python', "icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                                # <BinOp left=<Value "python:icons.tag('check' if 'active' in extra_class else (subMenuItem.get('icon') or 'dot'))" (114:49)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70caf2430> -> __condition
                                __expression = __cache_140355449073136

                                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    pass
                                else:
                                    __content = __cache_140355449073136
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('\n\n                ')

                                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448967568
                                __attrs_140355448967568 = _static_140355540704128

                                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448967520
                                __default_140355448967520 = _DEFAULT_MARKER

                                # <Value 'subMenuItem/title' (116:46)> -> __cache_140355448970832
                                __token = 4710
                                try:
                                    __zt_tmp = __attrs_140355448967568
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __cache_140355448970832 = _static_140355540363392('path', 'subMenuItem/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                                # <BinOp left=<Value 'subMenuItem/title' (116:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cad99a0> -> __condition
                                __expression = __cache_140355448970832

                                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                                __value = _DEFAULT_MARKER
                                __condition = (__expression is __value)
                                if __condition:
                                    __append('\n                  Title\n                ')
                                else:
                                    __content = __cache_140355448970832
                                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                    __content = __convert(__content)
                                    if (__content is not None):
                                        __append(__content)
                                __append('\n                ')

                                # <Static value=<ast.Dict object at 0x7fa70cad9130> name=None at 7fa70cad9d90> -> __attrs_140355448979520
                                __attrs_140355448979520 = _static_140355448967472

                                # <Value 'not:subMenuItem/action' (122:37)> -> __condition
                                __token = 4927
                                try:
                                    __zt_tmp = __attrs_140355448979520
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __condition = _static_140355540363392('not', 'subMenuItem/action', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                if __condition:

                                    # <span ... (0:0)
                                    # --------------------------------------------------------
                                    __append('<span')

                                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448967664
                                    __default_140355448967664 = _DEFAULT_MARKER

                                    # <Interpolation value=<Substitution '${extra_class}' (121:29)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cad9b80> -> __attr_class
                                    __token = 4874
                                    __token = 4876
                                    try:
                                        __zt_tmp = __attrs_140355448979520
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_class = _static_140355540363392('path', 'extra_class', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                                    __attr_class = __attr_class
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

                                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448970880
                                    __default_140355448970880 = _DEFAULT_MARKER

                                    # <Substitution 'subMenuItem/extra/id | nothing' (124:27)> -> __attr_id
                                    __token = 5017
                                    try:
                                        __zt_tmp = __attrs_140355448979520
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __attr_id = _static_140355540363392('path', 'subMenuItem/extra/id | nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                                    if (__attr_id is not None):
                                        __append((' id="%s"' % __attr_id))
                                    __append(' >\n                  ')

                                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448982832
                                    __attrs_140355448982832 = _static_140355540704128

                                    # <Value "python:'active' in extra_class" (127:43)> -> __condition
                                    __token = 5134
                                    try:
                                        __zt_tmp = __attrs_140355448982832
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __condition = _static_140355540363392('python', "'active' in extra_class", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                    if __condition:

                                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448981872
                                        __default_140355448981872 = _DEFAULT_MARKER

                                        # <Value "python:icons.tag('check')" (128:51)> -> __cache_140355448983408
                                        __token = 5217
                                        try:
                                            __zt_tmp = __attrs_140355448982832
                                        except get('NameError', NameError):
                                            __zt_tmp = None

                                        __cache_140355448983408 = _static_140355540363392('python', "icons.tag('check')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                                        # <BinOp left=<Value "python:icons.tag('check')" (128:51)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cadc820> -> __condition
                                        __expression = __cache_140355448983408

                                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                                        __value = _DEFAULT_MARKER
                                        __condition = (__expression is __value)
                                        if __condition:
                                            pass
                                        else:
                                            __content = __cache_140355448983408
                                            __content = __convert(__content)
                                            if (__content is not None):
                                                __append(__content)
                                    __append('\n                  ')

                                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448980768
                                    __attrs_140355448980768 = _static_140355540704128

                                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448980192
                                    __default_140355448980192 = _DEFAULT_MARKER

                                    # <Value 'subMenuItem/title' (130:47)> -> __cache_140355448983312
                                    __token = 5312
                                    try:
                                        __zt_tmp = __attrs_140355448980768
                                    except get('NameError', NameError):
                                        __zt_tmp = None

                                    __cache_140355448983312 = _static_140355540363392('path', 'subMenuItem/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                                    # <BinOp left=<Value 'subMenuItem/title' (130:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cadc640> -> __condition
                                    __expression = __cache_140355448983312

                                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                                    __value = _DEFAULT_MARKER
                                    __condition = (__expression is __value)
                                    if __condition:

                                        # <span ... (0:0)
                                        # --------------------------------------------------------
                                        __append('<span >\n                    Title\n                  </span>')
                                    else:
                                        __content = __cache_140355448983312
                                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                                        __content = __convert(__content)
                                        if (__content is not None):
                                            __append(__content)
                                    __append('\n                </span>')
                                __append('\n              </a>')
                            __append('\n            ')
                            if (__backup_extra_class_140355449459280 is __marker):
                                del econtext['extra_class']
                            else:
                                econtext['extra_class'] = __backup_extra_class_140355449459280
                            __append('\n          </li>')
                            ____index_140355482646608 -= 1
                            if (____index_140355482646608 > 0):
                                __append('\n          ')
                        if (__backup_subMenuItem_140355449430320 is __marker):
                            del econtext['subMenuItem']
                        else:
                            econtext['subMenuItem'] = __backup_subMenuItem_140355449430320
                        __append('\n        </ul>')
                    __append('\n\n      </li>\n    ')
                    if (__backup_identifier_140355479783888 is __marker):
                        del econtext['identifier']
                    else:
                        econtext['identifier'] = __backup_identifier_140355479783888
                    if (__backup_submenu_140355449015936 is __marker):
                        del econtext['submenu']
                    else:
                        econtext['submenu'] = __backup_submenu_140355449015936
                    __append('\n  ')
                    ____index_140355449233168 -= 1
                    if (____index_140355449233168 > 0):
                        __append('')
                if (__backup_menuItem_140355449698432 is __marker):
                    del econtext['menuItem']
                else:
                    econtext['menuItem'] = __backup_menuItem_140355449698432
                __append('\n')
                __i18n_domain = __previous_i18n_domain_140355481087712
            if (__backup_toolbar_pos_140355449401408 is __marker):
                del econtext['toolbar_pos']
            else:
                econtext['toolbar_pos'] = __backup_toolbar_pos_140355449401408
            if (__backup_icons_140355449430176 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140355449430176
            if (__backup_menu_140355449015840 is __marker):
                del econtext['menu']
            else:
                econtext['menu'] = __backup_menu_140355449015840
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }