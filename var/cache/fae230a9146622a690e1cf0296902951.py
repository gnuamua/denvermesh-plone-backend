# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.z3cform-2.0.3-py3.9.egg/plone/z3cform/pagetemplates/wrappedform.pt'

__tokens = {22: ('context/@@ploneform-macros/titlelessform', 1, 22), 22: ('context/@@ploneform-macros/titlelessform', 1, 22)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info

_static_140362943564240 = __C2ZContextWrapper
_static_140362943564528 = __compile_zt_expr
_static_140362873071024 = 'titlelessform'
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

            # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873072608
            __attrs_140362873072608 = _static_140362943909360
            __backup_macroname_140362918788224 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fa8c73065b0> name=None at 7fa8c73068b0> -> __value
            __value = _static_140362873071024
            econtext['macroname'] = __value

            # <Value 'context/@@ploneform-macros/titlelessform' (1:22)> -> __macro
            __token = 22
            try:
                __zt_tmp = __attrs_140362873072608
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140362943564528('path', 'context/@@ploneform-macros/titlelessform', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __token = 22
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140362918788224 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140362918788224
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }