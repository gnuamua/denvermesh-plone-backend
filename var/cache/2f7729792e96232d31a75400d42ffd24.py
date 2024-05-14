# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/viewlets/menu.pt'

__tokens = {61: ('context/@@plone', 2, 30), 104: (' view/locked_ico', 3, 26), 147: ("s python:context.restrictedTraverse('@@iconresolver", 4, 24), 255: ('ploneview/showToolbar', 6, 33), 352: ('options/actions', 9, 34), 473: ('action/id', 13, 19), 502: (' action/selected | python:Fals', 14, 18), 407: ('contentview-${action/id}', 11, 12), 421: ('action/id', 11, 26), 568: ("nav-link ${python:'locked' if locked and actionid == 'history' else ''} ${action/cssClass | nothing} ${python:'active' if selected else None}", 18, 16), 579: ("python:'locked' if locked and actionid == 'history' else ''", 18, 27), 642: ('action/cssClass | nothing', 18, 90), 671: ("python:'active' if selected else None", 18, 119), 771: ('action/url', 21, 16), 800: (' action/link_target|nothin', 22, 17), 876: ("python:actionid != 'history'", 26, 27), 942: ("python:action['icon']", 27, 35), 1008: ("python:icons.tag(action['icon'] or 'toolbar-action', tag_class='me-1')", 28, 43), 1160: ('action/title', 31, 29), 1286: ("python:actionid == 'history'", 36, 31), 1360: ("python:icons.tag('lock' if locked else action['icon'], tag_class='me-1')", 37, 43), 1547: ('${context/ModificationDate}', 40, 28), 1549: ('context/ModificationDate', 40, 30), 1670: ('', 42, 31), 1685: ('${context/ModificationDate}', 43, 13), 1687: ('context/ModificationDate', 43, 15)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355529754944 = {'class': 'pat-display-time', 'datetime': '${context/ModificationDate}', 'data-pat-display-time': 'output-format: L LTS', }
_static_140355449327776 = {'class': 'toolbar-label', }
_static_140355448967712 = {'class': 'toolbar-label', }
_static_140355449159792 = {'class': "nav-link ${python:'locked' if locked and actionid == 'history' else ''} ${action/cssClass | nothing} ${python:'active' if selected else None}", 'href': '#', 'target': 'action/link_target|nothing', }
_static_140355449160896 = {'class': 'nav-item', 'id': 'contentview-${action/id}', }
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

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449101136
            __attrs_140355449101136 = _static_140355540704128
            __backup_ploneview_140355449098688 = get('ploneview', __marker)

            # <Value 'context/@@plone' (2:30)> -> __value
            __token = 61
            try:
                __zt_tmp = __attrs_140355449101136
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'context/@@plone', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['ploneview'] = __value
            __backup_locked_140355449100800 = get('locked', __marker)

            # <Value 'view/locked_icon' (3:26)> -> __value
            __token = 104
            try:
                __zt_tmp = __attrs_140355449101136
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/locked_icon', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['locked'] = __value
            __backup_icons_140355449098400 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (4:24)> -> __value
            __token = 147
            try:
                __zt_tmp = __attrs_140355449101136
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['icons'] = __value

            # <Value 'ploneview/showToolbar' (6:33)> -> __condition
            __token = 255
            try:
                __zt_tmp = __attrs_140355449101136
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'ploneview/showToolbar', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140355449461152 = __i18n_domain
                __i18n_domain = 'plone'
                __append('\n  ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449163488
                __attrs_140355449163488 = _static_140355540704128
                __backup_action_140355449460000 = get('action', __marker)

                # <Value 'options/actions' (9:34)> -> __iterator
                __token = 352
                try:
                    __zt_tmp = __attrs_140355449163488
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140355540363392('path', 'options/actions', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                (__iterator, ____index_140355449162672, ) = getname('repeat')('action', __iterator)
                econtext['action'] = None
                for __item in __iterator:
                    econtext['action'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7fa70cb084c0> name=None at 7fa70cb08790> -> __attrs_140355449160800
                    __attrs_140355449160800 = _static_140355449160896
                    __backup_actionid_140355449460096 = get('actionid', __marker)

                    # <Value 'action/id' (13:19)> -> __value
                    __token = 473
                    try:
                        __zt_tmp = __attrs_140355449160800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'action/id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['actionid'] = __value
                    __backup_selected_140355449160464 = get('selected', __marker)

                    # <Value 'action/selected | python:False' (14:18)> -> __value
                    __token = 502
                    try:
                        __zt_tmp = __attrs_140355449160800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'action/selected | python:False', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['selected'] = __value

                    # <li ... (0:0)
                    # --------------------------------------------------------
                    __append('<li class="nav-item"')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449160128
                    __default_140355449160128 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution 'contentview-${action/id}' (11:12)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cb082e0> -> __attr_id
                    __token = 407
                    __token = 421
                    try:
                        __zt_tmp = __attrs_140355449160800
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140355540363392('path', 'action/id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
                    __append(' >\n\n      ')

                    # <Static value=<ast.Dict object at 0x7fa70cb08070> name=None at 7fa70cb08850> -> __attrs_140355449401504
                    __attrs_140355449401504 = _static_140355449159792

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449401936
                    __default_140355449401936 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "nav-link ${python:'locked' if locked and actionid == 'history' else ''} ${action/cssClass | nothing} ${python:'active' if selected else None}" (18:16)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cb43a30> -> __attr_class
                    __token = 568
                    __token = 579
                    try:
                        __zt_tmp = __attrs_140355449401504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140355540363392('python', "'locked' if locked and actionid == 'history' else ''", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __token = 642
                    try:
                        __zt_tmp = __attrs_140355449401504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class_640 = _static_140355540363392('path', 'action/cssClass | nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_class_640 = __quote(__attr_class_640, '"', '&quot;', None, _DEFAULT_MARKER)
                    __token = 671
                    try:
                        __zt_tmp = __attrs_140355449401504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class_669 = _static_140355540363392('python', "'active' if selected else None", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_class_669 = __quote(__attr_class_669, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s%s%s%s%s' % ('nav-link ', (__attr_class if (__attr_class is not None) else ''), ' ', (__attr_class_640 if (__attr_class_640 is not None) else ''), ' ', (__attr_class_669 if (__attr_class_669 is not None) else ''), ))
                    if (__attr_class is None):
                        pass
                    else:
                        if (__attr_class is _DEFAULT_MARKER):
                            __attr_class = None
                        else:
                            __tt = type(__attr_class)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __attr_class = str(__attr_class)
                            else:
                                if (__tt is bytes):
                                    __attr_class = decode(__attr_class)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __attr_class = __attr_class.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__attr_class)
                                            __attr_class = (str(__attr_class) if (__attr_class is __converted) else __converted)
                                        else:
                                            __attr_class = __attr_class()
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449405056
                    __default_140355449405056 = _DEFAULT_MARKER

                    # <Substitution 'action/url' (21:16)> -> __attr_href
                    __token = 771
                    try:
                        __zt_tmp = __attrs_140355449401504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140355540363392('path', 'action/url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449403808
                    __default_140355449403808 = _DEFAULT_MARKER

                    # <Substitution 'action/link_target|nothing' (22:17)> -> __attr_target
                    __token = 800
                    try:
                        __zt_tmp = __attrs_140355449401504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_target = _static_140355540363392('path', 'action/link_target|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_target = __quote(__attr_target, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_target is not None):
                        __append((' target="%s"' % __attr_target))
                    __append(' >\n\n        ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449402848
                    __attrs_140355449402848 = _static_140355540704128

                    # <Value "python:actionid != 'history'" (26:27)> -> __condition
                    __token = 876
                    try:
                        __zt_tmp = __attrs_140355449402848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('python', "actionid != 'history'", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:
                        __append('\n          ')

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449101712
                        __attrs_140355449101712 = _static_140355540704128

                        # <Value "python:action['icon']" (27:35)> -> __condition
                        __token = 942
                        try:
                            __zt_tmp = __attrs_140355449101712
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140355540363392('python', "action['icon']", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449098544
                            __default_140355449098544 = _DEFAULT_MARKER

                            # <Value "python:icons.tag(action['icon'] or 'toolbar-action', tag_class='me-1')" (28:43)> -> __cache_140355449099072
                            __token = 1008
                            try:
                                __zt_tmp = __attrs_140355449101712
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140355449099072 = _static_140355540363392('python', "icons.tag(action['icon'] or 'toolbar-action', tag_class='me-1')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:icons.tag(action['icon'] or 'toolbar-action', tag_class='me-1')" (28:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70caf94c0> -> __condition
                            __expression = __cache_140355449099072

                            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140355449099072
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                        __append('\n          ')

                        # <Static value=<ast.Dict object at 0x7fa70cad9220> name=None at 7fa70cad9430> -> __attrs_140355448968288
                        __attrs_140355448968288 = _static_140355448967712

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="toolbar-label" >')

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448967424
                        __default_140355448967424 = _DEFAULT_MARKER

                        # <Value 'action/title' (31:29)> -> __cache_140355448969872
                        __token = 1160
                        try:
                            __zt_tmp = __attrs_140355448968288
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355448969872 = _static_140355540363392('path', 'action/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value 'action/title' (31:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cad9070> -> __condition
                        __expression = __cache_140355448969872

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('View name')
                        else:
                            __content = __cache_140355448969872
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n        ')
                    __append('\n\n        ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449327728
                    __attrs_140355449327728 = _static_140355540704128

                    # <Value "python:actionid == 'history'" (36:31)> -> __condition
                    __token = 1286
                    try:
                        __zt_tmp = __attrs_140355449327728
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('python', "actionid == 'history'", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:
                        __append('\n          ')

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449327968
                        __attrs_140355449327968 = _static_140355540704128

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449331520
                        __default_140355449331520 = _DEFAULT_MARKER

                        # <Value "python:icons.tag('lock' if locked else action['icon'], tag_class='me-1')" (37:43)> -> __cache_140355449328976
                        __token = 1360
                        try:
                            __zt_tmp = __attrs_140355449327968
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355449328976 = _static_140355540363392('python', "icons.tag('lock' if locked else action['icon'], tag_class='me-1')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value "python:icons.tag('lock' if locked else action['icon'], tag_class='me-1')" (37:43)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb31430> -> __condition
                        __expression = __cache_140355449328976

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140355449328976
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n          ')

                        # <Static value=<ast.Dict object at 0x7fa70cb310a0> name=None at 7fa70cb31df0> -> __attrs_140355449328352
                        __attrs_140355449328352 = _static_140355449327776

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="toolbar-label">\n            ')

                        # <Static value=<ast.Dict object at 0x7fa7117e4940> name=None at 7fa7117e4280> -> __attrs_140355449381552
                        __attrs_140355449381552 = _static_140355529754944

                        # <time ... (0:0)
                        # --------------------------------------------------------
                        __append('<time class="pat-display-time"')

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449382800
                        __default_140355449382800 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution '${context/ModificationDate}' (40:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cb3e580> -> __attr_datetime
                        __token = 1547
                        __token = 1549
                        try:
                            __zt_tmp = __attrs_140355449381552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_datetime = _static_140355540363392('path', 'context/ModificationDate', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        __attr_datetime = __quote(__attr_datetime, '"', '&quot;', None, _DEFAULT_MARKER)
                        __attr_datetime = __attr_datetime
                        if (__attr_datetime is None):
                            pass
                        else:
                            if (__attr_datetime is _DEFAULT_MARKER):
                                __attr_datetime = None
                            else:
                                __tt = type(__attr_datetime)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __attr_datetime = str(__attr_datetime)
                                else:
                                    if (__tt is bytes):
                                        __attr_datetime = decode(__attr_datetime)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __attr_datetime = __attr_datetime.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__attr_datetime)
                                                __attr_datetime = (str(__attr_datetime) if (__attr_datetime is __converted) else __converted)
                                            else:
                                                __attr_datetime = __attr_datetime()
                        if (__attr_datetime is not None):
                            __append((' datetime="%s"' % __attr_datetime))
                        __append(' data-pat-display-time="output-format: L LTS" >')

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449331088
                        __default_140355449331088 = _DEFAULT_MARKER

                        # <Value '' (42:31)> -> __cache_140355449330512
                        __token = 1670
                        try:
                            __zt_tmp = __attrs_140355449381552
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355449330512 = _static_140355540363392('path', '', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value '' (42:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb31b20> -> __condition
                        __expression = __cache_140355449330512

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <Interpolation value=<Substitution '${context/ModificationDate}' (43:13)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70cb3e550> -> __content_140355621335664
                            __token = 1685
                            __token = 1687
                            try:
                                __zt_tmp = __attrs_140355449381552
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_140355621335664 = _static_140355540363392('path', 'context/ModificationDate', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
                        else:
                            __content = __cache_140355449330512
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</time>\n          </span>\n        ')
                    __append('\n\n      </a>\n\n    </li>')
                    if (__backup_selected_140355449160464 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_140355449160464
                    if (__backup_actionid_140355449460096 is __marker):
                        del econtext['actionid']
                    else:
                        econtext['actionid'] = __backup_actionid_140355449460096
                    __append('\n  ')
                    ____index_140355449162672 -= 1
                    if (____index_140355449162672 > 0):
                        __append('')
                if (__backup_action_140355449460000 is __marker):
                    del econtext['action']
                else:
                    econtext['action'] = __backup_action_140355449460000
                __append('\n')
                __i18n_domain = __previous_i18n_domain_140355449461152
            if (__backup_icons_140355449098400 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140355449098400
            if (__backup_locked_140355449100800 is __marker):
                del econtext['locked']
            else:
                econtext['locked'] = __backup_locked_140355449100800
            if (__backup_ploneview_140355449098688 is __marker):
                del econtext['ploneview']
            else:
                econtext['ploneview'] = __backup_ploneview_140355449098688
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }