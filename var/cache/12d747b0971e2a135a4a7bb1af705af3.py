# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/viewlets/membertools.pt'

__tokens = {78: ('here/@@plone_context_state/is_toolbar_visible', 3, 23), 138: (' view/anonymou', 4, 13), 182: ('python:not isAnon and not toolbar_visible', 6, 20), 441: ('python:view.user_actions and not view.anonymous', 16, 22), 618: ('view/homelink_url', 22, 14), 677: ('view/user_name', 25, 25), 872: ('view/user_actions', 32, 29), 933: ('string:membertools-${action/id}', 34, 15), 1122: ('action/href', 41, 18), 1154: (' action/link_target|nothin', 42, 19), 1062: ('action/title', 39, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355448496720 = {'class': 'dropdown-item', 'href': '', 'target': 'action/link_target|nothing', }
_static_140355448498208 = {'id': 'string:membertools-${action/id}', }
_static_140355448548848 = {'class': 'dropdown-menu', 'aria-labelledby': 'dropdownMenu', 'role': 'menu', }
_static_140355448548416 = {'class': 'caret', }
_static_140355540704128 = {}
_static_140355448531792 = {'class': 'dropdown-toggle', 'id': 'user-name', 'data-bs-toggle': 'dropdown', 'href': 'view/homelink_url', }
_static_140355459798448 = {'class': 'dropdown dropdown-menu-end', 'id': 'portal-membertools', }
_static_140355459798688 = {'class': 'hiddenStructure', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355448808016 = {'id': 'portal-membertools-wrapper', }

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

            # <Static value=<ast.Dict object at 0x7fa70cab2250> name=None at 7fa70cab2100> -> __attrs_140355448810320
            __attrs_140355448810320 = _static_140355448808016
            __backup_toolbar_visible_140355492174864 = get('toolbar_visible', __marker)

            # <Value 'here/@@plone_context_state/is_toolbar_visible' (3:23)> -> __value
            __token = 78
            try:
                __zt_tmp = __attrs_140355448810320
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'here/@@plone_context_state/is_toolbar_visible', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['toolbar_visible'] = __value
            __backup_isAnon_140355449761408 = get('isAnon', __marker)

            # <Value 'view/anonymous' (4:13)> -> __value
            __token = 138
            try:
                __zt_tmp = __attrs_140355448810320
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/anonymous', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['isAnon'] = __value

            # <Value 'python:not isAnon and not toolbar_visible' (6:20)> -> __condition
            __token = 182
            try:
                __zt_tmp = __attrs_140355448810320
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('python', 'not isAnon and not toolbar_visible', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140355459799312 = __i18n_domain
                __i18n_domain = 'plone'

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="portal-membertools-wrapper" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa70d52d6a0> name=None at 7fa70d52d670> -> __attrs_140355459800992
                __attrs_140355459800992 = _static_140355459798688

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="hiddenStructure" >')
                __stream_140355459800272 = []
                __append_140355459800272 = __stream_140355459800272.append
                __append_140355459800272('Member tools')
                __msgid_140355459800272 = __re_whitespace(''.join(__stream_140355459800272)).strip()
                if 'heading_member_tools':
                    __append(translate('heading_member_tools', mapping=None, default=__msgid_140355459800272, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa70d52d5b0> name=None at 7fa70d52d4f0> -> __attrs_140355448530592
                __attrs_140355448530592 = _static_140355459798448

                # <Value 'python:view.user_actions and not view.anonymous' (16:22)> -> __condition
                __token = 441
                try:
                    __zt_tmp = __attrs_140355448530592
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('python', 'view.user_actions and not view.anonymous', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="dropdown dropdown-menu-end" id="portal-membertools" >\n    ')

                    # <Static value=<ast.Dict object at 0x7fa70ca6eb50> name=None at 7fa70ca6ee50> -> __attrs_140355448529536
                    __attrs_140355448529536 = _static_140355448531792

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="dropdown-toggle" id="user-name" data-bs-toggle="dropdown"')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448532368
                    __default_140355448532368 = _DEFAULT_MARKER

                    # <Substitution 'view/homelink_url' (22:14)> -> __attr_href
                    __token = 618
                    try:
                        __zt_tmp = __attrs_140355448529536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140355540363392('path', 'view/homelink_url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' >\n      ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448547408
                    __attrs_140355448547408 = _static_140355540704128

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448548224
                    __default_140355448548224 = _DEFAULT_MARKER

                    # <Value 'view/user_name' (25:25)> -> __cache_140355448546640
                    __token = 677
                    try:
                        __zt_tmp = __attrs_140355448547408
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355448546640 = _static_140355540363392('path', 'view/user_name', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/user_name' (25:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70ca72a60> -> __condition
                    __expression = __cache_140355448546640

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>John</span>')
                    else:
                        __content = __cache_140355448546640
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7fa70ca72c40> name=None at 7fa70ca72100> -> __attrs_140355448549280
                    __attrs_140355448549280 = _static_140355448548416

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="caret"></span>\n    </a>\n    ')

                    # <Static value=<ast.Dict object at 0x7fa70ca72df0> name=None at 7fa70ca72310> -> __attrs_140355448546976
                    __attrs_140355448546976 = _static_140355448548848

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="dropdown-menu" aria-labelledby="dropdownMenu" role="menu" >\n      ')

                    # <Static value=<ast.Dict object at 0x7fa70ca66820> name=None at 7fa70ca66f70> -> __attrs_140355448499024
                    __attrs_140355448499024 = _static_140355448498208
                    __backup_action_140355448932720 = get('action', __marker)

                    # <Value 'view/user_actions' (32:29)> -> __iterator
                    __token = 872
                    try:
                        __zt_tmp = __attrs_140355448499024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140355540363392('path', 'view/user_actions', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    (__iterator, ____index_140355448498304, ) = getname('repeat')('action', __iterator)
                    econtext['action'] = None
                    for __item in __iterator:
                        econtext['action'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li')

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448499792
                        __default_140355448499792 = _DEFAULT_MARKER

                        # <Substitution 'string:membertools-${action/id}' (34:15)> -> __attr_id
                        __token = 933
                        try:
                            __zt_tmp = __attrs_140355448499024
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_id = _static_140355540363392('string', 'membertools-${action/id}', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_id is not None):
                            __append((' id="%s"' % __attr_id))
                        __append(' >\n        ')

                        # <Static value=<ast.Dict object at 0x7fa70ca66250> name=None at 7fa70ca668e0> -> __attrs_140355448535840
                        __attrs_140355448535840 = _static_140355448496720

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="dropdown-item"')

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448497440
                        __default_140355448497440 = _DEFAULT_MARKER

                        # <Substitution 'action/href' (41:18)> -> __attr_href
                        __token = 1122
                        try:
                            __zt_tmp = __attrs_140355448535840
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140355540363392('path', 'action/href', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448534304
                        __default_140355448534304 = _DEFAULT_MARKER

                        # <Substitution 'action/link_target|nothing' (42:19)> -> __attr_target
                        __token = 1154
                        try:
                            __zt_tmp = __attrs_140355448535840
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_target = _static_140355540363392('path', 'action/link_target|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_target is not None):
                            __append((' target="%s"' % __attr_target))
                        __append(' >')

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448498592
                        __default_140355448498592 = _DEFAULT_MARKER

                        # <Value 'action/title' (39:24)> -> __cache_140355448498352
                        __token = 1062
                        try:
                            __zt_tmp = __attrs_140355448535840
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355448498352 = _static_140355540363392('path', 'action/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value 'action/title' (39:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70ca66a60> -> __condition
                        __expression = __cache_140355448498352

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                  action title\n        ')
                        else:
                            __content = __cache_140355448498352
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>\n      </li>')
                        ____index_140355448498304 -= 1
                        if (____index_140355448498304 > 0):
                            __append('\n      ')
                    if (__backup_action_140355448932720 is __marker):
                        del econtext['action']
                    else:
                        econtext['action'] = __backup_action_140355448932720
                    __append('\n    </ul>\n  </div>')
                __append('\n\n</div>')
                __i18n_domain = __previous_i18n_domain_140355459799312
            if (__backup_isAnon_140355449761408 is __marker):
                del econtext['isAnon']
            else:
                econtext['isAnon'] = __backup_isAnon_140355449761408
            if (__backup_toolbar_visible_140355492174864 is __marker):
                del econtext['toolbar_visible']
            else:
                econtext['toolbar_visible'] = __backup_toolbar_visible_140355492174864
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }