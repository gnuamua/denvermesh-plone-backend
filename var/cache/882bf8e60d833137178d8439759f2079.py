# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/viewlets/document_rights.pt'

__tokens = {97: ('context/Rights', 4, 18), 148: ('rights', 6, 24), 324: ('rights', 16, 22)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355540704128 = {}
_static_140355448548752 = {'class': 'section-heading', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355449443232 = {'class': 'text-muted', 'id': 'section-rights', }

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

            # <Static value=<ast.Dict object at 0x7fa70cb4d3a0> name=None at 7fa70cb449a0> -> __attrs_140355448548320
            __attrs_140355448548320 = _static_140355449443232
            __backup_rights_140355448500432 = get('rights', __marker)

            # <Value 'context/Rights' (4:18)> -> __value
            __token = 97
            try:
                __zt_tmp = __attrs_140355448548320
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'context/Rights', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['rights'] = __value

            # <Value 'rights' (6:24)> -> __condition
            __token = 148
            try:
                __zt_tmp = __attrs_140355448548320
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'rights', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140355448547168 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="text-muted" id="section-rights" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa70ca72d90> name=None at 7fa70ca721c0> -> __attrs_140355448547312
                __attrs_140355448547312 = _static_140355448548752

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="section-heading" >')
                __stream_140355448545872 = []
                __append_140355448545872 = __stream_140355448545872.append
                __append_140355448545872('\n      Rights\n  ')
                __msgid_140355448545872 = __re_whitespace(''.join(__stream_140355448545872)).strip()
                if 'section_rights_heading':
                    __append(translate('section_rights_heading', mapping=None, default=__msgid_140355448545872, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449106736
                __attrs_140355449106736 = _static_140355540704128

                # <small ... (0:0)
                # --------------------------------------------------------
                __append('<small>')

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449108368
                __default_140355449108368 = _DEFAULT_MARKER

                # <Value 'rights' (16:22)> -> __cache_140355448547216
                __token = 324
                try:
                    __zt_tmp = __attrs_140355449106736
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140355448547216 = _static_140355540363392('path', 'rights', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                # <BinOp left=<Value 'rights' (16:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70ca72f10> -> __condition
                __expression = __cache_140355448547216

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Copyleft NiceCorp Inc.')
                else:
                    __content = __cache_140355448547216
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</small>\n\n</section>')
                __i18n_domain = __previous_i18n_domain_140355448547168
            if (__backup_rights_140355448500432 is __marker):
                del econtext['rights']
            else:
                econtext['rights'] = __backup_rights_140355448500432
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }