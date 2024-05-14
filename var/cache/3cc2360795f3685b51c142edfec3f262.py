# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.portlets-5.0.7-py3.9.egg/plone/app/portlets/dashboard/dashboard.pt'

__tokens = {1128: ('${context/@@plone_portal_state/navigation_root_url}/dashboard', 36, 23), 1130: ('context/@@plone_portal_state/navigation_root_url', 36, 25), 1383: ('${context/@@plone_portal_state/navigation_root_url}/@@manage-dashboard?_authenticator=${view/auth_token}', 42, 23), 1385: ('context/@@plone_portal_state/navigation_root_url', 42, 25), 1471: ('view/auth_token', 42, 111), 1778: ('provider:plone.dashboard1', 53, 40), 1907: ('provider:plone.dashboard2', 56, 40), 2036: ('provider:plone.dashboard3', 59, 40), 2165: ('provider:plone.dashboard4', 62, 40), 468: ('context/portal_membership/getMemberInfo', 16, 23), 527: (' context/@@plone_portal_state/membe', 17, 18), 580: ("e python:memberinfo['fullname'] or member.getId() or member.getId", 18, 15), 741: ('name', 22, 27), 247: ('context/main_template/macros/master', 6, 23), 247: ('context/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140141462806144 = {'class': 'documentFirstHeading', }
_static_140141462783168 = 'master'
_static_140141462795312 = {'id': 'dashboard-portlets4', }
_static_140141462795024 = {'id': 'dashboard-portlets3', }
_static_140141471564176 = {'id': 'dashboard-portlets2', }
_static_140141462628576 = {'id': 'dashboard-portlets1', }
_static_140141462626800 = {'class': 'row row-cols-1 row-cols-md-2 gy-2', 'id': 'dashboard', }
_static_140141462710208 = {'class': 'nav-link', 'href': '${context/@@plone_portal_state/navigation_root_url}/@@manage-dashboard?_authenticator=${view/auth_token}', }
_static_140141462709632 = {'class': 'nav-item', }
_static_140141533071440 = __C2ZContextWrapper
_static_140141533071728 = __compile_zt_expr
_static_140141462623856 = {'class': 'active nav-link', 'href': '${context/@@plone_portal_state/navigation_root_url}/dashboard', }
_static_140141462625776 = {'class': 'nav-item', }
_static_140141462303312 = {'class': 'autotoc-nav nav nav-tabs mb-3', }
_static_140141462306384 = {'class': 'autotabs', }
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

    def render_content_core(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462304224
            __attrs_140141462304224 = _static_140141533420656
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7f753a143e50> name=None at 7f753a143e20> -> __attrs_140141462303408
            __attrs_140141462303408 = _static_140141462306384

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="autotabs">\n          ')

            # <Static value=<ast.Dict object at 0x7f753a143250> name=None at 7f753a143c70> -> __attrs_140141462623568
            __attrs_140141462623568 = _static_140141462303312

            # <nav ... (0:0)
            # --------------------------------------------------------
            __append('<nav class="autotoc-nav nav nav-tabs mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x7f753a191df0> name=None at 7f753a191e20> -> __attrs_140141462626160
            __attrs_140141462626160 = _static_140141462625776

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="nav-item">\n              ')

            # <Static value=<ast.Dict object at 0x7f753a191670> name=None at 7f753a191c10> -> __attrs_140141462712272
            __attrs_140141462712272 = _static_140141462623856

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="active nav-link"')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462625152
            __default_140141462625152 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${context/@@plone_portal_state/navigation_root_url}/dashboard' (36:23)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f753a191a00> -> __attr_href
            __token = 1128
            __token = 1130
            try:
                __zt_tmp = __attrs_140141462712272
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140141533071728('path', 'context/@@plone_portal_state/navigation_root_url', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/dashboard', ))
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is _DEFAULT_MARKER):
                    __attr_href = None
                else:
                    __tt = type(__attr_href)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_href = str(__attr_href)
                    else:
                        if (__tt is bytes):
                            __attr_href = decode(__attr_href)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_href = __attr_href.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_href)
                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                else:
                                    __attr_href = __attr_href()
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' >')
            __stream_140141462624576 = []
            __append_140141462624576 = __stream_140141462624576.append
            __append_140141462624576('Dashboard')
            __msgid_140141462624576 = __re_whitespace(''.join(__stream_140141462624576)).strip()
            if 'label_dashboard':
                __append(translate('label_dashboard', mapping=None, default=__msgid_140141462624576, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n            </span>\n            ')

            # <Static value=<ast.Dict object at 0x7f753a1a6580> name=None at 7f753a1a6310> -> __attrs_140141462711168
            __attrs_140141462711168 = _static_140141462709632

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="nav-item">\n              ')

            # <Static value=<ast.Dict object at 0x7f753a1a67c0> name=None at 7f753a1a6460> -> __attrs_140141462710304
            __attrs_140141462710304 = _static_140141462710208

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="nav-link"')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462709200
            __default_140141462709200 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${context/@@plone_portal_state/navigation_root_url}/@@manage-dashboard?_authenticator=${view/auth_token}' (42:23)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f753a1a63a0> -> __attr_href
            __token = 1383
            __token = 1385
            try:
                __zt_tmp = __attrs_140141462710304
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140141533071728('path', 'context/@@plone_portal_state/navigation_root_url', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 1471
            try:
                __zt_tmp = __attrs_140141462710304
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href_1469 = _static_140141533071728('path', 'view/auth_token', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            __attr_href_1469 = __quote(__attr_href_1469, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@manage-dashboard?_authenticator=', (__attr_href_1469 if (__attr_href_1469 is not None) else ''), ))
            if (__attr_href is None):
                pass
            else:
                if (__attr_href is _DEFAULT_MARKER):
                    __attr_href = None
                else:
                    __tt = type(__attr_href)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_href = str(__attr_href)
                    else:
                        if (__tt is bytes):
                            __attr_href = decode(__attr_href)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_href = __attr_href.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_href)
                                    __attr_href = (str(__attr_href) if (__attr_href is __converted) else __converted)
                                else:
                                    __attr_href = __attr_href()
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))
            __append(' >')
            __stream_140141462708912 = []
            __append_140141462708912 = __stream_140141462708912.append
            __append_140141462708912('Edit')
            __msgid_140141462708912 = __re_whitespace(''.join(__stream_140141462708912)).strip()
            if 'label_edit':
                __append(translate('label_edit', mapping=None, default=__msgid_140141462708912, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n            </span>\n          </nav>\n\n\n          ')

            # <Static value=<ast.Dict object at 0x7f753a1921f0> name=None at 7f753a1a6430> -> __attrs_140141462627232
            __attrs_140141462627232 = _static_140141462626800

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="row row-cols-1 row-cols-md-2 gy-2" id="dashboard" >\n            ')

            # <Static value=<ast.Dict object at 0x7f753a1928e0> name=None at 7f753a192b50> -> __attrs_140141462629920
            __attrs_140141462629920 = _static_140141462628576

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="dashboard-portlets1" >')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462629296
            __default_140141462629296 = _DEFAULT_MARKER

            # <Value 'provider:plone.dashboard1' (53:40)> -> __cache_140141462628528
            __token = 1778
            try:
                __zt_tmp = __attrs_140141462629920
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462628528 = _static_140141533071728('provider', 'plone.dashboard1', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.dashboard1' (53:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1929a0> -> __condition
            __expression = __cache_140141462628528

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140141462628528
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n            ')

            # <Static value=<ast.Dict object at 0x7f753aa18190> name=None at 7f753aa189a0> -> __attrs_140141471564752
            __attrs_140141471564752 = _static_140141471564176

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="dashboard-portlets2" >')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141471565616
            __default_140141471565616 = _DEFAULT_MARKER

            # <Value 'provider:plone.dashboard2' (56:40)> -> __cache_140141462630352
            __token = 1907
            try:
                __zt_tmp = __attrs_140141471564752
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462630352 = _static_140141533071728('provider', 'plone.dashboard2', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.dashboard2' (56:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a192ee0> -> __condition
            __expression = __cache_140141462630352

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140141462630352
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n            ')

            # <Static value=<ast.Dict object at 0x7f753a1bb310> name=None at 7f753a1bbdf0> -> __attrs_140141462797712
            __attrs_140141462797712 = _static_140141462795024

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="dashboard-portlets3" >')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462795504
            __default_140141462795504 = _DEFAULT_MARKER

            # <Value 'provider:plone.dashboard3' (59:40)> -> __cache_140141462794784
            __token = 2036
            try:
                __zt_tmp = __attrs_140141462797712
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462794784 = _static_140141533071728('provider', 'plone.dashboard3', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.dashboard3' (59:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1bb040> -> __condition
            __expression = __cache_140141462794784

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140141462794784
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n            ')

            # <Static value=<ast.Dict object at 0x7f753a1bb430> name=None at 7f753a1bb7f0> -> __attrs_140141462794496
            __attrs_140141462794496 = _static_140141462795312

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="dashboard-portlets4" >')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462796512
            __default_140141462796512 = _DEFAULT_MARKER

            # <Value 'provider:plone.dashboard4' (62:40)> -> __cache_140141462796656
            __token = 2165
            try:
                __zt_tmp = __attrs_140141462794496
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462796656 = _static_140141533071728('provider', 'plone.dashboard4', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.dashboard4' (62:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1bbc10> -> __condition
            __expression = __cache_140141462796656

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140141462796656
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n          </div>\n\n        </div>\n\n      ')
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

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462783408
            __attrs_140141462783408 = _static_140141533420656
            __previous_i18n_domain_140141462785040 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140141486670784 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f753a1b84c0> name=None at 7f753a1b80d0> -> __value
            __value = _static_140141462783168
            econtext['macroname'] = __value

            def __fill_content_title(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462805712
                __attrs_140141462805712 = _static_140141533420656
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f753a1bde80> name=None at 7f753a1bd490> -> __attrs_140141462758928
                __attrs_140141462758928 = _static_140141462806144
                __backup_memberinfo_140141462334864 = get('memberinfo', __marker)

                # <Value 'context/portal_membership/getMemberInfo' (16:23)> -> __value
                __token = 468
                try:
                    __zt_tmp = __attrs_140141462758928
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'context/portal_membership/getMemberInfo', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['memberinfo'] = __value
                __backup_member_140141462335296 = get('member', __marker)

                # <Value 'context/@@plone_portal_state/member' (17:18)> -> __value
                __token = 527
                try:
                    __zt_tmp = __attrs_140141462758928
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'context/@@plone_portal_state/member', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['member'] = __value
                __backup_name_140141462332656 = get('name', __marker)

                # <Value "python:memberinfo['fullname'] or member.getId() or member.getId()" (18:15)> -> __value
                __token = 580
                try:
                    __zt_tmp = __attrs_140141462758928
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', "memberinfo['fullname'] or member.getId() or member.getId()", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['name'] = __value

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading" >')
                __stream_140141462612224_user_name = ''
                __stream_140141462803984 = []
                __append_140141462803984 = __stream_140141462803984.append
                __append_140141462803984('\n        ')
                __stream_140141462612224_user_name = []
                __append_140141462612224_user_name = __stream_140141462612224_user_name.append

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462296128
                __attrs_140141462296128 = _static_140141533420656

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462294736
                __default_140141462294736 = _DEFAULT_MARKER

                # <Value 'name' (22:27)> -> __cache_140141462758592
                __token = 741
                try:
                    __zt_tmp = __attrs_140141462296128
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140141462758592 = _static_140141533071728('path', 'name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                # <BinOp left=<Value 'name' (22:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a141760> -> __condition
                __expression = __cache_140141462758592

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append_140141462612224_user_name('<span ></span>')
                else:
                    __content = __cache_140141462758592
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append_140141462612224_user_name(__content)
                __append_140141462803984('${user_name}')
                __stream_140141462612224_user_name = ''.join(__stream_140141462612224_user_name)
                __append_140141462803984('\n        &#8217;s dashboard\n      ')
                __msgid_140141462803984 = __re_whitespace(''.join(__stream_140141462803984)).strip()
                if 'heading_dashboard':
                    __append(translate('heading_dashboard', mapping={'user_name': __stream_140141462612224_user_name, }, default=__msgid_140141462803984, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>')
                if (__backup_name_140141462332656 is __marker):
                    del econtext['name']
                else:
                    econtext['name'] = __backup_name_140141462332656
                if (__backup_member_140141462335296 is __marker):
                    del econtext['member']
                else:
                    econtext['member'] = __backup_member_140141462335296
                if (__backup_memberinfo_140141462334864 is __marker):
                    del econtext['memberinfo']
                else:
                    econtext['memberinfo'] = __backup_memberinfo_140141462334864
                __append('\n    ')
            _slots = econtext['__slot_content_title'] = _deque((__fill_content_title, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462304512
                __attrs_140141462304512 = _static_140141533420656
                __append('\n      ')
                __token = None
                render_content_core(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_140141462783408
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140141533071728('path', 'context/main_template/macros/master', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140141486670784 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140141486670784
            __i18n_domain = __previous_i18n_domain_140141462785040
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_content_core': render_content_core, 'render': render, }