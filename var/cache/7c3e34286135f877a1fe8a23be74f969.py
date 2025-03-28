# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/viewlets/anontools.pt'

__tokens = {47: ('python:view.user_actions and view.anonymous', 2, 20), 181: ('view/user_actions', 6, 27), 296: ('action', 11, 11), 245: ('action/title', 9, 22)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355448864928 = set([])
_static_140355448865936 = set(['noresize', 'readonly', 'compact', 'ismap', 'multiple', 'selected', 'declare', 'disabled', 'noshade', 'checked', 'defer', 'nowrap', ])
_static_140355459606656 = {'href': '', }
_static_140355449327968 = {'class': 'list-inline-item', }
_static_140355449331184 = {'class': 'list-inline', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355448859904 = {'id': 'portal-anontools', }

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

            # <Static value=<ast.Dict object at 0x7fa70cabed00> name=None at 7fa70cabe820> -> __attrs_140355449328256
            __attrs_140355449328256 = _static_140355448859904

            # <Value 'python:view.user_actions and view.anonymous' (2:20)> -> __condition
            __token = 47
            try:
                __zt_tmp = __attrs_140355449328256
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('python', 'view.user_actions and view.anonymous', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="portal-anontools" >\n  ')

                # <Static value=<ast.Dict object at 0x7fa70cb31df0> name=None at 7fa70cb31880> -> __attrs_140355449331568
                __attrs_140355449331568 = _static_140355449331184

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="list-inline">\n    ')

                # <Static value=<ast.Dict object at 0x7fa70cb31160> name=None at 7fa70cb31520> -> __attrs_140355449331136
                __attrs_140355449331136 = _static_140355449327968
                __backup_action_140355449328640 = get('action', __marker)

                # <Value 'view/user_actions' (6:27)> -> __iterator
                __token = 181
                try:
                    __zt_tmp = __attrs_140355449331136
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140355540363392('path', 'view/user_actions', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                (__iterator, ____index_140355459606896, ) = getname('repeat')('action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="list-inline-item" >\n      ')

                    # <Static value=<ast.Dict object at 0x7fa70d4fe880> name=None at 7fa70d4fe8e0> -> __attrs_140355459605792
                    __attrs_140355459605792 = _static_140355459606656

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Value 'action' (11:11)> -> __cache_140355459607376
                    __token = 296
                    try:
                        __zt_tmp = __attrs_140355459605792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355459607376 = _static_140355540363392('path', 'action', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if ('href' not in __chain(__cache_140355459607376)):
                        __append(' href=""')
                    __attr_140355459608192 = __cache_140355459607376
                    for (name, value, ) in __attr_140355459608192.items():
                        if (name in _static_140355448865936):
                            if not bool(value):
                                continue
                            value = name
                        if ((name not in _static_140355448864928) and (value is not None)):
                            if (name in _static_140355448865936):
                                if not bool(value):
                                    continue
                                value = name
                            __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                    __append(' >')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459607184
                    __default_140355459607184 = _DEFAULT_MARKER

                    # <Value 'action/title' (9:22)> -> __cache_140355459604592
                    __token = 245
                    try:
                        __zt_tmp = __attrs_140355459605792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355459604592 = _static_140355540363392('path', 'action/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'action/title' (9:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70d4fe4c0> -> __condition
                    __expression = __cache_140355459604592

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n          action title\n      ')
                    else:
                        __content = __cache_140355459604592
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n    </li>')
                    ____index_140355459606896 -= 1
                    if (____index_140355459606896 > 0):
                        __append('\n    ')
                if (__backup_action_140355449328640 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140355449328640
                __append('\n  </ul>\n</div>')
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }