# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.locking-3.0.1-py3.9.egg/plone/locking/browser/info.pt'

__tokens = {60: ('view/info/is_locked_for_current_user', 3, 14), 114: (' view/lock_is_stealabl', 4, 16), 157: ('s view/lock_in', 5, 18), 185: ("ns python:context.restrictedTraverse('@@iconresolve", 6, 10), 299: ('locked', 10, 24), 401: ("python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')", 12, 39), 574: ('lock_details/author_page', 14, 38), 819: ('lock_details/author_page', 20, 18), 750: ('lock_details/fullname', 18, 24), 929: ('lock_details/time_difference', 24, 27), 1087: ('not:lock_details/author_page', 29, 41), 1273: ('lock_details/fullname', 33, 27), 1373: ('lock_details/time_difference', 36, 27), 1546: ('stealable', 42, 27), 1607: ('string:${context/absolute_url}/@@plone_lock_operations/force_unlock', 44, 21)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355449071744 = {'type': 'submit', 'value': 'Unlock', }
_static_140355459713056 = {'method': 'POST', 'action': 'string:${context/absolute_url}/@@plone_lock_operations/force_unlock', }
_static_140355537879824 = {'href': 'lock_details/author_page', }
_static_140355449160704 = {'class': 'portalMessage info alert alert-info', }
_static_140355540704128 = {}
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355448978352 = {'id': 'plone-lock-status', }

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

            # <Static value=<ast.Dict object at 0x7fa70cadbbb0> name=None at 7fa70cadb070> -> __attrs_140355459450336
            __attrs_140355459450336 = _static_140355448978352
            __backup_locked_140355449084656 = get('locked', __marker)

            # <Value 'view/info/is_locked_for_current_user' (3:14)> -> __value
            __token = 60
            try:
                __zt_tmp = __attrs_140355459450336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/info/is_locked_for_current_user', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['locked'] = __value
            __backup_stealable_140355448394176 = get('stealable', __marker)

            # <Value 'view/lock_is_stealable' (4:16)> -> __value
            __token = 114
            try:
                __zt_tmp = __attrs_140355459450336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/lock_is_stealable', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['stealable'] = __value
            __backup_lock_details_140355448948768 = get('lock_details', __marker)

            # <Value 'view/lock_info' (5:18)> -> __value
            __token = 157
            try:
                __zt_tmp = __attrs_140355459450336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/lock_info', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['lock_details'] = __value
            __backup_icons_140355459744960 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (6:10)> -> __value
            __token = 185
            try:
                __zt_tmp = __attrs_140355459450336
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['icons'] = __value
            __previous_i18n_domain_140355459451680 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="plone-lock-status" >\n  ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459450096
            __attrs_140355459450096 = _static_140355540704128

            # <Value 'locked' (10:24)> -> __condition
            __token = 299
            try:
                __zt_tmp = __attrs_140355459450096
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'locked', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7fa70cb08400> name=None at 7fa70cb08880> -> __attrs_140355449161712
                __attrs_140355449161712 = _static_140355449160704

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="portalMessage info alert alert-info">\n      ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449160032
                __attrs_140355449160032 = _static_140355540704128

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449162096
                __default_140355449162096 = _DEFAULT_MARKER

                # <Value "python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')" (12:39)> -> __cache_140355449162480
                __token = 401
                try:
                    __zt_tmp = __attrs_140355449160032
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140355449162480 = _static_140355540363392('python', "icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('lock-fill', tag_alt='locked', tag_class='mb-1 me-2')" (12:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb084f0> -> __condition
                __expression = __cache_140355449162480

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140355449162480
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448949776
                __attrs_140355448949776 = _static_140355540704128

                # <strong ... (0:0)
                # --------------------------------------------------------
                __append('<strong>')
                __stream_140355449160128 = []
                __append_140355449160128 = __stream_140355449160128.append
                __append_140355449160128('Locked')
                __msgid_140355449160128 = __re_whitespace(''.join(__stream_140355449160128)).strip()
                if 'label_locked':
                    __append(translate('label_locked', mapping=None, default=__msgid_140355449160128, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</strong>\n      ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448948096
                __attrs_140355448948096 = _static_140355540704128

                # <Value 'lock_details/author_page' (14:38)> -> __condition
                __token = 574
                try:
                    __zt_tmp = __attrs_140355448948096
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('path', 'lock_details/author_page', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:
                    __stream_140355459380160_time = ''
                    __stream_140355459380160_author = ''
                    __stream_140355448950688 = []
                    __append_140355448950688 = __stream_140355448950688.append
                    __append_140355448950688('\n          This item was locked by\n        ')
                    __stream_140355459380160_author = []
                    __append_140355459380160_author = __stream_140355459380160_author.append

                    # <Static value=<ast.Dict object at 0x7fa711fa4310> name=None at 7fa70cb605e0> -> __attrs_140355459712768
                    __attrs_140355459712768 = _static_140355537879824

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append_140355459380160_author('<a')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449598544
                    __default_140355449598544 = _DEFAULT_MARKER

                    # <Substitution 'lock_details/author_page' (20:18)> -> __attr_href
                    __token = 819
                    try:
                        __zt_tmp = __attrs_140355459712768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140355540363392('path', 'lock_details/author_page', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append_140355459380160_author((' href="%s"' % __attr_href))
                    __append_140355459380160_author(' >')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449521344
                    __default_140355449521344 = _DEFAULT_MARKER

                    # <Value 'lock_details/fullname' (18:24)> -> __cache_140355449522496
                    __token = 750
                    try:
                        __zt_tmp = __attrs_140355459712768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355449522496 = _static_140355540363392('path', 'lock_details/fullname', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/fullname' (18:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb60cd0> -> __condition
                    __expression = __cache_140355449522496

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355449522496
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140355459380160_author(__content)
                    __append_140355459380160_author('</a>')
                    __append_140355448950688('${author}')
                    __stream_140355459380160_author = ''.join(__stream_140355459380160_author)
                    __append_140355448950688('\n        ')
                    __stream_140355459380160_time = []
                    __append_140355459380160_time = __stream_140355459380160_time.append

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459713008
                    __attrs_140355459713008 = _static_140355540704128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140355459380160_time('<span >')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459714688
                    __default_140355459714688 = _DEFAULT_MARKER

                    # <Value 'lock_details/time_difference' (24:27)> -> __cache_140355459450672
                    __token = 929
                    try:
                        __zt_tmp = __attrs_140355459713008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355459450672 = _static_140355540363392('path', 'lock_details/time_difference', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/time_difference' (24:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70d4d8f40> -> __condition
                    __expression = __cache_140355459450672

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355459450672
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140355459380160_time(__content)
                    __append_140355459380160_time('</span>')
                    __append_140355448950688('${time}')
                    __stream_140355459380160_time = ''.join(__stream_140355459380160_time)
                    __append_140355448950688('\n         ago.\n      ')
                    __msgid_140355448950688 = __re_whitespace(''.join(__stream_140355448950688)).strip()
                    if 'description_webdav_locked_by_author_on_time':
                        __append(translate('description_webdav_locked_by_author_on_time', mapping={'author': __stream_140355459380160_author, 'time': __stream_140355459380160_time, }, default=__msgid_140355448950688, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459712000
                __attrs_140355459712000 = _static_140355540704128

                # <Value 'not:lock_details/author_page' (29:41)> -> __condition
                __token = 1087
                try:
                    __zt_tmp = __attrs_140355459712000
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('not', 'lock_details/author_page', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:
                    __stream_140355459380160_time = ''
                    __stream_140355459380160_author = ''
                    __stream_140355448947760 = []
                    __append_140355448947760 = __stream_140355448947760.append
                    __append_140355448947760('\n          This item was locked by\n        ')
                    __stream_140355459380160_author = []
                    __append_140355459380160_author = __stream_140355459380160_author.append

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459714736
                    __attrs_140355459714736 = _static_140355540704128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140355459380160_author('<span >')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459711376
                    __default_140355459711376 = _DEFAULT_MARKER

                    # <Value 'lock_details/fullname' (33:27)> -> __cache_140355459713104
                    __token = 1273
                    try:
                        __zt_tmp = __attrs_140355459714736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355459713104 = _static_140355540363392('path', 'lock_details/fullname', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/fullname' (33:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70d518bb0> -> __condition
                    __expression = __cache_140355459713104

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355459713104
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140355459380160_author(__content)
                    __append_140355459380160_author('</span>')
                    __append_140355448947760('${author}')
                    __stream_140355459380160_author = ''.join(__stream_140355459380160_author)
                    __append_140355448947760('\n        ')
                    __stream_140355459380160_time = []
                    __append_140355459380160_time = __stream_140355459380160_time.append

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448512464
                    __attrs_140355448512464 = _static_140355540704128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140355459380160_time('<span >')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448512320
                    __default_140355448512320 = _DEFAULT_MARKER

                    # <Value 'lock_details/time_difference' (36:27)> -> __cache_140355448509728
                    __token = 1373
                    try:
                        __zt_tmp = __attrs_140355448512464
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355448509728 = _static_140355540363392('path', 'lock_details/time_difference', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'lock_details/time_difference' (36:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70ca69400> -> __condition
                    __expression = __cache_140355448509728

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355448509728
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append_140355459380160_time(__content)
                    __append_140355459380160_time('</span>')
                    __append_140355448947760('${time}')
                    __stream_140355459380160_time = ''.join(__stream_140355459380160_time)
                    __append_140355448947760('\n         ago.\n      ')
                    __msgid_140355448947760 = __re_whitespace(''.join(__stream_140355448947760)).strip()
                    if 'description_webdav_locked_by_author_on_time':
                        __append(translate('description_webdav_locked_by_author_on_time', mapping={'author': __stream_140355459380160_author, 'time': __stream_140355459380160_time, }, default=__msgid_140355448947760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7fa70d518820> name=None at 7fa70d518490> -> __attrs_140355448509488
                __attrs_140355448509488 = _static_140355459713056

                # <Value 'stealable' (42:27)> -> __condition
                __token = 1546
                try:
                    __zt_tmp = __attrs_140355448509488
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('path', 'stealable', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form method="POST"')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448511552
                    __default_140355448511552 = _DEFAULT_MARKER

                    # <Substitution 'string:${context/absolute_url}/@@plone_lock_operations/force_unlock' (44:21)> -> __attr_action
                    __token = 1607
                    try:
                        __zt_tmp = __attrs_140355448509488
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140355540363392('string', '${context/absolute_url}/@@plone_lock_operations/force_unlock', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append(' >\n        ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449073568
                    __attrs_140355449073568 = _static_140355540704128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_140355459091136_unlock_button = ''
                    __stream_140355448508768 = []
                    __append_140355448508768 = __stream_140355448508768.append
                    __append_140355448508768('\n            If you are certain this user has abandoned the object,\n            you may\n          ')
                    __stream_140355459091136_unlock_button = []
                    __append_140355459091136_unlock_button = __stream_140355459091136_unlock_button.append

                    # <Static value=<ast.Dict object at 0x7fa70caf2880> name=None at 7fa70caf2d60> -> __attrs_140355449072080
                    __attrs_140355449072080 = _static_140355449071744

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append_140355459091136_unlock_button('<input type="submit"')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449070496
                    __default_140355449070496 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x7fa70caf2f40> at 7fa70caf2130> -> __attr_value
                    __attr_value = 'Unlock'
                    __attr_value = translate(__attr_value, default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append_140355459091136_unlock_button((' value="%s"' % __attr_value))
                    __append_140355459091136_unlock_button(' />')
                    __append_140355448508768('${unlock_button}')
                    __stream_140355459091136_unlock_button = ''.join(__stream_140355459091136_unlock_button)
                    __append_140355448508768('\n            the object. You will then be able to edit it.\n        ')
                    __msgid_140355448508768 = __re_whitespace(''.join(__stream_140355448508768)).strip()
                    if 'description_webdav_locked_steal':
                        __append(translate('description_webdav_locked_steal', mapping={'unlock_button': __stream_140355459091136_unlock_button, }, default=__msgid_140355448508768, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      </form>')
                __append('\n    </div>\n  ')
            __append('\n</div>')
            __i18n_domain = __previous_i18n_domain_140355459451680
            if (__backup_icons_140355459744960 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140355459744960
            if (__backup_lock_details_140355448948768 is __marker):
                del econtext['lock_details']
            else:
                econtext['lock_details'] = __backup_lock_details_140355448948768
            if (__backup_stealable_140355448394176 is __marker):
                del econtext['stealable']
            else:
                econtext['stealable'] = __backup_stealable_140355448394176
            if (__backup_locked_140355449084656 is __marker):
                del econtext['locked']
            else:
                econtext['locked'] = __backup_locked_140355449084656
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }