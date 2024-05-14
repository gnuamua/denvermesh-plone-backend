# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/Products.CMFPlone-6.0.11-py3.9.egg/Products/CMFPlone/browser/templates/colophon.pt'

__tokens = {}

from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355449760976 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }
_static_140355449384816 = {'href': 'http://plone.org', 'target': '_blank', 'title': 'This site was built using the Plone Open Source CMS/WCM.', }
_static_140355459549408 = {'class': 'card-body', }
_static_140355459550704 = {'class': 'card card-classic', 'id': 'portal-colophon', }

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

    def render_portlet(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7fa70d4f0df0> name=None at 7fa70d4f0a60> -> __attrs_140355459549312
            __attrs_140355459549312 = _static_140355459550704

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card card-classic" id="portal-colophon">\n    ')

            # <Static value=<ast.Dict object at 0x7fa70d4f08e0> name=None at 7fa70d4f0100> -> __attrs_140355459547440
            __attrs_140355459547440 = _static_140355459549408

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body">\n      ')

            # <Static value=<ast.Dict object at 0x7fa70cb3ef70> name=None at 7fa70cb3efa0> -> __attrs_140355449161088
            __attrs_140355449161088 = _static_140355449384816

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="http://plone.org" target="_blank"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449162960
            __default_140355449162960 = _DEFAULT_MARKER

            # <Translate msgid='title_built_with_plone' node=<ast.Constant object at 0x7fa70cb08700> at 7fa70cb080a0> -> __attr_title
            __attr_title = 'This site was built using the Plone Open Source CMS/WCM.'
            __attr_title = translate('title_built_with_plone', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>')
            __stream_140355449382176 = []
            __append_140355449382176 = __stream_140355449382176.append
            __append_140355449382176('\n        Powered by Plone')
            __msgid_140355449382176 = __re_whitespace(''.join(__stream_140355449382176)).strip()
            if 'label_powered_by_plone':
                __append(translate('label_powered_by_plone', mapping=None, default=__msgid_140355449382176, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n    </div>\n  </div>')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


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

            # <Static value=<ast.Dict object at 0x7fa70cb9acd0> name=None at 7fa70cb9a460> -> __attrs_140355449641328
            __attrs_140355449641328 = _static_140355449760976
            __previous_i18n_domain_140355449642864 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n  ')
            __token = None
            render_portlet(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
            __i18n_domain = __previous_i18n_domain_140355449642864
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_portlet': render_portlet, 'render': render, }