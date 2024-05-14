# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/Products.CMFPlone-6.0.11-py3.9.egg/Products/CMFPlone/browser/templates/plone-overview.pt'

__tokens = {581: ('${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', 16, 14), 583: ('string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css', 16, 16), 727: ('${string:${context/absolute_url}/++resource++plone-admin-ui.css}', 19, 14), 729: ('string:${context/absolute_url}/++resource++plone-admin-ui.css', 19, 16), 830: ('view/sites', 23, 24), 864: (' python:len(sites) > ', 24, 22), 1087: ('string:${context/absolute_url}/++resource++plone-logo.svg', 29, 36), 1755: ('sites', 44, 28), 1802: ('sites', 45, 39), 1852: ('python: view.outdated(site)', 46, 42), 1910: ("mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}", 47, 28), 1917: ("python: 'p-3 alert alert-warning' if outdated else ''", 47, 35), 2012: ('outdated', 48, 38), 2285: ('site/absolute_url', 50, 45), 2166: ("btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}", 49, 60), 2184: ("python:'btn-lg' if not many and not outdated  else ''", 49, 78), 2450: ('not: many', 53, 44), 2555: ('many', 54, 45), 2561: ('${python:site.title}', 54, 51), 2563: ('python:site.title', 54, 53), 2589: ('(${python:"/".join(site.getPhysicalPath())})', 54, 79), 2592: ('python:"/".join(site.getPhysicalPath())', 54, 82), 2851: ('outdated', 59, 43), 2912: ('python:view.upgrade_url(site)', 60, 51), 2990: ('not:view/can_manage', 61, 46), 3128: ('python:view.upgrade_url(site, can_manage=True)', 63, 54), 3620: ('sites', 74, 30), 3770: ('not:sites', 78, 30), 4017: ("python: '' if not sites else len(sites) + 1", 84, 44), 4100: (' string:${context/absolute_url}/@@plone-addsit', 85, 38), 4177: ('${action}', 86, 28), 4179: ('action', 86, 30), 4248: ('Plone${site_number}', 87, 59), 4255: ('site_number', 87, 66), 4341: ("btn btn-${python:'success' if sites else 'primary'}", 89, 31), 4351: ("python:'success' if sites else 'primary'", 89, 41), 4582: ('view/has_volto', 93, 35), 4624: ('${action}?site_id=Plone${site_number}&amp;classic=1', 94, 26), 4626: ('action', 94, 28), 4649: ('site_number', 94, 51), 4840: ('${action}?site_id=Plone${site_number}&amp;advanced=1', 98, 26), 4842: ('action', 98, 28), 4865: ('site_number', 98, 51), 6200: ('string:${context/absolute_url}/manage_main', 126, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355527531392 = {'href': '#', 'title': 'Go to the ZMI', }
_static_140355538415424 = {'class': 'row', }
_static_140355538414176 = {'href': 'https://6.docs.plone.org/', 'title': 'Plone 6 developer documentation', }
_static_140355538405600 = {'class': 'btn btn-secondary', 'href': '${action}?site_id=Plone${site_number}&amp;advanced=1', }
_static_140355538399088 = {'class': 'btn btn-info', 'href': '${action}?site_id=Plone${site_number}&amp;classic=1', }
_static_140355538397648 = {'type': 'submit', 'class': "btn btn-${python:'success' if sites else 'primary'}", }
_static_140355538390944 = {'type': 'hidden', 'name': 'site_id', 'value': 'Plone${site_number}', }
_static_140355538389072 = {'id': 'add-plone-site', 'method': 'get', 'action': '${action}', }
_static_140355539804064 = {'class': 'alert alert-warning p-1', }
_static_140355539792848 = {'class': 'col-md-12', }
_static_140355539795824 = {'type': 'submit', 'class': 'btn btn-warning me-3', }
_static_140355539794336 = {'type': 'hidden', 'name': 'came_from', 'value': 'python:view.upgrade_url(site, can_manage=True)', }
_static_140355539648416 = {'action': '', 'style': 'display: inline;', 'method': 'get', }
_static_140355539595120 = {'href': '#', 'id': 'go-to-site-link', 'class': "btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}", 'title': 'Go to your instance', }
_static_140355516485200 = {'class': "mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}", }
_static_140355516482560 = {'class': 'col-md-12 mb-4', }
_static_140355537653424 = {'class': 'row mb-5', }
_static_140355537652224 = {'href': 'http://plone.org', 'title': 'Plone Community Home', }
_static_140355540352832 = {'class': 'lead', }
_static_140355540351968 = {'src': '/++resource++plone-logo.svg', 'width': '215', 'height': '56', 'alt': 'Plone logo', }
_static_140355540245904 = {'class': 'row', }
_static_140355540244608 = {'class': 'container admin mt-5 mb-5 p-4', }
_static_140355540098544 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++resource++plone-admin-ui.css}', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355540096720 = {'rel': 'stylesheet', 'type': 'text/css', 'href': '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}', }
_static_140355537012144 = {'name': 'viewport', 'content': 'width=device-width, initial-scale=1', }
_static_140355537548288 = {'charset': 'utf-8', }
_static_140355540704128 = {}
_static_140355482864896 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }

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
            __append('<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n')

            # <Static value=<ast.Dict object at 0x7fa70eb2cd00> name=None at 7fa70eb2c760> -> __attrs_140355537549872
            __attrs_140355537549872 = _static_140355482864896
            __previous_i18n_domain_140355537550448 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n\n')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537548912
            __attrs_140355537548912 = _static_140355540704128

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n  ')

            # <Static value=<ast.Dict object at 0x7fa711f53400> name=None at 7fa711f530a0> -> __attrs_140355537551168
            __attrs_140355537551168 = _static_140355537548288

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8"/>\n  ')

            # <Static value=<ast.Dict object at 0x7fa711ed05b0> name=None at 7fa711ed0df0> -> __attrs_140355537011568
            __attrs_140355537011568 = _static_140355537012144

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="viewport" content="width=device-width, initial-scale=1"/>\n  ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355540095376
            __attrs_140355540095376 = _static_140355540704128

            # <title ... (0:0)
            # --------------------------------------------------------
            __append('<title>Plone</title>\n  ')

            # <Static value=<ast.Dict object at 0x7fa7121c16d0> name=None at 7fa7121c1700> -> __attrs_140355540097296
            __attrs_140355540097296 = _static_140355540096720

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355540096864
            __default_140355540096864 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++theme++barceloneta/css/barceloneta.min.css}' (16:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa7121c1400> -> __attr_href
            __token = 581
            __token = 583
            try:
                __zt_tmp = __attrs_140355540097296
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

            # <Static value=<ast.Dict object at 0x7fa7121c1df0> name=None at 7fa7121c1e20> -> __attrs_140355540242544
            __attrs_140355540242544 = _static_140355540098544

            # <link ... (0:0)
            # --------------------------------------------------------
            __append('<link rel="stylesheet" type="text/css"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355540098688
            __default_140355540098688 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${string:${context/absolute_url}/++resource++plone-admin-ui.css}' (19:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa7121c1b20> -> __attr_href
            __token = 727
            __token = 729
            try:
                __zt_tmp = __attrs_140355540242544
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
            __append(' />\n</head>\n\n\n')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355540243312
            __attrs_140355540243312 = _static_140355540704128
            __backup_sites_140355524214992 = get('sites', __marker)

            # <Value 'view/sites' (23:24)> -> __value
            __token = 830
            try:
                __zt_tmp = __attrs_140355540243312
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/sites', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['sites'] = __value
            __backup_many_140355524215184 = get('many', __marker)

            # <Value 'python:len(sites) > 1' (24:22)> -> __value
            __token = 864
            try:
                __zt_tmp = __attrs_140355540243312
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', 'len(sites) > 1', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['many'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body>\n  ')

            # <Static value=<ast.Dict object at 0x7fa7121e5880> name=None at 7fa7121e56d0> -> __attrs_140355540244944
            __attrs_140355540244944 = _static_140355540244608

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="container admin mt-5 mb-5 p-4">\n    ')

            # <Static value=<ast.Dict object at 0x7fa7121e5d90> name=None at 7fa7121e5dc0> -> __attrs_140355540246288
            __attrs_140355540246288 = _static_140355540245904

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header class="row">\n        ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355540349712
            __attrs_140355540349712 = _static_140355540704128

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')

            # <Static value=<ast.Dict object at 0x7fa7121ffbe0> name=None at 7fa7121ffc10> -> __attrs_140355540351056
            __attrs_140355540351056 = _static_140355540351968

            # <img ... (0:0)
            # --------------------------------------------------------
            __append('<img')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355537012000
            __default_140355537012000 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/++resource++plone-logo.svg' (29:36)> -> __attr_src
            __token = 1087
            try:
                __zt_tmp = __attrs_140355540351056
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_src = _static_140355540363392('string', '${context/absolute_url}/++resource++plone-logo.svg', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_src = __quote(__attr_src, '"', '&quot;', '/++resource++plone-logo.svg', _DEFAULT_MARKER)
            if (__attr_src is not None):
                __append((' src="%s"' % __attr_src))
            __append(' width="215" height="56"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355540351104
            __default_140355540351104 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7fa711f53d90> at 7fa711f53d30> -> __attr_alt
            __attr_alt = 'Plone logo'
            __attr_alt = translate(__attr_alt, default=__attr_alt, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_alt is not None):
                __append((' alt="%s"' % __attr_alt))
            __append(' /></p>\n        ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355540350288
            __attrs_140355540350288 = _static_140355540704128

            # <h1 ... (0:0)
            # --------------------------------------------------------
            __append('<h1>')
            __stream_140355540350960 = []
            __append_140355540350960 = __stream_140355540350960.append
            __append_140355540350960('Plone is up and running.')
            __msgid_140355540350960 = __re_whitespace(''.join(__stream_140355540350960)).strip()
            if __msgid_140355540350960:
                __append(translate(__msgid_140355540350960, mapping=None, default=__msgid_140355540350960, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h1>\n        ')

            # <Static value=<ast.Dict object at 0x7fa7121fff40> name=None at 7fa7121fff70> -> __attrs_140355537649920
            __attrs_140355537649920 = _static_140355540352832

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p class="lead">\n            ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537650976
            __attrs_140355537650976 = _static_140355540704128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_140355537650496 = []
            __append_140355537650496 = __stream_140355537650496.append
            __append_140355537650496(' For an introduction to Plone, documentation, demos, add-ons, support, and community, visit')
            __msgid_140355537650496 = __re_whitespace(''.join(__stream_140355537650496)).strip()
            if 'label_plone_org_description':
                __append(translate('label_plone_org_description', mapping=None, default=__msgid_140355537650496, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n            ')

            # <Static value=<ast.Dict object at 0x7fa711f6ca00> name=None at 7fa711f6ca30> -> __attrs_140355537652752
            __attrs_140355537652752 = _static_140355537652224

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a href="http://plone.org"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355537651504
            __default_140355537651504 = _DEFAULT_MARKER

            # <Translate msgid='label_plone_org_title' node=<ast.Constant object at 0x7fa711f6c820> at 7fa711f6c7f0> -> __attr_title
            __attr_title = 'Plone Community Home'
            __attr_title = translate('label_plone_org_title', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>plone.org</a>.\n          </p>\n\n    </header>\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa711f6ceb0> name=None at 7fa711f6cee0> -> __attrs_140355516481648
            __attrs_140355516481648 = _static_140355537653424

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article class="row mb-5">\n        ')

            # <Static value=<ast.Dict object at 0x7fa710b3c400> name=None at 7fa710b3c430> -> __attrs_140355516482992
            __attrs_140355516482992 = _static_140355516482560

            # <Value 'sites' (44:28)> -> __condition
            __token = 1755
            try:
                __zt_tmp = __attrs_140355516482992
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'sites', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="col-md-12 mb-4">\n            ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355516484048
                __attrs_140355516484048 = _static_140355540704128
                __backup_site_140355524084832 = get('site', __marker)

                # <Value 'sites' (45:39)> -> __iterator
                __token = 1802
                try:
                    __zt_tmp = __attrs_140355516484048
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140355540363392('path', 'sites', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                (__iterator, ____index_140355516484288, ) = getname('repeat')('site', __iterator)
                econtext['site'] = None
                for __item in __iterator:
                    econtext['site'] = __item
                    __append('\n                ')

                    # <Static value=<ast.Dict object at 0x7fa710b3ce50> name=None at 7fa710b3ce80> -> __attrs_140355539591664
                    __attrs_140355539591664 = _static_140355516485200
                    __backup_outdated_140355523667904 = get('outdated', __marker)

                    # <Value 'python: view.outdated(site)' (46:42)> -> __value
                    __token = 1852
                    try:
                        __zt_tmp = __attrs_140355539591664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140355540363392('python', ' view.outdated(site)', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    econtext['outdated'] = __value

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355516485392
                    __default_140355516485392 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "mb-3 ${python: 'p-3 alert alert-warning' if outdated else ''}" (47:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa710b3cd00> -> __attr_class
                    __token = 1910
                    __token = 1917
                    try:
                        __zt_tmp = __attrs_140355539591664
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140355540363392('python', " 'p-3 alert alert-warning' if outdated else ''", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('mb-3 ', (__attr_class if (__attr_class is not None) else ''), ))
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
                    __append('>\n                    ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355539592768
                    __attrs_140355539592768 = _static_140355540704128

                    # <Value 'outdated' (48:38)> -> __condition
                    __token = 2012
                    try:
                        __zt_tmp = __attrs_140355539592768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('path', 'outdated', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:

                        # <p ... (0:0)
                        # --------------------------------------------------------
                        __append('<p>')
                        __stream_140355539592288 = []
                        __append_140355539592288 = __stream_140355539592288.append
                        __append_140355539592288('This site configuration is outdated and needs to be upgraded:')
                        __msgid_140355539592288 = __re_whitespace(''.join(__stream_140355539592288)).strip()
                        if __msgid_140355539592288:
                            __append(translate(__msgid_140355539592288, mapping=None, default=__msgid_140355539592288, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</p>')
                    __append('\n                    ')

                    # <Static value=<ast.Dict object at 0x7fa712146f70> name=None at 7fa712146fa0> -> __attrs_140355539644960
                    __attrs_140355539644960 = _static_140355539595120

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355539594640
                    __default_140355539594640 = _DEFAULT_MARKER

                    # <Substitution 'site/absolute_url' (50:45)> -> __attr_href
                    __token = 2285
                    try:
                        __zt_tmp = __attrs_140355539644960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140355540363392('path', 'site/absolute_url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' id="go-to-site-link"')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355539593968
                    __default_140355539593968 = _DEFAULT_MARKER

                    # <Interpolation value=<Substitution "btn btn-primary ${python:'btn-lg' if not many and not outdated  else ''}" (49:60)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa712146b80> -> __attr_class
                    __token = 2166
                    __token = 2184
                    try:
                        __zt_tmp = __attrs_140355539644960
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140355540363392('python', "'btn-lg' if not many and not outdated  else ''", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    __attr_class = ('%s%s' % ('btn btn-primary ', (__attr_class if (__attr_class is not None) else ''), ))
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

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355539595216
                    __default_140355539595216 = _DEFAULT_MARKER

                    # <Translate msgid=None node=<ast.Constant object at 0x7fa7121469a0> at 7fa712146970> -> __attr_title
                    __attr_title = 'Go to your instance'
                    __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('>\n                        ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355539645920
                    __attrs_140355539645920 = _static_140355540704128

                    # <Value 'not: many' (53:44)> -> __condition
                    __token = 2450
                    try:
                        __zt_tmp = __attrs_140355539645920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('not', ' many', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:
                        __stream_140355539645536 = []
                        __append_140355539645536 = __stream_140355539645536.append
                        __append_140355539645536('View your Plone site')
                        __msgid_140355539645536 = __re_whitespace(''.join(__stream_140355539645536)).strip()
                        if __msgid_140355539645536:
                            __append(translate(__msgid_140355539645536, mapping=None, default=__msgid_140355539645536, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('\n                        ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355539646592
                    __attrs_140355539646592 = _static_140355540704128

                    # <Value 'many' (54:45)> -> __condition
                    __token = 2555
                    try:
                        __zt_tmp = __attrs_140355539646592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('path', 'many', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:

                        # <Interpolation value=<Substitution '${python:site.title} ' (54:51)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa712153a90> -> __content_140355621335664
                        __token = 2561
                        __token = 2563
                        try:
                            __zt_tmp = __attrs_140355539646592
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_140355621335664 = _static_140355540363392('python', 'site.title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        __content_140355621335664 = __quote(__content_140355621335664, '\x00', '&#0;', None, None)
                        __content_140355621335664 = ('%s%s' % ((__content_140355621335664 if (__content_140355621335664 is not None) else ''), ' ', ))
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

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355539647792
                        __attrs_140355539647792 = _static_140355540704128

                        # <small ... (0:0)
                        # --------------------------------------------------------
                        __append('<small>')

                        # <Interpolation value=<Substitution '(${python:"/".join(site.getPhysicalPath())})' (54:79)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa712153e50> -> __content_140355621335664
                        __token = 2589
                        __token = 2592
                        try:
                            __zt_tmp = __attrs_140355539647792
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __content_140355621335664 = _static_140355540363392('python', '"/".join(site.getPhysicalPath())', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        __content_140355621335664 = __quote(__content_140355621335664, '\x00', '&#0;', None, None)
                        __content_140355621335664 = ('%s%s%s' % ('(', (__content_140355621335664 if (__content_140355621335664 is not None) else ''), ')', ))
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
                        __append('</small>')
                    __append('\n                    </a>\n                    ')

                    # <Static value=<ast.Dict object at 0x7fa712153fa0> name=None at 7fa712153fd0> -> __attrs_140355539792656
                    __attrs_140355539792656 = _static_140355539648416

                    # <Value 'outdated' (59:43)> -> __condition
                    __token = 2851
                    try:
                        __zt_tmp = __attrs_140355539792656
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('path', 'outdated', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:

                        # <form ... (0:0)
                        # --------------------------------------------------------
                        __append('<form')

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355539645680
                        __default_140355539645680 = _DEFAULT_MARKER

                        # <Substitution 'python:view.upgrade_url(site)' (60:51)> -> __attr_action
                        __token = 2912
                        try:
                            __zt_tmp = __attrs_140355539792656
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_action = _static_140355540363392('python', 'view.upgrade_url(site)', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                        if (__attr_action is not None):
                            __append((' action="%s"' % __attr_action))
                        __append(' style="display: inline;" method="get">\n                        ')

                        # <Static value=<ast.Dict object at 0x7fa7121779a0> name=None at 7fa7121779d0> -> __attrs_140355539794816
                        __attrs_140355539794816 = _static_140355539794336

                        # <Value 'not:view/can_manage' (61:46)> -> __condition
                        __token = 2990
                        try:
                            __zt_tmp = __attrs_140355539794816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140355540363392('not', 'view/can_manage', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden" name="came_from"')

                            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355539793472
                            __default_140355539793472 = _DEFAULT_MARKER

                            # <Substitution 'python:view.upgrade_url(site, can_manage=True)' (63:54)> -> __attr_value
                            __token = 3128
                            try:
                                __zt_tmp = __attrs_140355539794816
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140355540363392('python', 'view.upgrade_url(site, can_manage=True)', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append('/>')
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x7fa712177f70> name=None at 7fa712177fa0> -> __attrs_140355539800608
                        __attrs_140355539800608 = _static_140355539795824

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" class="btn btn-warning me-3">')
                        __stream_140355539795344 = []
                        __append_140355539795344 = __stream_140355539795344.append
                        __append_140355539795344('Upgrade&hellip;')
                        __msgid_140355539795344 = __re_whitespace(''.join(__stream_140355539795344)).strip()
                        if 'label_upgrade_hellip':
                            __append(translate('label_upgrade_hellip', mapping=None, default=__msgid_140355539795344, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</button>\n                    </form>')
                    __append('\n                </div>')
                    if (__backup_outdated_140355523667904 is __marker):
                        del econtext['outdated']
                    else:
                        econtext['outdated'] = __backup_outdated_140355523667904
                    __append('\n            ')
                    ____index_140355516484288 -= 1
                    if (____index_140355516484288 > 0):
                        __append('')
                if (__backup_site_140355524084832 is __marker):
                    del econtext['site']
                else:
                    econtext['site'] = __backup_site_140355524084832
                __append('\n        </div>')
            __append('\n        ')

            # <Static value=<ast.Dict object at 0x7fa7121773d0> name=None at 7fa712177520> -> __attrs_140355539801184
            __attrs_140355539801184 = _static_140355539792848

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="col-md-12">\n            ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355539802240
            __attrs_140355539802240 = _static_140355540704128

            # <h2 ... (0:0)
            # --------------------------------------------------------
            __append('<h2 >')
            __stream_140355539801760 = []
            __append_140355539801760 = __stream_140355539801760.append
            __append_140355539801760('Add Plone site')
            __msgid_140355539801760 = __re_whitespace(''.join(__stream_140355539801760)).strip()
            if __msgid_140355539801760:
                __append(translate(__msgid_140355539801760, mapping=None, default=__msgid_140355539801760, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</h2>\n            ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355539803200
            __attrs_140355539803200 = _static_140355540704128

            # <Value 'sites' (74:30)> -> __condition
            __token = 3620
            try:
                __zt_tmp = __attrs_140355539803200
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'sites', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p>')
                __stream_140355539802720 = []
                __append_140355539802720 = __stream_140355539802720.append
                __append_140355539802720('\n                You can add another Plone site to the server.\n            ')
                __msgid_140355539802720 = __re_whitespace(''.join(__stream_140355539802720)).strip()
                if __msgid_140355539802720:
                    __append(translate(__msgid_140355539802720, mapping=None, default=__msgid_140355539802720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7fa712179fa0> name=None at 7fa712179f40> -> __attrs_140355538387584
            __attrs_140355538387584 = _static_140355539804064

            # <Value 'not:sites' (78:30)> -> __condition
            __token = 3770
            try:
                __zt_tmp = __attrs_140355538387584
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('not', 'sites', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <p ... (0:0)
                # --------------------------------------------------------
                __append('<p class="alert alert-warning p-1">')
                __stream_140355539803872 = []
                __append_140355539803872 = __stream_140355539803872.append
                __append_140355539803872('\n                Your Plone site has not been added yet.\n            ')
                __msgid_140355539803872 = __re_whitespace(''.join(__stream_140355539803872)).strip()
                if __msgid_140355539803872:
                    __append(translate(__msgid_140355539803872, mapping=None, default=__msgid_140355539803872, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</p>')
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7fa712020850> name=None at 7fa712020880> -> __attrs_140355538389744
            __attrs_140355538389744 = _static_140355538389072
            __backup_site_number_140355524217392 = get('site_number', __marker)

            # <Value "python: '' if not sites else len(sites) + 1" (84:44)> -> __value
            __token = 4017
            try:
                __zt_tmp = __attrs_140355538389744
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', " '' if not sites else len(sites) + 1", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['site_number'] = __value
            __backup_action_140355527176880 = get('action', __marker)

            # <Value 'string:${context/absolute_url}/@@plone-addsite' (85:38)> -> __value
            __token = 4100
            try:
                __zt_tmp = __attrs_140355538389744
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('string', '${context/absolute_url}/@@plone-addsite', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['action'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form id="add-plone-site" method="get"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355538388256
            __default_140355538388256 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${action}' (86:28)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa7120205e0> -> __attr_action
            __token = 4177
            __token = 4179
            try:
                __zt_tmp = __attrs_140355538389744
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140355540363392('path', 'action', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_action = __attr_action
            if (__attr_action is None):
                pass
            else:
                if (__attr_action is _DEFAULT_MARKER):
                    __attr_action = None
                else:
                    __tt = type(__attr_action)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_action = str(__attr_action)
                    else:
                        if (__tt is bytes):
                            __attr_action = decode(__attr_action)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_action = __attr_action.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_action)
                                    __attr_action = (str(__attr_action) if (__attr_action is __converted) else __converted)
                                else:
                                    __attr_action = __attr_action()
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n                ')

            # <Static value=<ast.Dict object at 0x7fa712020fa0> name=None at 7fa712020fd0> -> __attrs_140355538396352
            __attrs_140355538396352 = _static_140355538390944

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input type="hidden" name="site_id"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355538395248
            __default_140355538395248 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution 'Plone${site_number}' (87:59)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa712022100> -> __attr_value
            __token = 4248
            __token = 4255
            try:
                __zt_tmp = __attrs_140355538396352
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_value = _static_140355540363392('path', 'site_number', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_value = ('%s%s' % ('Plone', (__attr_value if (__attr_value is not None) else ''), ))
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

            # <Static value=<ast.Dict object at 0x7fa7120229d0> name=None at 7fa712022a00> -> __attrs_140355538398080
            __attrs_140355538398080 = _static_140355538397648

            # <button ... (0:0)
            # --------------------------------------------------------
            __append('<button type="submit"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355538397024
            __default_140355538397024 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "btn btn-${python:'success' if sites else 'primary'}" (89:31)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa712022820> -> __attr_class
            __token = 4341
            __token = 4351
            try:
                __zt_tmp = __attrs_140355538398080
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140355540363392('python', "'success' if sites else 'primary'", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = ('%s%s' % ('btn btn-', (__attr_class if (__attr_class is not None) else ''), ))
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
            __append('>')
            __stream_140355538396736 = []
            __append_140355538396736 = __stream_140355538396736.append
            __append_140355538396736('Create a new Plone site')
            __msgid_140355538396736 = __re_whitespace(''.join(__stream_140355538396736)).strip()
            if __msgid_140355538396736:
                __append(translate(__msgid_140355538396736, mapping=None, default=__msgid_140355538396736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</button>\n                ')

            # <Static value=<ast.Dict object at 0x7fa712022f70> name=None at 7fa712022fd0> -> __attrs_140355538404064
            __attrs_140355538404064 = _static_140355538399088

            # <Value 'view/has_volto' (93:35)> -> __condition
            __token = 4582
            try:
                __zt_tmp = __attrs_140355538404064
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('path', 'view/has_volto', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="btn btn-info"')

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355538403536
                __default_140355538403536 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${action}?site_id=Plone${site_number}&amp;classic=1' (94:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa712024160> -> __attr_href
                __token = 4624
                __token = 4626
                try:
                    __zt_tmp = __attrs_140355538404064
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140355540363392('path', 'action', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                __token = 4649
                try:
                    __zt_tmp = __attrs_140355538404064
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href_4647 = _static_140355540363392('path', 'site_number', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                __attr_href_4647 = __quote(__attr_href_4647, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_href = ('%s%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '?site_id=Plone', (__attr_href_4647 if (__attr_href_4647 is not None) else ''), '&amp;classic=1', ))
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
                __stream_140355538398560 = []
                __append_140355538398560 = __stream_140355538398560.append
                __append_140355538398560('Create Classic UI Plone site')
                __msgid_140355538398560 = __re_whitespace(''.join(__stream_140355538398560)).strip()
                if __msgid_140355538398560:
                    __append(translate(__msgid_140355538398560, mapping=None, default=__msgid_140355538398560, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>')
            __append('\n                ')

            # <Static value=<ast.Dict object at 0x7fa7120248e0> name=None at 7fa712024910> -> __attrs_140355538406080
            __attrs_140355538406080 = _static_140355538405600

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a class="btn btn-secondary"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355538404976
            __default_140355538404976 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${action}?site_id=Plone${site_number}&amp;advanced=1' (98:26)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa712024700> -> __attr_href
            __token = 4840
            __token = 4842
            try:
                __zt_tmp = __attrs_140355538406080
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140355540363392('path', 'action', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 4865
            try:
                __zt_tmp = __attrs_140355538406080
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href_4863 = _static_140355540363392('path', 'site_number', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_href_4863 = __quote(__attr_href_4863, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_href = ('%s%s%s%s' % ((__attr_href if (__attr_href is not None) else ''), '?site_id=Plone', (__attr_href_4863 if (__attr_href_4863 is not None) else ''), '&amp;advanced=1', ))
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
            __stream_140355538404736 = []
            __append_140355538404736 = __stream_140355538404736.append
            __append_140355538404736('Advanced')
            __msgid_140355538404736 = __re_whitespace(''.join(__stream_140355538404736)).strip()
            if __msgid_140355538404736:
                __append(translate(__msgid_140355538404736, mapping=None, default=__msgid_140355538404736, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n            </form>')
            if (__backup_action_140355527176880 is __marker):
                del econtext['action']
            else:
                econtext['action'] = __backup_action_140355527176880
            if (__backup_site_number_140355524217392 is __marker):
                del econtext['site_number']
            else:
                econtext['site_number'] = __backup_site_number_140355524217392
            __append('\n            ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355538406752
            __attrs_140355538406752 = _static_140355540704128

            # <br ... (0:0)
            # --------------------------------------------------------
            __append('<br/>\n            ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355538411776
            __attrs_140355538411776 = _static_140355540704128

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_140355538407136 = []
            __append_140355538407136 = __stream_140355538407136.append
            __append_140355538407136("\n                Starting with Plone 6, 'Create a new Plone site' applies a\n                profile and creates default content for the new React based\n                default frontend Volto. You are however required to set up and run\n                an additional frontend service to use this setup.\n            ")
            __msgid_140355538407136 = __re_whitespace(''.join(__stream_140355538407136)).strip()
            if 'help_create_plone_site_buttons_1':
                __append(translate('help_create_plone_site_buttons_1', mapping=None, default=__msgid_140355538407136, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n            ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355538412736
            __attrs_140355538412736 = _static_140355540704128

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>')
            __stream_140355538914432_docs_link = ''
            __stream_140355538412256 = []
            __append_140355538412256 = __stream_140355538412256.append
            __append_140355538412256("\n                The 'Create Classic UI Plone site' button creates a Plone site configured\n                for HTML based output, as was already supported by previous Plone versions.\n                Please consult our\n                ")
            __stream_140355538914432_docs_link = []
            __append_140355538914432_docs_link = __stream_140355538914432_docs_link.append

            # <Static value=<ast.Dict object at 0x7fa712026a60> name=None at 7fa712026a90> -> __attrs_140355538414704
            __attrs_140355538414704 = _static_140355538414176

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140355538914432_docs_link('<a href="https://6.docs.plone.org/"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355538413456
            __default_140355538413456 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7fa712026880> at 7fa712026850> -> __attr_title
            __attr_title = 'Plone 6 developer documentation'
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append_140355538914432_docs_link((' title="%s"' % __attr_title))
            __append_140355538914432_docs_link('>')
            __stream_140355538413312 = []
            __append_140355538413312 = __stream_140355538413312.append
            __append_140355538413312('developer documentation overview ')
            __msgid_140355538413312 = __re_whitespace(''.join(__stream_140355538413312)).strip()
            if __msgid_140355538413312:
                __append_140355538914432_docs_link(translate(__msgid_140355538413312, mapping=None, default=__msgid_140355538413312, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_140355538914432_docs_link('</a>')
            __append_140355538412256('${docs_link}')
            __stream_140355538914432_docs_link = ''.join(__stream_140355538914432_docs_link)
            __append_140355538412256('\n                for more information about differences and requirements for\n                these frontends and possible upgrade paths from older Plone versions\n                to Plone 6.\n            ')
            __msgid_140355538412256 = __re_whitespace(''.join(__stream_140355538412256)).strip()
            if 'help_create_plone_site_buttons_2':
                __append(translate('help_create_plone_site_buttons_2', mapping={'docs_link': __stream_140355538914432_docs_link, }, default=__msgid_140355538412256, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</p>\n        </div>\n    </article>\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa712026f40> name=None at 7fa712026f70> -> __attrs_140355527528704
            __attrs_140355527528704 = _static_140355538415424

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append('<footer class="row">\n    ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355527529664
            __attrs_140355527529664 = _static_140355540704128

            # <p ... (0:0)
            # --------------------------------------------------------
            __append('<p>\n      ')

            # <Static value=<ast.Dict object at 0x7fa7115c5b80> name=None at 7fa7115c5820> -> __attrs_140355527531968
            __attrs_140355527531968 = _static_140355527531392

            # <a ... (0:0)
            # --------------------------------------------------------
            __append('<a')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355527531056
            __default_140355527531056 = _DEFAULT_MARKER

            # <Substitution 'string:${context/absolute_url}/manage_main' (126:29)> -> __attr_href
            __token = 6200
            try:
                __zt_tmp = __attrs_140355527531968
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_href = _static_140355540363392('string', '${context/absolute_url}/manage_main', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_href = __quote(__attr_href, '"', '&quot;', '#', _DEFAULT_MARKER)
            if (__attr_href is not None):
                __append((' href="%s"' % __attr_href))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355527531440
            __default_140355527531440 = _DEFAULT_MARKER

            # <Translate msgid=None node=<ast.Constant object at 0x7fa7115c58b0> at 7fa7115c5880> -> __attr_title
            __attr_title = 'Go to the ZMI'
            __attr_title = translate(__attr_title, default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))
            __append('>')
            __stream_140355527530288 = []
            __append_140355527530288 = __stream_140355527530288.append
            __append_140355527530288('Management Interface')
            __msgid_140355527530288 = __re_whitespace(''.join(__stream_140355527530288)).strip()
            if 'label_zmi_link':
                __append(translate('label_zmi_link', mapping=None, default=__msgid_140355527530288, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</a>\n      ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355527651728
            __attrs_140355527651728 = _static_140355540704128

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span>')
            __stream_140355527532400 = []
            __append_140355527532400 = __stream_140355527532400.append
            __append_140355527532400(' &#151; low-level technical configuration.')
            __msgid_140355527532400 = __re_whitespace(''.join(__stream_140355527532400)).strip()
            if 'label_zmi_link_description':
                __append(translate('label_zmi_link_description', mapping=None, default=__msgid_140355527532400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('</span>\n    </p>\n  </footer>\n</div>\n</body>')
            if (__backup_many_140355524215184 is __marker):
                del econtext['many']
            else:
                econtext['many'] = __backup_many_140355524215184
            if (__backup_sites_140355524214992 is __marker):
                del econtext['sites']
            else:
                econtext['sites'] = __backup_sites_140355524214992
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_140355537550448
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }