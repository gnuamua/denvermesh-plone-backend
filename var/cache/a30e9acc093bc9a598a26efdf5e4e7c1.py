# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/z3c.form-4.3-py3.9.egg/z3c/form/browser/text_display.pt'

__tokens = {173: ('view/id', 5, 29), 213: (' view/klas', 6, 31), 256: ('e view/sty', 7, 30), 299: ('le view/ti', 8, 29), 341: ('ang view/', 9, 27), 385: ('lick view/on', 10, 29), 435: ('click view/ondb', 11, 31), 489: ('sedown view/onmo', 12, 31), 542: ('mouseup view/o', 13, 28), 595: ('ouseover view/on', 14, 29), 650: ('mousemove view/o', 15, 28), 704: ('onmouseout view', 16, 26), 757: (' onkeypress vie', 17, 25), 809: ('   onkeydown v', 18, 23), 858: ('      onkeyu', 19, 20), 918: ('view/value', 20, 21), 939: ('view/value', 20, 42)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355540704128 = {}
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355458994384 = {'id': '', 'class': '', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', }
_static_140355449892928 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7fa70cbbb040> name=None at 7fa70d561730> -> __attrs_140355459905088
            __attrs_140355459905088 = _static_140355449892928
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x7fa70d4690d0> name=None at 7fa70d4692e0> -> __attrs_140355448548464
            __attrs_140355448548464 = _static_140355458994384

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355469469632
            __default_140355469469632 = _DEFAULT_MARKER

            # <Substitution 'view/id' (5:29)> -> __attr_id
            __token = 173
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140355540363392('path', 'view/id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459887840
            __default_140355459887840 = _DEFAULT_MARKER

            # <Substitution 'view/klass' (6:31)> -> __attr_class
            __token = 213
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140355540363392('path', 'view/klass', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_class is not None):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459890480
            __default_140355459890480 = _DEFAULT_MARKER

            # <Substitution 'view/style' (7:30)> -> __attr_style
            __token = 256
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140355540363392('path', 'view/style', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459889664
            __default_140355459889664 = _DEFAULT_MARKER

            # <Substitution 'view/title' (8:29)> -> __attr_title
            __token = 299
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140355540363392('path', 'view/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459889040
            __default_140355459889040 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (9:27)> -> __attr_lang
            __token = 341
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140355540363392('path', 'view/lang', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459887504
            __default_140355459887504 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (10:29)> -> __attr_onclick
            __token = 385
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140355540363392('path', 'view/onclick', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459887648
            __default_140355459887648 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (11:31)> -> __attr_ondblclick
            __token = 435
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140355540363392('path', 'view/ondblclick', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459888752
            __default_140355459888752 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (12:31)> -> __attr_onmousedown
            __token = 489
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140355540363392('path', 'view/onmousedown', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459887408
            __default_140355459887408 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (13:28)> -> __attr_onmouseup
            __token = 542
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140355540363392('path', 'view/onmouseup', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459890960
            __default_140355459890960 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (14:29)> -> __attr_onmouseover
            __token = 595
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140355540363392('path', 'view/onmouseover', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459888992
            __default_140355459888992 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (15:28)> -> __attr_onmousemove
            __token = 650
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140355540363392('path', 'view/onmousemove', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448674768
            __default_140355448674768 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (16:26)> -> __attr_onmouseout
            __token = 704
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140355540363392('path', 'view/onmouseout', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448672464
            __default_140355448672464 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (17:25)> -> __attr_onkeypress
            __token = 757
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140355540363392('path', 'view/onkeypress', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448546256
            __default_140355448546256 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (18:23)> -> __attr_onkeydown
            __token = 809
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140355540363392('path', 'view/onkeydown', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448549232
            __default_140355448549232 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (19:20)> -> __attr_onkeyup
            __token = 858
            try:
                __zt_tmp = __attrs_140355448548464
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140355540363392('path', 'view/onkeyup', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))
            __append('>')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449823680
            __attrs_140355449823680 = _static_140355540704128

            # <Value 'view/value' (20:21)> -> __condition
            __token = 918
            try:
                __zt_tmp = __attrs_140355449823680
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'view/value', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449823440
                __default_140355449823440 = _DEFAULT_MARKER

                # <Value 'view/value' (20:42)> -> __cache_140355482572544
                __token = 939
                try:
                    __zt_tmp = __attrs_140355449823680
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140355482572544 = _static_140355540363392('path', 'view/value', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/value' (20:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cbaa280> -> __condition
                __expression = __cache_140355482572544

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140355482572544
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
            __append('</span>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }