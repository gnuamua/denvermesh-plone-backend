# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.portlets-5.0.7-py3.9.egg/plone/app/portlets/browser/templates/manage_portlets_fallback.pt'

__tokens = {56: ('view/available', 2, 20), 104: ('nothing', 4, 30), 240: ('string:${view/object_url}/@@manage-portlets', 11, 12)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355459549360 = {'class': 'managePortletsFallback', 'href': 'string:${view/object_url}/@@manage-portlets', }
_static_140355540704128 = {}
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355448640128 = {'class': 'row managePortlets-row', }

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

            # <Static value=<ast.Dict object at 0x7fa70ca89280> name=None at 7fa70ca89e80> -> __attrs_140355448640416
            __attrs_140355448640416 = _static_140355448640128

            # <Value 'view/available' (2:20)> -> __condition
            __token = 56
            try:
                __zt_tmp = __attrs_140355448640416
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'view/available', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="row managePortlets-row" >\n  ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448640560
                __attrs_140355448640560 = _static_140355540704128

                # <Value 'nothing' (4:30)> -> __condition
                __token = 104
                try:
                    __zt_tmp = __attrs_140355448640560
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('path', 'nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:
                    __append('\n\t\t**********\n\t\tNEEDED COL\n\t\t**********\n  ')
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7fa70d4f08b0> name=None at 7fa70ca896d0> -> __attrs_140355459549552
                __attrs_140355459549552 = _static_140355459549360
                __previous_i18n_domain_140355459548016 = __i18n_domain
                __i18n_domain = 'plone'

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="managePortletsFallback"')

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459550032
                __default_140355459550032 = _DEFAULT_MARKER

                # <Substitution 'string:${view/object_url}/@@manage-portlets' (11:12)> -> __attr_href
                __token = 240
                try:
                    __zt_tmp = __attrs_140355459549552
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140355540363392('string', '${view/object_url}/@@manage-portlets', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >')
                __stream_140355448640656 = []
                __append_140355448640656 = __stream_140355448640656.append
                __append_140355448640656('\n        Manage portlets\n  ')
                __msgid_140355448640656 = __re_whitespace(''.join(__stream_140355448640656)).strip()
                if 'manage_portlets_link':
                    __append(translate('manage_portlets_link', mapping=None, default=__msgid_140355448640656, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>')
                __i18n_domain = __previous_i18n_domain_140355459548016
                __append('\n\n</div>')
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }