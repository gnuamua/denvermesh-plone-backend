# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/analytics/view_head.pt'

__tokens = {42: ('view/webstats_js', 2, 24), 87: ('webstats_head_js', 4, 20), 201: ('webstats_head_js', 8, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

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

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449462448
            __attrs_140355449462448 = _static_140355540704128
            __backup_webstats_head_js_140355449478544 = get('webstats_head_js', __marker)

            # <Value 'view/webstats_js' (2:24)> -> __value
            __token = 42
            try:
                __zt_tmp = __attrs_140355449462448
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/webstats_js', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['webstats_head_js'] = __value

            # <Value 'webstats_head_js' (4:20)> -> __condition
            __token = 87
            try:
                __zt_tmp = __attrs_140355449462448
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'webstats_head_js', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __append('\n  <!-- plone.analytics.head goes here -->\n  ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449430464
                __attrs_140355449430464 = _static_140355540704128

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449433968
                __default_140355449433968 = _DEFAULT_MARKER

                # <Value 'webstats_head_js' (8:31)> -> __cache_140355494592864
                __token = 201
                try:
                    __zt_tmp = __attrs_140355449430464
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140355494592864 = _static_140355540363392('path', 'webstats_head_js', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                # <BinOp left=<Value 'webstats_head_js' (8:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb4a760> -> __condition
                __expression = __cache_140355494592864

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span></span>')
                else:
                    __content = __cache_140355494592864
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n')
            if (__backup_webstats_head_js_140355449478544 is __marker):
                del econtext['webstats_head_js']
            else:
                econtext['webstats_head_js'] = __backup_webstats_head_js_140355449478544
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }