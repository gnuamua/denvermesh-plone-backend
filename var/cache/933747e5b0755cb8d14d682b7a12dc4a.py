# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/z3c.form-4.3-py3.9.egg/z3c/form/browser/textlines_hidden.pt'

__tokens = {256: ('view/id', 7, 26), 292: (' view/nam', 8, 27), 465: ('alue view/', 12, 24), 331: ('e view/tit', 9, 27), 374: ('ex view/tabin', 10, 29), 421: ('key view/acces', 11, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140362943564240 = __C2ZContextWrapper
_static_140362943564528 = __compile_zt_expr
_static_140362872474592 = {'id': '', 'name': '', 'value': '', 'class': 'hidden-widget', 'title': '', 'tabindex': '', 'accesskey': '', 'type': 'hidden', }
_static_140362883031680 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7fa8c7c86280> name=None at 7fa8c7c860a0> -> __attrs_140362872474544
            __attrs_140362872474544 = _static_140362883031680
            __append('\n')

            # <Static value=<ast.Dict object at 0x7fa8c7274be0> name=None at 7fa8c7274400> -> __attrs_140362873535168
            __attrs_140362873535168 = _static_140362872474592

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input')

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872473680
            __default_140362872473680 = _DEFAULT_MARKER

            # <Substitution 'view/id' (7:26)> -> __attr_id
            __token = 256
            try:
                __zt_tmp = __attrs_140362873535168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140362943564528('path', 'view/id', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872474400
            __default_140362872474400 = _DEFAULT_MARKER

            # <Substitution 'view/name' (8:27)> -> __attr_name
            __token = 292
            try:
                __zt_tmp = __attrs_140362873535168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140362943564528('path', 'view/name', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872472192
            __default_140362872472192 = _DEFAULT_MARKER

            # <Substitution 'view/value' (12:24)> -> __attr_value
            __token = 465
            try:
                __zt_tmp = __attrs_140362873535168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140362943564528('path', 'view/value', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' class="hidden-widget"')

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872471904
            __default_140362872471904 = _DEFAULT_MARKER

            # <Substitution 'view/title' (9:27)> -> __attr_title
            __token = 331
            try:
                __zt_tmp = __attrs_140362873535168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140362943564528('path', 'view/title', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873533344
            __default_140362873533344 = _DEFAULT_MARKER

            # <Substitution 'view/tabindex' (10:29)> -> __attr_tabindex
            __token = 374
            try:
                __zt_tmp = __attrs_140362873535168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_tabindex = _static_140362943564528('path', 'view/tabindex', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_tabindex = __quote(__attr_tabindex, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_tabindex is not None):
                __append((' tabindex="%s"' % __attr_tabindex))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873535552
            __default_140362873535552 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (11:29)> -> __attr_accesskey
            __token = 421
            try:
                __zt_tmp = __attrs_140362873535168
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_140362943564528('path', 'view/accesskey', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', '', _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))
            __append(' type="hidden" />\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }