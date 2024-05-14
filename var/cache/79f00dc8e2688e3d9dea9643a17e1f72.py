# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/Products.CMFPlone-6.0.11-py3.9.egg/Products/CMFPlone/browser/templates/plone-addsite.pt'

__tokens = {481: ('${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', 12, 14), 483: ('string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', 12, 16), 627: ('${string:${context/absolute_url}/++resource++plone-admin-ui.css}', 15, 14), 629: ('string:${context/absolute_url}/++resource++plone-admin-ui.css', 15, 16), 726: ('string:${context/absolute_url}/++resource++jstz-1.0.4.min.js', 16, 30), 831: ('string:${context/absolute_url}/++resource++plone-admin-ui.js', 18, 30), 1117: ('string:${context/absolute_url}/++resource++plone-logo.svg', 28, 35), 1405: ('view/profiles', 35, 25), 1449: (' profiles/bas', 36, 29), 1495: ('e profiles/defau', 37, 30), 1547: ('es profiles/extensi', 38, 32), 1592: ('ced request/advanced|not', 39, 21), 1332: ('string:${context/absolute_url}/@@plone-addsite', 34, 27), 2255: ('request/site_id|nothing', 55, 40), 3261: ('view/browser_language', 78, 49), 3333: (' python:view.grouped_languages(browser_language', 79, 49), 3426: ('grouped_languages', 80, 42), 3491: ('group/label', 81, 46), 3582: ('group/languages', 84, 41), 3645: ("python:lang['langcode']", 85, 46), 3718: (" python:lang['langcode'] == browser_languag", 86, 48), 3801: ("python: lang['label']", 87, 37), 4403: ('view/timezones', 108, 40), 4462: ('tz_list', 109, 42), 4517: ('group', 110, 46), 4576: ('python:tz_list[group]', 111, 51), 4621: ('tz/value', 111, 96), 4662: ('tz/label', 112, 31), 5112: ('advanced', 124, 30), 5742: ('not:advanced', 140, 32), 5897: ('python: len(base_profiles) > 1', 144, 30), 6069: ('base_profiles', 148, 36), 6388: (' info/i', 155, 43), 6336: ('info/id', 154, 41), 6442: ("d python: default_profile==info['id'] and 'checked' or nothi", 156, 44), 6577: ('info/id', 157, 68), 6586: ('${info/title}', 157, 77), 6588: ('info/title', 157, 79), 6660: ('info/description', 158, 52), 6678: ('${info/description}', 158, 70), 6680: ('info/description', 158, 72), 7046: ("python:[p for p in extension_profiles if p.get('selected', None)]", 170, 40), 7143: ('python: extension_profiles or advanced', 171, 30), 7212: ('python: has_selected and not advanced', 172, 29), 7286: ('python: advanced', 173, 34), 7692: ('extension_profiles', 183, 39), 7757: ('info/selected|nothing', 184, 44), 7824: ('python: not selected or advanced', 185, 43), 7943: ('python: advanced', 187, 37), 8090: ('${info/id}', 190, 33), 8092: ('info/id', 190, 35), 8132: ('${info/id}', 191, 30), 8134: ('info/id', 191, 32), 8245: ('info/selected|nothing', 193, 50), 8329: ('${info/id}', 194, 57), 8331: ('info/id', 194, 59), 8342: ('${info/title}', 194, 70), 8344: ('info/title', 194, 72), 8446: ("python: advanced and info['description']", 196, 39), 8511: ('${info/description}', 197, 22), 8513: ('info/description', 197, 24), 8656: ('python: selected and not advanced', 201, 43), 8812: ('${info/id}', 204, 31), 8814: ('info/id', 204, 33)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355493530112 = {'class': 'btn btn-success mt-3', 'type': 'submit', 'name': 'submit', }
_static_140355537011808 = {'type': 'hidden', 'name': 'form.submitted:boolean', 'value': 'True', }
_static_140355493542832 = {'class': 'col-md-12 mt-3', }
_static_140355523774256 = {'type': 'hidden', 'name': 'extension_ids:list', 'value': '${info/id}', }
_static_140355523774928 = {'class': 'form-text', }
_static_140355524559728 = {'class': 'form-check-label', 'for': '${info/id}', }
_static_140355539593392 = {'type': 'checkbox', 'name': 'extension_ids:list', 'value': '${info/id}', 'id': '${info/id}', 'class': 'form-check-input', 'checked': 'info/selected|nothing', }
_static_140355539591280 = {'class': 'form-check mb-3', }
_static_140355549507440 = {'class': 'lead', }
_static_140355515719008 = {'class': 'col-md-12 mt-3', }
_static_140355515717040 = {'class': 'form-text', }
_static_140355515716416 = {'class': 'form-text', }
_static_140355549380912 = {'class': 'form-check-label', 'for': 'info/id', }
_static_140355539800848 = {'type': 'radio', 'name': 'profile_id:string', 'value': 'profile', 'class': 'form-check-input', 'id': 'info/id', 'checked': "python: default_profile==info['id'] and 'checked' or nothing", }
_static_140355539800560 = {'class': 'form-check mb-3', }
_static_140355528088976 = {'class': 'lead', }
_static_140355528088064 = {'class': 'mb-3', }
_static_140355528085616 = {'class': 'col-md-12', }
_static_140355528981280 = {'type': 'hidden', 'name': 'setup_content:boolean', 'value': 'true', }
_static_140355528981520 = {'class': 'form-text', }
_static_140355523135280 = {'class': 'form-check-label', 'for': 'example-content', }
_static_140355523137152 = {'class': 'form-check-input', 'id': 'example-content', 'type': 'checkbox', 'name': 'setup_content:boolean', 'checked': 'checked', }
_static_140355515982416 = {'class': 'form-check', }
_static_140355515983664 = {'class': 'col-md-12 mb-3', }
_static_140355515985056 = {'class': 'form-text', }
_static_140355527797632 = {'value': 'UTC', }
_static_140355527795040 = {'label': 'group', }
_static_140355527816816 = {'id': 'portal_timezone', 'name': 'portal_timezone', 'class': 'form-select', }
_static_140355527815280 = {'for': 'portal_timezone', 'class': 'form-label', }
_static_140355516200752 = {'class': 'col-md-12 mb-3 tzx', }
_static_140355516202096 = {'class': 'form-text', }
_static_140355516200512 = {'value': 'en', 'selected': "python:lang['langcode'] == browser_language", }
_static_140355494387872 = {'label': 'group/label', }
_static_140355537396640 = {'name': 'default_language', 'class': 'form-select', }
_static_140355537397984 = {'for': 'default_language', 'class': 'form-label', }
_static_140355537395776 = {'class': 'col-md-12 mb-3', }
_static_140355524518336 = {'class': 'form-text', }
_static_140355484736336 = {'type': 'text', 'name': 'title', 'size': '30', 'value': 'Site', 'class': 'form-control', }
_static_140355484737248 = {'for': 'title', 'class': 'form-label', }
_static_140355539646832 = {'class': 'col-md-12 mb-3', }
_static_140355539648320 = {'class': 'form-text', }
_static_140355491092992 = {'type': 'text', 'name': 'site_id', 'size': '20', 'id': 'site_id', 'class': 'form-control', 'value': 'request/site_id|nothing', }
_static_140355491092848 = {'for': 'site_id', 'class': 'form-label', }
_static_140355491090496 = {'class': 'col-md-12 mb-3 mb-3', }
_static_140355514828400 = {'class': 'lead', }
_static_140355514829696 = {'class': 'col-md-12', }
_static_140355537280400 = {'class': 'row', }
_static_140355491866512 = {'action': '#', 'method': 'post', }
_static_140355491866992 = {'src': '/++resource++plone-logo.svg', 'width': '215', 'height': '56', 'alt': 'Plone logo', }
_static_140355539231264 = {'class': 'row', }
_static_140355539232848 = {'class': 'container admin mt-5 mb-5 p-4 ', }
_static_140355490381536 = {'src': 'string:${context/absolute_url}/++resource++plone-admin-ui.js', }
_static_140355490379712 = {'src': 'string:${context/absolute_url}/++resource++jstz-1.0.4.min.js', }
_static_140355490380960 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++resource++plone-admin-ui.css}', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355525389376 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', }
_static_140355525386400 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1', }
_static_140355529454880 = {'charset': 'utf-8', }
_static_140355540704128 = {}
_static_140355529401680 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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
            __append('<!DOCTYPE html>\n')

            # <Static value=<ast.Dict object at 0x7fa71178e550> name=None at 7fa71178e280> -> __attrs_140355529456848
            __attrs_140355529456848 = _static_140355529401680
            __previous_i18n_domain_140355529455072 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355529453632
            __attrs_140355529453632 = _static_140355540704128

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n  ')

            # <Static value=<ast.Dict object at 0x7fa71179b520> name=None at 7fa71179bac0> -> __attrs_140355529456128
            __attrs_140355529456128 = _static_140355529454880

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n  ')

            # <Static value=<ast.Dict object at 0x7fa7113ba0a0> name=None at 7fa7113ba5e0> -> __attrs_140355525390144
            __attrs_140355525390144 = _static_140355525386400

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1" />\n  ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355525389040
            __attrs_140355525389040 = _static_140355540704128

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>')
            __stream_140355525389952 = []
            __append_140355525389952 = __stream_140355525389952.append
            __append_140355525389952('Create a Plone site')
            __msgid_140355525389952 = __re_whitespace(''.join(__stream_140355525389952)).strip()
            if __msgid_140355525389952:
                __append(translate(__msgid_140355525389952, mapping=None, default=__msgid_140355525389952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</title>\n  ')

            # <Static value=<ast.Dict object at 0x7fa7113bac40> name=None at 7fa7113bacd0> -> __attrs_140355490379184
            __attrs_140355490379184 = _static_140355525389376

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355525389424
            __default_140355525389424 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}' (12:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa7113ba610> -> __attr_href
            __token = 481
            __token = 483
            try:
                __zt_tmp = __attrs_140355490379184
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140355540363392('string', '${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
            __append(' />\n  ')

            # <Static value=<ast.Dict object at 0x7fa70f257ca0> name=None at 7fa70f2576d0> -> __attrs_140355490379424
            __attrs_140355490379424 = _static_140355490380960

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355490378416
            __default_140355490378416 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++resource++plone-admin-ui.css}' (15:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa70f257430> -> __attr_href
            __token = 627
            __token = 629
            try:
                __zt_tmp = __attrs_140355490379424
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140355540363392('string', '${context/absolute_url}/++resource++plone-admin-ui.css', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
            __append(' />\n  ')

            # <Static value=<ast.Dict object at 0x7fa70f2577c0> name=None at 7fa70f257910> -> __attrs_140355490381680
            __attrs_140355490381680 = _static_140355490379712

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355490379952
            __default_140355490379952 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++jstz-1.0.4.min.js' (16:30)> -> __attr_src
            __token = 726
            try:
                __zt_tmp = __attrs_140355490381680
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140355540363392('string', '${context/absolute_url}/++resource++jstz-1.0.4.min.js', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append('>\n  </script>\n  ')

            # <Static value=<ast.Dict object at 0x7fa70f257ee0> name=None at 7fa70f257580> -> __attrs_140355539232608
            __attrs_140355539232608 = _static_140355490381536

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355539233616
            __default_140355539233616 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-admin-ui.js' (18:30)> -> __attr_src
            __token = 831
            try:
                __zt_tmp = __attrs_140355539232608
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140355540363392('string', '${context/absolute_url}/++resource++plone-admin-ui.js', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append('>\n  </script>\n</head>\n\n')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355539233280
            __attrs_140355539233280 = _static_140355540704128

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n\n  ')

            # <Static value=<ast.Dict object at 0x7fa7120ee850> name=None at 7fa7120eedc0> -> __attrs_140355539231552
            __attrs_140355539231552 = _static_140355539232848

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container admin mt-5 mb-5 p-4 ">\n    ')

            # <Static value=<ast.Dict object at 0x7fa7120ee220> name=None at 7fa7120eebe0> -> __attrs_140355491867328
            __attrs_140355491867328 = _static_140355539231264

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header class="row">\n      ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355491866560
            __attrs_140355491866560 = _static_140355540704128

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')

            # <Static value=<ast.Dict object at 0x7fa70f3c2970> name=None at 7fa70f3c2400> -> __attrs_140355491865792
            __attrs_140355491865792 = _static_140355491866992

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355491867184
            __default_140355491867184 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-logo.svg' (28:35)> -> __attr_src
            __token = 1117
            try:
                __zt_tmp = __attrs_140355491865792
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140355540363392('string', '${context/absolute_url}/++resource++plone-logo.svg', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', '/++resource++plone-logo.svg', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append(' width="215" height="56"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355491865696
            __default_140355491865696 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7fa70f3c2340> at 7fa70f3c2370> -> __attr_alt
            __attr_alt = 'Plone logo'
            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))
            __append(' /></p>\n    </header>\n    ')

            # <Static value=<ast.Dict object at 0x7fa70f3c2790> name=None at 7fa70f3c27f0> -> __attrs_140355537280448
            __attrs_140355537280448 = _static_140355491866512
            __backup_profiles_140355517998560 = get('profiles', __marker)

            # <Value 'view/profiles' (35:25)> -> __value
            __token = 1405
            try:
                __zt_tmp = __attrs_140355537280448
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/profiles', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['profiles'] = __value
            __backup_base_profiles_140355516900592 = get('base_profiles', __marker)

            # <Value 'profiles/base' (36:29)> -> __value
            __token = 1449
            try:
                __zt_tmp = __attrs_140355537280448
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'profiles/base', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['base_profiles'] = __value
            __backup_default_profile_140355516900544 = get('default_profile', __marker)

            # <Value 'profiles/default' (37:30)> -> __value
            __token = 1495
            try:
                __zt_tmp = __attrs_140355537280448
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'profiles/default', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['default_profile'] = __value
            __backup_extension_profiles_140355516901600 = get('extension_profiles', __marker)

            # <Value 'profiles/extensions' (38:32)> -> __value
            __token = 1547
            try:
                __zt_tmp = __attrs_140355537280448
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'profiles/extensions', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['extension_profiles'] = __value
            __backup_advanced_140355516900688 = get('advanced', __marker)

            # <Value 'request/advanced|nothing' (39:21)> -> __value
            __token = 1592
            try:
                __zt_tmp = __attrs_140355537280448
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'request/advanced|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['advanced'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355537278000
            __default_140355537278000 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/@@plone-addsite' (34:27)> -> __attr_action
            __token = 1332
            try:
                __zt_tmp = __attrs_140355537280448
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140355540363392('string', '${context/absolute_url}/@@plone-addsite', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append(' method="post">\n      ')

            # <Static value=<ast.Dict object at 0x7fa711f11d90> name=None at 7fa711f116d0> -> __attrs_140355537280688
            __attrs_140355537280688 = _static_140355537280400

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article class="row">\n        ')

            # <Static value=<ast.Dict object at 0x7fa7109a8b80> name=None at 7fa711f11520> -> __attrs_140355514830224
            __attrs_140355514830224 = _static_140355514829696

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12">\n          ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355514827152
            __attrs_140355514827152 = _static_140355540704128

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355514829504
            __attrs_140355514829504 = _static_140355540704128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_140355514827008 = []
            __append_140355514827008 = __stream_140355514827008.append
            __append_140355514827008('Create a Plone site')
            __msgid_140355514827008 = __re_whitespace(''.join(__stream_140355514827008)).strip()
            if __msgid_140355514827008:
                __append(translate(__msgid_140355514827008, mapping=None, default=__msgid_140355514827008, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span></h1>\n          ')

            # <Static value=<ast.Dict object at 0x7fa7109a8670> name=None at 7fa7109a8a90> -> __attrs_140355514828832
            __attrs_140355514828832 = _static_140355514828400

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="lead">')
            __stream_140355514827680 = []
            __append_140355514827680 = __stream_140355514827680.append
            __append_140355514827680('Adds a new Plone content management system site to the underlying application server.')
            __msgid_140355514827680 = __re_whitespace(''.join(__stream_140355514827680)).strip()
            if __msgid_140355514827680:
                __append(translate(__msgid_140355514827680, mapping=None, default=__msgid_140355514827680, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n        </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7fa70f305040> name=None at 7fa70f305670> -> __attrs_140355491091504
            __attrs_140355491091504 = _static_140355491090496

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3 mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x7fa70f305970> name=None at 7fa70f305d60> -> __attrs_140355491092752
            __attrs_140355491092752 = _static_140355491092848

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="site_id" class="form-label">')
            __stream_140355491092320 = []
            __append_140355491092320 = __stream_140355491092320.append
            __append_140355491092320('\n              Path identifier\n            ')
            __msgid_140355491092320 = __re_whitespace(''.join(__stream_140355491092320)).strip()
            if __msgid_140355491092320:
                __append(translate(__msgid_140355491092320, mapping=None, default=__msgid_140355491092320, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x7fa70f305a00> name=None at 7fa70f3059d0> -> __attrs_140355539645440
            __attrs_140355539645440 = _static_140355491092992

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="text" name="site_id" size="20" id="site_id" class="form-control"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355539646784
            __default_140355539646784 = _DEFAULT_MARKER

            # <Substitution 'request/site_id|nothing' (55:40)> -> __attr_value
            __token = 2255
            try:
                __zt_tmp = __attrs_140355539645440
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140355540363392('path', 'request/site_id|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' />\n\n            ')

            # <Static value=<ast.Dict object at 0x7fa712153f40> name=None at 7fa712153220> -> __attrs_140355539648368
            __attrs_140355539648368 = _static_140355539648320

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_140355539646736 = []
            __append_140355539646736 = __stream_140355539646736.append
            __append_140355539646736('\n              The ID of the site. No special characters or spaces are allowed. This ends up as part of the URL unless hidden by an upstream web server.\n            ')
            __msgid_140355539646736 = __re_whitespace(''.join(__stream_140355539646736)).strip()
            if __msgid_140355539646736:
                __append(translate(__msgid_140355539646736, mapping=None, default=__msgid_140355539646736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7fa712153970> name=None at 7fa712153070> -> __attrs_140355484736240
            __attrs_140355484736240 = _static_140355539646832

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x7fa70ecf5ee0> name=None at 7fa70ecf5fd0> -> __attrs_140355484735040
            __attrs_140355484735040 = _static_140355484737248

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="title" class="form-label">')
            __stream_140355484735760 = []
            __append_140355484735760 = __stream_140355484735760.append
            __append_140355484735760('Title')
            __msgid_140355484735760 = __re_whitespace(''.join(__stream_140355484735760)).strip()
            if 'label_title':
                __append(translate('label_title', mapping=None, default=__msgid_140355484735760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x7fa70ecf5b50> name=None at 7fa70ecf57c0> -> __attrs_140355524521840
            __attrs_140355524521840 = _static_140355484736336

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="text" name="title" size="30"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355524519920
            __default_140355524519920 = _DEFAULT_MARKER

            # <Translate msgid='text_default_site_title' node=<ast.Constant object at 0x7fa7112e6f40> at 7fa7112e6d30> -> __attr_value
            __attr_value = 'Site'
            __attr_value = translate('text_default_site_title', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_value is not None):
                __append((' value="%s"' % __attr_value))
            __append(' class="form-control" />\n\n            ')

            # <Static value=<ast.Dict object at 0x7fa7112e61c0> name=None at 7fa7112e68b0> -> __attrs_140355524519680
            __attrs_140355524519680 = _static_140355524518336

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_140355524520400 = []
            __append_140355524520400 = __stream_140355524520400.append
            __append_140355524520400('\n              A short title for the site. This will be shown as part of the title of the browser window on each page.\n            ')
            __msgid_140355524520400 = __re_whitespace(''.join(__stream_140355524520400)).strip()
            if __msgid_140355524520400:
                __append(translate(__msgid_140355524520400, mapping=None, default=__msgid_140355524520400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7fa711f2e040> name=None at 7fa711f2efa0> -> __attrs_140355537398752
            __attrs_140355537398752 = _static_140355537395776

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3">\n            ')

            # <Static value=<ast.Dict object at 0x7fa711f2e8e0> name=None at 7fa711f2ee50> -> __attrs_140355537398416
            __attrs_140355537398416 = _static_140355537397984

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="default_language" class="form-label">')
            __stream_140355537399136 = []
            __append_140355537399136 = __stream_140355537399136.append
            __append_140355537399136('Language')
            __msgid_140355537399136 = __re_whitespace(''.join(__stream_140355537399136)).strip()
            if __msgid_140355537399136:
                __append(translate(__msgid_140355537399136, mapping=None, default=__msgid_140355537399136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x7fa711f2e3a0> name=None at 7fa711f2e550> -> __attrs_140355494391376
            __attrs_140355494391376 = _static_140355537396640
            __backup_browser_language_140355516899392 = get('browser_language', __marker)

            # <Value 'view/browser_language' (78:49)> -> __value
            __token = 3261
            try:
                __zt_tmp = __attrs_140355494391376
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/browser_language', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['browser_language'] = __value
            __backup_grouped_languages_140355516523472 = get('grouped_languages', __marker)

            # <Value 'python:view.grouped_languages(browser_language)' (79:49)> -> __value
            __token = 3333
            try:
                __zt_tmp = __attrs_140355494391376
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', 'view.grouped_languages(browser_language)', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['grouped_languages'] = __value

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select name="default_language" class="form-select">\n              ')

            # <Static value=<ast.Dict object at 0x7fa70f62a0a0> name=None at 7fa70f62a100> -> __attrs_140355494389024
            __attrs_140355494389024 = _static_140355494387872
            __backup_group_140355516526208 = get('group', __marker)

            # <Value 'grouped_languages' (80:42)> -> __iterator
            __token = 3426
            try:
                __zt_tmp = __attrs_140355494389024
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140355540363392('path', 'grouped_languages', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            (__iterator, ____index_140355494388064, ) = getname('repeat')('group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <optgroup ... (0:0)
                # --------------------------------------------------------
                __append('<optgroup')

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355494388256
                __default_140355494388256 = _DEFAULT_MARKER

                # <Substitution 'group/label' (81:46)> -> __attr_label
                __token = 3491
                try:
                    __zt_tmp = __attrs_140355494389024
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_label = _static_140355540363392('path', 'group/label', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                __attr_label = __quote(__attr_label, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_label is not None):
                    __append((' label="%s"' % __attr_label))
                __append('>\n\n                ')

                # <Static value=<ast.Dict object at 0x7fa710af7640> name=None at 7fa710af76d0> -> __attrs_140355516200944
                __attrs_140355516200944 = _static_140355516200512
                __backup_lang_140355516037632 = get('lang', __marker)

                # <Value 'group/languages' (84:41)> -> __iterator
                __token = 3582
                try:
                    __zt_tmp = __attrs_140355516200944
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140355540363392('path', 'group/languages', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                (__iterator, ____index_140355516200368, ) = getname('repeat')('lang', __iterator)
                econtext['lang'] = None
                for __item in __iterator:
                    econtext['lang'] = __item

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355516199888
                    __default_140355516199888 = _DEFAULT_MARKER

                    # <Substitution "python:lang['langcode']" (85:46)> -> __attr_value
                    __token = 3645
                    try:
                        __zt_tmp = __attrs_140355516200944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140355540363392('python', "lang['langcode']", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', 'en', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355516202960
                    __default_140355516202960 = _DEFAULT_MARKER

                    # <Boolean "python:lang['langcode'] == browser_language" (86:48)> -> __attr_selected
                    __token = 3718
                    try:
                        __zt_tmp = __attrs_140355516200944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_selected = _static_140355540363392('python', "lang['langcode'] == browser_language", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if (__attr_selected is _DEFAULT_MARKER):
                        __attr_selected = None
                    else:
                        if __attr_selected:
                            __attr_selected = 'selected'
                        else:
                            __attr_selected = None
                    if (__attr_selected is not None):
                        __append((' selected="%s"' % __attr_selected))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355494390128
                    __default_140355494390128 = _DEFAULT_MARKER

                    # <Value "python: lang['label']" (87:37)> -> __cache_140355494388880
                    __token = 3801
                    try:
                        __zt_tmp = __attrs_140355516200944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355494388880 = _static_140355540363392('python', " lang['label']", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value "python: lang['label']" (87:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70f62aa90> -> __condition
                    __expression = __cache_140355494388880

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                  English\n                ')
                    else:
                        __content = __cache_140355494388880
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>')
                    ____index_140355516200368 -= 1
                    if (____index_140355516200368 > 0):
                        __append('\n                ')
                if (__backup_lang_140355516037632 is __marker):
                    del econtext['lang']
                else:
                    econtext['lang'] = __backup_lang_140355516037632
                __append('\n\n              </optgroup>')
                ____index_140355494388064 -= 1
                if (____index_140355494388064 > 0):
                    __append('\n              ')
            if (__backup_group_140355516526208 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_140355516526208
            __append('\n            </select>')
            if (__backup_grouped_languages_140355516523472 is __marker):
                del econtext['grouped_languages']
            else:
                econtext['grouped_languages'] = __backup_grouped_languages_140355516523472
            if (__backup_browser_language_140355516899392 is __marker):
                del econtext['browser_language']
            else:
                econtext['browser_language'] = __backup_browser_language_140355516899392
            __append('\n\n            ')

            # <Static value=<ast.Dict object at 0x7fa710af7c70> name=None at 7fa710af7ca0> -> __attrs_140355516202288
            __attrs_140355516202288 = _static_140355516202096

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_140355516198976 = []
            __append_140355516198976 = __stream_140355516198976.append
            __append_140355516198976('\n              The main language of the site.\n            ')
            __msgid_140355516198976 = __re_whitespace(''.join(__stream_140355516198976)).strip()
            if __msgid_140355516198976:
                __append(translate(__msgid_140355516198976, mapping=None, default=__msgid_140355516198976, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7fa710af7730> name=None at 7fa710af7d90> -> __attrs_140355527819072
            __attrs_140355527819072 = _static_140355516200752

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mb-3 tzx">\n            ')

            # <Static value=<ast.Dict object at 0x7fa71160b070> name=None at 7fa71160b0d0> -> __attrs_140355527818016
            __attrs_140355527818016 = _static_140355527815280

            # <label ... (0:0)
            # --------------------------------------------------------
            __append('<label for="portal_timezone" class="form-label">')
            __stream_140355527817488 = []
            __append_140355527817488 = __stream_140355527817488.append
            __append_140355527817488('\n              Default timezone\n            ')
            __msgid_140355527817488 = __re_whitespace(''.join(__stream_140355527817488)).strip()
            if __msgid_140355527817488:
                __append(translate(__msgid_140355527817488, mapping=None, default=__msgid_140355527817488, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</label>\n\n            ')

            # <Static value=<ast.Dict object at 0x7fa71160b670> name=None at 7fa71160b160> -> __attrs_140355527817632
            __attrs_140355527817632 = _static_140355527816816
            __backup_tz_list_140355516523520 = get('tz_list', __marker)

            # <Value 'view/timezones' (108:40)> -> __value
            __token = 4403
            try:
                __zt_tmp = __attrs_140355527817632
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/timezones', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['tz_list'] = __value

            # <select ... (0:0)
            # --------------------------------------------------------
            __append('<select id="portal_timezone" name="portal_timezone" class="form-select">\n              ')

            # <Static value=<ast.Dict object at 0x7fa711606160> name=None at 7fa711606220> -> __attrs_140355527795184
            __attrs_140355527795184 = _static_140355527795040
            __backup_group_140355515595024 = get('group', __marker)

            # <Value 'tz_list' (109:42)> -> __iterator
            __token = 4462
            try:
                __zt_tmp = __attrs_140355527795184
            except get('NameError', NameError):
                __zt_tmp = None

            __iterator = _static_140355540363392('path', 'tz_list', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            (__iterator, ____index_140355527796000, ) = getname('repeat')('group', __iterator)
            econtext['group'] = None
            for __item in __iterator:
                econtext['group'] = __item

                # <optgroup ... (0:0)
                # --------------------------------------------------------
                __append('<optgroup')

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355527797872
                __default_140355527797872 = _DEFAULT_MARKER

                # <Substitution 'group' (110:46)> -> __attr_label
                __token = 4517
                try:
                    __zt_tmp = __attrs_140355527795184
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_label = _static_140355540363392('path', 'group', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                __attr_label = __quote(__attr_label, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_label is not None):
                    __append((' label="%s"' % __attr_label))
                __append('>\n                ')

                # <Static value=<ast.Dict object at 0x7fa711606b80> name=None at 7fa711606cd0> -> __attrs_140355527794944
                __attrs_140355527794944 = _static_140355527797632
                __backup_tz_140355515661424 = get('tz', __marker)

                # <Value 'python:tz_list[group]' (111:51)> -> __iterator
                __token = 4576
                try:
                    __zt_tmp = __attrs_140355527794944
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140355540363392('python', 'tz_list[group]', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                (__iterator, ____index_140355527797344, ) = getname('repeat')('tz', __iterator)
                econtext['tz'] = None
                for __item in __iterator:
                    econtext['tz'] = __item

                    # <option ... (0:0)
                    # --------------------------------------------------------
                    __append('<option')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355527797056
                    __default_140355527797056 = _DEFAULT_MARKER

                    # <Substitution 'tz/value' (111:96)> -> __attr_value
                    __token = 4621
                    try:
                        __zt_tmp = __attrs_140355527794944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140355540363392('path', 'tz/value', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', 'UTC', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append('>')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355527797008
                    __default_140355527797008 = _DEFAULT_MARKER

                    # <Value 'tz/label' (112:31)> -> __cache_140355527796912
                    __token = 4662
                    try:
                        __zt_tmp = __attrs_140355527794944
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355527796912 = _static_140355540363392('path', 'tz/label', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'tz/label' (112:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa7116066d0> -> __condition
                    __expression = __cache_140355527796912

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n                  UTC\n                ')
                    else:
                        __content = __cache_140355527796912
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</option>')
                    ____index_140355527797344 -= 1
                    if (____index_140355527797344 > 0):
                        __append('\n                ')
                if (__backup_tz_140355515661424 is __marker):
                    del econtext['tz']
                else:
                    econtext['tz'] = __backup_tz_140355515661424
                __append('\n              </optgroup>')
                ____index_140355527796000 -= 1
                if (____index_140355527796000 > 0):
                    __append('\n              ')
            if (__backup_group_140355515595024 is __marker):
                del econtext['group']
            else:
                econtext['group'] = __backup_group_140355515595024
            __append('\n            </select>')
            if (__backup_tz_list_140355516523520 is __marker):
                del econtext['tz_list']
            else:
                econtext['tz_list'] = __backup_tz_list_140355516523520
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7fa710ac2ca0> name=None at 7fa710ac2c70> -> __attrs_140355515984384
            __attrs_140355515984384 = _static_140355515985056

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="form-text">')
            __stream_140355527798592 = []
            __append_140355527798592 = __stream_140355527798592.append
            __append_140355527798592('\n              The default timezone setting of the portal.\n              Users will be able to set their own timezone, if available timezones are defined in the date and time settings.\n            ')
            __msgid_140355527798592 = __re_whitespace(''.join(__stream_140355527798592)).strip()
            if __msgid_140355527798592:
                __append(translate(__msgid_140355527798592, mapping=None, default=__msgid_140355527798592, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</div>\n          </div>\n\n          ')

            # <Static value=<ast.Dict object at 0x7fa710ac2730> name=None at 7fa710ac28b0> -> __attrs_140355515981984
            __attrs_140355515981984 = _static_140355515983664

            # <Value 'advanced' (124:30)> -> __condition
            __token = 5112
            try:
                __zt_tmp = __attrs_140355515981984
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'advanced', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12 mb-3">\n            ')

                # <Static value=<ast.Dict object at 0x7fa710ac2250> name=None at 7fa710ac2220> -> __attrs_140355515982128
                __attrs_140355515982128 = _static_140355515982416

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-check">\n              ')

                # <Static value=<ast.Dict object at 0x7fa711194e80> name=None at 7fa711194a30> -> __attrs_140355523136336
                __attrs_140355523136336 = _static_140355523137152

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-check-input" id="example-content" type="checkbox" name="setup_content:boolean" checked="checked" />\n              ')

                # <Static value=<ast.Dict object at 0x7fa711194730> name=None at 7fa711194760> -> __attrs_140355528979216
                __attrs_140355528979216 = _static_140355523135280

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-check-label" for="example-content">')
                __stream_140355523133936 = []
                __append_140355523133936 = __stream_140355523133936.append
                __append_140355523133936('Example content')
                __msgid_140355523133936 = __re_whitespace(''.join(__stream_140355523133936)).strip()
                if __msgid_140355523133936:
                    __append(translate(__msgid_140355523133936, mapping=None, default=__msgid_140355523133936, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n              ')

                # <Static value=<ast.Dict object at 0x7fa711727c10> name=None at 7fa711727ca0> -> __attrs_140355528978688
                __attrs_140355528978688 = _static_140355528981520

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-text">')
                __stream_140355528978496 = []
                __append_140355528978496 = __stream_140355528978496.append
                __append_140355528978496('\n                Should the default example content be added to the site?\n              ')
                __msgid_140355528978496 = __re_whitespace(''.join(__stream_140355528978496)).strip()
                if __msgid_140355528978496:
                    __append(translate(__msgid_140355528978496, mapping=None, default=__msgid_140355528978496, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n            </div>\n          </div>')
            __append('\n\n          ')

            # <Static value=<ast.Dict object at 0x7fa711727b20> name=None at 7fa711727280> -> __attrs_140355528978928
            __attrs_140355528978928 = _static_140355528981280

            # <Value 'not:advanced' (140:32)> -> __condition
            __token = 5742
            try:
                __zt_tmp = __attrs_140355528978928
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('not', 'advanced', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="setup_content:boolean" value="true" />')
            __append('\n\n          ')

            # <Static value=<ast.Dict object at 0x7fa71164d070> name=None at 7fa71164d5e0> -> __attrs_140355528086480
            __attrs_140355528086480 = _static_140355528085616

            # <Value 'python: len(base_profiles) > 1' (144:30)> -> __condition
            __token = 5897
            try:
                __zt_tmp = __attrs_140355528086480
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('python', ' len(base_profiles) > 1', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12">\n            ')

                # <Static value=<ast.Dict object at 0x7fa71164da00> name=None at 7fa71164d9a0> -> __attrs_140355528089168
                __attrs_140355528089168 = _static_140355528088064

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3">\n              ')

                # <Static value=<ast.Dict object at 0x7fa71164dd90> name=None at 7fa71164dfa0> -> __attrs_140355539801376
                __attrs_140355539801376 = _static_140355528088976

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="lead">')
                __stream_140355528087584 = []
                __append_140355528087584 = __stream_140355528087584.append
                __append_140355528087584('Base configuration')
                __msgid_140355528087584 = __re_whitespace(''.join(__stream_140355528087584)).strip()
                if __msgid_140355528087584:
                    __append(translate(__msgid_140355528087584, mapping=None, default=__msgid_140355528087584, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>\n\n              ')

                # <Static value=<ast.Dict object at 0x7fa7121791f0> name=None at 7fa712179340> -> __attrs_140355539802048
                __attrs_140355539802048 = _static_140355539800560
                __backup_info_140355515661904 = get('info', __marker)

                # <Value 'base_profiles' (148:36)> -> __iterator
                __token = 6069
                try:
                    __zt_tmp = __attrs_140355539802048
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140355540363392('path', 'base_profiles', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                (__iterator, ____index_140355539800320, ) = getname('repeat')('info', __iterator)
                econtext['info'] = None
                for __item in __iterator:
                    econtext['info'] = __item

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check mb-3">\n                ')

                    # <Static value=<ast.Dict object at 0x7fa712179310> name=None at 7fa712179160> -> __attrs_140355549383168
                    __attrs_140355549383168 = _static_140355539800848

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="radio" name="profile_id:string"')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355549382832
                    __default_140355549382832 = _DEFAULT_MARKER

                    # <Substitution 'info/id' (155:43)> -> __attr_value
                    __token = 6388
                    try:
                        __zt_tmp = __attrs_140355549383168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140355540363392('path', 'info/id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', 'profile', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' class="form-check-input"')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355549383888
                    __default_140355549383888 = _DEFAULT_MARKER

                    # <Substitution 'info/id' (154:41)> -> __attr_id
                    __token = 6336
                    try:
                        __zt_tmp = __attrs_140355549383168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140355540363392('path', 'info/id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355549381392
                    __default_140355549381392 = _DEFAULT_MARKER

                    # <Boolean "python: default_profile==info['id'] and 'checked' or nothing" (156:44)> -> __attr_checked
                    __token = 6442
                    try:
                        __zt_tmp = __attrs_140355549383168
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_140355540363392('python', " default_profile==info['id'] and 'checked' or nothing", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' />\n                ')

                    # <Static value=<ast.Dict object at 0x7fa712a9c130> name=None at 7fa712a9c5e0> -> __attrs_140355549381680
                    __attrs_140355549381680 = _static_140355549380912

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-check-label"')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355549383264
                    __default_140355549383264 = _DEFAULT_MARKER

                    # <Substitution 'info/id' (157:68)> -> __attr_for
                    __token = 6577
                    try:
                        __zt_tmp = __attrs_140355549381680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_140355540363392('path', 'info/id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((' for="%s"' % __attr_for))
                    __append('>')

                    # <Interpolation value=<Substitution '${info/title}' (157:77)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa712a9c190> -> __content_140355621335664
                    __token = 6586
                    __token = 6588
                    try:
                        __zt_tmp = __attrs_140355549381680
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140355621335664 = _static_140355540363392('path', 'info/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
                    __append('</label>\n                ')

                    # <Static value=<ast.Dict object at 0x7fa710a81340> name=None at 7fa710a81c70> -> __attrs_140355515716224
                    __attrs_140355515716224 = _static_140355515716416

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-text">')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355515719152
                    __default_140355515719152 = _DEFAULT_MARKER

                    # <Value 'info/description' (158:52)> -> __cache_140355549383360
                    __token = 6660
                    try:
                        __zt_tmp = __attrs_140355515716224
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355549383360 = _static_140355540363392('path', 'info/description', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'info/description' (158:52)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa710a81f10> -> __condition
                    __expression = __cache_140355549383360

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <Interpolation value=<Substitution '${info/description}' (158:70)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa710a81160> -> __content_140355621335664
                        __token = 6678
                        __token = 6680
                        try:
                            __zt_tmp = __attrs_140355515716224
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_140355621335664 = _static_140355540363392('path', 'info/description', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
                        __content = __cache_140355549383360
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n              </div>')
                    ____index_140355539800320 -= 1
                    if (____index_140355539800320 > 0):
                        __append('\n              ')
                if (__backup_info_140355515661904 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_140355515661904
                __append('\n\n              ')

                # <Static value=<ast.Dict object at 0x7fa710a815b0> name=None at 7fa710a81fd0> -> __attrs_140355515719344
                __attrs_140355515719344 = _static_140355515717040

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-text">')
                __stream_140355515717472 = []
                __append_140355515717472 = __stream_140355515717472.append
                __append_140355515717472("\n                You normally don't need to change anything here unless you have specific reasons and know what you are doing.\n              ")
                __msgid_140355515717472 = __re_whitespace(''.join(__stream_140355515717472)).strip()
                if __msgid_140355515717472:
                    __append(translate(__msgid_140355515717472, mapping=None, default=__msgid_140355515717472, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n\n            </div>\n          </div>')
            __append('\n\n\n          ')

            # <Static value=<ast.Dict object at 0x7fa710a81d60> name=None at 7fa710a81af0> -> __attrs_140355493541728
            __attrs_140355493541728 = _static_140355515719008
            __backup_has_selected_140355516523376 = get('has_selected', __marker)

            # <Value "python:[p for p in extension_profiles if p.get('selected', None)]" (170:40)> -> __value
            __token = 7046
            try:
                __zt_tmp = __attrs_140355493541728
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "[p for p in extension_profiles if p.get('selected', None)]", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['has_selected'] = __value

            # <Value 'python: extension_profiles or advanced' (171:30)> -> __condition
            __token = 7143
            try:
                __zt_tmp = __attrs_140355493541728
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('python', ' extension_profiles or advanced', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <Negate value=<Value 'python: has_selected and not advanced' (172:29)> at 7fa70f55b700> -> __cache_140355493541632

                # <Value 'python: has_selected and not advanced' (172:29)> -> __cache_140355493541632
                __token = 7212
                try:
                    __zt_tmp = __attrs_140355493541728
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140355493541632 = _static_140355540363392('python', ' has_selected and not advanced', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                __cache_140355493541632 = not __cache_140355493541632
                __condition = __cache_140355493541632
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="col-md-12 mt-3">')
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355493541872
                __attrs_140355493541872 = _static_140355540704128

                # <Value 'python: advanced' (173:34)> -> __condition
                __token = 7286
                try:
                    __zt_tmp = __attrs_140355493541872
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('python', ' advanced', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355493541008
                    __attrs_140355493541008 = _static_140355540704128

                    # <h2 ... (0:0)
                    # --------------------------------------------------------
                    __append('<h2>')
                    __stream_140355493540192 = []
                    __append_140355493540192 = __stream_140355493540192.append
                    __append_140355493540192('Add-ons')
                    __msgid_140355493540192 = __re_whitespace(''.join(__stream_140355493540192)).strip()
                    if __msgid_140355493540192:
                        __append(translate(__msgid_140355493540192, mapping=None, default=__msgid_140355493540192, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</h2>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7fa712abaf70> name=None at 7fa712aba370> -> __attrs_140355549505856
                    __attrs_140355549505856 = _static_140355549507440

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="lead" >')
                    __stream_140355493539952 = []
                    __append_140355493539952 = __stream_140355493539952.append
                    __append_140355493539952('\n                Select any add-ons you want to activate immediately.\n                You can also activate add-ons after the site has been created using the Add-ons control panel.\n              ')
                    __msgid_140355493539952 = __re_whitespace(''.join(__stream_140355493539952)).strip()
                    if __msgid_140355493539952:
                        __append(translate(__msgid_140355493539952, mapping=None, default=__msgid_140355493539952, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</div>\n            ')
                __append('\n\n            ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355549507008
                __attrs_140355549507008 = _static_140355540704128
                __backup_info_140355515658592 = get('info', __marker)

                # <Value 'extension_profiles' (183:39)> -> __iterator
                __token = 7692
                try:
                    __zt_tmp = __attrs_140355549507008
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140355540363392('path', 'extension_profiles', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                (__iterator, ____index_140355549507536, ) = getname('repeat')('info', __iterator)
                econtext['info'] = None
                for __item in __iterator:
                    econtext['info'] = __item
                    __append('\n              ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355549505520
                    __attrs_140355549505520 = _static_140355540704128
                    __backup_selected_140355517407872 = get('selected', __marker)

                    # <Value 'info/selected|nothing' (184:44)> -> __value
                    __token = 7757
                    try:
                        __zt_tmp = __attrs_140355549505520
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('path', 'info/selected|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['selected'] = __value
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355549505952
                    __attrs_140355549505952 = _static_140355540704128

                    # <Value 'python: not selected or advanced' (185:43)> -> __condition
                    __token = 7824
                    try:
                        __zt_tmp = __attrs_140355549505952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('python', ' not selected or advanced', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7fa712146070> name=None at 7fa712146850> -> __attrs_140355539594832
                        __attrs_140355539594832 = _static_140355539591280

                        # <Value 'python: advanced' (187:37)> -> __condition
                        __token = 7943
                        try:
                            __zt_tmp = __attrs_140355539594832
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140355540363392('python', ' advanced', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        if __condition:

                            # <div ... (0:0)
                            # --------------------------------------------------------
                            __append('<div class="form-check mb-3">\n                    ')

                            # <Static value=<ast.Dict object at 0x7fa7121468b0> name=None at 7fa712146040> -> __attrs_140355524561120
                            __attrs_140355524561120 = _static_140355539593392

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="checkbox" name="extension_ids:list"')

                            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355539592288
                            __default_140355539592288 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${info/id}' (190:33)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa712146100> -> __attr_value
                            __token = 8090
                            __token = 8092
                            try:
                                __zt_tmp = __attrs_140355524561120
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140355540363392('path', 'info/id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_value = __attr_value
                            if (__attr_value is None):
                                pass
                            else:
                                if (__attr_value is _DEFAULT_MARKER):
                                    __attr_value = None
                                else:
                                    __tt = type(__attr_value)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_value = str(__attr_value)
                                    else:
                                        if (__tt is bytes):
                                            __attr_value = decode(__attr_value)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_value = __attr_value.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_value)
                                                    __attr_value = (str(__attr_value) if (__attr_value is __converted) else __converted)
                                                else:
                                                    __attr_value = __attr_value()
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))

                            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355524559920
                            __default_140355524559920 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${info/id}' (191:30)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa7112f01f0> -> __attr_id
                            __token = 8132
                            __token = 8134
                            try:
                                __zt_tmp = __attrs_140355524561120
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_id = _static_140355540363392('path', 'info/id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_id = __attr_id
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
                            __append(' class="form-check-input"')

                            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355524561312
                            __default_140355524561312 = _DEFAULT_MARKER

                            # <Boolean 'info/selected|nothing' (193:50)> -> __attr_checked
                            __token = 8245
                            try:
                                __zt_tmp = __attrs_140355524561120
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_checked = _static_140355540363392('path', 'info/selected|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            if (__attr_checked is _DEFAULT_MARKER):
                                __attr_checked = None
                            else:
                                if __attr_checked:
                                    __attr_checked = 'checked'
                                else:
                                    __attr_checked = None
                            if (__attr_checked is not None):
                                __append((' checked="%s"' % __attr_checked))
                            __append(' />\n                    ')

                            # <Static value=<ast.Dict object at 0x7fa7112f0370> name=None at 7fa7112f07c0> -> __attrs_140355524561696
                            __attrs_140355524561696 = _static_140355524559728

                            # <label ... (0:0)
                            # --------------------------------------------------------
                            __append('<label class="form-check-label"')

                            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355524561888
                            __default_140355524561888 = _DEFAULT_MARKER

                            # <Interpolation value=<Substitution '${info/id}' (194:57)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa7112f0c40> -> __attr_for
                            __token = 8329
                            __token = 8331
                            try:
                                __zt_tmp = __attrs_140355524561696
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_for = _static_140355540363392('path', 'info/id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                            __attr_for = __attr_for
                            if (__attr_for is None):
                                pass
                            else:
                                if (__attr_for is _DEFAULT_MARKER):
                                    __attr_for = None
                                else:
                                    __tt = type(__attr_for)
                                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                                        __attr_for = str(__attr_for)
                                    else:
                                        if (__tt is bytes):
                                            __attr_for = decode(__attr_for)
                                        else:
                                            if (__tt is not str):
                                                try:
                                                    __attr_for = __attr_for.__html__
                                                except get('AttributeError', AttributeError):
                                                    __converted = convert(__attr_for)
                                                    __attr_for = (str(__attr_for) if (__attr_for is __converted) else __converted)
                                                else:
                                                    __attr_for = __attr_for()
                            if (__attr_for is not None):
                                __append((' for="%s"' % __attr_for))
                            __append(' >')

                            # <Interpolation value=<Substitution '${info/title}' (194:70)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa7112f0760> -> __content_140355621335664
                            __token = 8342
                            __token = 8344
                            try:
                                __zt_tmp = __attrs_140355524561696
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __content_140355621335664 = _static_140355540363392('path', 'info/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
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
                            __append('</label>\n                    ')

                            # <Static value=<ast.Dict object at 0x7fa7112309d0> name=None at 7fa711230df0> -> __attrs_140355523772480
                            __attrs_140355523772480 = _static_140355523774928

                            # <Value "python: advanced and info['description']" (196:39)> -> __condition
                            __token = 8446
                            try:
                                __zt_tmp = __attrs_140355523772480
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __condition = _static_140355540363392('python', " advanced and info['description']", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            if __condition:

                                # <div ... (0:0)
                                # --------------------------------------------------------
                                __append('<div class="form-text">')

                                # <Interpolation value=<Substitution '\n                      ${info/description}\n                    ' (196:81)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa711230760> -> __content_140355621335664
                                __token = 8511
                                __token = 8513
                                try:
                                    __zt_tmp = __attrs_140355523772480
                                except get('NameError', NameError):
                                    __zt_tmp = None

                                __content_140355621335664 = _static_140355540363392('path', 'info/description', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                                __content_140355621335664 = __quote(__content_140355621335664, '\x00', '&#0;', None, None)
                                __content_140355621335664 = ('%s%s%s' % ('\n                      ', (__content_140355621335664 if (__content_140355621335664 is not None) else ''), '\n                    ', ))
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
                                __append('</div>')
                            __append('\n                  </div>')
                        __append('\n                ')
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355523772528
                    __attrs_140355523772528 = _static_140355540704128

                    # <Value 'python: selected and not advanced' (201:43)> -> __condition
                    __token = 8656
                    try:
                        __zt_tmp = __attrs_140355523772528
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('python', ' selected and not advanced', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7fa711230730> name=None at 7fa7112301c0> -> __attrs_140355523772672
                        __attrs_140355523772672 = _static_140355523774256

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="hidden" name="extension_ids:list"')

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355523773344
                        __default_140355523773344 = _DEFAULT_MARKER

                        # <Interpolation value=<Substitution '${info/id}' (204:31)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa7112307c0> -> __attr_value
                        __token = 8812
                        __token = 8814
                        try:
                            __zt_tmp = __attrs_140355523772672
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140355540363392('path', 'info/id', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        __attr_value = __attr_value
                        if (__attr_value is None):
                            pass
                        else:
                            if (__attr_value is _DEFAULT_MARKER):
                                __attr_value = None
                            else:
                                __tt = type(__attr_value)
                                if ((__tt is int) or (__tt is float) or (__tt is int)):
                                    __attr_value = str(__attr_value)
                                else:
                                    if (__tt is bytes):
                                        __attr_value = decode(__attr_value)
                                    else:
                                        if (__tt is not str):
                                            try:
                                                __attr_value = __attr_value.__html__
                                            except get('AttributeError', AttributeError):
                                                __converted = convert(__attr_value)
                                                __attr_value = (str(__attr_value) if (__attr_value is __converted) else __converted)
                                            else:
                                                __attr_value = __attr_value()
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n                ')
                    __append('\n              ')
                    if (__backup_selected_140355517407872 is __marker):
                        del econtext['selected']
                    else:
                        econtext['selected'] = __backup_selected_140355517407872
                    __append('\n            ')
                    ____index_140355549507536 -= 1
                    if (____index_140355549507536 > 0):
                        __append('')
                if (__backup_info_140355515658592 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_140355515658592
                __append('\n          ')
                __condition = __cache_140355493541632
                if __condition:
                    __append('</div>')
            if (__backup_has_selected_140355516523376 is __marker):
                del econtext['has_selected']
            else:
                econtext['has_selected'] = __backup_has_selected_140355516523376
            __append('\n          ')

            # <Static value=<ast.Dict object at 0x7fa70f55bbb0> name=None at 7fa70f55b910> -> __attrs_140355549504512
            __attrs_140355549504512 = _static_140355493542832

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12 mt-3">\n            ')

            # <Static value=<ast.Dict object at 0x7fa711ed0460> name=None at 7fa711ed0250> -> __attrs_140355537013488
            __attrs_140355537013488 = _static_140355537011808

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="form.submitted:boolean" value="True" />\n            ')

            # <Static value=<ast.Dict object at 0x7fa70f558a00> name=None at 7fa70f558e50> -> __attrs_140355493528672
            __attrs_140355493528672 = _static_140355493530112

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button class="btn btn-success mt-3" type="submit" name="submit">')
            __stream_140355537011088 = []
            __append_140355537011088 = __stream_140355537011088.append
            __append_140355537011088('Create Plone Site')
            __msgid_140355537011088 = __re_whitespace(''.join(__stream_140355537011088)).strip()
            if __msgid_140355537011088:
                __append(translate(__msgid_140355537011088, mapping=None, default=__msgid_140355537011088, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n          </div>\n      </article>\n    </form>')
            if (__backup_advanced_140355516900688 is __marker):
                del econtext['advanced']
            else:
                econtext['advanced'] = __backup_advanced_140355516900688
            if (__backup_extension_profiles_140355516901600 is __marker):
                del econtext['extension_profiles']
            else:
                econtext['extension_profiles'] = __backup_extension_profiles_140355516901600
            if (__backup_default_profile_140355516900544 is __marker):
                del econtext['default_profile']
            else:
                econtext['default_profile'] = __backup_default_profile_140355516900544
            if (__backup_base_profiles_140355516900592 is __marker):
                del econtext['base_profiles']
            else:
                econtext['base_profiles'] = __backup_base_profiles_140355516900592
            if (__backup_profiles_140355517998560 is __marker):
                del econtext['profiles']
            else:
                econtext['profiles'] = __backup_profiles_140355517998560
            __append('\n  </div>\n</body>\n\n</html>')
            __i18n_domain = __previous_i18n_domain_140355529455072
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }