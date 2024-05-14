# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/viewlets/keywords.pt'

__tokens = {75: ('context/Subject|nothing', 3, 22), 120: (' nocall:modules/Products.PythonScripts.standard/url_quot', 4, 20), 214: ('categories', 6, 24), 481: ('categories', 18, 37), 627: ('python:url_quote(category)', 23, 21), 708: ('string:${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}', 26, 16), 851: ('category', 29, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355448523312 = {'class': 'btn btn-sm btn-outline-primary', 'href': '#', 'rel': 'nofollow', }
_static_140355540704128 = {}
_static_140355459796752 = {'class': 'card-title section-heading d-none', }
_static_140355459398096 = {'class': 'viewlet keywords-viewlet', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355448529440 = {'id': 'section-category', }

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

            # <Static value=<ast.Dict object at 0x7fa70ca6e220> name=None at 7fa70ca6e310> -> __attrs_140355448532848
            __attrs_140355448532848 = _static_140355448529440
            __backup_categories_140355459515632 = get('categories', __marker)

            # <Value 'context/Subject|nothing' (3:22)> -> __value
            __token = 75
            try:
                __zt_tmp = __attrs_140355448532848
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'context/Subject|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['categories'] = __value
            __backup_url_quote_140355449232736 = get('url_quote', __marker)

            # <Value 'nocall:modules/Products.PythonScripts.standard/url_quote' (4:20)> -> __value
            __token = 120
            try:
                __zt_tmp = __attrs_140355448532848
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('nocall', 'modules/Products.PythonScripts.standard/url_quote', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['url_quote'] = __value

            # <Value 'categories' (6:24)> -> __condition
            __token = 214
            try:
                __zt_tmp = __attrs_140355448532848
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'categories', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140355459396224 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-category" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa70d4cb9d0> name=None at 7fa70d4cb490> -> __attrs_140355459795792
                __attrs_140355459795792 = _static_140355459398096

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="viewlet keywords-viewlet">\n\n    ')

                # <Static value=<ast.Dict object at 0x7fa70d52cf10> name=None at 7fa70d52cee0> -> __attrs_140355459796032
                __attrs_140355459796032 = _static_140355459796752

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="card-title section-heading d-none" >')
                __stream_140355459794784 = []
                __append_140355459794784 = __stream_140355459794784.append
                __append_140355459794784('\n      Keywords\n    ')
                __msgid_140355459794784 = __re_whitespace(''.join(__stream_140355459794784)).strip()
                if 'section_keywords_heading':
                    __append(translate('section_keywords_heading', mapping=None, default=__msgid_140355459794784, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n\n    ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459796176
                __attrs_140355459796176 = _static_140355540704128
                __backup_category_140355449639408 = get('category', __marker)

                # <Value 'categories' (18:37)> -> __iterator
                __token = 481
                try:
                    __zt_tmp = __attrs_140355459796176
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140355540363392('path', 'categories', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                (__iterator, ____index_140355459793440, ) = getname('repeat')('category', __iterator)
                econtext['category'] = None
                for __item in __iterator:
                    econtext['category'] = __item
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7fa70ca6ca30> name=None at 7fa70ca6c400> -> __attrs_140355448522832
                    __attrs_140355448522832 = _static_140355448523312
                    __backup_quotedCat_140355482518192 = get('quotedCat', __marker)

                    # <Value 'python:url_quote(category)' (23:21)> -> __value
                    __token = 627
                    try:
                        __zt_tmp = __attrs_140355448522832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('python', 'url_quote(category)', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['quotedCat'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="btn btn-sm btn-outline-primary"')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448523840
                    __default_140355448523840 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}' (26:16)> -> __attr_href
                    __token = 708
                    try:
                        __zt_tmp = __attrs_140355448522832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140355540363392('string', '${context/@@plone_portal_state/navigation_root_url}/@@search?Subject%3Alist=${quotedCat}', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' rel="nofollow" >\n        ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448978256
                    __attrs_140355448978256 = _static_140355540704128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448522784
                    __default_140355448522784 = _DEFAULT_MARKER

                    # <Value 'category' (29:27)> -> __cache_140355448522064
                    __token = 851
                    try:
                        __zt_tmp = __attrs_140355448978256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355448522064 = _static_140355540363392('path', 'category', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'category' (29:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70ca6ce20> -> __condition
                    __expression = __cache_140355448522064

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355448522064
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n      </a>')
                    if (__backup_quotedCat_140355482518192 is __marker):
                        del econtext['quotedCat']
                    else:
                        econtext['quotedCat'] = __backup_quotedCat_140355482518192
                    __append('\n    ')
                    ____index_140355459793440 -= 1
                    if (____index_140355459793440 > 0):
                        __append('')
                if (__backup_category_140355449639408 is __marker):
                    del econtext['category']
                else:
                    econtext['category'] = __backup_category_140355449639408
                __append('\n\n  </div>\n\n</section>')
                __i18n_domain = __previous_i18n_domain_140355459396224
            if (__backup_url_quote_140355449232736 is __marker):
                del econtext['url_quote']
            else:
                econtext['url_quote'] = __backup_url_quote_140355449232736
            if (__backup_categories_140355459515632 is __marker):
                del econtext['categories']
            else:
                econtext['categories'] = __backup_categories_140355459515632
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }