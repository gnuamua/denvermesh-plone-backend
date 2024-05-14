# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/links/favicon.pt'

__tokens = {55: ('${python: view.mimetype}', 3, 14), 57: ('python: view.mimetype', 3, 16), 121: ('python: view.favicon_path', 5, 15), 227: ('python: view.favicon_path', 10, 15)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355449847568 = {'rel': 'mask-icon', 'href': 'python: view.favicon_path', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355449430848 = {'rel': 'preload icon', 'type': '${python: view.mimetype}', 'href': 'python: view.favicon_path', }
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

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449478496
            __attrs_140355449478496 = _static_140355540704128
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7fa70cb4a340> name=None at 7fa70cb4a5b0> -> __attrs_140355449846800
            __attrs_140355449846800 = _static_140355449430848

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="preload icon"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449847616
            __default_140355449847616 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${python: view.mimetype}' (3:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cbafb80> -> __attr_type
            __token = 55
            __token = 57
            try:
                __zt_tmp = __attrs_140355449846800
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_type = _static_140355540363392('python', ' view.mimetype', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_type = __quote(__attr_type, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_type = __attr_type
            if (__attr_type is None):
                pass
            else:
                if (__attr_type is _DEFAULT_MARKER):
                    __attr_type = None
                else:
                    __tt = type(__attr_type)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_type = str(__attr_type)
                    else:
                        if (__tt is bytes):
                            __attr_type = decode(__attr_type)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_type = __attr_type.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_type)
                                    __attr_type = (str(__attr_type) if (__attr_type is __converted) else __converted)
                                else:
                                    __attr_type = __attr_type()
            if (__attr_type is not None):
                __append((' type="%s"' % __attr_type))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449843968
            __default_140355449843968 = _DEFAULT_MARKER

            # <Substitution 'python: view.favicon_path' (5:15)> -> __attr_href
            __token = 121
            try:
                __zt_tmp = __attrs_140355449846800
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140355540363392('python', ' view.favicon_path', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' />\n  ')

            # <Static value=<ast.Dict object at 0x7fa70cbaff10> name=None at 7fa70cbaf5e0> -> __attrs_140355449601952
            __attrs_140355449601952 = _static_140355449847568

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="mask-icon"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449844016
            __default_140355449844016 = _DEFAULT_MARKER

            # <Substitution 'python: view.favicon_path' (10:15)> -> __attr_href
            __token = 227
            try:
                __zt_tmp = __attrs_140355449601952
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140355540363392('python', ' view.favicon_path', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' />\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }