# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.portlets-5.0.7-py3.9.egg/plone/app/portlets/browser/templates/edit-manager-macros.pt'

__tokens = {178: ('view/addable_portlets', 9, 19), 234: ('portlets', 11, 23), 286: ('view/context_url', 13, 17), 417: ('view/referer', 20, 19), 708: ('python: view.context_url()', 33, 31), 809: ("python:request['ACTUAL_URL'].replace(view.context_url(), '')", 37, 22), 1040: ('portlets', 43, 35), 1152: ('string:${portlet/addview}', 46, 24), 1080: ('portlet/title', 44, 29), 1614: ('view/portlets', 68, 16), 1685: ('portlets', 73, 21), 1822: ('portlets', 79, 29), 1885: ("python:not portlet['visible'] and 'blockedPortlet' or ''", 81, 30), 1967: (' context/@@authenticator/authenticato', 82, 24), 2061: ('string:managedPortlet card mb-3 ${hiddenPortletClass}', 85, 17), 2143: (' portlet/has', 86, 27), 2181: ('e view/view_na', 87, 23), 2364: ('not:portlet/editview', 94, 25), 2432: ('string:${portlet/editview}?referer=${view/url_quote_referer}', 96, 18), 2324: ('portlet/title', 93, 24), 2685: ('not:repeat/portlet/start', 105, 29), 2765: ('portlet/up_url', 107, 23), 2929: ('view/url_quote_referer', 113, 25), 3103: ('view/key', 119, 25), 3264: ('portlet/name', 125, 25), 3433: ('view/view_name', 131, 25), 3520: ('authenticator', 134, 39), 3728: ('string:${portlet/name}-up', 139, 25), 3961: ('not:repeat/portlet/end', 147, 29), 4039: ('portlet/down_url', 149, 23), 4205: ('view/url_quote_referer', 155, 25), 4379: ('view/key', 161, 25), 4540: ('portlet/name', 167, 25), 4709: ('view/view_name', 173, 25), 4796: ('authenticator', 176, 39), 5006: ('string:${portlet/name}-down', 181, 25), 5236: ('not: portlet/visible', 189, 29), 5312: ('portlet/show_url', 191, 23), 5478: ('view/url_quote_referer', 197, 25), 5652: ('view/key', 203, 25), 5813: ('portlet/name', 209, 25), 5982: ('view/view_name', 215, 25), 6069: ('authenticator', 218, 39), 6243: ('string:${portlet/name}-show', 222, 25), 6479: ('portlet/visible', 230, 29), 6550: ('portlet/hide_url', 232, 23), 6716: ('view/url_quote_referer', 238, 25), 6890: ('view/key', 244, 25), 7051: ('portlet/name', 250, 25), 7220: ('view/view_name', 256, 25), 7307: ('authenticator', 259, 39), 7481: ('string:${portlet/name}-hide', 263, 25), 7749: ('portlet/delete_url', 272, 23), 7917: ('view/url_quote_referer', 278, 25), 8091: ('view/key', 284, 25), 8252: ('portlet/name', 290, 25), 8421: ('view/view_name', 296, 25), 8508: ('authenticator', 299, 39), 8715: ('string:${portlet/name}-remove', 304, 25)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140141462666688 = {'class': 'btn btn-outline-secondary btn-sm', 'title': 'Remove', 'type': 'submit', 'name': 'string:${portlet/name}-remove', }
_static_140141462227888 = {'name': 'viewname', 'type': 'hidden', 'value': 'view/view_name', }
_static_140141462334288 = {'name': 'name', 'type': 'hidden', 'value': 'portlet/name', }
_static_140141462333520 = {'name': 'key', 'type': 'hidden', 'value': 'view/key', }
_static_140141462701488 = {'name': 'referer', 'type': 'hidden', 'value': 'view/url_quote_referer', }
_static_140141462701344 = {'class': 'portlet-action delete', 'method': 'POST', 'action': 'portlet/delete_url', }
_static_140141471598960 = {'class': 'btn btn-outline-secondary btn-sm', 'type': 'submit', 'name': 'string:${portlet/name}-hide', }
_static_140141462777616 = {'name': 'viewname', 'type': 'hidden', 'value': 'view/view_name', }
_static_140141462777520 = {'name': 'name', 'type': 'hidden', 'value': 'portlet/name', }
_static_140141462372160 = {'name': 'key', 'type': 'hidden', 'value': 'view/key', }
_static_140141462371200 = {'name': 'referer', 'type': 'hidden', 'value': 'view/url_quote_referer', }
_static_140141462341904 = {'class': 'portlet-action', 'method': 'POST', 'action': 'portlet/hide_url', }
_static_140141462341280 = {'class': 'btn btn-outline-secondary btn-sm', 'type': 'submit', 'name': 'string:${portlet/name}-show', }
_static_140141462125632 = {'name': 'viewname', 'type': 'hidden', 'value': 'view/view_name', }
_static_140141462126208 = {'name': 'name', 'type': 'hidden', 'value': 'portlet/name', }
_static_140141462320800 = {'name': 'key', 'type': 'hidden', 'value': 'view/key', }
_static_140141462320656 = {'name': 'referer', 'type': 'hidden', 'value': 'view/url_quote_referer', }
_static_140141462637344 = {'class': 'portlet-action', 'method': 'POST', 'action': 'portlet/show_url', }
_static_140141462670112 = {'class': 'btn btn-outline-secondary btn-sm', 'title': 'Move down', 'type': 'submit', 'name': 'string:${portlet/name}-down', }
_static_140141462059184 = {'name': 'viewname', 'type': 'hidden', 'value': 'view/view_name', }
_static_140141462060000 = {'name': 'name', 'type': 'hidden', 'value': 'portlet/name', }
_static_140141462624240 = {'name': 'key', 'type': 'hidden', 'value': 'view/key', }
_static_140141462622800 = {'name': 'referer', 'type': 'hidden', 'value': 'view/url_quote_referer', }
_static_140141462038320 = {'class': 'portlet-action down', 'method': 'POST', 'action': 'portlet/down_url', }
_static_140141462160816 = {'class': 'btn btn-outline-secondary btn-sm', 'title': 'Move up', 'type': 'submit', 'name': 'string:${portlet/name}-up', }
_static_140141462116432 = {'name': 'viewname', 'type': 'hidden', 'value': 'view/view_name', }
_static_140141462115664 = {'name': 'name', 'type': 'hidden', 'value': 'portlet/name', }
_static_140141462803600 = {'name': 'key', 'type': 'hidden', 'value': 'view/key', }
_static_140141462806240 = {'name': 'referer', 'type': 'hidden', 'value': 'view/url_quote_referer', }
_static_140141462061696 = {'class': 'portlet-action up', 'method': 'POST', 'action': 'portlet/up_url', }
_static_140141462064816 = {'class': 'card-body managedPortletActions', }
_static_140141462096624 = {'href': 'string:${portlet/editview}?referer=${view/url_quote_referer}', }
_static_140141462763072 = {'class': 'card-header d-flex align-items-center justify-content-between', }
_static_140141462710688 = {'class': 'string:managedPortlet card mb-3 ${hiddenPortletClass}', 'data-portlethash': 'portlet/hash', 'data-viewname': 'view/view_name', }
_static_140141462629296 = {'class': 'portletAssignment', }
_static_140141462145536 = {'class': 'btn btn-secondary', 'type': 'submit', 'value': 'Add portlet', }
_static_140141462303264 = {'value': 'string:${portlet/addview}', }
_static_140141533420656 = {}
_static_140141462682352 = {'value': "python:request['ACTUAL_URL'].replace(view.context_url(), '')", }
_static_140141462794400 = {'class': 'add-portlet form-select', 'name': ':action', 'data-context-url': 'python: view.context_url()', }
_static_140141462796752 = {'class': 'hiddenStructure', }
_static_140141462759600 = {'name': 'referer', 'type': 'hidden', 'value': 'view/referer', }
_static_140141533071440 = __C2ZContextWrapper
_static_140141533071728 = __compile_zt_expr
_static_140141462688912 = {'action': '#', 'method': 'post', }
_static_140141462689872 = {'class': 'section mb-4', }

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

    def render_portlet_add_form(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f753a1a1850> name=None at 7f753a1a17c0> -> __attrs_140141462688960
            __attrs_140141462688960 = _static_140141462689872
            __previous_i18n_domain_140141462689776 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="section mb-4" >\n\n  ')

            # <Static value=<ast.Dict object at 0x7f753a1a1490> name=None at 7f753a1a16d0> -> __attrs_140141462677104
            __attrs_140141462677104 = _static_140141462688912
            __backup_portlets_140141462144960 = get('portlets', __marker)

            # <Value 'view/addable_portlets' (9:19)> -> __value
            __token = 178
            try:
                __zt_tmp = __attrs_140141462677104
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('path', 'view/addable_portlets', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['portlets'] = __value

            # <Value 'portlets' (11:23)> -> __condition
            __token = 234
            try:
                __zt_tmp = __attrs_140141462677104
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140141533071728('path', 'portlets', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            if __condition:

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462691600
                __default_140141462691600 = _DEFAULT_MARKER

                # <Substitution 'view/context_url' (13:17)> -> __attr_action
                __token = 286
                try:
                    __zt_tmp = __attrs_140141462677104
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_140141533071728('path', 'view/context_url', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', '#', _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append(' method="post" >\n\n    ')

                # <Static value=<ast.Dict object at 0x7f753a1b28b0> name=None at 7f753a1b2bb0> -> __attrs_140141462794880
                __attrs_140141462794880 = _static_140141462759600

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input name="referer" type="hidden"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462759456
                __default_140141462759456 = _DEFAULT_MARKER

                # <Substitution 'view/referer' (20:19)> -> __attr_value
                __token = 417
                try:
                    __zt_tmp = __attrs_140141462794880
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'view/referer', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n\n    ')

                # <Static value=<ast.Dict object at 0x7f753a1bb9d0> name=None at 7f753a1bb640> -> __attrs_140141462797952
                __attrs_140141462797952 = _static_140141462796752

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="hiddenStructure" >')
                __stream_140141462798240 = []
                __append_140141462798240 = __stream_140141462798240.append
                __append_140141462798240('\n            Add portlet\n    ')
                __msgid_140141462798240 = __re_whitespace(''.join(__stream_140141462798240)).strip()
                if 'label_add_portlet':
                    __append(translate('label_add_portlet', mapping=None, default=__msgid_140141462798240, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f753a1bb0a0> name=None at 7f753a1bb4f0> -> __attrs_140141462794352
                __attrs_140141462794352 = _static_140141462794400

                # <select ... (0:0)
                # --------------------------------------------------------
                __append('<select class="add-portlet form-select" name=":action"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462794496
                __default_140141462794496 = _DEFAULT_MARKER

                # <Substitution 'python: view.context_url()' (33:31)> -> __attr_data_context_url
                __token = 708
                try:
                    __zt_tmp = __attrs_140141462794352
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_context_url = _static_140141533071728('python', ' view.context_url()', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_data_context_url = __quote(__attr_data_context_url, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_context_url is not None):
                    __append((' data-context-url="%s"' % __attr_data_context_url))
                __append(' >\n      ')

                # <Static value=<ast.Dict object at 0x7f753a19faf0> name=None at 7f753a19f610> -> __attrs_140141462304752
                __attrs_140141462304752 = _static_140141462682352

                # <option ... (0:0)
                # --------------------------------------------------------
                __append('<option')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462680048
                __default_140141462680048 = _DEFAULT_MARKER

                # <Substitution "python:request['ACTUAL_URL'].replace(view.context_url(), '')" (37:22)> -> __attr_value
                __token = 809
                try:
                    __zt_tmp = __attrs_140141462304752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('python', "request['ACTUAL_URL'].replace(view.context_url(), '')", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' >')
                __stream_140141462683600 = []
                __append_140141462683600 = __stream_140141462683600.append
                __append_140141462683600('\n                Add portlet&hellip;\n      ')
                __msgid_140141462683600 = __re_whitespace(''.join(__stream_140141462683600)).strip()
                if 'label_add_portlet_ellipsis':
                    __append(translate('label_add_portlet_ellipsis', mapping=None, default=__msgid_140141462683600, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</option>\n      ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462306192
                __attrs_140141462306192 = _static_140141533420656
                __backup_portlet_140141462414912 = get('portlet', __marker)

                # <Value 'portlets' (43:35)> -> __iterator
                __token = 1040
                try:
                    __zt_tmp = __attrs_140141462306192
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140141533071728('path', 'portlets', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                (__iterator, ____index_140141462305712, ) = getname('repeat')('portlet', __iterator)
                econtext['portlet'] = None
                for __item in __iterator:
                    econtext['portlet'] = __item
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x7f753a143220> name=None at 7f753a143c10> -> __attrs_140141462303552
                    __attrs_140141462303552 = _static_140141462303264

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462303888
                    __default_140141462303888 = _DEFAULT_MARKER

                    # <Substitution 'string:${portlet/addview}' (46:24)> -> __attr_value
                    __token = 1152
                    try:
                        __zt_tmp = __attrs_140141462303552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('string', '${portlet/addview}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' >')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462304512
                    __default_140141462304512 = _DEFAULT_MARKER

                    # <Value 'portlet/title' (44:29)> -> __cache_140141462303072
                    __token = 1080
                    try:
                        __zt_tmp = __attrs_140141462303552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141462303072 = _static_140141533071728('path', 'portlet/title', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'portlet/title' (44:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a143dc0> -> __condition
                    __expression = __cache_140141462303072

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140141462303072
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>\n      ')
                    ____index_140141462305712 -= 1
                    if (____index_140141462305712 > 0):
                        __append('')
                if (__backup_portlet_140141462414912 is __marker):
                    del econtext['portlet']
                else:
                    econtext['portlet'] = __backup_portlet_140141462414912
                __append('\n\n    </select>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462302976
                __attrs_140141462302976 = _static_140141533420656

                # <noscript ... (0:0)
                # --------------------------------------------------------
                __append('<noscript>\n      ')

                # <Static value=<ast.Dict object at 0x7f753a11ca00> name=None at 7f753a11c160> -> __attrs_140141462628000
                __attrs_140141462628000 = _static_140141462145536

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="btn btn-secondary" type="submit"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462626416
                __default_140141462626416 = _DEFAULT_MARKER

                # <Translate msgid='label_add_portlet' node=<ast.Constant object at 0x7f753a192490> at 7f753a192310> -> __attr_value
                __attr_value = 'Add portlet'
                __attr_value = translate('label_add_portlet', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n    </noscript>\n\n  </form>')
            if (__backup_portlets_140141462144960 is __marker):
                del econtext['portlets']
            else:
                econtext['portlets'] = __backup_portlets_140141462144960
            __append('\n</div>')
            __i18n_domain = __previous_i18n_domain_140141462689776
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_current_portlets_list(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f753a192bb0> name=None at 7f753a11c940> -> __attrs_140141462627376
            __attrs_140141462627376 = _static_140141462629296
            __backup_portlets_140141462635952 = get('portlets', __marker)

            # <Value 'view/portlets' (68:16)> -> __value
            __token = 1614
            try:
                __zt_tmp = __attrs_140141462627376
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('path', 'view/portlets', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['portlets'] = __value
            __previous_i18n_domain_140141462627904 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="portletAssignment" >\n\n  ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462627184
            __attrs_140141462627184 = _static_140141533420656

            # <Value 'portlets' (73:21)> -> __condition
            __token = 1685
            try:
                __zt_tmp = __attrs_140141462627184
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140141533071728('path', 'portlets', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            if __condition:

                # <h5 ... (0:0)
                # --------------------------------------------------------
                __append('<h5 >')
                __stream_140141462627952 = []
                __append_140141462627952 = __stream_140141462627952.append
                __append_140141462627952('\n        Portlets assigned here\n  ')
                __msgid_140141462627952 = __re_whitespace(''.join(__stream_140141462627952)).strip()
                if 'heading_portlets_assigned_here':
                    __append(translate('heading_portlets_assigned_here', mapping=None, default=__msgid_140141462627952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h5>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462709728
            __attrs_140141462709728 = _static_140141533420656
            __backup_portlet_140141462635136 = get('portlet', __marker)

            # <Value 'portlets' (79:29)> -> __iterator
            __token = 1822
            try:
                __zt_tmp = __attrs_140141462709728
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140141533071728('path', 'portlets', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            (__iterator, ____index_140141462709008, ) = getname('repeat')('portlet', __iterator)
            econtext['portlet'] = None
            for __item in __iterator:
                econtext['portlet'] = __item
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7f753a1a69a0> name=None at 7f753a1a64f0> -> __attrs_140141462710736
                __attrs_140141462710736 = _static_140141462710688
                __backup_hiddenPortletClass_140141462062464 = get('hiddenPortletClass', __marker)

                # <Value "python:not portlet['visible'] and 'blockedPortlet' or ''" (81:30)> -> __value
                __token = 1885
                try:
                    __zt_tmp = __attrs_140141462710736
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', "not portlet['visible'] and 'blockedPortlet' or ''", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['hiddenPortletClass'] = __value
                __backup_authenticator_140141462144384 = get('authenticator', __marker)

                # <Value 'context/@@authenticator/authenticator' (82:24)> -> __value
                __token = 1967
                try:
                    __zt_tmp = __attrs_140141462710736
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['authenticator'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462709248
                __default_140141462709248 = _DEFAULT_MARKER

                # <Substitution 'string:managedPortlet card mb-3 ${hiddenPortletClass}' (85:17)> -> __attr_class
                __token = 2061
                try:
                    __zt_tmp = __attrs_140141462710736
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_class = _static_140141533071728('string', 'managedPortlet card mb-3 ${hiddenPortletClass}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_class is not None):
                    __append((' class="%s"' % __attr_class))

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462711504
                __default_140141462711504 = _DEFAULT_MARKER

                # <Substitution 'portlet/hash' (86:27)> -> __attr_data_portlethash
                __token = 2143
                try:
                    __zt_tmp = __attrs_140141462710736
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_portlethash = _static_140141533071728('path', 'portlet/hash', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_data_portlethash = __quote(__attr_data_portlethash, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_portlethash is not None):
                    __append((' data-portlethash="%s"' % __attr_data_portlethash))

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462709584
                __default_140141462709584 = _DEFAULT_MARKER

                # <Substitution 'view/view_name' (87:23)> -> __attr_data_viewname
                __token = 2181
                try:
                    __zt_tmp = __attrs_140141462710736
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_viewname = _static_140141533071728('path', 'view/view_name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_data_viewname = __quote(__attr_data_viewname, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_data_viewname is not None):
                    __append((' data-viewname="%s"' % __attr_data_viewname))
                __append(' >\n\n      ')

                # <Static value=<ast.Dict object at 0x7f753a1b3640> name=None at 7f753a1b3940> -> __attrs_140141462296368
                __attrs_140141462296368 = _static_140141462763072

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="card-header d-flex align-items-center justify-content-between">\n\n        ')

                # <Static value=<ast.Dict object at 0x7f753a110af0> name=None at 7f753a110760> -> __attrs_140141462062320
                __attrs_140141462062320 = _static_140141462096624

                # <Negate value=<Value 'not:portlet/editview' (94:25)> at 7f753a1082b0> -> __cache_140141462061744

                # <Value 'not:portlet/editview' (94:25)> -> __cache_140141462061744
                __token = 2364
                try:
                    __zt_tmp = __attrs_140141462062320
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140141462061744 = _static_140141533071728('not', 'portlet/editview', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __cache_140141462061744 = not __cache_140141462061744
                __condition = __cache_140141462061744
                if __condition:

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462061120
                    __default_140141462061120 = _DEFAULT_MARKER

                    # <Substitution 'string:${portlet/editview}?referer=${view/url_quote_referer}' (96:18)> -> __attr_href
                    __token = 2432
                    try:
                        __zt_tmp = __attrs_140141462062320
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140141533071728('string', '${portlet/editview}?referer=${view/url_quote_referer}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' >')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462097728
                __default_140141462097728 = _DEFAULT_MARKER

                # <Value 'portlet/title' (93:24)> -> __cache_140141462297856
                __token = 2324
                try:
                    __zt_tmp = __attrs_140141462062320
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140141462297856 = _static_140141533071728('path', 'portlet/title', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                # <BinOp left=<Value 'portlet/title' (93:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a141cd0> -> __condition
                __expression = __cache_140141462297856

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140141462297856
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __condition = __cache_140141462061744
                if __condition:
                    __append('</a>')
                __append('\n      </div>\n\n      ')

                # <Static value=<ast.Dict object at 0x7f753a108eb0> name=None at 7f753a1088e0> -> __attrs_140141462061792
                __attrs_140141462061792 = _static_140141462064816

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="card-body managedPortletActions">\n\n        ')

                # <Static value=<ast.Dict object at 0x7f753a108280> name=None at 7f753a108e50> -> __attrs_140141462806288
                __attrs_140141462806288 = _static_140141462061696

                # <Value 'not:repeat/portlet/start' (105:29)> -> __condition
                __token = 2685
                try:
                    __zt_tmp = __attrs_140141462806288
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('not', 'repeat/portlet/start', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form class="portlet-action up" method="POST"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462063568
                    __default_140141462063568 = _DEFAULT_MARKER

                    # <Substitution 'portlet/up_url' (107:23)> -> __attr_action
                    __token = 2765
                    try:
                        __zt_tmp = __attrs_140141462806288
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140141533071728('path', 'portlet/up_url', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append(' >\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a1bdee0> name=None at 7f753a1bd040> -> __attrs_140141462806192
                    __attrs_140141462806192 = _static_140141462806240

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="referer" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462805376
                    __default_140141462805376 = _DEFAULT_MARKER

                    # <Substitution 'view/url_quote_referer' (113:25)> -> __attr_value
                    __token = 2929
                    try:
                        __zt_tmp = __attrs_140141462806192
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'view/url_quote_referer', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a1bd490> name=None at 7f753a1bde50> -> __attrs_140141462117152
                    __attrs_140141462117152 = _static_140141462803600

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="key" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462114608
                    __default_140141462114608 = _DEFAULT_MARKER

                    # <Substitution 'view/key' (119:25)> -> __attr_value
                    __token = 3103
                    try:
                        __zt_tmp = __attrs_140141462117152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'view/key', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a115550> name=None at 7f753a115eb0> -> __attrs_140141462115088
                    __attrs_140141462115088 = _static_140141462115664

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="name" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462115376
                    __default_140141462115376 = _DEFAULT_MARKER

                    # <Substitution 'portlet/name' (125:25)> -> __attr_value
                    __token = 3264
                    try:
                        __zt_tmp = __attrs_140141462115088
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'portlet/name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a115850> name=None at 7f753a115910> -> __attrs_140141462162688
                    __attrs_140141462162688 = _static_140141462116432

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="viewname" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462161248
                    __default_140141462161248 = _DEFAULT_MARKER

                    # <Substitution 'view/view_name' (131:25)> -> __attr_value
                    __token = 3433
                    try:
                        __zt_tmp = __attrs_140141462162688
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'view/view_name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462163264
                    __attrs_140141462163264 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462161200
                    __default_140141462161200 = _DEFAULT_MARKER

                    # <Value 'authenticator' (134:39)> -> __cache_140141462159712
                    __token = 3520
                    try:
                        __zt_tmp = __attrs_140141462163264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141462159712 = _static_140141533071728('path', 'authenticator', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'authenticator' (134:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1203d0> -> __condition
                    __expression = __cache_140141462159712

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span></span>')
                    else:
                        __content = __cache_140141462159712
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a1205b0> name=None at 7f753a120400> -> __attrs_140141462039616
                    __attrs_140141462039616 = _static_140141462160816

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-outline-secondary btn-sm"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462159664
                    __default_140141462159664 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x7f753a1207c0> at 7f753a1206a0> -> __attr_title
                    __attr_title = 'Move up'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' type="submit"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462038560
                    __default_140141462038560 = _DEFAULT_MARKER

                    # <Substitution 'string:${portlet/name}-up' (139:25)> -> __attr_name
                    __token = 3728
                    try:
                        __zt_tmp = __attrs_140141462039616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140141533071728('string', '${portlet/name}-up', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((' name="%s"' % __attr_name))
                    __append(' >&#9650;</button>\n        </form>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f753a102730> name=None at 7f753a102a00> -> __attrs_140141462037312
                __attrs_140141462037312 = _static_140141462038320

                # <Value 'not:repeat/portlet/end' (147:29)> -> __condition
                __token = 3961
                try:
                    __zt_tmp = __attrs_140141462037312
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('not', 'repeat/portlet/end', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form class="portlet-action down" method="POST"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462040000
                    __default_140141462040000 = _DEFAULT_MARKER

                    # <Substitution 'portlet/down_url' (149:23)> -> __attr_action
                    __token = 4039
                    try:
                        __zt_tmp = __attrs_140141462037312
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140141533071728('path', 'portlet/down_url', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append(' >\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a191250> name=None at 7f753a1918b0> -> __attrs_140141462625824
                    __attrs_140141462625824 = _static_140141462622800

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="referer" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462624864
                    __default_140141462624864 = _DEFAULT_MARKER

                    # <Substitution 'view/url_quote_referer' (155:25)> -> __attr_value
                    __token = 4205
                    try:
                        __zt_tmp = __attrs_140141462625824
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'view/url_quote_referer', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a1917f0> name=None at 7f753a191be0> -> __attrs_140141462058176
                    __attrs_140141462058176 = _static_140141462624240

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="key" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462625488
                    __default_140141462625488 = _DEFAULT_MARKER

                    # <Substitution 'view/key' (161:25)> -> __attr_value
                    __token = 4379
                    try:
                        __zt_tmp = __attrs_140141462058176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'view/key', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a107be0> name=None at 7f753a107a00> -> __attrs_140141462058512
                    __attrs_140141462058512 = _static_140141462060000

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="name" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462057552
                    __default_140141462057552 = _DEFAULT_MARKER

                    # <Substitution 'portlet/name' (167:25)> -> __attr_value
                    __token = 4540
                    try:
                        __zt_tmp = __attrs_140141462058512
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'portlet/name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a1078b0> name=None at 7f753a107d60> -> __attrs_140141462060864
                    __attrs_140141462060864 = _static_140141462059184

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="viewname" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462057168
                    __default_140141462057168 = _DEFAULT_MARKER

                    # <Substitution 'view/view_name' (173:25)> -> __attr_value
                    __token = 4709
                    try:
                        __zt_tmp = __attrs_140141462060864
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'view/view_name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462669392
                    __attrs_140141462669392 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462669536
                    __default_140141462669536 = _DEFAULT_MARKER

                    # <Value 'authenticator' (176:39)> -> __cache_140141462667808
                    __token = 4796
                    try:
                        __zt_tmp = __attrs_140141462669392
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141462667808 = _static_140141533071728('path', 'authenticator', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'authenticator' (176:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a19cfd0> -> __condition
                    __expression = __cache_140141462667808

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span></span>')
                    else:
                        __content = __cache_140141462667808
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a19cb20> name=None at 7f753a19cc70> -> __attrs_140141462637680
                    __attrs_140141462637680 = _static_140141462670112

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-outline-secondary btn-sm"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462669584
                    __default_140141462669584 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x7f753a19c4f0> at 7f753a19c6a0> -> __attr_title
                    __attr_title = 'Move down'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' type="submit"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462637536
                    __default_140141462637536 = _DEFAULT_MARKER

                    # <Substitution 'string:${portlet/name}-down' (181:25)> -> __attr_name
                    __token = 5006
                    try:
                        __zt_tmp = __attrs_140141462637680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140141533071728('string', '${portlet/name}-down', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((' name="%s"' % __attr_name))
                    __append(' >&#9660;</button>\n        </form>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f753a194b20> name=None at 7f753a194340> -> __attrs_140141462637872
                __attrs_140141462637872 = _static_140141462637344

                # <Value 'not: portlet/visible' (189:29)> -> __condition
                __token = 5236
                try:
                    __zt_tmp = __attrs_140141462637872
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('not', ' portlet/visible', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form class="portlet-action" method="POST"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462635520
                    __default_140141462635520 = _DEFAULT_MARKER

                    # <Substitution 'portlet/show_url' (191:23)> -> __attr_action
                    __token = 5312
                    try:
                        __zt_tmp = __attrs_140141462637872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140141533071728('path', 'portlet/show_url', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append(' >\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a147610> name=None at 7f753a147520> -> __attrs_140141462319552
                    __attrs_140141462319552 = _static_140141462320656

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="referer" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462319840
                    __default_140141462319840 = _DEFAULT_MARKER

                    # <Substitution 'view/url_quote_referer' (197:25)> -> __attr_value
                    __token = 5478
                    try:
                        __zt_tmp = __attrs_140141462319552
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'view/url_quote_referer', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a1476a0> name=None at 7f753a147700> -> __attrs_140141462123952
                    __attrs_140141462123952 = _static_140141462320800

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="key" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462320464
                    __default_140141462320464 = _DEFAULT_MARKER

                    # <Substitution 'view/key' (203:25)> -> __attr_value
                    __token = 5652
                    try:
                        __zt_tmp = __attrs_140141462123952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'view/key', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a117e80> name=None at 7f753a117ee0> -> __attrs_140141462123472
                    __attrs_140141462123472 = _static_140141462126208

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="name" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462125056
                    __default_140141462125056 = _DEFAULT_MARKER

                    # <Substitution 'portlet/name' (209:25)> -> __attr_value
                    __token = 5813
                    try:
                        __zt_tmp = __attrs_140141462123472
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'portlet/name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a117c40> name=None at 7f753a117190> -> __attrs_140141462125152
                    __attrs_140141462125152 = _static_140141462125632

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="viewname" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462124528
                    __default_140141462124528 = _DEFAULT_MARKER

                    # <Substitution 'view/view_name' (215:25)> -> __attr_value
                    __token = 5982
                    try:
                        __zt_tmp = __attrs_140141462125152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'view/view_name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462435680
                    __attrs_140141462435680 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462436976
                    __default_140141462436976 = _DEFAULT_MARKER

                    # <Value 'authenticator' (218:39)> -> __cache_140141462435728
                    __token = 6069
                    try:
                        __zt_tmp = __attrs_140141462435680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141462435728 = _static_140141533071728('path', 'authenticator', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'authenticator' (218:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a163310> -> __condition
                    __expression = __cache_140141462435728

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span></span>')
                    else:
                        __content = __cache_140141462435728
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a14c6a0> name=None at 7f753a14cd00> -> __attrs_140141462343344
                    __attrs_140141462343344 = _static_140141462341280

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-outline-secondary btn-sm" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462341856
                    __default_140141462341856 = _DEFAULT_MARKER

                    # <Substitution 'string:${portlet/name}-show' (222:25)> -> __attr_name
                    __token = 6243
                    try:
                        __zt_tmp = __attrs_140141462343344
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140141533071728('string', '${portlet/name}-show', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((' name="%s"' % __attr_name))
                    __append(' >')
                    __stream_140141462435632 = []
                    __append_140141462435632 = __stream_140141462435632.append
                    __append_140141462435632('Show')
                    __msgid_140141462435632 = __re_whitespace(''.join(__stream_140141462435632)).strip()
                    if 'label_show_item':
                        __append(translate('label_show_item', mapping=None, default=__msgid_140141462435632, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n        </form>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f753a14c910> name=None at 7f753a14c070> -> __attrs_140141462343104
                __attrs_140141462343104 = _static_140141462341904

                # <Value 'portlet/visible' (230:29)> -> __condition
                __token = 6479
                try:
                    __zt_tmp = __attrs_140141462343104
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('path', 'portlet/visible', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <form ... (0:0)
                    # --------------------------------------------------------
                    __append('<form class="portlet-action" method="POST"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462342864
                    __default_140141462342864 = _DEFAULT_MARKER

                    # <Substitution 'portlet/hide_url' (232:23)> -> __attr_action
                    __token = 6550
                    try:
                        __zt_tmp = __attrs_140141462343104
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_action = _static_140141533071728('path', 'portlet/hide_url', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_action is not None):
                        __append((' action="%s"' % __attr_action))
                    __append(' >\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a153b80> name=None at 7f753a153e20> -> __attrs_140141462372304
                    __attrs_140141462372304 = _static_140141462371200

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="referer" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462369616
                    __default_140141462369616 = _DEFAULT_MARKER

                    # <Substitution 'view/url_quote_referer' (238:25)> -> __attr_value
                    __token = 6716
                    try:
                        __zt_tmp = __attrs_140141462372304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'view/url_quote_referer', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a153f40> name=None at 7f753a153ca0> -> __attrs_140141462371824
                    __attrs_140141462371824 = _static_140141462372160

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="key" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462368752
                    __default_140141462368752 = _DEFAULT_MARKER

                    # <Substitution 'view/key' (244:25)> -> __attr_value
                    __token = 6890
                    try:
                        __zt_tmp = __attrs_140141462371824
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'view/key', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a1b6eb0> name=None at 7f753a1b6f70> -> __attrs_140141462774544
                    __attrs_140141462774544 = _static_140141462777520

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="name" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462776224
                    __default_140141462776224 = _DEFAULT_MARKER

                    # <Substitution 'portlet/name' (250:25)> -> __attr_value
                    __token = 7051
                    try:
                        __zt_tmp = __attrs_140141462774544
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'portlet/name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a1b6f10> name=None at 7f753a1b6d90> -> __attrs_140141462776848
                    __attrs_140141462776848 = _static_140141462777616

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input name="viewname" type="hidden"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462777376
                    __default_140141462777376 = _DEFAULT_MARKER

                    # <Substitution 'view/view_name' (256:25)> -> __attr_value
                    __token = 7220
                    try:
                        __zt_tmp = __attrs_140141462776848
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'view/view_name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n          ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141471598576
                    __attrs_140141471598576 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141471600208
                    __default_140141471600208 = _DEFAULT_MARKER

                    # <Value 'authenticator' (259:39)> -> __cache_140141471599776
                    __token = 7307
                    try:
                        __zt_tmp = __attrs_140141471598576
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141471599776 = _static_140141533071728('path', 'authenticator', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'authenticator' (259:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753aa201f0> -> __condition
                    __expression = __cache_140141471599776

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span></span>')
                    else:
                        __content = __cache_140141471599776
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f753aa20970> name=None at 7f753aa200d0> -> __attrs_140141462700720
                    __attrs_140141462700720 = _static_140141471598960

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-outline-secondary btn-sm" type="submit"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462702544
                    __default_140141462702544 = _DEFAULT_MARKER

                    # <Substitution 'string:${portlet/name}-hide' (263:25)> -> __attr_name
                    __token = 7481
                    try:
                        __zt_tmp = __attrs_140141462700720
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140141533071728('string', '${portlet/name}-hide', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((' name="%s"' % __attr_name))
                    __append(' >')
                    __stream_140141471596656 = []
                    __append_140141471596656 = __stream_140141471596656.append
                    __append_140141471596656('Hide')
                    __msgid_140141471596656 = __re_whitespace(''.join(__stream_140141471596656)).strip()
                    if 'label_hide_item':
                        __append(translate('label_hide_item', mapping=None, default=__msgid_140141471596656, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n        </form>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f753a1a4520> name=None at 7f753a1a44c0> -> __attrs_140141462703504
                __attrs_140141462703504 = _static_140141462701344

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form class="portlet-action delete" method="POST"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462703648
                __default_140141462703648 = _DEFAULT_MARKER

                # <Substitution 'portlet/delete_url' (272:23)> -> __attr_action
                __token = 7749
                try:
                    __zt_tmp = __attrs_140141462703504
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_140141533071728('path', 'portlet/delete_url', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append(' >\n          ')

                # <Static value=<ast.Dict object at 0x7f753a1a45b0> name=None at 7f753a1a46a0> -> __attrs_140141462334144
                __attrs_140141462334144 = _static_140141462701488

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input name="referer" type="hidden"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462332992
                __default_140141462332992 = _DEFAULT_MARKER

                # <Substitution 'view/url_quote_referer' (278:25)> -> __attr_value
                __token = 7917
                try:
                    __zt_tmp = __attrs_140141462334144
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'view/url_quote_referer', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n          ')

                # <Static value=<ast.Dict object at 0x7f753a14a850> name=None at 7f753a14a250> -> __attrs_140141462335200
                __attrs_140141462335200 = _static_140141462333520

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input name="key" type="hidden"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462335104
                __default_140141462335104 = _DEFAULT_MARKER

                # <Substitution 'view/key' (284:25)> -> __attr_value
                __token = 8091
                try:
                    __zt_tmp = __attrs_140141462335200
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'view/key', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n          ')

                # <Static value=<ast.Dict object at 0x7f753a14ab50> name=None at 7f753a14a040> -> __attrs_140141462226208
                __attrs_140141462226208 = _static_140141462334288

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input name="name" type="hidden"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462226064
                __default_140141462226064 = _DEFAULT_MARKER

                # <Substitution 'portlet/name' (290:25)> -> __attr_value
                __token = 8252
                try:
                    __zt_tmp = __attrs_140141462226208
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'portlet/name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n          ')

                # <Static value=<ast.Dict object at 0x7f753a130bb0> name=None at 7f753a130c70> -> __attrs_140141462228368
                __attrs_140141462228368 = _static_140141462227888

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input name="viewname" type="hidden"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462225824
                __default_140141462225824 = _DEFAULT_MARKER

                # <Substitution 'view/view_name' (296:25)> -> __attr_value
                __token = 8421
                try:
                    __zt_tmp = __attrs_140141462228368
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'view/view_name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n          ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462227840
                __attrs_140141462227840 = _static_140141533420656

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462227120
                __default_140141462227120 = _DEFAULT_MARKER

                # <Value 'authenticator' (299:39)> -> __cache_140141462225488
                __token = 8508
                try:
                    __zt_tmp = __attrs_140141462227840
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140141462225488 = _static_140141533071728('path', 'authenticator', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                # <BinOp left=<Value 'authenticator' (299:39)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1301c0> -> __condition
                __expression = __cache_140141462225488

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span></span>')
                else:
                    __content = __cache_140141462225488
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n          ')

                # <Static value=<ast.Dict object at 0x7f753a19bdc0> name=None at 7f753a19b070> -> __attrs_140141462666544
                __attrs_140141462666544 = _static_140141462666688

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button class="btn btn-outline-secondary btn-sm"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462667072
                __default_140141462667072 = _DEFAULT_MARKER

                # <Translate msgid=None node=<ast.Constant object at 0x7f753a19b640> at 7f753a19bc40> -> __attr_title
                __attr_title = 'Remove'
                __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_title is not None):
                    __append((' title="%s"' % __attr_title))
                __append(' type="submit"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462663952
                __default_140141462663952 = _DEFAULT_MARKER

                # <Substitution 'string:${portlet/name}-remove' (304:25)> -> __attr_name
                __token = 8715
                try:
                    __zt_tmp = __attrs_140141462666544
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140141533071728('string', '${portlet/name}-remove', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))
                __append(' >&times;</button>\n        </form>\n\n      </div>\n\n    </div>')
                if (__backup_authenticator_140141462144384 is __marker):
                    del econtext['authenticator']
                else:
                    econtext['authenticator'] = __backup_authenticator_140141462144384
                if (__backup_hiddenPortletClass_140141462062464 is __marker):
                    del econtext['hiddenPortletClass']
                else:
                    econtext['hiddenPortletClass'] = __backup_hiddenPortletClass_140141462062464
                __append('\n  ')
                ____index_140141462709008 -= 1
                if (____index_140141462709008 > 0):
                    __append('')
            if (__backup_portlet_140141462635136 is __marker):
                del econtext['portlet']
            else:
                econtext['portlet'] = __backup_portlet_140141462635136
            __append('\n</div>')
            __i18n_domain = __previous_i18n_domain_140141462627904
            if (__backup_portlets_140141462635952 is __marker):
                del econtext['portlets']
            else:
                econtext['portlets'] = __backup_portlets_140141462635952
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
            __token = None
            render_portlet_add_form(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n')
            __token = None
            render_current_portlets_list(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_portlet_add_form': render_portlet_add_form, 'render_current_portlets_list': render_current_portlets_list, 'render': render, }