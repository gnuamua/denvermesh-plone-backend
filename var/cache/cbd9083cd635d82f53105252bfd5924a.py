# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/viewlets/toc.pt'

__tokens = {135: ('view/enabled', 5, 24)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info

_static_140355449423472 = {'class': 'portletItem', }
_static_140355449422176 = {'class': 'portletContent', }
_static_140355459730832 = {'class': 'portletHeader', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355459730064 = {'class': 'portlet toc', 'id': 'document-toc', 'role': 'section', 'style': 'display: none', }

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

            # <Static value=<ast.Dict object at 0x7fa70d51ca90> name=None at 7fa70d51c340> -> __attrs_140355459727856
            __attrs_140355459727856 = _static_140355459730064

            # <Value 'view/enabled' (5:24)> -> __condition
            __token = 135
            try:
                __zt_tmp = __attrs_140355459727856
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'view/enabled', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140355459729488 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="portlet toc" id="document-toc" role="section" style="display: none" >\n  ')

                # <Static value=<ast.Dict object at 0x7fa70d51cd90> name=None at 7fa70d51ce20> -> __attrs_140355459730880
                __attrs_140355459730880 = _static_140355459730832

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="portletHeader" >')
                __stream_140355459731312 = []
                __append_140355459731312 = __stream_140355459731312.append
                __append_140355459731312('Contents')
                __msgid_140355459731312 = __re_whitespace(''.join(__stream_140355459731312)).strip()
                if 'label_tableofcontents':
                    __append(translate('label_tableofcontents', mapping=None, default=__msgid_140355459731312, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n  ')

                # <Static value=<ast.Dict object at 0x7fa70cb48160> name=None at 7fa70cb486a0> -> __attrs_140355449422608
                __attrs_140355449422608 = _static_140355449422176

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section class="portletContent">\n    ')

                # <Static value=<ast.Dict object at 0x7fa70cb48670> name=None at 7fa70cb48eb0> -> __attrs_140355449423328
                __attrs_140355449423328 = _static_140355449423472

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="portletItem">\n    </div>\n  </section>\n</section>')
                __i18n_domain = __previous_i18n_domain_140355459729488
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }