# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.registry-2.0.4-py3.9.egg/plone/app/registry/browser/templates/controlpanel_layout.pt'

__tokens = {446: ('view/label', 16, 25), 524: ('view/description | nothing', 18, 26), 586: ('view/description', 19, 34), 680: ('context/@@global_statusmessage/macros/portal_message', 24, 28), 680: ('context/@@global_statusmessage/macros/portal_message', 24, 28), 879: ('view/contents', 30, 39), 247: ('context/@@prefs_main_template/macros/master', 6, 23), 247: ('context/@@prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140362872550160 = {'id': 'layout-contents', }
_static_140362872551312 = {'id': 'content-core', }
_static_140362872551504 = 'portal_message'
_static_140362863203136 = {'class': 'lead', }
_static_140362943564240 = __C2ZContextWrapper
_static_140362943564528 = __compile_zt_expr
_static_140362873388816 = 'master'
_static_140362943909360 = {}

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

            # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873387280
            __attrs_140362873387280 = _static_140362943909360
            __previous_i18n_domain_140362873388720 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140362893940416 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7fa8c7353f10> name=None at 7fa8c7353340> -> __value
            __value = _static_140362873388816
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873386656
                __attrs_140362873386656 = _static_140362943909360
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362917344448
                __attrs_140362917344448 = _static_140362943909360

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n\n        ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362863202752
                __attrs_140362863202752 = _static_140362943909360

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>')

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362863205440
                __default_140362863205440 = _DEFAULT_MARKER

                # <Value 'view/label' (16:25)> -> __cache_140362863204048
                __token = 446
                try:
                    __zt_tmp = __attrs_140362863202752
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140362863204048 = _static_140362943564528('path', 'view/label', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/label' (16:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c699df10> -> __condition
                __expression = __cache_140362863204048

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('View Title')
                else:
                    __content = __cache_140362863204048
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</h1>\n        ')

                # <Static value=<ast.Dict object at 0x7fa8c699d340> name=None at 7fa8c699db80> -> __attrs_140362863202368
                __attrs_140362863202368 = _static_140362863203136

                # <Value 'view/description | nothing' (18:26)> -> __condition
                __token = 524
                try:
                    __zt_tmp = __attrs_140362863202368
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140362943564528('path', 'view/description | nothing', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="lead" >')

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362863203856
                    __default_140362863203856 = _DEFAULT_MARKER

                    # <Value 'view/description' (19:34)> -> __cache_140362863205344
                    __token = 586
                    try:
                        __zt_tmp = __attrs_140362863202368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140362863205344 = _static_140362943564528('path', 'view/description', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                    # <BinOp left=<Value 'view/description' (19:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c699d9d0> -> __condition
                    __expression = __cache_140362863205344

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('View Description')
                    else:
                        __content = __cache_140362863205344
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</p>')
                __append('\n\n      </header>\n\n      ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872552128
                __attrs_140362872552128 = _static_140362943909360
                __backup_macroname_140362893940736 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x7fa8c7287850> name=None at 7fa8c7287f10> -> __value
                __value = _static_140362872551504
                econtext['macroname'] = __value

                # <Value 'context/@@global_statusmessage/macros/portal_message' (24:28)> -> __macro
                __token = 680
                try:
                    __zt_tmp = __attrs_140362872552128
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140362943564528('path', 'context/@@global_statusmessage/macros/portal_message', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __token = 680
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140362893940736 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140362893940736
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7fa8c7287790> name=None at 7fa8c7287490> -> __attrs_140362872550880
                __attrs_140362872550880 = _static_140362872551312

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n        ')

                # <Static value=<ast.Dict object at 0x7fa8c7287310> name=None at 7fa8c72876a0> -> __attrs_140362872553040
                __attrs_140362872553040 = _static_140362872550160

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="layout-contents">\n          ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873195392
                __attrs_140362873195392 = _static_140362943909360

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873195968
                __default_140362873195968 = _DEFAULT_MARKER

                # <Value 'view/contents' (30:39)> -> __cache_140362873196448
                __token = 879
                try:
                    __zt_tmp = __attrs_140362873195392
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140362873196448 = _static_140362943564528('path', 'view/contents', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/contents' (30:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c7324c70> -> __condition
                __expression = __cache_140362873196448

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span></span>')
                else:
                    __content = __cache_140362873196448
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n        </div>\n      </div>\n\n    ')
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/@@prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_140362873387280
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140362943564528('path', 'context/@@prefs_main_template/macros/master', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140362893940416 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140362893940416
            __i18n_domain = __previous_i18n_domain_140362873388720
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }