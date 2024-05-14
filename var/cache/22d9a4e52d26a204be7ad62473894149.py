# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.portlets-5.0.7-py3.9.egg/plone/app/portlets/browser/templates/manage-dashboard.pt'

__tokens = {1118: ('${context/@@plone_portal_state/navigation_root_url}/dashboard', 38, 21), 1120: ('context/@@plone_portal_state/navigation_root_url', 38, 23), 1316: ('${context/@@plone_portal_state/navigation_root_url}/@@manage-dashboard?_authenticator=${view/auth_token}', 42, 21), 1318: ('context/@@plone_portal_state/navigation_root_url', 42, 23), 1404: ('view/auth_token', 42, 109), 1717: ('provider:plone.dashboard1', 52, 40), 1846: ('provider:plone.dashboard2', 55, 40), 1975: ('provider:plone.dashboard3', 58, 40), 2104: ('provider:plone.dashboard4', 61, 40), 435: ("python:request.set('disable_border',1)", 14, 25), 512: (" python:request.set('disable_plone.leftcolumn',1", 15, 37), 599: ("o python:request.set('disable_plone.rightcolumn',", 16, 36), 247: ('context/main_template/macros/master', 6, 23), 247: ('context/main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from collections import deque as _deque
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140141462304032 = {'class': 'documentFirstHeading', }
_static_140141462636528 = 'master'
_static_140141462691648 = {'id': 'dashboard-portlets4', }
_static_140141462750784 = {'id': 'dashboard-portlets3', }
_static_140141462751600 = {'id': 'dashboard-portlets2', }
_static_140141462455440 = {'class': '', 'id': 'dashboard-portlets1', }
_static_140141462437312 = {'class': 'row row-cols-1 row-cols-md-2 gx-5 gy-5', 'id': 'dashboard', }
_static_140141462446672 = {'class': 'active nav-link', 'href': '${context/@@plone_portal_state/navigation_root_url}/@@manage-dashboard?_authenticator=${view/auth_token}', }
_static_140141533071440 = __C2ZContextWrapper
_static_140141533071728 = __compile_zt_expr
_static_140141462796704 = {'class': 'nav-link', 'href': '${context/@@plone_portal_state/navigation_root_url}/dashboard', }
_static_140141462794736 = {'class': 'autotoc-nav nav nav-tabs mb-3', }
_static_140141462782256 = {'class': 'autotabs', }
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

    def render_main(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462304368
            __attrs_140141462304368 = _static_140141533420656
            __append('\n\n        ')

            # <Static value=<ast.Dict object at 0x7f753a1b8130> name=None at 7f753a1b8580> -> __attrs_140141462783408
            __attrs_140141462783408 = _static_140141462782256

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="autotabs">\n          ')

            # <Static value=<ast.Dict object at 0x7f753a1bb1f0> name=None at 7f753a1bbdc0> -> __attrs_140141462797904
            __attrs_140141462797904 = _static_140141462794736

            # <nav ... (0:0)
            # --------------------------------------------------------
            __append('<nav class="autotoc-nav nav nav-tabs mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x7f753a1bb9a0> name=None at 7f753a1bb700> -> __attrs_140141462794496
            __attrs_140141462794496 = _static_140141462796704

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="nav-link"')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462796128
            __default_140141462796128 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${context/@@plone_portal_state/navigation_root_url}/dashboard' (38:21)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f753a1bbb20> -> __attr_href
            __token = 1118
            __token = 1120
            try:
                __zt_tmp = __attrs_140141462794496
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
            __stream_140141462795024 = []
            __append_140141462795024 = __stream_140141462795024.append
            __append_140141462795024('Dashboard')
            __msgid_140141462795024 = __re_whitespace(''.join(__stream_140141462795024)).strip()
            if 'label_dashboard':
                __append(translate('label_dashboard', mapping=None, default=__msgid_140141462795024, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n            ')

            # <Static value=<ast.Dict object at 0x7f753a166250> name=None at 7f753a1ae4c0> -> __attrs_140141462434768
            __attrs_140141462434768 = _static_140141462446672

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="active nav-link"')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462435104
            __default_140141462435104 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${context/@@plone_portal_state/navigation_root_url}/@@manage-dashboard?_authenticator=${view/auth_token}' (42:21)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f753a163c70> -> __attr_href
            __token = 1316
            __token = 1318
            try:
                __zt_tmp = __attrs_140141462434768
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140141533071728('path', 'context/@@plone_portal_state/navigation_root_url', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 1404
            try:
                __zt_tmp = __attrs_140141462434768
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href_1402 = _static_140141533071728('path', 'view/auth_token', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            __attr_href_1402 = __quote(__attr_href_1402, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/@@manage-dashboard?_authenticator=', (__attr_href_1402 if (__attr_href_1402 is not None) else ''), ))
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
            __stream_140141462797232 = []
            __append_140141462797232 = __stream_140141462797232.append
            __append_140141462797232('Edit')
            __msgid_140141462797232 = __re_whitespace(''.join(__stream_140141462797232)).strip()
            if 'label_edit':
                __append(translate('label_edit', mapping=None, default=__msgid_140141462797232, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n          </nav>\n\n          ')

            # <Static value=<ast.Dict object at 0x7f753a163dc0> name=None at 7f753a1631c0> -> __attrs_140141462681344
            __attrs_140141462681344 = _static_140141462437312

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="row row-cols-1 row-cols-md-2 gx-5 gy-5" id="dashboard" >\n            ')

            # <Static value=<ast.Dict object at 0x7f753a168490> name=None at 7f753a168070> -> __attrs_140141462749968
            __attrs_140141462749968 = _static_140141462455440

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="" id="dashboard-portlets1" >')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462454432
            __default_140141462454432 = _DEFAULT_MARKER

            # <Value 'provider:plone.dashboard1' (52:40)> -> __cache_140141462396496
            __token = 1717
            try:
                __zt_tmp = __attrs_140141462749968
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462396496 = _static_140141533071728('provider', 'plone.dashboard1', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.dashboard1' (52:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a168550> -> __condition
            __expression = __cache_140141462396496

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140141462396496
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n            ')

            # <Static value=<ast.Dict object at 0x7f753a1b0970> name=None at 7f753a1b09d0> -> __attrs_140141462752464
            __attrs_140141462752464 = _static_140141462751600

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="dashboard-portlets2" >')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462751120
            __default_140141462751120 = _DEFAULT_MARKER

            # <Value 'provider:plone.dashboard2' (55:40)> -> __cache_140141462752848
            __token = 1846
            try:
                __zt_tmp = __attrs_140141462752464
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462752848 = _static_140141533071728('provider', 'plone.dashboard2', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.dashboard2' (55:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1b0280> -> __condition
            __expression = __cache_140141462752848

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140141462752848
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n            ')

            # <Static value=<ast.Dict object at 0x7f753a1b0640> name=None at 7f753a1b0910> -> __attrs_140141462691456
            __attrs_140141462691456 = _static_140141462750784

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="dashboard-portlets3" >')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462751792
            __default_140141462751792 = _DEFAULT_MARKER

            # <Value 'provider:plone.dashboard3' (58:40)> -> __cache_140141462752128
            __token = 1975
            try:
                __zt_tmp = __attrs_140141462691456
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462752128 = _static_140141533071728('provider', 'plone.dashboard3', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.dashboard3' (58:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1b04c0> -> __condition
            __expression = __cache_140141462752128

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140141462752128
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n            ')

            # <Static value=<ast.Dict object at 0x7f753a1a1f40> name=None at 7f753a1a1cd0> -> __attrs_140141462689728
            __attrs_140141462689728 = _static_140141462691648

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="dashboard-portlets4" >')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462689296
            __default_140141462689296 = _DEFAULT_MARKER

            # <Value 'provider:plone.dashboard4' (61:40)> -> __cache_140141462688912
            __token = 2104
            try:
                __zt_tmp = __attrs_140141462689728
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462688912 = _static_140141533071728('provider', 'plone.dashboard4', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.dashboard4' (61:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1a19d0> -> __condition
            __expression = __cache_140141462688912

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140141462688912
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n          </div>\n        </div>\n\n      ')
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

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462635856
            __attrs_140141462635856 = _static_140141533420656
            __previous_i18n_domain_140141462636240 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140141487114304 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f753a1947f0> name=None at 7f753a194c70> -> __value
            __value = _static_140141462636528
            econtext['macroname'] = __value

            def __fill_top_slot(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462137632
                __attrs_140141462137632 = _static_140141533420656
                __backup_dummy_140141462353136 = get('dummy', __marker)

                # <Value "python:request.set('disable_border',1)" (14:25)> -> __value
                __token = 435
                try:
                    __zt_tmp = __attrs_140141462137632
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', "request.set('disable_border',1)", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['dummy'] = __value
                __backup_disable_column_one_140141462635664 = get('disable_column_one', __marker)

                # <Value "python:request.set('disable_plone.leftcolumn',1)" (15:37)> -> __value
                __token = 512
                try:
                    __zt_tmp = __attrs_140141462137632
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', "request.set('disable_plone.leftcolumn',1)", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['disable_column_one'] = __value
                __backup_disable_column_two_140141462637920 = get('disable_column_two', __marker)

                # <Value "python:request.set('disable_plone.rightcolumn',1)" (16:36)> -> __value
                __token = 599
                try:
                    __zt_tmp = __attrs_140141462137632
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', "request.set('disable_plone.rightcolumn',1)", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['disable_column_two'] = __value
                if (__backup_disable_column_two_140141462637920 is __marker):
                    del econtext['disable_column_two']
                else:
                    econtext['disable_column_two'] = __backup_disable_column_two_140141462637920
                if (__backup_disable_column_one_140141462635664 is __marker):
                    del econtext['disable_column_one']
                else:
                    econtext['disable_column_one'] = __backup_disable_column_one_140141462635664
                if (__backup_dummy_140141462353136 is __marker):
                    del econtext['dummy']
                else:
                    econtext['dummy'] = __backup_dummy_140141462353136
            _slots = econtext['__slot_top_slot'] = _deque((__fill_top_slot, ))

            def __fill_content_title(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462304224
                __attrs_140141462304224 = _static_140141533420656
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f753a143520> name=None at 7f753a143e50> -> __attrs_140141462306000
                __attrs_140141462306000 = _static_140141462304032

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading" >')
                __stream_140141462304320 = []
                __append_140141462304320 = __stream_140141462304320.append
                __append_140141462304320('\n        Edit your dashboard\n      ')
                __msgid_140141462304320 = __re_whitespace(''.join(__stream_140141462304320)).strip()
                if 'title_edit_dashboard':
                    __append(translate('title_edit_dashboard', mapping=None, default=__msgid_140141462304320, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n    ')
            _slots = econtext['__slot_content_title'] = _deque((__fill_content_title, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462305808
                __attrs_140141462305808 = _static_140141533420656
                __append('\n\n      ')
                __token = None
                render_main(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n    ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/main_template/macros/master' (6:23)> -> __macro
            __token = 247
            try:
                __zt_tmp = __attrs_140141462635856
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140141533071728('path', 'context/main_template/macros/master', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            __token = 247
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140141487114304 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140141487114304
            __i18n_domain = __previous_i18n_domain_140141462636240
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_main': render_main, 'render': render, }