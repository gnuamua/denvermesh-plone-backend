# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/viewlets/path_bar.pt'

__tokens = {96: ('python:view.breadcrumbs', 5, 19), 286: ('${python:view.navigation_root_url}', 12, 43), 288: ('python:view.navigation_root_url', 12, 45), 417: ('breadcrumbs', 15, 34), 494: ('not: repeat/crumb/end', 17, 27), 535: ("${python:crumb['absolute_url']}", 18, 18), 537: ("python:crumb['absolute_url']", 18, 20), 568: ("${python:crumb['Title']}", 18, 51), 570: ("python:crumb['Title']", 18, 53), 704: ('repeat/crumb/end', 21, 27), 731: ("${python:crumb['Title']}", 22, 9), 733: ("python:crumb['Title']", 22, 11)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355459573648 = {'class': 'breadcrumb-item active', 'aria-current': 'page', }
_static_140355449327824 = {'href': "${python:crumb['absolute_url']}", }
_static_140355449328688 = {'class': 'breadcrumb-item', }
_static_140355540704128 = {}
_static_140355448584656 = {'href': '${python:view.navigation_root_url}', }
_static_140355448585856 = {'class': 'breadcrumb-item', }
_static_140355448908096 = {'class': 'breadcrumb', }
_static_140355448909536 = {'class': 'container', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355448498832 = {'id': 'portal-breadcrumbs', 'aria-label': 'breadcrumb', }

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
            __append('\n')

            # <Static value=<ast.Dict object at 0x7fa70ca66a90> name=None at 7fa70ca663a0> -> __attrs_140355448909344
            __attrs_140355448909344 = _static_140355448498832
            __backup_breadcrumbs_140355448508912 = get('breadcrumbs', __marker)

            # <Value 'python:view.breadcrumbs' (5:19)> -> __value
            __token = 96
            try:
                __zt_tmp = __attrs_140355448909344
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', 'view.breadcrumbs', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['breadcrumbs'] = __value
            __previous_i18n_domain_140355448908288 = __i18n_domain
            __i18n_domain = 'plone'

            # <nav ... (0:0)
            # --------------------------------------------------------
            __append('<nav id="portal-breadcrumbs"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448908048
            __default_140355448908048 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7fa70ca66880> at 7fa70ca66070> -> __attr_aria_label
            __attr_aria_label = 'breadcrumb'
            __attr_aria_label = translate(__attr_aria_label, default=__attr_aria_label, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_aria_label is not None):
                __append((' aria-label="%s"' % __attr_aria_label))
            __append(' >\n  ')

            # <Static value=<ast.Dict object at 0x7fa70cacaee0> name=None at 7fa70caca3a0> -> __attrs_140355448908672
            __attrs_140355448908672 = _static_140355448909536

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container">\n    ')

            # <Static value=<ast.Dict object at 0x7fa70caca940> name=None at 7fa70cacaa30> -> __attrs_140355448585568
            __attrs_140355448585568 = _static_140355448908096

            # <ol ... (0:0)
            # --------------------------------------------------------
            __append('<ol class="breadcrumb">\n      ')

            # <Static value=<ast.Dict object at 0x7fa70ca7be80> name=None at 7fa70ca7b2b0> -> __attrs_140355448582544
            __attrs_140355448582544 = _static_140355448585856

            # <li ... (0:0)
            # --------------------------------------------------------
            __append('<li class="breadcrumb-item">')

            # <Static value=<ast.Dict object at 0x7fa70ca7b9d0> name=None at 7fa70ca7b130> -> __attrs_140355448586048
            __attrs_140355448586048 = _static_140355448584656

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448585472
            __default_140355448585472 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${python:view.navigation_root_url}' (12:43)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70ca7beb0> -> __attr_href
            __token = 286
            __token = 288
            try:
                __zt_tmp = __attrs_140355448586048
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140355540363392('python', 'view.navigation_root_url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
            __append(' >')
            __stream_140355448584368 = []
            __append_140355448584368 = __stream_140355448584368.append
            __append_140355448584368('Home')
            __msgid_140355448584368 = __re_whitespace(''.join(__stream_140355448584368)).strip()
            if 'tabs_home':
                __append(translate('tabs_home', mapping=None, default=__msgid_140355448584368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a></li>\n      ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449329792
            __attrs_140355449329792 = _static_140355540704128
            __backup_crumb_140355448860480 = get('crumb', __marker)

            # <Value 'breadcrumbs' (15:34)> -> __iterator
            __token = 417
            try:
                __zt_tmp = __attrs_140355449329792
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140355540363392('path', 'breadcrumbs', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            (__iterator, ____index_140355449328256, ) = getname('repeat')('crumb', __iterator)
            econtext['crumb'] = None
            for __item in __iterator:
                econtext['crumb'] = __item
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7fa70cb31430> name=None at 7fa70cb31fa0> -> __attrs_140355449330608
                __attrs_140355449330608 = _static_140355449328688

                # <Value 'not: repeat/crumb/end' (17:27)> -> __condition
                __token = 494
                try:
                    __zt_tmp = __attrs_140355449330608
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('not', ' repeat/crumb/end', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="breadcrumb-item" >')

                    # <Static value=<ast.Dict object at 0x7fa70cb310d0> name=None at 7fa70cb31070> -> __attrs_140355459572736
                    __attrs_140355459572736 = _static_140355449327824

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449329456
                    __default_140355449329456 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "${python:crumb['absolute_url']}" (18:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cb31df0> -> __attr_href
                    __token = 535
                    __token = 537
                    try:
                        __zt_tmp = __attrs_140355459572736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140355540363392('python', "crumb['absolute_url']", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
                    __append('>')

                    # <Interpolation value=<Substitution "${python:crumb['Title']}" (18:51)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70d4f6e20> -> __content_140355621335664
                    __token = 568
                    __token = 570
                    try:
                        __zt_tmp = __attrs_140355459572736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140355621335664 = _static_140355540363392('python', "crumb['Title']", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __content_140355621335664 = __quote(__content_140355621335664, '\x00', '&#0;', None, None)
                    __content_140355621335664 = __content_140355621335664
                    if (__content_140355621335664 is None):
                        pass
                    else:
                        if (__content_140355621335664 is None):
                            __content_140355621335664 = None
                        else:
                            __tt = type(__content_140355621335664)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140355621335664 = str(__content_140355621335664)
                            else:
                                if (__tt is bytes):
                                    __content_140355621335664 = decode(__content_140355621335664)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140355621335664 = __content_140355621335664.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140355621335664)
                                            __content_140355621335664 = (str(__content_140355621335664) if (__content_140355621335664 is __converted) else __converted)
                                        else:
                                            __content_140355621335664 = __content_140355621335664()
                    if (__content_140355621335664 is not None):
                        __append(__content_140355621335664)
                    __append('</a></li>')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7fa70d4f6790> name=None at 7fa70d4f6370> -> __attrs_140355459572880
                __attrs_140355459572880 = _static_140355459573648

                # <Value 'repeat/crumb/end' (21:27)> -> __condition
                __token = 704
                try:
                    __zt_tmp = __attrs_140355459572880
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('path', 'repeat/crumb/end', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="breadcrumb-item active" aria-current="page" >')

                    # <Interpolation value=<Substitution "${python:crumb['Title']}" (22:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70d4f6dc0> -> __content_140355621335664
                    __token = 731
                    __token = 733
                    try:
                        __zt_tmp = __attrs_140355459572880
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140355621335664 = _static_140355540363392('python', "crumb['Title']", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __content_140355621335664 = __quote(__content_140355621335664, '\x00', '&#0;', None, None)
                    __content_140355621335664 = __content_140355621335664
                    if (__content_140355621335664 is None):
                        pass
                    else:
                        if (__content_140355621335664 is None):
                            __content_140355621335664 = None
                        else:
                            __tt = type(__content_140355621335664)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140355621335664 = str(__content_140355621335664)
                            else:
                                if (__tt is bytes):
                                    __content_140355621335664 = decode(__content_140355621335664)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140355621335664 = __content_140355621335664.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140355621335664)
                                            __content_140355621335664 = (str(__content_140355621335664) if (__content_140355621335664 is __converted) else __converted)
                                        else:
                                            __content_140355621335664 = __content_140355621335664()
                    if (__content_140355621335664 is not None):
                        __append(__content_140355621335664)
                    __append('</li>')
                __append('\n      ')
                ____index_140355449328256 -= 1
                if (____index_140355449328256 > 0):
                    __append('')
            if (__backup_crumb_140355448860480 is __marker):
                del econtext['crumb']
            else:
                econtext['crumb'] = __backup_crumb_140355448860480
            __append('\n    </ol>\n  </div>\n</nav>')
            __i18n_domain = __previous_i18n_domain_140355448908288
            if (__backup_breadcrumbs_140355448508912 is __marker):
                del econtext['breadcrumbs']
            else:
                econtext['breadcrumbs'] = __backup_breadcrumbs_140355448508912
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }