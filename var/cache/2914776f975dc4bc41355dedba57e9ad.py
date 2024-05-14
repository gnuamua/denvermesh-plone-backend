# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/viewlets/document_relateditems.pt'

__tokens = {71: ('view/related_items', 3, 19), 112: (' nocall:context/@@plon', 4, 21), 159: ('t nocall:context/@@plone_layo', 5, 22), 216: ('ng nocall:plone_view/normalizeStr', 6, 24), 275: ('ate nocall:context/@@plone_context_s', 7, 21), 339: ("tion python:context.portal_registry.get('types_use_view_action_in_listings'", 8, 22), 456: ('related', 10, 24), 678: ('related', 21, 30), 767: ('item/Description', 24, 16), 805: (' item/portal_typ', 25, 20), 849: ("s python:'contenttype-' + normalizeString(item_typ", 26, 25), 925: ('te item/review_state|python: context_state.workflow_stat', 27, 22), 1013: ("ass python: 'state-' + normalizeString(item_wf_st", 28, 27), 1083: ('_url item/getURL|item/absolut', 29, 15), 1133: ("m_url python:(item_type in use_view_action) and item_url+'/view' or it", 30, 14), 1230: ('_image python:item.', 31, 19), 1368: ('${item_url}', 37, 19), 1370: ('item_url', 37, 21), 1392: ('${item/pretty_title_or_id}', 38, 11), 1394: ('item/pretty_title_or_id', 38, 13), 1444: ('${item/Description}', 39, 15), 1446: ('item/Description', 39, 17), 1573: ("python:item.getURL() +'/@@images/image/thumb'", 45, 21), 1659: ('item_has_image', 47, 26), 1720: ('string:$getIcon', 49, 17), 1753: (' item/Descriptio', 50, 16)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355459712720 = {'class': 'ms-3', 'src': '', 'alt': 'item/Description', }
_static_140355459713872 = {'class': 'h6 stretched-link', 'href': '${item_url}', }
_static_140355482647904 = {'class': 'media-body', }
_static_140355448477104 = {'class': 'media position-relative', }
_static_140355540704128 = {}
_static_140355459860368 = {'class': 'section-heading', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355449082400 = {'id': 'section-related', }

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

            # <Static value=<ast.Dict object at 0x7fa70caf5220> name=None at 7fa70caf57f0> -> __attrs_140355459857376
            __attrs_140355459857376 = _static_140355449082400
            __backup_related_140355448959376 = get('related', __marker)

            # <Value 'view/related_items' (3:19)> -> __value
            __token = 71
            try:
                __zt_tmp = __attrs_140355459857376
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/related_items', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['related'] = __value
            __backup_plone_view_140355448653568 = get('plone_view', __marker)

            # <Value 'nocall:context/@@plone' (4:21)> -> __value
            __token = 112
            try:
                __zt_tmp = __attrs_140355459857376
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('nocall', 'context/@@plone', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_plone_layout_140355448673616 = get('plone_layout', __marker)

            # <Value 'nocall:context/@@plone_layout' (5:22)> -> __value
            __token = 159
            try:
                __zt_tmp = __attrs_140355459857376
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('nocall', 'context/@@plone_layout', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['plone_layout'] = __value
            __backup_normalizeString_140355448504224 = get('normalizeString', __marker)

            # <Value 'nocall:plone_view/normalizeString' (6:24)> -> __value
            __token = 216
            try:
                __zt_tmp = __attrs_140355459857376
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('nocall', 'plone_view/normalizeString', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['normalizeString'] = __value
            __backup_context_state_140355448584128 = get('context_state', __marker)

            # <Value 'nocall:context/@@plone_context_state' (7:21)> -> __value
            __token = 275
            try:
                __zt_tmp = __attrs_140355459857376
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('nocall', 'context/@@plone_context_state', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_use_view_action_140355448522304 = get('use_view_action', __marker)

            # <Value "python:context.portal_registry.get('types_use_view_action_in_listings', [])" (8:22)> -> __value
            __token = 339
            try:
                __zt_tmp = __attrs_140355459857376
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "context.portal_registry.get('types_use_view_action_in_listings', [])", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['use_view_action'] = __value

            # <Value 'related' (10:24)> -> __condition
            __token = 456
            try:
                __zt_tmp = __attrs_140355459857376
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'related', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140355448931808 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-related" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa70d53c790> name=None at 7fa70d53c160> -> __attrs_140355459862240
                __attrs_140355459862240 = _static_140355459860368

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header class="section-heading" >')
                __stream_140355459861424 = []
                __append_140355459861424 = __stream_140355459861424.append
                __append_140355459861424('\n      Related content\n  ')
                __msgid_140355459861424 = __re_whitespace(''.join(__stream_140355459861424)).strip()
                if 'section_related_heading':
                    __append(translate('section_related_heading', mapping=None, default=__msgid_140355459861424, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</header>\n\n  <!-- section content -->\n  ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448477776
                __attrs_140355448477776 = _static_140355540704128
                __backup_item_140355448933536 = get('item', __marker)

                # <Value 'related' (21:30)> -> __iterator
                __token = 678
                try:
                    __zt_tmp = __attrs_140355448477776
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140355540363392('path', 'related', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                (__iterator, ____index_140355448476960, ) = getname('repeat')('item', __iterator)
                econtext['item'] = None
                for __item in __iterator:
                    econtext['item'] = __item
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7fa70ca615b0> name=None at 7fa70ca61fd0> -> __attrs_140355448475808
                    __attrs_140355448475808 = _static_140355448477104
                    __backup_desc_140355459861568 = get('desc', __marker)

                    # <Value 'item/Description' (24:16)> -> __value
                    __token = 767
                    try:
                        __zt_tmp = __attrs_140355448475808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'item/Description', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['desc'] = __value
                    __backup_item_type_140355448478304 = get('item_type', __marker)

                    # <Value 'item/portal_type' (25:20)> -> __value
                    __token = 805
                    try:
                        __zt_tmp = __attrs_140355448475808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'item/portal_type', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['item_type'] = __value
                    __backup_item_type_class_140355448477200 = get('item_type_class', __marker)

                    # <Value "python:'contenttype-' + normalizeString(item_type)" (26:25)> -> __value
                    __token = 849
                    try:
                        __zt_tmp = __attrs_140355448475808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('python', "'contenttype-' + normalizeString(item_type)", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['item_type_class'] = __value
                    __backup_item_wf_state_140355448475712 = get('item_wf_state', __marker)

                    # <Value 'item/review_state|python: context_state.workflow_state()' (27:22)> -> __value
                    __token = 925
                    try:
                        __zt_tmp = __attrs_140355448475808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'item/review_state|python: context_state.workflow_state()', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['item_wf_state'] = __value
                    __backup_item_wf_state_class_140355448478448 = get('item_wf_state_class', __marker)

                    # <Value "python: 'state-' + normalizeString(item_wf_state)" (28:27)> -> __value
                    __token = 1013
                    try:
                        __zt_tmp = __attrs_140355448475808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('python', " 'state-' + normalizeString(item_wf_state)", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['item_wf_state_class'] = __value
                    __backup_item_url_140355448479216 = get('item_url', __marker)

                    # <Value 'item/getURL|item/absolute_url' (29:15)> -> __value
                    __token = 1083
                    try:
                        __zt_tmp = __attrs_140355448475808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'item/getURL|item/absolute_url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['item_url'] = __value
                    __backup_item_url_140355448476528 = get('item_url', __marker)

                    # <Value "python:(item_type in use_view_action) and item_url+'/view' or item_url" (30:14)> -> __value
                    __token = 1133
                    try:
                        __zt_tmp = __attrs_140355448475808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('python', "(item_type in use_view_action) and item_url+'/view' or item_url", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['item_url'] = __value
                    __backup_item_has_image_140355448478400 = get('item_has_image', __marker)

                    # <Value 'python:item.getIcon' (31:19)> -> __value
                    __token = 1230
                    try:
                        __zt_tmp = __attrs_140355448475808
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('python', 'item.getIcon', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['item_has_image'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="media position-relative" >\n\n      ')

                    # <Static value=<ast.Dict object at 0x7fa70eaf7d60> name=None at 7fa70eaf7e50> -> __attrs_140355482645168
                    __attrs_140355482645168 = _static_140355482647904

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="media-body">\n        ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355482647184
                    __attrs_140355482647184 = _static_140355540704128

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>')

                    # <Static value=<ast.Dict object at 0x7fa70d518b50> name=None at 7fa70eaf7b50> -> __attrs_140355459712816
                    __attrs_140355459712816 = _static_140355459713872

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a class="h6 stretched-link"')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459712288
                    __default_140355459712288 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution '${item_url}' (37:19)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70d518e20> -> __attr_href
                    __token = 1368
                    __token = 1370
                    try:
                        __zt_tmp = __attrs_140355459712816
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140355540363392('path', 'item_url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
                    __append(' >')

                    # <Interpolation value=<Substitution '${item/pretty_title_or_id}' (38:11)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70d518d00> -> __content_140355621335664
                    __token = 1392
                    __token = 1394
                    try:
                        __zt_tmp = __attrs_140355459712816
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140355621335664 = _static_140355540363392('path', 'item/pretty_title_or_id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
                    __append('</a></div>\n        ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459713344
                    __attrs_140355459713344 = _static_140355540704128

                    # <small ... (0:0)
                    # --------------------------------------------------------
                    __append('<small>')

                    # <Interpolation value=<Substitution '${item/Description}' (39:15)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70d5181c0> -> __content_140355621335664
                    __token = 1444
                    __token = 1446
                    try:
                        __zt_tmp = __attrs_140355459713344
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140355621335664 = _static_140355540363392('path', 'item/Description', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
                    __append('</small>\n      </div>\n\n      ')

                    # <Static value=<ast.Dict object at 0x7fa70d5186d0> name=None at 7fa70d5183d0> -> __attrs_140355459855168
                    __attrs_140355459855168 = _static_140355459712720
                    __backup_getIcon_140355448477536 = get('getIcon', __marker)

                    # <Value "python:item.getURL() +'/@@images/image/thumb'" (45:21)> -> __value
                    __token = 1573
                    try:
                        __zt_tmp = __attrs_140355459855168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('python', "item.getURL() +'/@@images/image/thumb'", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['getIcon'] = __value

                    # <Value 'item_has_image' (47:26)> -> __condition
                    __token = 1659
                    try:
                        __zt_tmp = __attrs_140355459855168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('path', 'item_has_image', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:

                        # <img ... (0:0)
                        # --------------------------------------------------------
                        __append('<img class="ms-3"')

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459854976
                        __default_140355459854976 = _DEFAULT_MARKER

                        # <Substitution 'string:$getIcon' (49:17)> -> __attr_src
                        __token = 1720
                        try:
                            __zt_tmp = __attrs_140355459855168
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_src = _static_140355540363392('string', '$getIcon', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_src is not None):
                            __append((' src="%s"' % __attr_src))

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459857088
                        __default_140355459857088 = _DEFAULT_MARKER

                        # <Substitution 'item/Description' (50:16)> -> __attr_alt
                        __token = 1753
                        try:
                            __zt_tmp = __attrs_140355459855168
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_alt = _static_140355540363392('path', 'item/Description', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        __attr_alt = __quote(__attr_alt, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_alt is not None):
                            __append((' alt="%s"' % __attr_alt))
                        __append(' />')
                    if (__backup_getIcon_140355448477536 is __marker):
                        del econtext['getIcon']
                    else:
                        econtext['getIcon'] = __backup_getIcon_140355448477536
                    __append('\n\n    </div>')
                    if (__backup_item_has_image_140355448478400 is __marker):
                        del econtext['item_has_image']
                    else:
                        econtext['item_has_image'] = __backup_item_has_image_140355448478400
                    if (__backup_item_url_140355448476528 is __marker):
                        del econtext['item_url']
                    else:
                        econtext['item_url'] = __backup_item_url_140355448476528
                    if (__backup_item_url_140355448479216 is __marker):
                        del econtext['item_url']
                    else:
                        econtext['item_url'] = __backup_item_url_140355448479216
                    if (__backup_item_wf_state_class_140355448478448 is __marker):
                        del econtext['item_wf_state_class']
                    else:
                        econtext['item_wf_state_class'] = __backup_item_wf_state_class_140355448478448
                    if (__backup_item_wf_state_140355448475712 is __marker):
                        del econtext['item_wf_state']
                    else:
                        econtext['item_wf_state'] = __backup_item_wf_state_140355448475712
                    if (__backup_item_type_class_140355448477200 is __marker):
                        del econtext['item_type_class']
                    else:
                        econtext['item_type_class'] = __backup_item_type_class_140355448477200
                    if (__backup_item_type_140355448478304 is __marker):
                        del econtext['item_type']
                    else:
                        econtext['item_type'] = __backup_item_type_140355448478304
                    if (__backup_desc_140355459861568 is __marker):
                        del econtext['desc']
                    else:
                        econtext['desc'] = __backup_desc_140355459861568
                    __append('\n  ')
                    ____index_140355448476960 -= 1
                    if (____index_140355448476960 > 0):
                        __append('')
                if (__backup_item_140355448933536 is __marker):
                    del econtext['item']
                else:
                    econtext['item'] = __backup_item_140355448933536
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_140355448931808
            if (__backup_use_view_action_140355448522304 is __marker):
                del econtext['use_view_action']
            else:
                econtext['use_view_action'] = __backup_use_view_action_140355448522304
            if (__backup_context_state_140355448584128 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_140355448584128
            if (__backup_normalizeString_140355448504224 is __marker):
                del econtext['normalizeString']
            else:
                econtext['normalizeString'] = __backup_normalizeString_140355448504224
            if (__backup_plone_layout_140355448673616 is __marker):
                del econtext['plone_layout']
            else:
                econtext['plone_layout'] = __backup_plone_layout_140355448673616
            if (__backup_plone_view_140355448653568 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_140355448653568
            if (__backup_related_140355448959376 is __marker):
                del econtext['related']
            else:
                econtext['related'] = __backup_related_140355448959376
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }