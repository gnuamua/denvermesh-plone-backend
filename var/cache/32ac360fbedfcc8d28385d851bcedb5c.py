# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.volto-4.4.0-py3.9.egg/plone/volto/browser/voltobackendwarning.pt'

__tokens = {33: ('nocall: context/@@iconresolver', 1, 33), 253: ("python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')", 6, 41)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355459837760 = {'href': 'https://6.docs.plone.org/volto/index.html', }
_static_140355459837616 = {'href': 'https://6.docs.plone.org/install/install-from-packages.html', }
_static_140355449895712 = {'class': 'content', }
_static_140355449163536 = {'class': 'portalMessage statusmessage statusmessage-warning alert alert-warning', 'role': 'alert', }
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

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449160080
            __attrs_140355449160080 = _static_140355540704128
            __backup_icons_140355448949968 = get('icons', __marker)

            # <Value 'nocall: context/@@iconresolver' (1:33)> -> __value
            __token = 33
            try:
                __zt_tmp = __attrs_140355449160080
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('nocall', ' context/@@iconresolver', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['icons'] = __value
            __previous_i18n_domain_140355449162048 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa70cb08f10> name=None at 7fa70cb085b0> -> __attrs_140355449161328
            __attrs_140355449161328 = _static_140355449163536

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="portalMessage statusmessage statusmessage-warning alert alert-warning" role="alert">\n        ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449893648
            __attrs_140355449893648 = _static_140355540704128

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449896912
            __default_140355449896912 = _DEFAULT_MARKER

            # <Value "python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')" (6:41)> -> __cache_140355449894224
            __token = 253
            try:
                __zt_tmp = __attrs_140355449893648
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355449894224 = _static_140355540363392('python', "icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value "python:icons.tag('plone-statusmessage-warning', tag_alt='warning', tag_class='statusmessage-icon mb-1 me-2')" (6:41)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cbbbd00> -> __condition
            __expression = __cache_140355449894224

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140355449894224
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449896096
            __attrs_140355449896096 = _static_140355540704128

            # <strong ... (0:0)
            # --------------------------------------------------------
            __append('<strong>')
            __stream_140355449893072 = []
            __append_140355449893072 = __stream_140355449893072.append
            __append_140355449893072('Warning')
            __msgid_140355449893072 = __re_whitespace(''.join(__stream_140355449893072)).strip()
            if __msgid_140355449893072:
                __append(translate(__msgid_140355449893072, mapping=None, default=__msgid_140355449893072, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</strong>:\n        ')

            # <Static value=<ast.Dict object at 0x7fa70cbbbb20> name=None at 7fa70cbbb460> -> __attrs_140355459397952
            __attrs_140355459397952 = _static_140355449895712

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="content">\n            ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459399056
            __attrs_140355459399056 = _static_140355540704128
            __stream_140355459396416 = []
            __append_140355459396416 = __stream_140355459396416.append
            __append_140355459396416('You have accessed the Plone backend through its Classic UI frontend.')
            __msgid_140355459396416 = __re_whitespace(''.join(__stream_140355459396416)).strip()
            if 'volto_backend_warning':
                __append(translate('volto_backend_warning', mapping=None, default=__msgid_140355459396416, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459399248
            __attrs_140355459399248 = _static_140355540704128

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n            ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459397472
            __attrs_140355459397472 = _static_140355540704128

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br />\n            ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459398816
            __attrs_140355459398816 = _static_140355540704128
            __stream_140355459399200 = []
            __append_140355459399200 = __stream_140355459399200.append
            __append_140355459399200("If you want to use Plone's new frontend Volto instead:\n              ")

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459859648
            __attrs_140355459859648 = _static_140355540704128

            # <ul ... (0:0)
            # --------------------------------------------------------
            __append_140355459399200('<ul>\n                ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459862096
            __attrs_140355459862096 = _static_140355540704128

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140355459399200('<li>Install Volto, if not already installed.</li>\n                ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459834592
            __attrs_140355459834592 = _static_140355540704128

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140355459399200('<li>Start Volto, if not already started.</li>\n                ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459835600
            __attrs_140355459835600 = _static_140355540704128

            # <li ... (0:0)
            # --------------------------------------------------------
            __append_140355459399200('<li>Visit the Volto frontend.</li>\n              </ul>\n              For more information, please read the documentation for how to\n              ')

            # <Static value=<ast.Dict object at 0x7fa70d536eb0> name=None at 7fa70d536f70> -> __attrs_140355459834688
            __attrs_140355459834688 = _static_140355459837616

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140355459399200('<a href="https://6.docs.plone.org/install/install-from-packages.html">Install Plone from its packages</a>\n              and refer to the full Volto documentation\n              ')

            # <Static value=<ast.Dict object at 0x7fa70d536f40> name=None at 7fa70cbbbdc0> -> __attrs_140355459446240
            __attrs_140355459446240 = _static_140355459837760

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140355459399200('<a href="https://6.docs.plone.org/volto/index.html">Frontend</a>.')
            __msgid_140355459399200 = __re_whitespace(''.join(__stream_140355459399200)).strip()
            if 'volto_backend_warning_link':
                __append(translate('volto_backend_warning_link', mapping=None, default=__msgid_140355459399200, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n        </span>\n    </div>\n\n')
            __i18n_domain = __previous_i18n_domain_140355449162048
            if (__backup_icons_140355448949968 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140355448949968
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }