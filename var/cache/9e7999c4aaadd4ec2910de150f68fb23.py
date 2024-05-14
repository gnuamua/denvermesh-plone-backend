# -*- coding: utf-8 -*-
__filename = 'manage_activateInterfacesForm'

__tokens = {27: ('here/manage_page_header', 1, 27), 91: ('here/manage_tabs', 2, 27), 229: ('here/meta_type', 8, 21), 481: ('here/listInterfaces', 15, 30), 526: ('here/plugins/listPluginTypeInfo', 16, 23), 643: ('nocall:info/interface', 18, 30), 692: (" python:info['methods'][0", 19, 26), 753: ('e info/', 20, 33), 787: ('le info/ti', 21, 23), 826: ('ves python:here.plugins.listPlugins(interf', 22, 24), 897: ('_ids python:[x[0] for x in act', 23, 23), 952: ('  pau string:${here/plugins/absolute_url}/manage_p', 24, 18), 1033: ('python:here.testImplements(interface)', 25, 23), 1169: ('interface_name', 27, 33), 1207: (" python:here.getId() in act_ids and 'checked' or '", 28, 22), 1328: ('string:${pau}?plugin_type=${info/id}', 31, 32), 1396: ('title/title', 32, 29), 1446: ('method', 33, 31), 1665: ('here/manage_page_footer', 47, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140141462832224 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'submit', 'value': ' Update ', }
_static_140141461301376 = {'href': '', }
_static_140141478698528 = {'type': 'checkbox', 'name': 'interfaces:list', 'value': '', 'checked': "python:here.getId() in act_ids and 'checked' or ''", }
_static_140141462333424 = {'align': 'left', 'valign': 'top', 'class': 'form-label', }
_static_140141462143328 = {'cellspacing': '0', 'cellpadding': '2', 'border': '0', }
_static_140141461847584 = {'type': 'hidden', 'name': 'interfaces:default', 'value': '', }
_static_140141461523088 = {'action': 'manage_activateInterfaces', 'method': 'post', }
_static_140141462115184 = {'class': 'form-help', }
_static_140141462115808 = {'class': 'container-fluid', }
_static_140141533071440 = __C2ZContextWrapper
_static_140141533071728 = __compile_zt_expr
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

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462436160
            __attrs_140141462436160 = _static_140141533420656

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462435056
            __default_140141462435056 = _DEFAULT_MARKER

            # <Value 'here/manage_page_header' (1:27)> -> __cache_140141461895968
            __token = 27
            try:
                __zt_tmp = __attrs_140141462436160
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141461895968 = _static_140141533071728('path', 'here/manage_page_header', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753ac1fa00> -> __condition
            __expression = __cache_140141461895968

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Header</h1>')
            else:
                __content = __cache_140141461895968
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461361232
            __attrs_140141461361232 = _static_140141533420656

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461362624
            __default_140141461362624 = _DEFAULT_MARKER

            # <Value 'here/manage_tabs' (2:27)> -> __cache_140141461360704
            __token = 91
            try:
                __zt_tmp = __attrs_140141461361232
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141461360704 = _static_140141533071728('path', 'here/manage_tabs', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_tabs' (2:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a05d0a0> -> __condition
            __expression = __cache_140141461360704

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2> TABS </h2>')
            else:
                __content = __cache_140141461360704
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f753a1155e0> name=None at 7f753a115e50> -> __attrs_140141462116672
            __attrs_140141462116672 = _static_140141462115808

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n\n')

            # <Static value=<ast.Dict object at 0x7f753a115370> name=None at 7f753a1157c0> -> __attrs_140141461520688
            __attrs_140141461520688 = _static_140141462115184

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="form-help">\n  Choose the functionality this\n  ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461521312
            __attrs_140141461521312 = _static_140141533420656

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461524048
            __default_140141461524048 = _DEFAULT_MARKER

            # <Value 'here/meta_type' (8:21)> -> __cache_140141461520880
            __token = 229
            try:
                __zt_tmp = __attrs_140141461521312
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141461520880 = _static_140141533071728('path', 'here/meta_type', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/meta_type' (8:21)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a084610> -> __condition
            __expression = __cache_140141461520880

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span> Foo Plugin </span>')
            else:
                __content = __cache_140141461520880
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n  will perform.\n</p>\n\n')

            # <Static value=<ast.Dict object at 0x7f753a084a90> name=None at 7f753a084760> -> __attrs_140141461847632
            __attrs_140141461847632 = _static_140141461523088

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form action="manage_activateInterfaces" method="post">\n')

            # <Static value=<ast.Dict object at 0x7f753a0d3e20> name=None at 7f753a0d3190> -> __attrs_140141461846624
            __attrs_140141461846624 = _static_140141461847584

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="interfaces:default" value=""/>\n')

            # <Static value=<ast.Dict object at 0x7f753a11c160> name=None at 7f753a11c430> -> __attrs_140141462333040
            __attrs_140141462333040 = _static_140141462143328
            __backup_interfaces_140141461296128 = get('interfaces', __marker)

            # <Value 'here/listInterfaces' (15:30)> -> __value
            __token = 481
            try:
                __zt_tmp = __attrs_140141462333040
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('path', 'here/listInterfaces', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['interfaces'] = __value

            # <table ... (0:0)
            # --------------------------------------------------------
            __append('<table cellspacing="0" cellpadding="2" border="0">\n  ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462332272
            __attrs_140141462332272 = _static_140141533420656
            __backup_info_140141452420864 = get('info', __marker)

            # <Value 'here/plugins/listPluginTypeInfo' (16:23)> -> __iterator
            __token = 526
            try:
                __zt_tmp = __attrs_140141462332272
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140141533071728('path', 'here/plugins/listPluginTypeInfo', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            (__iterator, ____index_140141462332944, ) = getname('repeat')('info', __iterator)
            econtext['info'] = None
            for __item in __iterator:
                econtext['info'] = __item

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x7f753a14a7f0> name=None at 7f7542569760> -> __attrs_140141525066176
                __attrs_140141525066176 = _static_140141462333424
                __backup_interface_140141472844192 = get('interface', __marker)

                # <Value 'nocall:info/interface' (18:30)> -> __value
                __token = 643
                try:
                    __zt_tmp = __attrs_140141525066176
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('nocall', 'info/interface', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['interface'] = __value
                __backup_method_140141462105584 = get('method', __marker)

                # <Value "python:info['methods'][0]" (19:26)> -> __value
                __token = 692
                try:
                    __zt_tmp = __attrs_140141525066176
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', "info['methods'][0]", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['method'] = __value
                __backup_interface_name_140141461311392 = get('interface_name', __marker)

                # <Value 'info/id' (20:33)> -> __value
                __token = 753
                try:
                    __zt_tmp = __attrs_140141525066176
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'info/id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['interface_name'] = __value
                __backup_title_140141461310528 = get('title', __marker)

                # <Value 'info/title' (21:23)> -> __value
                __token = 787
                try:
                    __zt_tmp = __attrs_140141525066176
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'info/title', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['title'] = __value
                __backup_actives_140141462322192 = get('actives', __marker)

                # <Value 'python:here.plugins.listPlugins(interface)' (22:24)> -> __value
                __token = 826
                try:
                    __zt_tmp = __attrs_140141525066176
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', 'here.plugins.listPlugins(interface)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['actives'] = __value
                __backup_act_ids_140141461307936 = get('act_ids', __marker)

                # <Value 'python:[x[0] for x in actives]' (23:23)> -> __value
                __token = 897
                try:
                    __zt_tmp = __attrs_140141525066176
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', '[x[0] for x in actives]', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['act_ids'] = __value
                __backup_pau_140141452420768 = get('pau', __marker)

                # <Value 'string:${here/plugins/absolute_url}/manage_plugins' (24:18)> -> __value
                __token = 952
                try:
                    __zt_tmp = __attrs_140141525066176
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('string', '${here/plugins/absolute_url}/manage_plugins', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['pau'] = __value

                # <Value 'python:here.testImplements(interface)' (25:23)> -> __condition
                __token = 1033
                try:
                    __zt_tmp = __attrs_140141525066176
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('python', 'here.testImplements(interface)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td align="left" valign="top" class="form-label">\n        ')

                    # <Static value=<ast.Dict object at 0x7f753b0e5e20> name=None at 7f753b0e5940> -> __attrs_140141461301088
                    __attrs_140141461301088 = _static_140141478698528

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" name="interfaces:list"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461301232
                    __default_140141461301232 = _DEFAULT_MARKER

                    # <Substitution 'interface_name' (27:33)> -> __attr_value
                    __token = 1169
                    try:
                        __zt_tmp = __attrs_140141461301088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'interface_name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461302144
                    __default_140141461302144 = _DEFAULT_MARKER

                    # <Boolean "python:here.getId() in act_ids and 'checked' or ''" (28:22)> -> __attr_checked
                    __token = 1207
                    try:
                        __zt_tmp = __attrs_140141461301088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_140141533071728('python', "here.getId() in act_ids and 'checked' or ''", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' />&nbsp;\n        ')

                    # <Static value=<ast.Dict object at 0x7f753a04e880> name=None at 7f753a04e5b0> -> __attrs_140141461299264
                    __attrs_140141461299264 = _static_140141461301376

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461299840
                    __default_140141461299840 = _DEFAULT_MARKER

                    # <Substitution 'string:${pau}?plugin_type=${info/id}' (31:32)> -> __attr_href
                    __token = 1328
                    try:
                        __zt_tmp = __attrs_140141461299264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140141533071728('string', '${pau}?plugin_type=${info/id}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>\n          ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141452459792
                    __attrs_140141452459792 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141452459456
                    __default_140141452459456 = _DEFAULT_MARKER

                    # <Value 'title/title' (32:29)> -> __cache_140141452458736
                    __token = 1396
                    try:
                        __zt_tmp = __attrs_140141452459792
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141452458736 = _static_140141533071728('path', 'title/title', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'title/title' (32:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f75397df220> -> __condition
                    __expression = __cache_140141452458736

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span/>')
                    else:
                        __content = __cache_140141452458736
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n        ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141452457536
                    __attrs_140141452457536 = _static_140141533420656

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i>(')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141452459360
                    __attrs_140141452459360 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141452458640
                    __default_140141452458640 = _DEFAULT_MARKER

                    # <Value 'method' (33:31)> -> __cache_140141452457584
                    __token = 1446
                    try:
                        __zt_tmp = __attrs_140141452459360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141452457584 = _static_140141533071728('path', 'method', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'method' (33:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f75397df430> -> __condition
                    __expression = __cache_140141452457584

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span/>')
                    else:
                        __content = __cache_140141452457584
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(')</i>\n    </td>')
                if (__backup_pau_140141452420768 is __marker):
                    del econtext['pau']
                else:
                    econtext['pau'] = __backup_pau_140141452420768
                if (__backup_act_ids_140141461307936 is __marker):
                    del econtext['act_ids']
                else:
                    econtext['act_ids'] = __backup_act_ids_140141461307936
                if (__backup_actives_140141462322192 is __marker):
                    del econtext['actives']
                else:
                    econtext['actives'] = __backup_actives_140141462322192
                if (__backup_title_140141461310528 is __marker):
                    del econtext['title']
                else:
                    econtext['title'] = __backup_title_140141461310528
                if (__backup_interface_name_140141461311392 is __marker):
                    del econtext['interface_name']
                else:
                    econtext['interface_name'] = __backup_interface_name_140141461311392
                if (__backup_method_140141462105584 is __marker):
                    del econtext['method']
                else:
                    econtext['method'] = __backup_method_140141462105584
                if (__backup_interface_140141472844192 is __marker):
                    del econtext['interface']
                else:
                    econtext['interface'] = __backup_interface_140141472844192
                __append('\n  </tr>')
                ____index_140141462332944 -= 1
                if (____index_140141462332944 > 0):
                    __append('\n  ')
            if (__backup_info_140141452420864 is __marker):
                del econtext['info']
            else:
                econtext['info'] = __backup_info_140141452420864
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141452457488
            __attrs_140141452457488 = _static_140141533420656

            # <tr ... (0:0)
            # --------------------------------------------------------
            __append('<tr>\n    ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141471598912
            __attrs_140141471598912 = _static_140141533420656

            # <td ... (0:0)
            # --------------------------------------------------------
            __append('<td>\n      ')

            # <Static value=<ast.Dict object at 0x7f753a1c4460> name=None at 7f753a1c4bb0> -> __attrs_140141471598384
            __attrs_140141471598384 = _static_140141462832224

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="btn btn-primary" type="submit" name="submit" value=" Update " />\n    </td>\n  </tr>\n</table>')
            if (__backup_interfaces_140141461296128 is __marker):
                del econtext['interfaces']
            else:
                econtext['interfaces'] = __backup_interfaces_140141461296128
            __append('\n</form>\n\n</main>\n\n')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462853376
            __attrs_140141462853376 = _static_140141533420656

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462854096
            __default_140141462854096 = _DEFAULT_MARKER

            # <Value 'here/manage_page_footer' (47:27)> -> __cache_140141462854864
            __token = 1665
            try:
                __zt_tmp = __attrs_140141462853376
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462854864 = _static_140141533071728('path', 'here/manage_page_footer', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_footer' (47:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1c9b80> -> __condition
            __expression = __cache_140141462854864

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Footer</h1>')
            else:
                __content = __cache_140141462854864
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }