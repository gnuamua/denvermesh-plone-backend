# -*- coding: utf-8 -*-
__filename = '/index_html'

__tokens = {56: ('template/title', 4, 24), 612: ('template/title', 18, 27), 641: ('context/title_or_id', 18, 56), 733: ('template/title', 21, 27), 762: ('template/title', 21, 56), 888: ('template/id', 26, 45)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140141461896256 = {'href': 'https://zope.readthedocs.io', }
_static_140141462116288 = {'src': '/++resource++logo/Zope.svg', 'id': 'logo', 'alt': 'Zope logo', }
_static_140141462114800 = {'href': 'https://www.zope.dev', 'target': '_blank', }
_static_140141461648624 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '/++resource++logo/default.css', }
_static_140141475579312 = {'rel': 'shortcut icon', 'type': 'image/x-icon', 'href': '/++resource++logo/favicon/favicon.svg', }
_static_140141461293280 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1, shrink-to-fit=no', }
_static_140141462160432 = {'charset': 'utf-8', }
_static_140141533071440 = __C2ZContextWrapper
_static_140141533071728 = __compile_zt_expr
_static_140141533420656 = {}

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

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461955536
            __attrs_140141461955536 = _static_140141533420656

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html>\n  ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461663952
            __attrs_140141461663952 = _static_140141533420656

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462162928
            __attrs_140141462162928 = _static_140141533420656

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462161680
            __default_140141462161680 = _DEFAULT_MARKER

            # <Value 'template/title' (4:24)> -> __cache_140141462162400
            __token = 56
            try:
                __zt_tmp = __attrs_140141462162928
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462162400 = _static_140141533071728('path', 'template/title', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'template/title' (4:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a120b80> -> __condition
            __expression = __cache_140141462162400

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('The title')
            else:
                __content = __cache_140141462162400
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</title>\n    ')

            # <Static value=<ast.Dict object at 0x7f753a120430> name=None at 7f753a1200d0> -> __attrs_140141461295008
            __attrs_140141461295008 = _static_140141462160432

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n    ')

            # <Static value=<ast.Dict object at 0x7f753a04c8e0> name=None at 7f753a04cdc0> -> __attrs_140141461294048
            __attrs_140141461294048 = _static_140141461293280

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />\n    ')

            # <Static value=<ast.Dict object at 0x7f753adec5b0> name=None at 7f753adeceb0> -> __attrs_140141461650592
            __attrs_140141461650592 = _static_140141475579312

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="shortcut icon" type="image/x-icon" href="/++resource++logo/favicon/favicon.svg" />\n    ')

            # <Static value=<ast.Dict object at 0x7f753a0a34f0> name=None at 7f753a0a3700> -> __attrs_140141461648528
            __attrs_140141461648528 = _static_140141461648624

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css" href="/++resource++logo/default.css" />\n  </head>\n  ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462118016
            __attrs_140141462118016 = _static_140141533420656

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n    ')

            # <Static value=<ast.Dict object at 0x7f753a1151f0> name=None at 7f753a115310> -> __attrs_140141462117440
            __attrs_140141462117440 = _static_140141462114800

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="https://www.zope.dev" target="_blank">\n      ')

            # <Static value=<ast.Dict object at 0x7f753a1157c0> name=None at 7f753a115640> -> __attrs_140141600654432
            __attrs_140141600654432 = _static_140141462116288

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img src="/++resource++logo/Zope.svg" id="logo" alt="Zope logo" />\n    </a>\n    ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461866720
            __attrs_140141461866720 = _static_140141533420656

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>\n      ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461865808
            __attrs_140141461865808 = _static_140141533420656

            # <Value 'template/title' (18:27)> -> __condition
            __token = 612
            try:
                __zt_tmp = __attrs_140141461865808
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140141533071728('path', 'template/title', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461868352
                __default_140141461868352 = _DEFAULT_MARKER

                # <Value 'context/title_or_id' (18:56)> -> __cache_140141461868208
                __token = 641
                try:
                    __zt_tmp = __attrs_140141461865808
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140141461868208 = _static_140141533071728('path', 'context/title_or_id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/title_or_id' (18:56)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0d8f70> -> __condition
                __expression = __cache_140141461868208

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>\n        content title or id\n      </span>')
                else:
                    __content = __cache_140141461868208
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            __append(':\n      ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462125632
            __attrs_140141462125632 = _static_140141533420656

            # <Value 'template/title' (21:27)> -> __condition
            __token = 733
            try:
                __zt_tmp = __attrs_140141462125632
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140141533071728('path', 'template/title', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462125728
                __default_140141462125728 = _DEFAULT_MARKER

                # <Value 'template/title' (21:56)> -> __cache_140141462125056
                __token = 762
                try:
                    __zt_tmp = __attrs_140141462125632
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140141462125056 = _static_140141533071728('path', 'template/title', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                # <BinOp left=<Value 'template/title' (21:56)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a117220> -> __condition
                __expression = __cache_140141462125056

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>\n        optional template title\n      </span>')
                else:
                    __content = __cache_140141462125056
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            __append('\n    </h1>\n    ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462123088
            __attrs_140141462123088 = _static_140141533420656

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>\n      This is Page Template ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462126448
            __attrs_140141462126448 = _static_140141533420656

            # <em ... (0:0)
            # --------------------------------------------------------
            __append('<em>')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462126544
            __default_140141462126544 = _DEFAULT_MARKER

            # <Value 'template/id' (26:45)> -> __cache_140141462126064
            __token = 888
            try:
                __zt_tmp = __attrs_140141462126448
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462126064 = _static_140141533071728('path', 'template/id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'template/id' (26:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a117a30> -> __condition
            __expression = __cache_140141462126064

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('template id')
            else:
                __content = __cache_140141462126064
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('</em>.\n    </p>\n    ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461895968
            __attrs_140141461895968 = _static_140141533420656

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>\n      For documentation, please visit\n      ')

            # <Static value=<ast.Dict object at 0x7f753a0dfc40> name=None at 7f753a0dfc10> -> __attrs_140141461893616
            __attrs_140141461893616 = _static_140141461896256

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="https://zope.readthedocs.io">https://zope.readthedocs.io</a>.\n    </p>\n  </body>\n</html>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }