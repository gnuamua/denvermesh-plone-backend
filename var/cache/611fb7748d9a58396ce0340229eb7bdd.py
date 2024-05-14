# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/links/rsslink.pt'

__tokens = {28: ('view/rsslinks', 1, 28), 58: ('${link/url}', 2, 14), 60: ('link/url', 2, 16), 110: ('${link/title}', 4, 15), 112: ('link/title', 4, 17)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355449846224 = {'href': '${link/url}', 'rel': 'alternate', 'title': '${link/title}', 'type': 'application/rss+xml', }
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

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449843920
            __attrs_140355449843920 = _static_140355540704128
            __backup_link_140355449844160 = get('link', __marker)

            # <Value 'view/rsslinks' (1:28)> -> __iterator
            __token = 28
            try:
                __zt_tmp = __attrs_140355449843920
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140355540363392('path', 'view/rsslinks', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            (__iterator, ____index_140355449843776, ) = getname('repeat')('link', __iterator)
            econtext['link'] = None
            for __item in __iterator:
                econtext['link'] = __item
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7fa70cbaf9d0> name=None at 7fa70cbafd90> -> __attrs_140355482574320
                __attrs_140355482574320 = _static_140355449846224

                # <link ... (0:0)
                # --------------------------------------------------------
                __append('<link')

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449844736
                __default_140355449844736 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${link/url}' (2:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cbaf280> -> __attr_href
                __token = 58
                __token = 60
                try:
                    __zt_tmp = __attrs_140355482574320
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140355540363392('path', 'link/url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_href = __attr_href
                if (__attr_href is None):
                    pass
                else:
                    if (__attr_href is _DEFAULT_MARKER):
                        __attr_href = None
                    else:
                        __tt = type(__attr_href)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_href = str(__attr_href)
                        else:
                            if (__tt is bytes):
                                __attr_href = decode(__attr_href)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_href = __attr_href.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_href)
                                        __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                    else:
                                        __attr_href = __attr_href()
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' rel="alternate"')

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355482571680
                __default_140355482571680 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${link/title}' (4:15)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cb4a340> -> __attr_title
                __token = 110
                __token = 112
                try:
                    __zt_tmp = __attrs_140355482574320
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_title = _static_140355540363392('path', 'link/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_title = __attr_title
                if (__attr_title is None):
                    pass
                else:
                    if (__attr_title is _DEFAULT_MARKER):
                        __attr_title = None
                    else:
                        __tt = type(__attr_title)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_title = str(__attr_title)
                        else:
                            if (__tt is bytes):
                                __attr_title = decode(__attr_title)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_title = __attr_title.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_title)
                                        __attr_title = (str(__attr_title) if (__attr_title is __converted) else __converted)
                                    else:
                                        __attr_title = __attr_title()
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append(' type="application/rss+xml" />\n')
                ____index_140355449843776 -= 1
                if (____index_140355449843776 > 0):
                    __append('')
            if (__backup_link_140355449844160 is __marker):
                del econtext['link']
            else:
                econtext['link'] = __backup_link_140355449844160
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }