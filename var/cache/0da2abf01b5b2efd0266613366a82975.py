# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.portlets-5.0.7-py3.9.egg/plone/app/portlets/browser/templates/edit-manager.pt'

__tokens = {320: ('string:portletmanager-${view/normalized_manager_name}', 9, 12), 415: ('context/@@manage-portlets-macros/macros/portlet-add-form', 13, 26), 415: ('context/@@manage-portlets-macros/macros/portlet-add-form', 13, 26), 507: ('context/@@manage-portlets-macros/macros/current-portlets-list', 15, 26), 507: ('context/@@manage-portlets-macros/macros/current-portlets-list', 15, 26)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140141462172048 = 'current-portlets-list'
_static_140141462174688 = 'portlet-add-form'
_static_140141533420656 = {}
_static_140141533071440 = __C2ZContextWrapper
_static_140141533071728 = __compile_zt_expr
_static_140141462608528 = {'class': 'portlets-manager pat-manage-portlets', 'id': 'string:portletmanager-${view/normalized_manager_name}', }
_static_140141462609008 = {'xmlns': 'http://www.w3.org/1999/xhtml', }

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

            # <Static value=<ast.Dict object at 0x7f753a18dc70> name=None at 7f753a18d7c0> -> __attrs_140141462608192
            __attrs_140141462608192 = _static_140141462609008
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f753a18da90> name=None at 7f753a18d340> -> __attrs_140141462173104
            __attrs_140141462173104 = _static_140141462608528

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="portlets-manager pat-manage-portlets"')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462175120
            __default_140141462175120 = _DEFAULT_MARKER

            # <Substitution 'string:portletmanager-${view/normalized_manager_name}' (9:12)> -> __attr_id
            __token = 320
            try:
                __zt_tmp = __attrs_140141462173104
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140141533071728('string', 'portletmanager-${view/normalized_manager_name}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))
            __append(' >\n\n    ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462173488
            __attrs_140141462173488 = _static_140141533420656
            __backup_macroname_140141507135168 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f753a123be0> name=None at 7f753a1233d0> -> __value
            __value = _static_140141462174688
            econtext['macroname'] = __value

            # <Value 'context/@@manage-portlets-macros/macros/portlet-add-form' (13:26)> -> __macro
            __token = 415
            try:
                __zt_tmp = __attrs_140141462173488
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140141533071728('path', 'context/@@manage-portlets-macros/macros/portlet-add-form', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            __token = 415
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140141507135168 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140141507135168
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462172000
            __attrs_140141462172000 = _static_140141533420656
            __backup_macroname_140141485890816 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f753a123190> name=None at 7f753a123b80> -> __value
            __value = _static_140141462172048
            econtext['macroname'] = __value

            # <Value 'context/@@manage-portlets-macros/macros/current-portlets-list' (15:26)> -> __macro
            __token = 507
            try:
                __zt_tmp = __attrs_140141462172000
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140141533071728('path', 'context/@@manage-portlets-macros/macros/current-portlets-list', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            __token = 507
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140141485890816 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140141485890816
            __append('\n\n  </div>\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }