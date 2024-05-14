# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.i18n-4.0.1-py3.9.egg/plone/app/i18n/locales/browser/languageselector.pt'

__tokens = {29: ('view/available', 1, 29), 118: ('view/showFlags', 4, 18), 151: (' view/language', 5, 17), 183: ('l context/@@plone_context_state/view_u', 6, 15), 241: ('rl view/portal_', 7, 16), 271: ("ons python:context.restrictedTraverse('@@iconresolv", 8, 10), 371: ('languages', 11, 31), 423: ('lang/code', 13, 17), 454: (' lang/selecte', 14, 20), 490: ('s string:language-${cod', 15, 20), 534: ("nt python: selected and 'currentLanguage ' or", 16, 17), 641: ('string:${current}${codeclass}', 19, 18), 753: ('lang/flag|nothing', 24, 18), 789: (' lang/native|lang/nam', 25, 17), 833: ('g python:showFlags and fl', 26, 20), 921: ('string:${here_url}?set_language=${code}', 29, 18), 980: (' nam', 30, 18), 1041: ('showflag', 33, 31), 1092: ("python:icons.tag(flag, tag_class='plone-icon-flag')", 34, 40), 1204: ('not: showflag', 36, 34), 1251: ('name', 37, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355449845168 = {'href': '', 'title': 'name', }
_static_140355448946800 = {'class': 'string:${current}${codeclass}', }
_static_140355449084800 = {'id': 'portal-languageselector', }
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

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448931664
            __attrs_140355448931664 = _static_140355540704128

            # <Value 'view/available' (1:29)> -> __condition
            __token = 29
            try:
                __zt_tmp = __attrs_140355448931664
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'view/available', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7fa70caf5b80> name=None at 7fa70caf5f40> -> __attrs_140355449083312
                __attrs_140355449083312 = _static_140355449084800
                __backup_showFlags_140355459620768 = get('showFlags', __marker)

                # <Value 'view/showFlags' (4:18)> -> __value
                __token = 118
                try:
                    __zt_tmp = __attrs_140355449083312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'view/showFlags', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['showFlags'] = __value
                __backup_languages_140355459743808 = get('languages', __marker)

                # <Value 'view/languages' (5:17)> -> __value
                __token = 151
                try:
                    __zt_tmp = __attrs_140355449083312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'view/languages', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['languages'] = __value
                __backup_here_url_140355448531456 = get('here_url', __marker)

                # <Value 'context/@@plone_context_state/view_url' (6:15)> -> __value
                __token = 183
                try:
                    __zt_tmp = __attrs_140355449083312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'context/@@plone_context_state/view_url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['here_url'] = __value
                __backup_portal_url_140355448655008 = get('portal_url', __marker)

                # <Value 'view/portal_url' (7:16)> -> __value
                __token = 241
                try:
                    __zt_tmp = __attrs_140355449083312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'view/portal_url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __backup_icons_140355448548992 = get('icons', __marker)

                # <Value "python:context.restrictedTraverse('@@iconresolver')" (8:10)> -> __value
                __token = 271
                try:
                    __zt_tmp = __attrs_140355449083312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['icons'] = __value

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul id="portal-languageselector" >\n    ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449083264
                __attrs_140355449083264 = _static_140355540704128
                __backup_lang_140355448531984 = get('lang', __marker)

                # <Value 'languages' (11:31)> -> __iterator
                __token = 371
                try:
                    __zt_tmp = __attrs_140355449083264
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140355540363392('path', 'languages', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                (__iterator, ____index_140355448949392, ) = getname('repeat')('lang', __iterator)
                econtext['lang'] = None
                for __item in __iterator:
                    econtext['lang'] = __item
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7fa70cad4070> name=None at 7fa70cad4c40> -> __attrs_140355448950256
                    __attrs_140355448950256 = _static_140355448946800
                    __backup_code_140355459449184 = get('code', __marker)

                    # <Value 'lang/code' (13:17)> -> __value
                    __token = 423
                    try:
                        __zt_tmp = __attrs_140355448950256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'lang/code', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['code'] = __value
                    __backup_selected_140355448912480 = get('selected', __marker)

                    # <Value 'lang/selected' (14:20)> -> __value
                    __token = 454
                    try:
                        __zt_tmp = __attrs_140355448950256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'lang/selected', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['selected'] = __value
                    __backup_codeclass_140355459487728 = get('codeclass', __marker)

                    # <Value 'string:language-${code}' (15:20)> -> __value
                    __token = 490
                    try:
                        __zt_tmp = __attrs_140355448950256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('string', 'language-${code}', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['codeclass'] = __value
                    __backup_current_140355448910560 = get('current', __marker)

                    # <Value "python: selected and 'currentLanguage ' or ''" (16:17)> -> __value
                    __token = 534
                    try:
                        __zt_tmp = __attrs_140355448950256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('python', " selected and 'currentLanguage ' or ''", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['current'] = __value

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448949632
                    __default_140355448949632 = _DEFAULT_MARKER

                    # <Substitution 'string:${current}${codeclass}' (19:18)> -> __attr_class
                    __token = 641
                    try:
                        __zt_tmp = __attrs_140355448950256
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140355540363392('string', '${current}${codeclass}', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x7fa70cbaf5b0> name=None at 7fa70cbafd60> -> __attrs_140355449846800
                    __attrs_140355449846800 = _static_140355449845168
                    __backup_flag_140355448948576 = get('flag', __marker)

                    # <Value 'lang/flag|nothing' (24:18)> -> __value
                    __token = 753
                    try:
                        __zt_tmp = __attrs_140355449846800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'lang/flag|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['flag'] = __value
                    __backup_name_140355448949968 = get('name', __marker)

                    # <Value 'lang/native|lang/name' (25:17)> -> __value
                    __token = 789
                    try:
                        __zt_tmp = __attrs_140355449846800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'lang/native|lang/name', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['name'] = __value
                    __backup_showflag_140355448950640 = get('showflag', __marker)

                    # <Value 'python:showFlags and flag' (26:20)> -> __value
                    __token = 833
                    try:
                        __zt_tmp = __attrs_140355449846800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('python', 'showFlags and flag', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['showflag'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449845216
                    __default_140355449845216 = _DEFAULT_MARKER

                    # <Substitution 'string:${here_url}?set_language=${code}' (29:18)> -> __attr_href
                    __token = 921
                    try:
                        __zt_tmp = __attrs_140355449846800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140355540363392('string', '${here_url}?set_language=${code}', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449843872
                    __default_140355449843872 = _DEFAULT_MARKER

                    # <Substitution 'name' (30:18)> -> __attr_title
                    __token = 980
                    try:
                        __zt_tmp = __attrs_140355449846800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140355540363392('path', 'name', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' >\n          ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449359808
                    __attrs_140355449359808 = _static_140355540704128

                    # <Value 'showflag' (33:31)> -> __condition
                    __token = 1041
                    try:
                        __zt_tmp = __attrs_140355449359808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('path', 'showflag', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459551136
                        __attrs_140355459551136 = _static_140355540704128

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459549360
                        __default_140355459549360 = _DEFAULT_MARKER

                        # <Value "python:icons.tag(flag, tag_class='plone-icon-flag')" (34:40)> -> __cache_140355459548112
                        __token = 1092
                        try:
                            __zt_tmp = __attrs_140355459551136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355459548112 = _static_140355540363392('python', "icons.tag(flag, tag_class='plone-icon-flag')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag(flag, tag_class='plone-icon-flag')" (34:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70d4f05e0> -> __condition
                        __expression = __cache_140355459548112

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <img ... (0:0)
                            # --------------------------------------------------------
                            __append('<img />')
                        else:
                            __content = __cache_140355459548112
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n          ')
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459547488
                    __attrs_140355459547488 = _static_140355540704128

                    # <Value 'not: showflag' (36:34)> -> __condition
                    __token = 1204
                    try:
                        __zt_tmp = __attrs_140355459547488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('not', ' showflag', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459550032
                        __default_140355459550032 = _DEFAULT_MARKER

                        # <Value 'name' (37:32)> -> __cache_140355459550656
                        __token = 1251
                        try:
                            __zt_tmp = __attrs_140355459547488
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355459550656 = _static_140355540363392('path', 'name', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value 'name' (37:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70d4f0d60> -> __condition
                        __expression = __cache_140355459550656

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('language name')
                        else:
                            __content = __cache_140355459550656
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    __append('\n        </a>')
                    if (__backup_showflag_140355448950640 is __marker):
                        del econtext['showflag']
                    else:
                        econtext['showflag'] = __backup_showflag_140355448950640
                    if (__backup_name_140355448949968 is __marker):
                        del econtext['name']
                    else:
                        econtext['name'] = __backup_name_140355448949968
                    if (__backup_flag_140355448948576 is __marker):
                        del econtext['flag']
                    else:
                        econtext['flag'] = __backup_flag_140355448948576
                    __append('\n      </li>')
                    if (__backup_current_140355448910560 is __marker):
                        del econtext['current']
                    else:
                        econtext['current'] = __backup_current_140355448910560
                    if (__backup_codeclass_140355459487728 is __marker):
                        del econtext['codeclass']
                    else:
                        econtext['codeclass'] = __backup_codeclass_140355459487728
                    if (__backup_selected_140355448912480 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_140355448912480
                    if (__backup_code_140355459449184 is __marker):
                        del econtext['code']
                    else:
                        econtext['code'] = __backup_code_140355459449184
                    __append('\n    ')
                    ____index_140355448949392 -= 1
                    if (____index_140355448949392 > 0):
                        __append('')
                if (__backup_lang_140355448531984 is __marker):
                    del econtext['lang']
                else:
                    econtext['lang'] = __backup_lang_140355448531984
                __append('\n  </ul>')
                if (__backup_icons_140355448548992 is __marker):
                    del econtext['icons']
                else:
                    econtext['icons'] = __backup_icons_140355448548992
                if (__backup_portal_url_140355448655008 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_140355448655008
                if (__backup_here_url_140355448531456 is __marker):
                    del econtext['here_url']
                else:
                    econtext['here_url'] = __backup_here_url_140355448531456
                if (__backup_languages_140355459743808 is __marker):
                    del econtext['languages']
                else:
                    econtext['languages'] = __backup_languages_140355459743808
                if (__backup_showFlags_140355459620768 is __marker):
                    del econtext['showFlags']
                else:
                    econtext['showFlags'] = __backup_showFlags_140355459620768
                __append('\n')
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }