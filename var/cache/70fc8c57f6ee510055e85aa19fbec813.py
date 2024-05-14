# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/Products.CMFPlone-6.0.11-py3.9.egg/Products/CMFPlone/browser/templates/basic_error_message.pt'

__tokens = {293: ('python:view.is_manager()', 8, 27), 352: ('not:isManager', 11, 24), 423: ('isManager', 12, 24), 434: ('${options/error_type}', 12, 35), 436: ('options/error_type', 12, 37), 694: ('isManager', 23, 21), 705: ('${options/error_type}', 23, 32), 707: ('options/error_type', 23, 34), 755: ('isManager', 25, 22), 786: ('options/error_tb', 26, 20), 834: ('not:isManager', 28, 26)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355484546480 = {'class': 'documentFirstHeading', }
_static_140355537394176 = {'class': 'documentFirstHeading', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355540704128 = {}
_static_140355484700240 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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

            # <Static value=<ast.Dict object at 0x7fa70ecece50> name=None at 7fa70ecec250> -> __attrs_140355523701584
            __attrs_140355523701584 = _static_140355484700240
            __previous_i18n_domain_140355523700720 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355523700768
            __attrs_140355523700768 = _static_140355540704128
            __backup_isManager_140355519296704 = get('isManager', __marker)

            # <Value 'python:view.is_manager()' (8:27)> -> __value
            __token = 293
            try:
                __zt_tmp = __attrs_140355523700768
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', 'view.is_manager()', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['isManager'] = __value
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355523702208
            __attrs_140355523702208 = _static_140355540704128

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n  ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537392352
            __attrs_140355537392352 = _static_140355540704128

            # <Value 'not:isManager' (11:24)> -> __condition
            __token = 352
            try:
                __zt_tmp = __attrs_140355537392352
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('not', 'isManager', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <title ... (0:0)
                # --------------------------------------------------------
                __append('<title>')
                __stream_140355523699040 = []
                __append_140355523699040 = __stream_140355523699040.append
                __append_140355523699040('Error')
                __msgid_140355523699040 = __re_whitespace(''.join(__stream_140355523699040)).strip()
                if __msgid_140355523699040:
                    __append(translate(__msgid_140355523699040, mapping=None, default=__msgid_140355523699040, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</title>')
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537393360
            __attrs_140355537393360 = _static_140355540704128

            # <Value 'isManager' (12:24)> -> __condition
            __token = 423
            try:
                __zt_tmp = __attrs_140355537393360
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'isManager', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <title ... (0:0)
                # --------------------------------------------------------
                __append('<title>')

                # <Interpolation value=<Substitution '${options/error_type}' (12:35)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa711f2d580> -> __content_140355621335664
                __token = 434
                __token = 436
                try:
                    __zt_tmp = __attrs_140355537393360
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140355621335664 = _static_140355540363392('path', 'options/error_type', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                __content_140355621335664 = __quote(__content_140355621335664, '\x00', '&#0;', None, None)
                __content_140355621335664 = __content_140355621335664
                if (__content_140355621335664 is None):
                    pass
                else:
                    if (__content_140355621335664 is None):
                        __content_140355621335664 = None
                    else:
                        __tt = type(__content_140355621335664)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140355621335664 = str(__content_140355621335664)
                        else:
                            if (__tt is bytes):
                                __content_140355621335664 = decode(__content_140355621335664)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140355621335664 = __content_140355621335664.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140355621335664)
                                        __content_140355621335664 = (str(__content_140355621335664) if (__content_140355621335664 is __converted) else __converted)
                                    else:
                                        __content_140355621335664 = __content_140355621335664()
                if (__content_140355621335664 is not None):
                    __append(__content_140355621335664)
                __append('</title>')
            __append('\n</head>\n\n')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537393312
            __attrs_140355537393312 = _static_140355540704128

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n  ')

            # <Static value=<ast.Dict object at 0x7fa711f2da00> name=None at 7fa711f2dca0> -> __attrs_140355484545136
            __attrs_140355484545136 = _static_140355537394176

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1 class="documentFirstHeading">')
            __stream_140355537394080 = []
            __append_140355537394080 = __stream_140355537394080.append
            __append_140355537394080('\n      We&#8217;re sorry, but there seems to be an error&hellip;\n  ')
            __msgid_140355537394080 = __re_whitespace(''.join(__stream_140355537394080)).strip()
            if 'heading_site_error_sorry':
                __append(translate('heading_site_error_sorry', mapping=None, default=__msgid_140355537394080, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n\n  ')

            # <Static value=<ast.Dict object at 0x7fa70ecc75b0> name=None at 7fa70ecc7160> -> __attrs_140355484549072
            __attrs_140355484549072 = _static_140355484546480

            # <Value 'isManager' (23:21)> -> __condition
            __token = 694
            try:
                __zt_tmp = __attrs_140355484549072
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'isManager', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2 class="documentFirstHeading">')

                # <Interpolation value=<Substitution '${options/error_type}' (23:32)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70ecc7eb0> -> __content_140355621335664
                __token = 705
                __token = 707
                try:
                    __zt_tmp = __attrs_140355484549072
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140355621335664 = _static_140355540363392('path', 'options/error_type', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                __content_140355621335664 = __quote(__content_140355621335664, '\x00', '&#0;', None, None)
                __content_140355621335664 = __content_140355621335664
                if (__content_140355621335664 is None):
                    pass
                else:
                    if (__content_140355621335664 is None):
                        __content_140355621335664 = None
                    else:
                        __tt = type(__content_140355621335664)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140355621335664 = str(__content_140355621335664)
                        else:
                            if (__tt is bytes):
                                __content_140355621335664 = decode(__content_140355621335664)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140355621335664 = __content_140355621335664.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140355621335664)
                                        __content_140355621335664 = (str(__content_140355621335664) if (__content_140355621335664 is __converted) else __converted)
                                    else:
                                        __content_140355621335664 = __content_140355621335664()
                if (__content_140355621335664 is not None):
                    __append(__content_140355621335664)
                __append('</h2>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355484547536
            __attrs_140355484547536 = _static_140355540704128

            # <Value 'isManager' (25:22)> -> __condition
            __token = 755
            try:
                __zt_tmp = __attrs_140355484547536
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'isManager', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <pre ... (0:0)
                # --------------------------------------------------------
                __append('<pre>')

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355484548352
                __default_140355484548352 = _DEFAULT_MARKER

                # <Value 'options/error_tb' (26:20)> -> __cache_140355484547392
                __token = 786
                try:
                    __zt_tmp = __attrs_140355484547536
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140355484547392 = _static_140355540363392('path', 'options/error_tb', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                # <BinOp left=<Value 'options/error_tb' (26:20)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70ecc7850> -> __condition
                __expression = __cache_140355484547392

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140355484547392
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</pre>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355515295680
            __attrs_140355515295680 = _static_140355540704128

            # <Value 'not:isManager' (28:26)> -> __condition
            __token = 834
            try:
                __zt_tmp = __attrs_140355515295680
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('not', 'isManager', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355515297216
                __attrs_140355515297216 = _static_140355540704128

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_140355527841376_site_admin = ''
                __stream_140355515295344 = []
                __append_140355515295344 = __stream_140355515295344.append
                __append_140355515295344('\n      If you are certain you have the correct web address but are encountering an error, please\n      contact the ')
                __stream_140355527841376_site_admin = []
                __append_140355527841376_site_admin = __stream_140355527841376_site_admin.append

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355515294192
                __attrs_140355515294192 = _static_140355540704128

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_140355527841376_site_admin('<span>')
                __stream_140355515296592 = []
                __append_140355515296592 = __stream_140355515296592.append
                __append_140355515296592('site administration')
                __msgid_140355515296592 = __re_whitespace(''.join(__stream_140355515296592)).strip()
                if 'label_site_admin':
                    __append_140355527841376_site_admin(translate('label_site_admin', mapping=None, default=__msgid_140355515296592, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append_140355527841376_site_admin('</span>')
                __append_140355515295344('${site_admin}')
                __stream_140355527841376_site_admin = ''.join(__stream_140355527841376_site_admin)
                __append_140355515295344('.\n      ')
                __msgid_140355515295344 = __re_whitespace(''.join(__stream_140355515295344)).strip()
                if 'description_site_error_mail_site_admin':
                    __append(translate('description_site_error_mail_site_admin', mapping={'site_admin': __stream_140355527841376_site_admin, }, default=__msgid_140355515295344, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n  ')
            __append('\n\n</body>\n')
            if (__backup_isManager_140355519296704 is __marker):
                del econtext['isManager']
            else:
                econtext['isManager'] = __backup_isManager_140355519296704
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_140355523700720
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }