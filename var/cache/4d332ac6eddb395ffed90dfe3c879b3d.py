# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/viewlets/toolbar.pt'

__tokens = {94: ('view/context_state', 4, 25), 130: (" python:context.restrictedTraverse('@@iconresolver'", 5, 16), 206: ('r python: view.get_personal_bar', 6, 22), 261: ('os view/toolbar_posit', 7, 20), 322: ('context_state/is_toolbar_visible', 9, 24), 680: ("python:icons.tag('arrow-bar-left')", 25, 41), 875: ("python:icons.tag('arrow-bar-right')", 31, 41), 1033: ('view/base_render', 37, 23), 1084: ('toolbar_main', 39, 23), 1137: ('toolbar_main', 41, 33), 1295: ('personal_bar/user_actions', 46, 24), 1191: ("personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}", 45, 16), 1219: ("python:'dropend' if toolbar_pos == 'side' else ''", 45, 44), 1546: ('personal_bar/homelink_url', 55, 16), 1633: ("python:icons.tag('toolbar-action/personaltools', tag_class='')", 58, 41), 1763: ('personal_bar/user_name', 60, 27), 2000: ('${personal_bar/user_name}', 69, 38), 2002: ('personal_bar/user_name', 69, 40), 2076: ('personal_bar/user_actions', 71, 31), 2193: ('action', 74, 15), 2269: ("python:icons.tag(action.get('icon', 'dot'), tag_class='')", 77, 41), 2372: ('action/title', 78, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355448770320 = set([])
_static_140355448766864 = set(['noresize', 'readonly', 'compact', 'ismap', 'multiple', 'selected', 'declare', 'disabled', 'noshade', 'checked', 'defer', 'nowrap', ])
_static_140355449143056 = {'class': 'nav-link dropdown-item', }
_static_140355482521408 = {'class': 'dropdown-header', }
_static_140355449523360 = {'class': 'dropdown-menu', 'id': 'collapse-personaltools', 'aria-labelledby': 'personaltools-menulink', }
_static_140355449404192 = {'class': 'toolbar-label', }
_static_140355449825840 = {'class': 'nav-link dropdown-toggle', 'id': 'personaltools-menulink', 'aria-expanded': 'false', 'data-bs-offset': '0,0', 'data-bs-toggle': 'dropdown', 'href': 'personal_bar/homelink_url', }
_static_140355449330560 = {'class': "personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}", }
_static_140355449162144 = {'class': 'nav flex-column plone-toolbar-main', }
_static_140355449162576 = {'class': 'toolbar-expand', 'aria-label': 'Pin', }
_static_140355540704128 = {}
_static_140355449461248 = {'class': 'toolbar-collapse', 'aria-label': 'Unpin', }
_static_140355449133136 = {'class': 'toolbar-header nav', }
_static_140355449132752 = {'class': 'pat-toolbar', 'id': 'edit-zone', 'role': 'toolbar', 'data-bs-scroll': 'true', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355449380928 = {'id': 'edit-bar', 'role': 'toolbar', }

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

            # <Static value=<ast.Dict object at 0x7fa70cb3e040> name=None at 7fa70cb3e550> -> __attrs_140355449360336
            __attrs_140355449360336 = _static_140355449380928
            __backup_context_state_140355449760688 = get('context_state', __marker)

            # <Value 'view/context_state' (4:25)> -> __value
            __token = 94
            try:
                __zt_tmp = __attrs_140355449360336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/context_state', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_icons_140355449761696 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (5:16)> -> __value
            __token = 130
            try:
                __zt_tmp = __attrs_140355449360336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_personal_bar_140355449403376 = get('personal_bar', __marker)

            # <Value 'python: view.get_personal_bar()' (6:22)> -> __value
            __token = 206
            try:
                __zt_tmp = __attrs_140355449360336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', ' view.get_personal_bar()', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['personal_bar'] = __value
            __backup_toolbar_pos_140355449492864 = get('toolbar_pos', __marker)

            # <Value 'view/toolbar_position' (7:20)> -> __value
            __token = 261
            try:
                __zt_tmp = __attrs_140355449360336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/toolbar_position', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['toolbar_pos'] = __value

            # <Value 'context_state/is_toolbar_visible' (9:24)> -> __condition
            __token = 322
            try:
                __zt_tmp = __attrs_140355449360336
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'context_state/is_toolbar_visible', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140355449358224 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="edit-bar" role="toolbar" >\n\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa70cb016d0> name=None at 7fa70cb01730> -> __attrs_140355449131552
                __attrs_140355449131552 = _static_140355449132752

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="pat-toolbar" id="edit-zone" role="toolbar" data-bs-scroll="true" >\n\n    ')

                # <Static value=<ast.Dict object at 0x7fa70cb01850> name=None at 7fa70cb01820> -> __attrs_140355449134864
                __attrs_140355449134864 = _static_140355449133136

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="toolbar-header nav">\n      ')

                # <Static value=<ast.Dict object at 0x7fa70cb51a00> name=None at 7fa70cb015e0> -> __attrs_140355449461152
                __attrs_140355449461152 = _static_140355449461248

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="toolbar-collapse"')

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449459472
                __default_140355449459472 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7fa70cb516a0> at 7fa70cb51fd0> -> __attr_aria_label
                __attr_aria_label = 'Unpin'
                __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append(' >\n        ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449163008
                __attrs_140355449163008 = _static_140355540704128

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449163440
                __default_140355449163440 = _DEFAULT_MARKER

                # <Value "python:icons.tag('arrow-bar-left')" (25:41)> -> __cache_140355449163392
                __token = 680
                try:
                    __zt_tmp = __attrs_140355449163008
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140355449163392 = _static_140355540363392('python', "icons.tag('arrow-bar-left')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('arrow-bar-left')" (25:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb08c70> -> __condition
                __expression = __cache_140355449163392

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140355449163392
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>\n      ')

                # <Static value=<ast.Dict object at 0x7fa70cb08b50> name=None at 7fa70cb086a0> -> __attrs_140355449160800
                __attrs_140355449160800 = _static_140355449162576

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="toolbar-expand"')

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449163248
                __default_140355449163248 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7fa70cb08490> at 7fa70cb085e0> -> __attr_aria_label
                __attr_aria_label = 'Pin'
                __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_aria_label is not None):
                    __append((' aria-label="%s"' % __attr_aria_label))
                __append(' >\n        ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449329888
                __attrs_140355449329888 = _static_140355540704128

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449329552
                __default_140355449329552 = _DEFAULT_MARKER

                # <Value "python:icons.tag('arrow-bar-right')" (31:41)> -> __cache_140355449160512
                __token = 875
                try:
                    __zt_tmp = __attrs_140355449329888
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140355449160512 = _static_140355540363392('python', "icons.tag('arrow-bar-right')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('arrow-bar-right')" (31:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb08280> -> __condition
                __expression = __cache_140355449160512

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140355449160512
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      </a>\n    </div>\n\n    ')

                # <Static value=<ast.Dict object at 0x7fa70cb089a0> name=None at 7fa70cb08970> -> __attrs_140355449132464
                __attrs_140355449132464 = _static_140355449162144
                __backup_toolbar_main_140355449760976 = get('toolbar_main', __marker)

                # <Value 'view/base_render' (37:23)> -> __value
                __token = 1033
                try:
                    __zt_tmp = __attrs_140355449132464
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'view/base_render', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['toolbar_main'] = __value

                # <Value 'toolbar_main' (39:23)> -> __condition
                __token = 1084
                try:
                    __zt_tmp = __attrs_140355449132464
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('path', 'toolbar_main', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="nav flex-column plone-toolbar-main" >\n      ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449329024
                    __attrs_140355449329024 = _static_140355540704128

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449328832
                    __default_140355449328832 = _DEFAULT_MARKER

                    # <Value 'toolbar_main' (41:33)> -> __cache_140355449327920
                    __token = 1137
                    try:
                        __zt_tmp = __attrs_140355449329024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355449327920 = _static_140355540363392('path', 'toolbar_main', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'toolbar_main' (41:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb31eb0> -> __condition
                    __expression = __cache_140355449327920

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n      </li>')
                    else:
                        __content = __cache_140355449327920
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n    </ul>')
                if (__backup_toolbar_main_140355449760976 is __marker):
                    del econtext['toolbar_main']
                else:
                    econtext['toolbar_main'] = __backup_toolbar_main_140355449760976
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7fa70cb31b80> name=None at 7fa70cb31a90> -> __attrs_140355449825024
                __attrs_140355449825024 = _static_140355449330560

                # <Value 'personal_bar/user_actions' (46:24)> -> __condition
                __token = 1295
                try:
                    __zt_tmp = __attrs_140355449825024
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('path', 'personal_bar/user_actions', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449330464
                    __default_140355449330464 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "personaltools-wrapper nav ${python:'dropend' if toolbar_pos == 'side' else ''}" (45:16)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cb31340> -> __attr_class
                    __token = 1191
                    __token = 1219
                    try:
                        __zt_tmp = __attrs_140355449825024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140355540363392('python', "'dropend' if toolbar_pos == 'side' else ''", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('personaltools-wrapper nav ', (__attr_class if (__attr_class is not None) else ''), ))
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
                    __append(' >\n\n      ')

                    # <Static value=<ast.Dict object at 0x7fa70cbaaa30> name=None at 7fa70cbaac40> -> __attrs_140355449405104
                    __attrs_140355449405104 = _static_140355449825840

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="nav-link dropdown-toggle" id="personaltools-menulink" aria-expanded="false" data-bs-offset="0,0" data-bs-toggle="dropdown"')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449823824
                    __default_140355449823824 = _DEFAULT_MARKER

                    # <Substitution 'personal_bar/homelink_url' (55:16)> -> __attr_href
                    __token = 1546
                    try:
                        __zt_tmp = __attrs_140355449405104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140355540363392('path', 'personal_bar/homelink_url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449402272
                    __attrs_140355449402272 = _static_140355540704128

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449402992
                    __default_140355449402992 = _DEFAULT_MARKER

                    # <Value "python:icons.tag('toolbar-action/personaltools', tag_class='')" (58:41)> -> __cache_140355449403184
                    __token = 1633
                    try:
                        __zt_tmp = __attrs_140355449402272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355449403184 = _static_140355540363392('python', "icons.tag('toolbar-action/personaltools', tag_class='')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag('toolbar-action/personaltools', tag_class='')" (58:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb43160> -> __condition
                    __expression = __cache_140355449403184

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355449403184
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x7fa70cb43b20> name=None at 7fa70cb43a00> -> __attrs_140355449401504
                    __attrs_140355449401504 = _static_140355449404192

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="toolbar-label" >')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449401840
                    __default_140355449401840 = _DEFAULT_MARKER

                    # <Value 'personal_bar/user_name' (60:27)> -> __cache_140355449401792
                    __token = 1763
                    try:
                        __zt_tmp = __attrs_140355449401504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355449401792 = _static_140355540363392('path', 'personal_bar/user_name', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'personal_bar/user_name' (60:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb439d0> -> __condition
                    __expression = __cache_140355449401792

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('User')
                    else:
                        __content = __cache_140355449401792
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n      </a>\n\n      ')

                    # <Static value=<ast.Dict object at 0x7fa70cb60ca0> name=None at 7fa70cb60970> -> __attrs_140355449522208
                    __attrs_140355449522208 = _static_140355449523360

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="dropdown-menu" id="collapse-personaltools" aria-labelledby="personaltools-menulink" >\n        ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355482519920
                    __attrs_140355482519920 = _static_140355540704128

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li>\n          ')

                    # <Static value=<ast.Dict object at 0x7fa70ead8f40> name=None at 7fa70ead8f10> -> __attrs_140355482518336
                    __attrs_140355482518336 = _static_140355482521408

                    # <h6 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h6 class="dropdown-header">')

                    # <Interpolation value=<Substitution '${personal_bar/user_name}' (69:38)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70ead85b0> -> __content_140355621335664
                    __token = 2000
                    __token = 2002
                    try:
                        __zt_tmp = __attrs_140355482518336
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140355621335664 = _static_140355540363392('path', 'personal_bar/user_name', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __content_140355621335664 = __quote(__content_140355621335664, '\x00', '&#0;', None, None)
                    __content_140355621335664 = __content_140355621335664
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
                    __append('</h6>\n        </li>\n        ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355482518000
                    __attrs_140355482518000 = _static_140355540704128
                    __backup_action_140355449612368 = get('action', __marker)

                    # <Value 'personal_bar/user_actions' (71:31)> -> __iterator
                    __token = 2076
                    try:
                        __zt_tmp = __attrs_140355482518000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140355540363392('path', 'personal_bar/user_actions', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    (__iterator, ____index_140355482520640, ) = getname('repeat')('action', __iterator)
                    econtext['action'] = None
                    for __item in __iterator:
                        econtext['action'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li>\n          ')

                        # <Static value=<ast.Dict object at 0x7fa70cb03f10> name=None at 7fa70cb03640> -> __attrs_140355449140992
                        __attrs_140355449140992 = _static_140355449143056

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Value 'action' (74:15)> -> __cache_140355449140656
                        __token = 2193
                        try:
                            __zt_tmp = __attrs_140355449140992
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355449140656 = _static_140355540363392('path', 'action', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        if ('class' not in __chain(__cache_140355449140656)):
                            __append(' class="nav-link dropdown-item"')
                        __attr_140355449141232 = __cache_140355449140656
                        for (name, value, ) in __attr_140355449141232.items():
                            if (name in _static_140355448766864):
                                if not bool(value):
                                    continue
                                value = name
                            if ((name not in _static_140355448770320) and (value is not None)):
                                if (name in _static_140355448766864):
                                    if not bool(value):
                                        continue
                                    value = name
                                __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                        __append(' >\n            ')

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449139408
                        __attrs_140355449139408 = _static_140355540704128

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449141184
                        __default_140355449141184 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(action.get('icon', 'dot'), tag_class='')" (77:41)> -> __cache_140355449141904
                        __token = 2269
                        try:
                            __zt_tmp = __attrs_140355449139408
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355449141904 = _static_140355540363392('python', "icons.tag(action.get('icon', 'dot'), tag_class='')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(action.get('icon', 'dot'), tag_class='')" (77:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb03940> -> __condition
                        __expression = __cache_140355449141904

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140355449141904
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449611600
                        __attrs_140355449611600 = _static_140355540704128

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449139504
                        __default_140355449139504 = _DEFAULT_MARKER

                        # <Value 'action/title' (78:41)> -> __cache_140355449140416
                        __token = 2372
                        try:
                            __zt_tmp = __attrs_140355449611600
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355449140416 = _static_140355540363392('path', 'action/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value 'action/title' (78:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb03400> -> __condition
                        __expression = __cache_140355449140416

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              action title\n            ')
                        else:
                            __content = __cache_140355449140416
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n          </a>\n        </li>')
                        ____index_140355482520640 -= 1
                        if (____index_140355482520640 > 0):
                            __append('\n        ')
                    if (__backup_action_140355449612368 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_140355449612368
                    __append('\n      </ul>\n\n    </div>')
                __append('\n  </div>\n</section>')
                __i18n_domain = __previous_i18n_domain_140355449358224
            if (__backup_toolbar_pos_140355449492864 is __marker):
                del econtext['toolbar_pos']
            else:
                econtext['toolbar_pos'] = __backup_toolbar_pos_140355449492864
            if (__backup_personal_bar_140355449403376 is __marker):
                del econtext['personal_bar']
            else:
                econtext['personal_bar'] = __backup_personal_bar_140355449403376
            if (__backup_icons_140355449761696 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140355449761696
            if (__backup_context_state_140355449760688 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_140355449760688
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }