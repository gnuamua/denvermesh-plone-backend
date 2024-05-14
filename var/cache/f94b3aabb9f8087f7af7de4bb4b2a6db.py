# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.portlets-5.0.7-py3.9.egg/plone/app/portlets/browser/templates/dashboard-column.pt'

__tokens = {27: ('options/portlets', 1, 27), 158: ('string:portletwrapper-${portlet/hash}', 4, 12), 222: (' portlet/has', 5, 25), 76: ("python:view.safe_render(portlet['renderer'])", 2, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140141462040288 = {'id': 'string:portletwrapper-${portlet/hash}', 'data-portlethash': 'portlet/hash', }
_static_140141533071440 = __C2ZContextWrapper
_static_140141533071728 = __compile_zt_expr
_static_140141533420656 = {}

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

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462037360
            __attrs_140141462037360 = _static_140141533420656
            __backup_portlet_140141462317424 = get('portlet', __marker)

            # <Value 'options/portlets' (1:27)> -> __iterator
            __token = 27
            try:
                __zt_tmp = __attrs_140141462037360
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140141533071728('path', 'options/portlets', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            (__iterator, ____index_140141462037408, ) = getname('repeat')('portlet', __iterator)
            econtext['portlet'] = None
            for __item in __iterator:
                econtext['portlet'] = __item
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7f753a102ee0> name=None at 7f753a102eb0> -> __attrs_140141462159712
                __attrs_140141462159712 = _static_140141462040288

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462163024
                __default_140141462163024 = _DEFAULT_MARKER

                # <Substitution 'string:portletwrapper-${portlet/hash}' (4:12)> -> __attr_id
                __token = 158
                try:
                    __zt_tmp = __attrs_140141462159712
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140141533071728('string', 'portletwrapper-${portlet/hash}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462162832
                __default_140141462162832 = _DEFAULT_MARKER

                # <Substitution 'portlet/hash' (5:25)> -> __attr_data_portlethash
                __token = 222
                try:
                    __zt_tmp = __attrs_140141462159712
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_portlethash = _static_140141533071728('path', 'portlet/hash', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_data_portlethash = __quote(__attr_data_portlethash, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_portlethash is not None):
                    __append((' data-portlethash="%s"' % __attr_data_portlethash))
                __append(' >')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462039232
                __default_140141462039232 = _DEFAULT_MARKER

                # <Value "python:view.safe_render(portlet['renderer'])" (2:30)> -> __cache_140141462039040
                __token = 76
                try:
                    __zt_tmp = __attrs_140141462159712
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140141462039040 = _static_140141533071728('python', "view.safe_render(portlet['renderer'])", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                # <BinOp left=<Value "python:view.safe_render(portlet['renderer'])" (2:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1024c0> -> __condition
                __expression = __cache_140141462039040

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140141462039040
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n')
                ____index_140141462037408 -= 1
                if (____index_140141462037408 > 0):
                    __append('')
            if (__backup_portlet_140141462317424 is __marker):
                del econtext['portlet']
            else:
                econtext['portlet'] = __backup_portlet_140141462317424
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }