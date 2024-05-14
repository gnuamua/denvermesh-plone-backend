# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/viewlets/contentviews.pt'

__tokens = {61: ('context/@@plone', 2, 30), 131: ('ploneview/showToolbar', 4, 33), 240: ('view/tabSet1', 9, 23), 302: ('python: view.menu_template(actions=actions)', 11, 32), 460: ('provider:plone.contentmenu', 17, 32), 600: ('view/tabSet2', 23, 23), 662: ('python: view.menu_template(actions=actions)', 25, 32)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355448980816 = {'class': 'border-top my-2', }
_static_140355448978064 = {'class': 'border-top my-2', }
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

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448977200
            __attrs_140355448977200 = _static_140355540704128
            __backup_ploneview_140355449357504 = get('ploneview', __marker)

            # <Value 'context/@@plone' (2:30)> -> __value
            __token = 61
            try:
                __zt_tmp = __attrs_140355448977200
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'context/@@plone', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['ploneview'] = __value

            # <Value 'ploneview/showToolbar' (4:33)> -> __condition
            __token = 131
            try:
                __zt_tmp = __attrs_140355448977200
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'ploneview/showToolbar', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140355448979168 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448979072
                __attrs_140355448979072 = _static_140355540704128
                __backup_actions_140355449613328 = get('actions', __marker)

                # <Value 'view/tabSet1' (9:23)> -> __value
                __token = 240
                try:
                    __zt_tmp = __attrs_140355448979072
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'view/tabSet1', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448981296
                __attrs_140355448981296 = _static_140355540704128

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448981872
                __default_140355448981872 = _DEFAULT_MARKER

                # <Value 'python: view.menu_template(actions=actions)' (11:32)> -> __cache_140355448977344
                __token = 302
                try:
                    __zt_tmp = __attrs_140355448981296
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140355448977344 = _static_140355540363392('python', ' view.menu_template(actions=actions)', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                # <BinOp left=<Value 'python: view.menu_template(actions=actions)' (11:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cadb670> -> __condition
                __expression = __cache_140355448977344

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_140355448977344
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  ')
                if (__backup_actions_140355449613328 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_140355449613328
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa70cadba90> name=None at 7fa70cadb970> -> __attrs_140355448980480
                __attrs_140355448980480 = _static_140355448978064

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="border-top my-2"></li>\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448979568
                __attrs_140355448979568 = _static_140355540704128
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448982064
                __attrs_140355448982064 = _static_140355540704128

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448980000
                __default_140355448980000 = _DEFAULT_MARKER

                # <Value 'provider:plone.contentmenu' (17:32)> -> __cache_140355448982832
                __token = 460
                try:
                    __zt_tmp = __attrs_140355448982064
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140355448982832 = _static_140355540363392('provider', 'plone.contentmenu', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                # <BinOp left=<Value 'provider:plone.contentmenu' (17:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cadca60> -> __condition
                __expression = __cache_140355448982832

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_140355448982832
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  \n\n  ')

                # <Static value=<ast.Dict object at 0x7fa70cadc550> name=None at 7fa70cadc1f0> -> __attrs_140355449043936
                __attrs_140355449043936 = _static_140355448980816

                # <li ... (0:0)
                # --------------------------------------------------------
                __append('<li class="border-top my-2"></li>\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449044560
                __attrs_140355449044560 = _static_140355540704128
                __backup_actions_140355448655824 = get('actions', __marker)

                # <Value 'view/tabSet2' (23:23)> -> __value
                __token = 600
                try:
                    __zt_tmp = __attrs_140355449044560
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'view/tabSet2', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['actions'] = __value
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449042832
                __attrs_140355449042832 = _static_140355540704128

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449041776
                __default_140355449041776 = _DEFAULT_MARKER

                # <Value 'python: view.menu_template(actions=actions)' (25:32)> -> __cache_140355449042544
                __token = 662
                try:
                    __zt_tmp = __attrs_140355449042832
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140355449042544 = _static_140355540363392('python', ' view.menu_template(actions=actions)', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                # <BinOp left=<Value 'python: view.menu_template(actions=actions)' (25:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70caeb970> -> __condition
                __expression = __cache_140355449042544

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div></div>')
                else:
                    __content = __cache_140355449042544
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n  ')
                if (__backup_actions_140355448655824 is __marker):
                    del econtext['actions']
                else:
                    econtext['actions'] = __backup_actions_140355448655824
                __append('\n\n')
                __i18n_domain = __previous_i18n_domain_140355448979168
            if (__backup_ploneview_140355449357504 is __marker):
                del econtext['ploneview']
            else:
                econtext['ploneview'] = __backup_ploneview_140355449357504
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }