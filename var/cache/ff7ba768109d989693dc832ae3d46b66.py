# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/viewlets/document_byline.pt'

__tokens = {53: ('view/show', 2, 24), 154: ('here/creators', 6, 30), 206: (' context/@@plone_portal_state/navigation_root_ur', 7, 37), 306: ('python:creator_ids and view.show_about()', 9, 31), 466: ('creator_ids', 13, 31), 536: ('python: view.get_url_path(user_id)', 15, 29), 600: (' python:view.get_fullname(user_id', 16, 28), 814: ('url_path', 20, 28), 750: ('${navigation_root_url}/${url_path}', 19, 19), 752: ('navigation_root_url', 19, 21), 775: ('url_path', 19, 44), 835: ('${fullname}', 21, 11), 837: ('fullname', 21, 13), 959: ('not:url_path', 23, 31), 984: ('${fullname}', 24, 11), 986: ('fullname', 24, 13), 1130: ('view/pub_date', 32, 25), 1168: (' context/ModificationDat', 33, 23), 1231: ('e python:view.show_modification_date', 34, 36), 1348: ('published', 37, 25), 1450: ('python:context.toLocalizedTime(published)', 40, 25), 1536: ('show_modification_date', 41, 26), 1645: ('show_modification_date', 45, 25), 1782: ('python:context.toLocalizedTime(modified)', 50, 25), 1912: ('view/isExpired', 56, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355448652944 = {'class': 'state-expired', }
_static_140355449329600 = {'class': 'documentModified', }
_static_140355448916816 = {'class': 'documentPublished', }
_static_140355459616976 = {'class': 'badge rounded-pill bg-light text-dark fw-normal fs-6', }
_static_140355459617456 = {'class': 'badge rounded-pill bg-light text-dark fw-normal fs-6', 'href': '${navigation_root_url}/${url_path}', }
_static_140355448905984 = {'class': 'label-by-author', }
_static_140355540704128 = {}
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355459399056 = {'id': 'section-byline', }

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

            # <Static value=<ast.Dict object at 0x7fa70d4cbd90> name=None at 7fa70d4cba00> -> __attrs_140355448907280
            __attrs_140355448907280 = _static_140355459399056

            # <Value 'view/show' (2:24)> -> __condition
            __token = 53
            try:
                __zt_tmp = __attrs_140355448907280
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'view/show', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140355448907136 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-byline" >\n  ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448907664
                __attrs_140355448907664 = _static_140355540704128
                __backup_creator_ids_140355482520640 = get('creator_ids', __marker)

                # <Value 'here/creators' (6:30)> -> __value
                __token = 154
                try:
                    __zt_tmp = __attrs_140355448907664
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'here/creators', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['creator_ids'] = __value
                __backup_navigation_root_url_140355449139888 = get('navigation_root_url', __marker)

                # <Value 'context/@@plone_portal_state/navigation_root_url' (7:37)> -> __value
                __token = 206
                try:
                    __zt_tmp = __attrs_140355448907664
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'context/@@plone_portal_state/navigation_root_url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['navigation_root_url'] = __value

                # <Value 'python:creator_ids and view.show_about()' (9:31)> -> __condition
                __token = 306
                try:
                    __zt_tmp = __attrs_140355448907664
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('python', 'creator_ids and view.show_about()', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:
                    __append('\n    ')

                    # <Static value=<ast.Dict object at 0x7fa70caca100> name=None at 7fa70cacaf10> -> __attrs_140355448907040
                    __attrs_140355448907040 = _static_140355448905984

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="label-by-author">\n      ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459614848
                    __attrs_140355459614848 = _static_140355540704128
                    __stream_140355459614752 = []
                    __append_140355459614752 = __stream_140355459614752.append
                    __append_140355459614752('by')
                    __msgid_140355459614752 = __re_whitespace(''.join(__stream_140355459614752)).strip()
                    if __msgid_140355459614752:
                        __append(translate(__msgid_140355459614752, mapping=None, default=__msgid_140355459614752, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459614176
                    __attrs_140355459614176 = _static_140355540704128
                    __backup_user_id_140355449642720 = get('user_id', __marker)

                    # <Value 'creator_ids' (13:31)> -> __iterator
                    __token = 466
                    try:
                        __zt_tmp = __attrs_140355459614176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140355540363392('path', 'creator_ids', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    (__iterator, ____index_140355459615856, ) = getname('repeat')('user_id', __iterator)
                    econtext['user_id'] = None
                    for __item in __iterator:
                        econtext['user_id'] = __item
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459616144
                        __attrs_140355459616144 = _static_140355540704128
                        __backup_url_path_140355459744096 = get('url_path', __marker)

                        # <Value 'python: view.get_url_path(user_id)' (15:29)> -> __value
                        __token = 536
                        try:
                            __zt_tmp = __attrs_140355459616144
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140355540363392('python', ' view.get_url_path(user_id)', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        econtext['url_path'] = __value
                        __backup_fullname_140355449698960 = get('fullname', __marker)

                        # <Value 'python:view.get_fullname(user_id)' (16:28)> -> __value
                        __token = 600
                        try:
                            __zt_tmp = __attrs_140355459616144
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140355540363392('python', 'view.get_fullname(user_id)', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        econtext['fullname'] = __value
                        __append('\n          ')

                        # <Static value=<ast.Dict object at 0x7fa70d5012b0> name=None at 7fa70d500430> -> __attrs_140355459620480
                        __attrs_140355459620480 = _static_140355459617456

                        # <Value 'url_path' (20:28)> -> __condition
                        __token = 814
                        try:
                            __zt_tmp = __attrs_140355459620480
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140355540363392('path', 'url_path', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        if __condition:

                            # <a ... (0:0)
                            # --------------------------------------------------------
                            __append('<a class="badge rounded-pill bg-light text-dark fw-normal fs-6"')

                            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459620096
                            __default_140355459620096 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${navigation_root_url}/${url_path}' (19:19)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70d501f70> -> __attr_href
                            __token = 750
                            __token = 752
                            try:
                                __zt_tmp = __attrs_140355459620480
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href = _static_140355540363392('path', 'navigation_root_url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                            __token = 775
                            try:
                                __zt_tmp = __attrs_140355459620480
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_href_773 = _static_140355540363392('path', 'url_path', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            __attr_href_773 = __quote(__attr_href_773, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_href = ('%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '/', (__attr_href_773 if (__attr_href_773 is not None) else ''), ))
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

                            # <Interpolation value=<Substitution '${fullname}' (21:11)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70d501d60> -> __content_140355621335664
                            __token = 835
                            __token = 837
                            try:
                                __zt_tmp = __attrs_140355459620480
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_140355621335664 = _static_140355540363392('path', 'fullname', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
                            __append('</a>')
                        __append('\n          ')

                        # <Static value=<ast.Dict object at 0x7fa70d5010d0> name=None at 7fa70d501a90> -> __attrs_140355459620048
                        __attrs_140355459620048 = _static_140355459616976

                        # <Value 'not:url_path' (23:31)> -> __condition
                        __token = 959
                        try:
                            __zt_tmp = __attrs_140355459620048
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140355540363392('not', 'url_path', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="badge rounded-pill bg-light text-dark fw-normal fs-6" >')

                            # <Interpolation value=<Substitution '${fullname}' (24:11)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70caccf40> -> __content_140355621335664
                            __token = 984
                            __token = 986
                            try:
                                __zt_tmp = __attrs_140355459620048
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_140355621335664 = _static_140355540363392('path', 'fullname', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
                            __append('</span>')
                        __append('\n        ')
                        if (__backup_fullname_140355449698960 is __marker):
                            del econtext['fullname']
                        else:
                            econtext['fullname'] = __backup_fullname_140355449698960
                        if (__backup_url_path_140355459744096 is __marker):
                            del econtext['url_path']
                        else:
                            econtext['url_path'] = __backup_url_path_140355459744096
                        __append('\n      ')
                        ____index_140355459615856 -= 1
                        if (____index_140355459615856 > 0):
                            __append('')
                    if (__backup_user_id_140355449642720 is __marker):
                        del econtext['user_id']
                    else:
                        econtext['user_id'] = __backup_user_id_140355449642720
                    __append('\n    &mdash;\n    </span>\n  ')
                if (__backup_navigation_root_url_140355449139888 is __marker):
                    del econtext['navigation_root_url']
                else:
                    econtext['navigation_root_url'] = __backup_navigation_root_url_140355449139888
                if (__backup_creator_ids_140355482520640 is __marker):
                    del econtext['creator_ids']
                else:
                    econtext['creator_ids'] = __backup_creator_ids_140355482520640
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459614896
                __attrs_140355459614896 = _static_140355540704128
                __backup_published_140355449230816 = get('published', __marker)

                # <Value 'view/pub_date' (32:25)> -> __value
                __token = 1130
                try:
                    __zt_tmp = __attrs_140355459614896
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'view/pub_date', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['published'] = __value
                __backup_modified_140355449139552 = get('modified', __marker)

                # <Value 'context/ModificationDate' (33:23)> -> __value
                __token = 1168
                try:
                    __zt_tmp = __attrs_140355459614896
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'context/ModificationDate', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['modified'] = __value
                __backup_show_modification_date_140355459744768 = get('show_modification_date', __marker)

                # <Value 'python:view.show_modification_date()' (34:36)> -> __value
                __token = 1231
                try:
                    __zt_tmp = __attrs_140355459614896
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('python', 'view.show_modification_date()', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['show_modification_date'] = __value
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7fa70caccb50> name=None at 7fa70cacc220> -> __attrs_140355448915232
                __attrs_140355448915232 = _static_140355448916816

                # <Value 'published' (37:25)> -> __condition
                __token = 1348
                try:
                    __zt_tmp = __attrs_140355448915232
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('path', 'published', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="documentPublished" >\n      ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449101376
                    __attrs_140355449101376 = _static_140355540704128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_140355449100224 = []
                    __append_140355449100224 = __stream_140355449100224.append
                    __append_140355449100224('published')
                    __msgid_140355449100224 = __re_whitespace(''.join(__stream_140355449100224)).strip()
                    if 'box_published':
                        __append(translate('box_published', mapping=None, default=__msgid_140355449100224, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449330896
                    __attrs_140355449330896 = _static_140355540704128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449101568
                    __default_140355449101568 = _DEFAULT_MARKER

                    # <Value 'python:context.toLocalizedTime(published)' (40:25)> -> __cache_140355449099216
                    __token = 1450
                    try:
                        __zt_tmp = __attrs_140355449330896
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355449099216 = _static_140355540363392('python', 'context.toLocalizedTime(published)', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:context.toLocalizedTime(published)' (40:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70caf95b0> -> __condition
                    __expression = __cache_140355449099216

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('Published')
                    else:
                        __content = __cache_140355449099216
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n      ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449329456
                    __attrs_140355449329456 = _static_140355540704128

                    # <Value 'show_modification_date' (41:26)> -> __condition
                    __token = 1536
                    try:
                        __zt_tmp = __attrs_140355449329456
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('path', 'show_modification_date', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:
                        __append(',')
                    __append('\n    </span>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7fa70cb317c0> name=None at 7fa70cb31430> -> __attrs_140355449327824
                __attrs_140355449327824 = _static_140355449329600

                # <Value 'show_modification_date' (45:25)> -> __condition
                __token = 1645
                try:
                    __zt_tmp = __attrs_140355449327824
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('path', 'show_modification_date', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="documentModified" >\n      ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449327920
                    __attrs_140355449327920 = _static_140355540704128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_140355449328400 = []
                    __append_140355449328400 = __stream_140355449328400.append
                    __append_140355449328400('\n      last modified\n      ')
                    __msgid_140355449328400 = __re_whitespace(''.join(__stream_140355449328400)).strip()
                    if 'box_last_modified':
                        __append(translate('box_last_modified', mapping=None, default=__msgid_140355449328400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n      ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448808592
                    __attrs_140355448808592 = _static_140355540704128

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448810944
                    __default_140355448810944 = _DEFAULT_MARKER

                    # <Value 'python:context.toLocalizedTime(modified)' (50:25)> -> __cache_140355448808208
                    __token = 1782
                    try:
                        __zt_tmp = __attrs_140355448808592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355448808208 = _static_140355540363392('python', 'context.toLocalizedTime(modified)', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'python:context.toLocalizedTime(modified)' (50:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cab2b50> -> __condition
                    __expression = __cache_140355448808208

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n      Modified\n      ')
                    else:
                        __content = __cache_140355448808208
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n    </span>')
                __append('\n  ')
                if (__backup_show_modification_date_140355459744768 is __marker):
                    del econtext['show_modification_date']
                else:
                    econtext['show_modification_date'] = __backup_show_modification_date_140355459744768
                if (__backup_modified_140355449139552 is __marker):
                    del econtext['modified']
                else:
                    econtext['modified'] = __backup_modified_140355449139552
                if (__backup_published_140355449230816 is __marker):
                    del econtext['published']
                else:
                    econtext['published'] = __backup_published_140355449230816
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448811232
                __attrs_140355448811232 = _static_140355540704128

                # <Value 'view/isExpired' (56:30)> -> __condition
                __token = 1912
                try:
                    __zt_tmp = __attrs_140355448811232
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('path', 'view/isExpired', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:
                    __append('\n    &mdash;\n    ')

                    # <Static value=<ast.Dict object at 0x7fa70ca8c490> name=None at 7fa70ca8ce20> -> __attrs_140355448651984
                    __attrs_140355448651984 = _static_140355448652944

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="state-expired" >')
                    __stream_140355448652032 = []
                    __append_140355448652032 = __stream_140355448652032.append
                    __append_140355448652032('expired')
                    __msgid_140355448652032 = __re_whitespace(''.join(__stream_140355448652032)).strip()
                    if 'time_expired':
                        __append(translate('time_expired', mapping=None, default=__msgid_140355448652032, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n  ')
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_140355448907136
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }