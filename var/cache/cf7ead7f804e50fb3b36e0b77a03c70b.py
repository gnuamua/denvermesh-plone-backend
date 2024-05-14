# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/viewlets/document_actions.pt'

__tokens = {63: ('view/actions', 2, 24), 393: ('nocall: context/@@plone/normalizeString', 17, 28), 451: (" python:context.restrictedTraverse('@@iconresolver'", 18, 17), 557: ('view/actions', 21, 32), 617: ("python:'document-action-' + normalizeString(daction['id'])", 23, 17), 772: ('daction/url', 28, 20), 806: (' daction/link_target|nothin', 29, 21), 855: ('e daction/description|nothi', 30, 19), 958: ("python:icons.tag(daction.get('icon'))", 33, 45), 1031: ('daction/title', 34, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355449013344 = {'href': '', 'target': 'daction/link_target|nothing', 'title': 'daction/description|nothing', }
_static_140355449191728 = {'id': "python:'document-action-' + normalizeString(daction['id'])", }
_static_140355448519648 = {'class': 'list-inline', }
_static_140355448959472 = {'class': 'd-none', }
_static_140355540704128 = {}
_static_140355459446240 = {'class': 'viewlet viewlet-document-actions', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355459445424 = {'id': 'section-document-actions', }

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

            # <Static value=<ast.Dict object at 0x7fa70d4d72b0> name=None at 7fa70d4d7520> -> __attrs_140355459444944
            __attrs_140355459444944 = _static_140355459445424

            # <Value 'view/actions' (2:24)> -> __condition
            __token = 63
            try:
                __zt_tmp = __attrs_140355459444944
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'view/actions', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140355459448784 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-document-actions" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa70d4d75e0> name=None at 7fa70d4d7310> -> __attrs_140355449191584
                __attrs_140355449191584 = _static_140355459446240

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="viewlet viewlet-document-actions">\n    ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449189280
                __attrs_140355449189280 = _static_140355540704128
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7fa70cad71f0> name=None at 7fa70cad7d90> -> __attrs_140355448961968
                __attrs_140355448961968 = _static_140355448959472

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="d-none" >')
                __stream_140355516200848 = []
                __append_140355516200848 = __stream_140355516200848.append
                __append_140355516200848('\n              Document Actions\n      ')
                __msgid_140355516200848 = __re_whitespace(''.join(__stream_140355516200848)).strip()
                if 'heading_document_actions':
                    __append(translate('heading_document_actions', mapping=None, default=__msgid_140355516200848, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n\n      ')

                # <Static value=<ast.Dict object at 0x7fa70ca6bbe0> name=None at 7fa70ca6bfd0> -> __attrs_140355448500576
                __attrs_140355448500576 = _static_140355448519648
                __backup_normalizeString_140355459448112 = get('normalizeString', __marker)

                # <Value 'nocall: context/@@plone/normalizeString' (17:28)> -> __value
                __token = 393
                try:
                    __zt_tmp = __attrs_140355448500576
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('nocall', ' context/@@plone/normalizeString', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['normalizeString'] = __value
                __backup_icons_140355449189568 = get('icons', __marker)

                # <Value "python:context.restrictedTraverse('@@iconresolver')" (18:17)> -> __value
                __token = 451
                try:
                    __zt_tmp = __attrs_140355448500576
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['icons'] = __value

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="list-inline" >\n        ')

                # <Static value=<ast.Dict object at 0x7fa70cb0fd30> name=None at 7fa70cb0f9a0> -> __attrs_140355448518352
                __attrs_140355448518352 = _static_140355449191728
                __backup_daction_140355492195152 = get('daction', __marker)

                # <Value 'view/actions' (21:32)> -> __iterator
                __token = 557
                try:
                    __zt_tmp = __attrs_140355448518352
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140355540363392('path', 'view/actions', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                (__iterator, ____index_140355448517152, ) = getname('repeat')('daction', __iterator)
                econtext['daction'] = None
                for __item in __iterator:
                    econtext['daction'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448517008
                    __default_140355448517008 = _DEFAULT_MARKER

                    # <Substitution "python:'document-action-' + normalizeString(daction['id'])" (23:17)> -> __attr_id
                    __token = 617
                    try:
                        __zt_tmp = __attrs_140355448518352
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140355540363392('python', "'document-action-' + normalizeString(daction['id'])", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))
                    __append(' >\n          ')

                    # <Static value=<ast.Dict object at 0x7fa70cae4460> name=None at 7fa70cae4c40> -> __attrs_140355449012480
                    __attrs_140355449012480 = _static_140355449013344

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449014592
                    __default_140355449014592 = _DEFAULT_MARKER

                    # <Substitution 'daction/url' (28:20)> -> __attr_href
                    __token = 772
                    try:
                        __zt_tmp = __attrs_140355449012480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140355540363392('path', 'daction/url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449016176
                    __default_140355449016176 = _DEFAULT_MARKER

                    # <Substitution 'daction/link_target|nothing' (29:21)> -> __attr_target
                    __token = 806
                    try:
                        __zt_tmp = __attrs_140355449012480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_target = _static_140355540363392('path', 'daction/link_target|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_target is not None):
                        __append((' target="%s"' % __attr_target))

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449016032
                    __default_140355449016032 = _DEFAULT_MARKER

                    # <Substitution 'daction/description|nothing' (30:19)> -> __attr_title
                    __token = 855
                    try:
                        __zt_tmp = __attrs_140355449012480
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140355540363392('path', 'daction/description|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' >\n            ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449520912
                    __attrs_140355449520912 = _static_140355540704128

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449523648
                    __default_140355449523648 = _DEFAULT_MARKER

                    # <Value "python:icons.tag(daction.get('icon'))" (33:45)> -> __cache_140355448947760
                    __token = 958
                    try:
                        __zt_tmp = __attrs_140355449520912
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355448947760 = _static_140355540363392('python', "icons.tag(daction.get('icon'))", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value "python:icons.tag(daction.get('icon'))" (33:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb60d60> -> __condition
                    __expression = __cache_140355448947760

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355448947760
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n            ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449847280
                    __attrs_140355449847280 = _static_140355540704128

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449844640
                    __default_140355449844640 = _DEFAULT_MARKER

                    # <Value 'daction/title' (34:31)> -> __cache_140355449843968
                    __token = 1031
                    try:
                        __zt_tmp = __attrs_140355449847280
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355449843968 = _static_140355540363392('path', 'daction/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'daction/title' (34:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cbaf9d0> -> __condition
                    __expression = __cache_140355449843968

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span >\n                            Menu Title\n            </span>')
                    else:
                        __content = __cache_140355449843968
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          </a>\n        </li>')
                    ____index_140355448517152 -= 1
                    if (____index_140355448517152 > 0):
                        __append('\n        ')
                if (__backup_daction_140355492195152 is __marker):
                    del econtext['daction']
                else:
                    econtext['daction'] = __backup_daction_140355492195152
                __append('\n      </ul>')
                if (__backup_icons_140355449189568 is __marker):
                    del econtext['icons']
                else:
                    econtext['icons'] = __backup_icons_140355449189568
                if (__backup_normalizeString_140355459448112 is __marker):
                    del econtext['normalizeString']
                else:
                    econtext['normalizeString'] = __backup_normalizeString_140355459448112
                __append('\n    \n\n  </div>\n</section>')
                __i18n_domain = __previous_i18n_domain_140355459448784
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }