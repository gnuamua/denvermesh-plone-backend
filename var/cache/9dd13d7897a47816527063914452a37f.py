# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/viewlets/social_tags.pt'

__tokens = {22: ('view/tags', 1, 22), 64: ('tag', 3, 8)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info

_static_140355482573744 = set([])
_static_140355449521008 = set(['noresize', 'readonly', 'compact', 'ismap', 'multiple', 'selected', 'declare', 'disabled', 'noshade', 'checked', 'defer', 'nowrap', ])
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

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449698384
            __attrs_140355449698384 = _static_140355540704128
            __backup_tag_140355449461872 = get('tag', __marker)

            # <Value 'view/tags' (1:22)> -> __iterator
            __token = 22
            try:
                __zt_tmp = __attrs_140355449698384
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140355540363392('path', 'view/tags', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            (__iterator, ____index_140355449697184, ) = getname('repeat')('tag', __iterator)
            econtext['tag'] = None
            for __item in __iterator:
                econtext['tag'] = __item

                # <meta ... (0:0)
                # --------------------------------------------------------
                __append('<meta')

                # <Value 'tag' (3:8)> -> __cache_140355449696608
                __token = 64
                try:
                    __zt_tmp = __attrs_140355449698384
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140355449696608 = _static_140355540363392('path', 'tag', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                __attr_140355449698768 = __cache_140355449696608
                for (name, value, ) in __attr_140355449698768.items():
                    if (name in _static_140355449521008):
                        if not bool(value):
                            continue
                        value = name
                    if ((name not in _static_140355482573744) and (value is not None)):
                        if (name in _static_140355449521008):
                            if not bool(value):
                                continue
                            value = name
                        __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
                __append(' />')
                ____index_140355449697184 -= 1
                if (____index_140355449697184 > 0):
                    __append('\n')
            if (__backup_tag_140355449461872 is __marker):
                del econtext['tag']
            else:
                econtext['tag'] = __backup_tag_140355449461872
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }