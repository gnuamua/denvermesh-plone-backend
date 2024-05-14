# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.users-3.0.6-py3.9.egg/plone/app/users/browser/account-panel.pt'

__tokens = {372: ('${view/label}', 10, 37), 374: ('view/label', 10, 39), 469: ('${view/description}', 14, 20), 471: ('view/description', 14, 22), 657: ('view/prepareObjectTabs', 21, 26), 800: ('view_actions', 26, 33), 961: ('action/selected|nothing', 31, 26), 845: ('contentview-${action/id}', 28, 19), 859: ('action/id', 28, 33), 892: ('${action/url}', 29, 21), 894: ('action/url', 29, 23), 1058: ("python:'autotoc-level-1' + (' nav-link active' if selected else ' nav-link')", 34, 23), 1199: ('${action/title}', 37, 13), 1201: ('action/title', 37, 15), 1289: ('context/@@ploneform-macros/titlelessform', 42, 26), 1289: ('context/@@ploneform-macros/titlelessform', 42, 26), 231: ('context/main_template/macros/master', 5, 23), 231: ('context/main_template/macros/master', 5, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER
from collections import deque as _deque

_static_140141471619680 = 'titlelessform'
_static_140141471617952 = {'id': 'contentview-${action/id}', 'href': '${action/url}', 'class': "python:'autotoc-level-1' + (' nav-link active' if selected else ' nav-link')", }
_static_140141471599344 = {'class': 'nav-item', }
_static_140141471597952 = {'class': 'nav nav-tabs', }
_static_140141471596304 = {'class': 'autotoc-nav mb-3', }
_static_140141471594960 = {'class': 'autotabs', }
_static_140141471593040 = {'class': 'lead', }
_static_140141533071440 = __C2ZContextWrapper
_static_140141533071728 = __compile_zt_expr
_static_140141471587008 = {'class': 'documentFirstHeading', }
_static_140141471584464 = 'master'
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

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141471584800
            __attrs_140141471584800 = _static_140141533420656
            __previous_i18n_domain_140141471584944 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140141515195904 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f753aa1d0d0> name=None at 7f753aa1d100> -> __value
            __value = _static_140141471584464
            econtext['macroname'] = __value

            def __fill_content_title(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141471585856
                __attrs_140141471585856 = _static_140141533420656
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f753aa1dac0> name=None at 7f753aa1d940> -> __attrs_140141471587344
                __attrs_140141471587344 = _static_140141471587008

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')

                # <Interpolation value=<Substitution '${view/label}' (10:37)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f753aa1dd60> -> __content_140141614154928
                __token = 372
                __token = 374
                try:
                    __zt_tmp = __attrs_140141471587344
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140141614154928 = _static_140141533071728('path', 'view/label', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __content_140141614154928 = __quote(__content_140141614154928, '\x00', '&#0;', None, None)
                __content_140141614154928 = __content_140141614154928
                if (__content_140141614154928 is None):
                    pass
                else:
                    if (__content_140141614154928 is None):
                        __content_140141614154928 = None
                    else:
                        __tt = type(__content_140141614154928)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140141614154928 = str(__content_140141614154928)
                        else:
                            if (__tt is bytes):
                                __content_140141614154928 = decode(__content_140141614154928)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140141614154928 = __content_140141614154928.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140141614154928)
                                        __content_140141614154928 = (str(__content_140141614154928) if (__content_140141614154928 is __converted) else __converted)
                                    else:
                                        __content_140141614154928 = __content_140141614154928()
                if (__content_140141614154928 is not None):
                    __append(__content_140141614154928)
                __append('</h1>\n  ')
            _slots = econtext['__slot_content_title'] = _deque((__fill_content_title, ))

            def __fill_content_description(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141471587824
                __attrs_140141471587824 = _static_140141533420656
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f753aa1f250> name=None at 7f753aa1f280> -> __attrs_140141471593424
                __attrs_140141471593424 = _static_140141471593040

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')

                # <Interpolation value=<Substitution '${view/description}' (14:20)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f753aa1f520> -> __content_140141614154928
                __token = 469
                __token = 471
                try:
                    __zt_tmp = __attrs_140141471593424
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140141614154928 = _static_140141533071728('path', 'view/description', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __content_140141614154928 = __quote(__content_140141614154928, '\x00', '&#0;', None, None)
                __content_140141614154928 = __content_140141614154928
                if (__content_140141614154928 is None):
                    pass
                else:
                    if (__content_140141614154928 is None):
                        __content_140141614154928 = None
                    else:
                        __tt = type(__content_140141614154928)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140141614154928 = str(__content_140141614154928)
                        else:
                            if (__tt is bytes):
                                __content_140141614154928 = decode(__content_140141614154928)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140141614154928 = __content_140141614154928.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140141614154928)
                                        __content_140141614154928 = (str(__content_140141614154928) if (__content_140141614154928 is __converted) else __converted)
                                    else:
                                        __content_140141614154928 = __content_140141614154928()
                if (__content_140141614154928 is not None):
                    __append(__content_140141614154928)
                __append('</p>\n  ')
            _slots = econtext['__slot_content_description'] = _deque((__fill_content_description, ))

            def __fill_content_core(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141471593904
                __attrs_140141471593904 = _static_140141533420656
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f753aa1f9d0> name=None at 7f753aa1fa00> -> __attrs_140141471595344
                __attrs_140141471595344 = _static_140141471594960

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="autotabs">\n      ')

                # <Static value=<ast.Dict object at 0x7f753aa1ff10> name=None at 7f753aa1ff40> -> __attrs_140141471596752
                __attrs_140141471596752 = _static_140141471596304
                __backup_view_actions_140141471932272 = get('view_actions', __marker)

                # <Value 'view/prepareObjectTabs' (21:26)> -> __value
                __token = 657
                try:
                    __zt_tmp = __attrs_140141471596752
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'view/prepareObjectTabs', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['view_actions'] = __value

                # <nav ... (0:0)
                # --------------------------------------------------------
                __append('<nav class="autotoc-nav mb-3" >\n        ')

                # <Static value=<ast.Dict object at 0x7f753aa20580> name=None at 7f753aa205b0> -> __attrs_140141471598336
                __attrs_140141471598336 = _static_140141471597952

                # <ul ... (0:0)
                # --------------------------------------------------------
                __append('<ul class="nav nav-tabs">\n          ')

                # <Static value=<ast.Dict object at 0x7f753aa20af0> name=None at 7f753aa20b20> -> __attrs_140141471599728
                __attrs_140141471599728 = _static_140141471599344
                __backup_action_140141471597280 = get('action', __marker)

                # <Value 'view_actions' (26:33)> -> __iterator
                __token = 800
                try:
                    __zt_tmp = __attrs_140141471599728
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140141533071728('path', 'view_actions', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                (__iterator, ____index_140141471600064, ) = getname('repeat')('action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="nav-item" >\n            ')

                    # <Static value=<ast.Dict object at 0x7f753aa253a0> name=None at 7f753aa253d0> -> __attrs_140141471619008
                    __attrs_140141471619008 = _static_140141471617952
                    __backup_selected_140141471598672 = get('selected', __marker)

                    # <Value 'action/selected|nothing' (31:26)> -> __value
                    __token = 961
                    try:
                        __zt_tmp = __attrs_140141471619008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140141533071728('path', 'action/selected|nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    econtext['selected'] = __value

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141471617424
                    __default_140141471617424 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution 'contentview-${action/id}' (28:19)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f753aa25250> -> __attr_id
                    __token = 845
                    __token = 859
                    try:
                        __zt_tmp = __attrs_140141471619008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140141533071728('path', 'action/id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_id = ('%s%s' % ('contentview-', (__attr_id if (__attr_id is not None) else ''), ))
                    if (__attr_id is None):
                        pass
                    else:
                        if (__attr_id is _DEFAULT_MARKER):
                            __attr_id = None
                        else:
                            __tt = type(__attr_id)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_id = str(__attr_id)
                            else:
                                if (__tt is bytes):
                                    __attr_id = decode(__attr_id)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_id = __attr_id.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_id)
                                            __attr_id = (str(__attr_id) if (__attr_id is __converted) else __converted)
                                        else:
                                            __attr_id = __attr_id()
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141471618192
                    __default_140141471618192 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${action/url}' (29:21)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f753aa25070> -> __attr_href
                    __token = 892
                    __token = 894
                    try:
                        __zt_tmp = __attrs_140141471619008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140141533071728('path', 'action/url', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_href = __attr_href
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

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141471618480
                    __default_140141471618480 = _DEFAULT_MARKER

                    # <Substitution "python:'autotoc-level-1' + (' nav-link active' if selected else ' nav-link')" (34:23)> -> __attr_class
                    __token = 1058
                    try:
                        __zt_tmp = __attrs_140141471619008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140141533071728('python', "'autotoc-level-1' + (' nav-link active' if selected else ' nav-link')", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append(' >')
                    __stream_140141471600592 = []
                    __append_140141471600592 = __stream_140141471600592.append

                    # <Interpolation value=<Substitution '${action/title}' (37:13)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f753aa25a00> -> __content_140141614154928
                    __token = 1199
                    __token = 1201
                    try:
                        __zt_tmp = __attrs_140141471619008
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140141614154928 = _static_140141533071728('path', 'action/title', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __content_140141614154928 = __quote(__content_140141614154928, '\x00', '&#0;', None, None)
                    __content_140141614154928 = __content_140141614154928
                    if (__content_140141614154928 is None):
                        pass
                    else:
                        if (__content_140141614154928 is None):
                            __content_140141614154928 = None
                        else:
                            __tt = type(__content_140141614154928)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140141614154928 = str(__content_140141614154928)
                            else:
                                if (__tt is bytes):
                                    __content_140141614154928 = decode(__content_140141614154928)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140141614154928 = __content_140141614154928.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140141614154928)
                                            __content_140141614154928 = (str(__content_140141614154928) if (__content_140141614154928 is __converted) else __converted)
                                        else:
                                            __content_140141614154928 = __content_140141614154928()
                    if (__content_140141614154928 is not None):
                        __append_140141471600592(__content_140141614154928)
                    __msgid_140141471600592 = __re_whitespace(''.join(__stream_140141471600592)).strip()
                    if __msgid_140141471600592:
                        __append(translate(__msgid_140141471600592, mapping=None, default=__msgid_140141471600592, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>')
                    if (__backup_selected_140141471598672 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_140141471598672
                    __append('\n          </li>')
                    ____index_140141471600064 -= 1
                    if (____index_140141471600064 > 0):
                        __append('\n          ')
                if (__backup_action_140141471597280 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140141471597280
                __append('\n        </ul>\n      </nav>')
                if (__backup_view_actions_140141471932272 is __marker):
                    del econtext['view_actions']
                else:
                    econtext['view_actions'] = __backup_view_actions_140141471932272
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141471620016
                __attrs_140141471620016 = _static_140141533420656
                __backup_macroname_140141511408192 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x7f753aa25a60> name=None at 7f753aa25a90> -> __value
                __value = _static_140141471619680
                econtext['macroname'] = __value

                # <Value 'context/@@ploneform-macros/titlelessform' (42:26)> -> __macro
                __token = 1289
                try:
                    __zt_tmp = __attrs_140141471620016
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140141533071728('path', 'context/@@ploneform-macros/titlelessform', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __token = 1289
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140141511408192 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140141511408192
                __append('\n    </div>\n  ')
            _slots = econtext['__slot_content_core'] = _deque((__fill_content_core, ))

            # <Value 'context/main_template/macros/master' (5:23)> -> __macro
            __token = 231
            try:
                __zt_tmp = __attrs_140141471584800
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140141533071728('path', 'context/main_template/macros/master', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            __token = 231
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140141515195904 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140141515195904
            __i18n_domain = __previous_i18n_domain_140141471584944
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }