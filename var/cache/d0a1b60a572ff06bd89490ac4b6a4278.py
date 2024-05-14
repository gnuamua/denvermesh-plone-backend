# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.textfield-2.0.1-py3.9.egg/plone/app/textfield/widget_textarea_display.pt'

__tokens = {138: ("python:getattr(view.field, 'output_mime_type', None) == 'text/x-html-safe'", 4, 23), 339: (' view/klas', 12, 15), 315: ('view/id', 11, 13), 366: ('e view/sty', 13, 14), 393: ('le view/ti', 14, 13), 419: ('ang view/', 15, 11), 447: ('lick view/on', 16, 13), 481: ('click view/ondb', 17, 15), 519: ('sedown view/onmo', 18, 15), 556: ('mouseup view/o', 19, 12), 593: ('ouseover view/on', 20, 13), 632: ('mousemove view/o', 21, 12), 670: ('onmouseout view', 22, 10), 707: (' onkeypress vie', 23, 9), 743: ('   onkeydown v', 24, 7), 776: ('      onkeyu', 25, 4), 839: ('view/value', 27, 25), 877: ('safe_structure', 27, 63), 929: ('view/value', 28, 36), 971: ('not: safe_structure', 29, 30), 1018: ('view/value', 30, 26)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355540704128 = {}
_static_140355459855120 = {'class': '', 'id': '', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355449162144 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7fa70cb089a0> name=None at 7fa70cb088e0> -> __attrs_140355449160560
            __attrs_140355449160560 = _static_140355449162144
            __backup_safe_structure_140355470312352 = get('safe_structure', __marker)

            # <Value "python:getattr(view.field, 'output_mime_type', None) == 'text/x-html-safe'" (4:23)> -> __value
            __token = 138
            try:
                __zt_tmp = __attrs_140355449160560
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "getattr(view.field, 'output_mime_type', None) == 'text/x-html-safe'", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['safe_structure'] = __value
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7fa70d53b310> name=None at 7fa70d53b9d0> -> __attrs_140355469856480
            __attrs_140355469856480 = _static_140355459855120

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459856608
            __default_140355459856608 = _DEFAULT_MARKER

            # <Substitution 'view/klass' (12:15)> -> __attr_class
            __token = 339
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140355540363392('path', 'view/klass', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355470334848
            __default_140355470334848 = _DEFAULT_MARKER

            # <Substitution 'view/id' (11:13)> -> __attr_id
            __token = 315
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140355540363392('path', 'view/id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355470335904
            __default_140355470335904 = _DEFAULT_MARKER

            # <Substitution 'view/style' (13:14)> -> __attr_style
            __token = 366
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140355540363392('path', 'view/style', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355470332208
            __default_140355470332208 = _DEFAULT_MARKER

            # <Substitution 'view/title' (14:13)> -> __attr_title
            __token = 393
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140355540363392('path', 'view/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355470332400
            __default_140355470332400 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (15:11)> -> __attr_lang
            __token = 419
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140355540363392('path', 'view/lang', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355470333840
            __default_140355470333840 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (16:13)> -> __attr_onclick
            __token = 447
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140355540363392('path', 'view/onclick', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355470334128
            __default_140355470334128 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (17:15)> -> __attr_ondblclick
            __token = 481
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140355540363392('path', 'view/ondblclick', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355470333072
            __default_140355470333072 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (18:15)> -> __attr_onmousedown
            __token = 519
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140355540363392('path', 'view/onmousedown', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355470334704
            __default_140355470334704 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (19:12)> -> __attr_onmouseup
            __token = 556
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140355540363392('path', 'view/onmouseup', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355470335856
            __default_140355470335856 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (20:13)> -> __attr_onmouseover
            __token = 593
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140355540363392('path', 'view/onmouseover', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355481086272
            __default_140355481086272 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (21:12)> -> __attr_onmousemove
            __token = 632
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140355540363392('path', 'view/onmousemove', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355469901152
            __default_140355469901152 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (22:10)> -> __attr_onmouseout
            __token = 670
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140355540363392('path', 'view/onmouseout', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355469901536
            __default_140355469901536 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (23:9)> -> __attr_onkeypress
            __token = 707
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140355540363392('path', 'view/onkeypress', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355469900528
            __default_140355469900528 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (24:7)> -> __attr_onkeydown
            __token = 743
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140355540363392('path', 'view/onkeydown', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355469855184
            __default_140355469855184 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (25:4)> -> __attr_onkeyup
            __token = 776
            try:
                __zt_tmp = __attrs_140355469856480
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140355540363392('path', 'view/onkeyup', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))
            __append(' >')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355469856000
            __attrs_140355469856000 = _static_140355540704128

            # <Value 'view/value' (27:25)> -> __condition
            __token = 839
            try:
                __zt_tmp = __attrs_140355469856000
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'view/value', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459951152
                __attrs_140355459951152 = _static_140355540704128

                # <Value 'safe_structure' (27:63)> -> __condition
                __token = 877
                try:
                    __zt_tmp = __attrs_140355459951152
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('path', 'safe_structure', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355469855520
                    __default_140355469855520 = _DEFAULT_MARKER

                    # <Value 'view/value' (28:36)> -> __cache_140355469856384
                    __token = 929
                    try:
                        __zt_tmp = __attrs_140355459951152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355469856384 = _static_140355540363392('path', 'view/value', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/value' (28:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70dec4eb0> -> __condition
                    __expression = __cache_140355469856384

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355469856384
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459952544
                __attrs_140355459952544 = _static_140355540704128

                # <Value 'not: safe_structure' (29:30)> -> __condition
                __token = 971
                try:
                    __zt_tmp = __attrs_140355459952544
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('not', ' safe_structure', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459952016
                    __default_140355459952016 = _DEFAULT_MARKER

                    # <Value 'view/value' (30:26)> -> __cache_140355459949664
                    __token = 1018
                    try:
                        __zt_tmp = __attrs_140355459952544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355459949664 = _static_140355540363392('path', 'view/value', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/value' (30:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70d5529a0> -> __condition
                    __expression = __cache_140355459949664

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355459949664
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
            __append('</span>\n')
            if (__backup_safe_structure_140355470312352 is __marker):
                del econtext['safe_structure']
            else:
                econtext['safe_structure'] = __backup_safe_structure_140355470312352
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }