# -*- coding: utf-8 -*-
__filename = 'index_html'

__tokens = {56: ('template/title', 4, 24), 612: ('template/title', 18, 27), 641: ('context/title_or_id', 18, 56), 733: ('template/title', 21, 27), 762: ('template/title', 21, 56), 888: ('template/id', 26, 45)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_139882339044320 = {'href': 'https://zope.readthedocs.io', }
_static_139882338894512 = {'src': '/++resource++logo/Zope.svg', 'id': 'logo', 'alt': 'Zope logo', }
_static_139882327755984 = {'href': 'https://www.zope.dev', 'target': '_blank', }
_static_139882331182944 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '/++resource++logo/default.css', }
_static_139882337747728 = {'rel': 'shortcut icon', 'type': 'image/x-icon', 'href': '/++resource++logo/favicon/favicon.svg', }
_static_139882337748352 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1, shrink-to-fit=no', }
_static_139882337748064 = {'charset': 'utf-8', }
_static_139882332106464 = __C2ZContextWrapper
_static_139882332106272 = __compile_zt_expr
_static_139882332754032 = {}

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
            __append('<!DOCTYPE html>\n')

            # <Static value=<ast.Dict object at 0x7f38e4c11070> name=None at 7f38e4c11100> -> __attrs_139882341528384
            __attrs_139882341528384 = _static_139882332754032

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html>\n  ')

            # <Static value=<ast.Dict object at 0x7f38e4c11070> name=None at 7f38e4c11100> -> __attrs_139882341530112
            __attrs_139882341530112 = _static_139882332754032

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x7f38e4c11070> name=None at 7f38e4c11100> -> __attrs_139882315863472
            __attrs_139882315863472 = _static_139882332754032

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>')

            # <Symbol value=<DEFAULT> at 7f38e4ccb6d0> -> __default_139882286776816
            __default_139882286776816 = _DEFAULT_MARKER

            # <Value 'template/title' (4:24)> -> __cache_139882312439888
            __token = 56
            try:
                __zt_tmp = __attrs_139882315863472
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882312439888 = _static_139882332106272('path', 'template/title', econtext=econtext)(_static_139882332106464(econtext, __zt_tmp))

            # <BinOp left=<Value 'template/title' (4:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e4ccb6d0> at 7f38e38b18e0> -> __condition
            __expression = __cache_139882312439888

            # <Symbol value=<DEFAULT> at 7f38e4ccb6d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('The title')
            else:
                __content = __cache_139882312439888
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</title>\n    ')

            # <Static value=<ast.Dict object at 0x7f38e50d4460> name=None at 7f38e50d4520> -> __attrs_139882337750032
            __attrs_139882337750032 = _static_139882337748064

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n    ')

            # <Static value=<ast.Dict object at 0x7f38e50d4580> name=None at 7f38e50d4eb0> -> __attrs_139882337750272
            __attrs_139882337750272 = _static_139882337748352

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />\n    ')

            # <Static value=<ast.Dict object at 0x7f38e50d4310> name=None at 7f38e50d42b0> -> __attrs_139882331183904
            __attrs_139882331183904 = _static_139882337747728

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="shortcut icon" type="image/x-icon" href="/++resource++logo/favicon/favicon.svg" />\n    ')

            # <Static value=<ast.Dict object at 0x7f38e4a91760> name=None at 7f38e4a91730> -> __attrs_139882331182656
            __attrs_139882331182656 = _static_139882331182944

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css" href="/++resource++logo/default.css" />\n  </head>\n  ')

            # <Static value=<ast.Dict object at 0x7f38e4c11070> name=None at 7f38e4c11100> -> __attrs_139882331183520
            __attrs_139882331183520 = _static_139882332754032

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n    ')

            # <Static value=<ast.Dict object at 0x7f38e474ccd0> name=None at 7f38e474c7f0> -> __attrs_139882327753152
            __attrs_139882327753152 = _static_139882327755984

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="https://www.zope.dev" target="_blank">\n      ')

            # <Static value=<ast.Dict object at 0x7f38e51ec2b0> name=None at 7f38e1e03ee0> -> __attrs_139882282870384
            __attrs_139882282870384 = _static_139882338894512

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img src="/++resource++logo/Zope.svg" id="logo" alt="Zope logo" />\n    </a>\n    ')

            # <Static value=<ast.Dict object at 0x7f38e4c11070> name=None at 7f38e4c11100> -> __attrs_139882282642640
            __attrs_139882282642640 = _static_139882332754032

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>\n      ')

            # <Static value=<ast.Dict object at 0x7f38e4c11070> name=None at 7f38e4c11100> -> __attrs_139882319960768
            __attrs_139882319960768 = _static_139882332754032

            # <Value 'template/title' (18:27)> -> __condition
            __token = 612
            try:
                __zt_tmp = __attrs_139882319960768
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882332106272('path', 'template/title', econtext=econtext)(_static_139882332106464(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7f38e4ccb6d0> -> __default_139882319960528
                __default_139882319960528 = _DEFAULT_MARKER

                # <Value 'context/title_or_id' (18:56)> -> __cache_139882319402464
                __token = 641
                try:
                    __zt_tmp = __attrs_139882319960768
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139882319402464 = _static_139882332106272('path', 'context/title_or_id', econtext=econtext)(_static_139882332106464(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/title_or_id' (18:56)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e4ccb6d0> at 7f38e3dca820> -> __condition
                __expression = __cache_139882319402464

                # <Symbol value=<DEFAULT> at 7f38e4ccb6d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>\n        content title or id\n      </span>')
                else:
                    __content = __cache_139882319402464
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            __append(':\n      ')

            # <Static value=<ast.Dict object at 0x7f38e4c11070> name=None at 7f38e4c11100> -> __attrs_139882323779648
            __attrs_139882323779648 = _static_139882332754032

            # <Value 'template/title' (21:27)> -> __condition
            __token = 733
            try:
                __zt_tmp = __attrs_139882323779648
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_139882332106272('path', 'template/title', econtext=econtext)(_static_139882332106464(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7f38e4ccb6d0> -> __default_139882323781280
                __default_139882323781280 = _DEFAULT_MARKER

                # <Value 'template/title' (21:56)> -> __cache_139882323780704
                __token = 762
                try:
                    __zt_tmp = __attrs_139882323779648
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_139882323780704 = _static_139882332106272('path', 'template/title', econtext=econtext)(_static_139882332106464(econtext, __zt_tmp))

                # <BinOp left=<Value 'template/title' (21:56)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e4ccb6d0> at 7f38e43823a0> -> __condition
                __expression = __cache_139882323780704

                # <Symbol value=<DEFAULT> at 7f38e4ccb6d0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>\n        optional template title\n      </span>')
                else:
                    __content = __cache_139882323780704
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            __append('\n    </h1>\n    ')

            # <Static value=<ast.Dict object at 0x7f38e4c11070> name=None at 7f38e4c11100> -> __attrs_139882323783152
            __attrs_139882323783152 = _static_139882332754032

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>\n      This is Page Template ')

            # <Static value=<ast.Dict object at 0x7f38e4c11070> name=None at 7f38e4c11100> -> __attrs_139882323781760
            __attrs_139882323781760 = _static_139882332754032

            # <em ... (0:0)
            # --------------------------------------------------------
            __append('<em>')

            # <Symbol value=<DEFAULT> at 7f38e4ccb6d0> -> __default_139882323782096
            __default_139882323782096 = _DEFAULT_MARKER

            # <Value 'template/id' (26:45)> -> __cache_139882323782576
            __token = 888
            try:
                __zt_tmp = __attrs_139882323781760
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_139882323782576 = _static_139882332106272('path', 'template/id', econtext=econtext)(_static_139882332106464(econtext, __zt_tmp))

            # <BinOp left=<Value 'template/id' (26:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f38e4ccb6d0> at 7f38e4382af0> -> __condition
            __expression = __cache_139882323782576

            # <Symbol value=<DEFAULT> at 7f38e4ccb6d0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('template id')
            else:
                __content = __cache_139882323782576
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</em>.\n    </p>\n    ')

            # <Static value=<ast.Dict object at 0x7f38e4c11070> name=None at 7f38e4c11100> -> __attrs_139882338250464
            __attrs_139882338250464 = _static_139882332754032

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>\n      For documentation, please visit\n      ')

            # <Static value=<ast.Dict object at 0x7f38e5210be0> name=None at 7f38e5210610> -> __attrs_139882313001376
            __attrs_139882313001376 = _static_139882339044320

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="https://zope.readthedocs.io">https://zope.readthedocs.io</a>.\n    </p>\n  </body>\n</html>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }