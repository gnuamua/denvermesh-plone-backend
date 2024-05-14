# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/Products.CMFPlone-6.0.11-py3.9.egg/Products/CMFPlone/browser/templates/main_template.pt'

__tokens = {71: ('string:&lt;!DOCTYPE ht', 2, 36), 344: ("python:context.restrictedTraverse('@@plone_portal_state')", 8, 31), 426: (" python:context.restrictedTraverse('@@plone_context_state'", 9, 23), 506: ("w python:context.restrictedTraverse('@@plone", 10, 19), 567: ("ns python:context.restrictedTraverse('@@iconresolve", 11, 13), 642: ("out python:context.restrictedTraverse('@@plone_layo", 12, 19), 709: ('lang python:portal_state.langu', 13, 10), 755: (' view nocall:view | nocall: plon', 14, 9), 804: (' dummy python: plone_layout.mark_vie', 15, 9), 862: ('tal_url python:portal_state.port', 16, 13), 921: ("rmission python:context.restrictedTraverse('portal_membership').checkP", 17, 17), 1018: ("roperties python:context.restrictedTraverse('portal_properties').site_", 18, 16), 1117: ("clude_head python:request.get('ajax_include_he", 19, 17), 1184: ('  ajax_load ', 20, 8), 1264: ('lang', 22, 27), 1313: ('provider:plone.httpheaders', 24, 40), 1416: ('provider:plone.htmlhead', 29, 32), 1471: ('nothing', 31, 26), 1757: ('provider:plone.scripts', 38, 32), 1882: ('provider:plone.htmlhead.links', 41, 33), 2021: ('portal_state/is_rtl', 46, 26), 2064: (" python:plone_layout.have_portlets('plone.leftcolumn', view", 47, 22), 2147: ("r python:plone_layout.have_portlets('plone.rightcolumn', vie", 48, 21), 2239: ('ss python:plone_layout.bodyClass(template, vi', 49, 28), 2415: ("  python:context.restrictedTraverse('@@plone_patterns_settings')", 52, 22), 2320: ('body_class', 50, 30), 2359: (" python:isRTL and 'rtl' or 'ltr", 51, 27), 2553: ('provider:plone.toolbar', 55, 32), 2664: ('provider:plone.portaltop', 58, 34), 2760: ('provider:plone.portalheader', 60, 36), 2880: ('provider:plone.mainnavigation', 65, 59), 3032: ('provider:plone.globalstatusmessage', 70, 42), 3211: ('provider:plone.abovecontent', 75, 59), 5052: ('sl', 130, 26), 5150: ('provider:plone.leftcolumn', 132, 38), 5325: ('sr', 138, 26), 5423: ('provider:plone.rightcolumn', 140, 38), 5586: ('provider:plone.portalfooter', 145, 34), 3606: ('provider:plone.abovecontenttitle', 91, 77), 3747: ('context/@@title', 94, 45), 3876: ('provider:plone.belowcontenttitle', 97, 77), 4028: ('context/@@description', 100, 44), 4175: ('provider:plone.belowcontentdescription', 103, 83), 4318: ('provider:plone.abovecontentbody', 107, 74), 4461: ('nothing', 110, 68), 4630: ('provider:plone.belowcontentbody', 115, 74), 4787: ('provider:plone.belowcontent', 119, 69)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355484697504 = {'id': 'viewlet-below-content', }
_static_140355529472608 = {'id': 'viewlet-below-content-body', }
_static_140355514766432 = {'id': 'content-core', }
_static_140355514766672 = {'id': 'viewlet-above-content-body', }
_static_140355514765904 = {'id': 'viewlet-below-content-description', }
_static_140355491923856 = {'id': 'viewlet-below-content-title', }
_static_140355538411968 = {'id': 'viewlet-above-content-title', }
_static_140355538388784 = {'id': 'content', }
_static_140355537279968 = {'id': 'portal-footer-wrapper', }
_static_140355484700288 = {'id': 'portal-column-two', }
_static_140355484735472 = {'id': 'portal-column-one', }
_static_140355515943376 = {'id': 'portal-column-content', }
_static_140355515944240 = {'id': 'viewlet-above-content', }
_static_140355491867472 = {'id': 'global_statusmessage', }
_static_140355491864976 = {'id': 'portal-mainnavigation', }
_static_140355523709200 = {'id': 'portal-header', }
_static_140355514827728 = {'id': 'portal-top', }
_static_140355491792352 = set([])
_static_140355491792640 = set(['noresize', 'readonly', 'compact', 'ismap', 'multiple', 'selected', 'declare', 'disabled', 'noshade', 'checked', 'defer', 'nowrap', ])
_static_140355536024336 = {'id': 'visual-portal-wrapper', 'class': 'body_class', 'dir': "python:isRTL and 'rtl' or 'ltr'", }
_static_140355536024672 = {'name': 'generator', 'content': 'Plone - https://plone.org/', }
_static_140355539165680 = {'charset': 'utf-8', }
_static_140355537397264 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'lang': 'lang', }
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

    def render_master(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_javascript_head_slot = econtext['__slot_javascript_head_slot'].pop()
        except:
            __slot_javascript_head_slot = None

        try:
            __slot_content = econtext['__slot_content'].pop()
        except:
            __slot_content = None

        try:
            __slot_global_statusmessage = econtext['__slot_global_statusmessage'].pop()
        except:
            __slot_global_statusmessage = None

        try:
            __slot_head_slot = econtext['__slot_head_slot'].pop()
        except:
            __slot_head_slot = None

        try:
            __slot_top_slot = econtext['__slot_top_slot'].pop()
        except:
            __slot_top_slot = None

        try:
            __slot_portlets_two_slot = econtext['__slot_portlets_two_slot'].pop()
        except:
            __slot_portlets_two_slot = None

        try:
            __slot_column_two_slot = econtext['__slot_column_two_slot'].pop()
        except:
            __slot_column_two_slot = None

        try:
            __slot_column_one_slot = econtext['__slot_column_one_slot'].pop()
        except:
            __slot_column_one_slot = None

        try:
            __slot_style_slot = econtext['__slot_style_slot'].pop()
        except:
            __slot_style_slot = None

        try:
            __slot_portlets_one_slot = econtext['__slot_portlets_one_slot'].pop()
        except:
            __slot_portlets_one_slot = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537398896
            __attrs_140355537398896 = _static_140355540704128
            __append('\n')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537398272
            __attrs_140355537398272 = _static_140355540704128

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355537399328
            __default_140355537399328 = _DEFAULT_MARKER

            # <Value 'string:<!DOCTYPE html>' (2:36)> -> __cache_140355537396688
            __token = 71
            try:
                __zt_tmp = __attrs_140355537398272
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355537396688 = _static_140355540363392('string', '<!DOCTYPE html>', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'string:<!DOCTYPE html>' (2:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa711f2ef10> -> __condition
            __expression = __cache_140355537396688

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140355537396688
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7fa711f2e610> name=None at 7fa711f2ec40> -> __attrs_140355537398656
            __attrs_140355537398656 = _static_140355537397264
            __backup_portal_state_140355521278256 = get('portal_state', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_portal_state')" (8:31)> -> __value
            __token = 344
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "context.restrictedTraverse('@@plone_portal_state')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['portal_state'] = __value
            __backup_context_state_140355526549264 = get('context_state', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_context_state')" (9:23)> -> __value
            __token = 426
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "context.restrictedTraverse('@@plone_context_state')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['context_state'] = __value
            __backup_plone_view_140355521945312 = get('plone_view', __marker)

            # <Value "python:context.restrictedTraverse('@@plone')" (10:19)> -> __value
            __token = 506
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "context.restrictedTraverse('@@plone')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['plone_view'] = __value
            __backup_icons_140355527191904 = get('icons', __marker)

            # <Value "python:context.restrictedTraverse('@@iconresolver')" (11:13)> -> __value
            __token = 567
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "context.restrictedTraverse('@@iconresolver')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['icons'] = __value
            __backup_plone_layout_140355521331456 = get('plone_layout', __marker)

            # <Value "python:context.restrictedTraverse('@@plone_layout')" (12:19)> -> __value
            __token = 642
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "context.restrictedTraverse('@@plone_layout')", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['plone_layout'] = __value
            __backup_lang_140355519500240 = get('lang', __marker)

            # <Value 'python:portal_state.language()' (13:10)> -> __value
            __token = 709
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', 'portal_state.language()', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['lang'] = __value
            __backup_view_140355522096816 = get('view', __marker)

            # <Value 'nocall:view | nocall: plone_view' (14:9)> -> __value
            __token = 755
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('nocall', 'view | nocall: plone_view', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['view'] = __value
            __backup_dummy_140355519296656 = get('dummy', __marker)

            # <Value 'python: plone_layout.mark_view(view)' (15:9)> -> __value
            __token = 804
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', ' plone_layout.mark_view(view)', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['dummy'] = __value
            __backup_portal_url_140355521774784 = get('portal_url', __marker)

            # <Value 'python:portal_state.portal_url()' (16:13)> -> __value
            __token = 862
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', 'portal_state.portal_url()', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['portal_url'] = __value
            __backup_checkPermission_140355523086512 = get('checkPermission', __marker)

            # <Value "python:context.restrictedTraverse('portal_membership').checkPermission" (17:17)> -> __value
            __token = 921
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "context.restrictedTraverse('portal_membership').checkPermission", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['checkPermission'] = __value
            __backup_site_properties_140355522096528 = get('site_properties', __marker)

            # <Value "python:context.restrictedTraverse('portal_properties').site_properties" (18:16)> -> __value
            __token = 1018
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "context.restrictedTraverse('portal_properties').site_properties", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['site_properties'] = __value
            __backup_ajax_include_head_140355523196000 = get('ajax_include_head', __marker)

            # <Value "python:request.get('ajax_include_head', False)" (19:17)> -> __value
            __token = 1117
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "request.get('ajax_include_head', False)", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['ajax_include_head'] = __value
            __backup_ajax_load_140355528711760 = get('ajax_load', __marker)

            # <Value 'python:False' (20:8)> -> __value
            __token = 1184
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', 'False', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['ajax_load'] = __value
            __previous_i18n_domain_140355491092368 = __i18n_domain
            __i18n_domain = 'plone'

            # <html ... (0:0)
            # --------------------------------------------------------
            __append('<html xmlns="http://www.w3.org/1999/xhtml"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355537399088
            __default_140355537399088 = _DEFAULT_MARKER

            # <Substitution 'lang' (22:27)> -> __attr_lang
            __token = 1264
            try:
                __zt_tmp = __attrs_140355537398656
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140355540363392('path', 'lang', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355539167168
            __attrs_140355539167168 = _static_140355540704128

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355539166256
            __default_140355539166256 = _DEFAULT_MARKER

            # <Value 'provider:plone.httpheaders' (24:40)> -> __cache_140355491091552
            __token = 1313
            try:
                __zt_tmp = __attrs_140355539167168
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355491091552 = _static_140355540363392('provider', 'plone.httpheaders', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.httpheaders' (24:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70f3054f0> -> __condition
            __expression = __cache_140355491091552

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140355491091552
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355539166976
            __attrs_140355539166976 = _static_140355540704128

            # <head ... (0:0)
            # --------------------------------------------------------
            __append('<head>\n    ')

            # <Static value=<ast.Dict object at 0x7fa7120de1f0> name=None at 7fa7120de250> -> __attrs_140355539167792
            __attrs_140355539167792 = _static_140355539165680

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta charset="utf-8" />\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355539166304
            __attrs_140355539166304 = _static_140355540704128

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355539165968
            __default_140355539165968 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead' (29:32)> -> __cache_140355539167456
            __token = 1416
            try:
                __zt_tmp = __attrs_140355539166304
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355539167456 = _static_140355540363392('provider', 'plone.htmlhead', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead' (29:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa7120de490> -> __condition
            __expression = __cache_140355539167456

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_140355539167456
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355538799200
            __attrs_140355538799200 = _static_140355540704128

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355538800256
            __default_140355538800256 = _DEFAULT_MARKER

            # <Value 'nothing' (31:26)> -> __cache_140355538798912
            __token = 1471
            try:
                __zt_tmp = __attrs_140355538799200
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355538798912 = _static_140355540363392('path', 'nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'nothing' (31:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa712084be0> -> __condition
            __expression = __cache_140355538798912

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n        Various slots where you can insert elements in the header from a template.\n    ')
            else:
                __content = __cache_140355538798912
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')
            if (__slot_top_slot is None):

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355538799776
                __attrs_140355538799776 = _static_140355540704128
            else:
                __slot_top_slot(__stream, econtext.copy(), rcontext)
            __append('\n    ')
            if (__slot_head_slot is None):

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537283296
                __attrs_140355537283296 = _static_140355540704128
            else:
                __slot_head_slot(__stream, econtext.copy(), rcontext)
            __append('\n    ')
            if (__slot_style_slot is None):

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537282720
                __attrs_140355537282720 = _static_140355540704128
            else:
                __slot_style_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537281760
            __attrs_140355537281760 = _static_140355540704128

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355537284112
            __default_140355537284112 = _DEFAULT_MARKER

            # <Value 'provider:plone.scripts' (38:32)> -> __cache_140355537283440
            __token = 1757
            try:
                __zt_tmp = __attrs_140355537281760
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355537283440 = _static_140355540363392('provider', 'plone.scripts', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.scripts' (38:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa711f12610> -> __condition
            __expression = __cache_140355537283440

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_140355537283440
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')
            if (__slot_javascript_head_slot is None):

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537284016
                __attrs_140355537284016 = _static_140355540704128
            else:
                __slot_javascript_head_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355536027360
            __attrs_140355536027360 = _static_140355540704128

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355536027552
            __default_140355536027552 = _DEFAULT_MARKER

            # <Value 'provider:plone.htmlhead.links' (41:33)> -> __cache_140355537283920
            __token = 1882
            try:
                __zt_tmp = __attrs_140355536027360
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355537283920 = _static_140355540363392('provider', 'plone.htmlhead.links', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.htmlhead.links' (41:33)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa711f12880> -> __condition
            __expression = __cache_140355537283920

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <link ... (0:0)
                # --------------------------------------------------------
                __append('<link />')
            else:
                __content = __cache_140355537283920
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    ')

            # <Static value=<ast.Dict object at 0x7fa711ddf460> name=None at 7fa711ddf5b0> -> __attrs_140355536024768
            __attrs_140355536024768 = _static_140355536024672

            # <meta ... (0:0)
            # --------------------------------------------------------
            __append('<meta name="generator" content="Plone - https://plone.org/" />\n\n  </head>\n\n  ')

            # <Static value=<ast.Dict object at 0x7fa711ddf310> name=None at 7fa711ddf340> -> __attrs_140355536026160
            __attrs_140355536026160 = _static_140355536024336
            __backup_isRTL_140355526548688 = get('isRTL', __marker)

            # <Value 'portal_state/is_rtl' (46:26)> -> __value
            __token = 2021
            try:
                __zt_tmp = __attrs_140355536026160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'portal_state/is_rtl', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['isRTL'] = __value
            __backup_sl_140355526603392 = get('sl', __marker)

            # <Value "python:plone_layout.have_portlets('plone.leftcolumn', view)" (47:22)> -> __value
            __token = 2064
            try:
                __zt_tmp = __attrs_140355536026160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "plone_layout.have_portlets('plone.leftcolumn', view)", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['sl'] = __value
            __backup_sr_140355525233872 = get('sr', __marker)

            # <Value "python:plone_layout.have_portlets('plone.rightcolumn', view)" (48:21)> -> __value
            __token = 2147
            try:
                __zt_tmp = __attrs_140355536026160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', "plone_layout.have_portlets('plone.rightcolumn', view)", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['sr'] = __value
            __backup_body_class_140355519632720 = get('body_class', __marker)

            # <Value 'python:plone_layout.bodyClass(template, view)' (49:28)> -> __value
            __token = 2239
            try:
                __zt_tmp = __attrs_140355536026160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', 'plone_layout.bodyClass(template, view)', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['body_class'] = __value

            # <body ... (0:0)
            # --------------------------------------------------------
            __append('<body')

            # <Value "python:context.restrictedTraverse('@@plone_patterns_settings')()" (52:22)> -> __cache_140355536024816
            __token = 2415
            try:
                __zt_tmp = __attrs_140355536026160
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355536024816 = _static_140355540363392('python', "context.restrictedTraverse('@@plone_patterns_settings')()", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if ('id' not in __chain(__cache_140355536024816)):
                __append(' id="visual-portal-wrapper"')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355536027264
            __default_140355536027264 = _DEFAULT_MARKER

            # <Substitution 'body_class' (50:30)> -> __attr_class
            __token = 2320
            try:
                __zt_tmp = __attrs_140355536026160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140355540363392('path', 'body_class', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_class is not None) and ('class' not in __chain(__cache_140355536024816))):
                __append((' class="%s"' % __attr_class))

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355536023664
            __default_140355536023664 = _DEFAULT_MARKER

            # <Substitution "python:isRTL and 'rtl' or 'ltr'" (51:27)> -> __attr_dir
            __token = 2359
            try:
                __zt_tmp = __attrs_140355536026160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_dir = _static_140355540363392('python', "isRTL and 'rtl' or 'ltr'", econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            __attr_dir = __quote(__attr_dir, '"', '&quot;', None, _DEFAULT_MARKER)
            if ((__attr_dir is not None) and ('dir' not in __chain(__cache_140355536024816))):
                __append((' dir="%s"' % __attr_dir))
            __attr_140355536026640 = __cache_140355536024816
            for (name, value, ) in __attr_140355536026640.items():
                if (name in _static_140355491792640):
                    if not bool(value):
                        continue
                    value = name
                if ((name not in _static_140355491792352) and (value is not None)):
                    if (name in _static_140355491792640):
                        if not bool(value):
                            continue
                        value = name
                    __append((((((' ' + name) + '=') + '"') + __quote(value, '"', '&quot;', None, None)) + '"'))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355514828496
            __attrs_140355514828496 = _static_140355540704128

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355514829216
            __default_140355514829216 = _DEFAULT_MARKER

            # <Value 'provider:plone.toolbar' (55:32)> -> __cache_140355514829840
            __token = 2553
            try:
                __zt_tmp = __attrs_140355514828496
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355514829840 = _static_140355540363392('provider', 'plone.toolbar', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.toolbar' (55:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa7109a8f40> -> __condition
            __expression = __cache_140355514829840

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_140355514829840
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa7109a83d0> name=None at 7fa7109a83a0> -> __attrs_140355514829504
            __attrs_140355514829504 = _static_140355514827728
            __previous_i18n_domain_140355514827104 = __i18n_domain
            __i18n_domain = 'plone'

            # <header ... (0:0)
            # --------------------------------------------------------
            __append('<header id="portal-top">\n      ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355523707712
            __attrs_140355523707712 = _static_140355540704128

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355523707280
            __default_140355523707280 = _DEFAULT_MARKER

            # <Value 'provider:plone.portaltop' (58:34)> -> __cache_140355523708960
            __token = 2664
            try:
                __zt_tmp = __attrs_140355523707712
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355523708960 = _static_140355540363392('provider', 'plone.portaltop', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portaltop' (58:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa711220850> -> __condition
            __expression = __cache_140355523708960

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_140355523708960
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      ')

            # <Static value=<ast.Dict object at 0x7fa711220910> name=None at 7fa711220a60> -> __attrs_140355523707184
            __attrs_140355523707184 = _static_140355523709200

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-header">\n        ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355491866944
            __attrs_140355491866944 = _static_140355540704128

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355523710640
            __default_140355523710640 = _DEFAULT_MARKER

            # <Value 'provider:plone.portalheader' (60:36)> -> __cache_140355523706944
            __token = 2760
            try:
                __zt_tmp = __attrs_140355491866944
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355523706944 = _static_140355540363392('provider', 'plone.portalheader', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portalheader' (60:36)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa711220b20> -> __condition
            __expression = __cache_140355523706944

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_140355523706944
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      </div>\n\n    </header>')
            __i18n_domain = __previous_i18n_domain_140355514827104
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa70f3c2190> name=None at 7fa70f3c2160> -> __attrs_140355491864832
            __attrs_140355491864832 = _static_140355491864976

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="portal-mainnavigation">')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355491865984
            __default_140355491865984 = _DEFAULT_MARKER

            # <Value 'provider:plone.mainnavigation' (65:59)> -> __cache_140355491865888
            __token = 2880
            try:
                __zt_tmp = __attrs_140355491864832
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355491865888 = _static_140355540363392('provider', 'plone.mainnavigation', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.mainnavigation' (65:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70f3c24f0> -> __condition
            __expression = __cache_140355491865888

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                __append('\n      The main navigation\n    ')
            else:
                __content = __cache_140355491865888
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa70f3c2b50> name=None at 7fa70f3c2640> -> __attrs_140355491866416
            __attrs_140355491866416 = _static_140355491867472

            # <section ... (0:0)
            # --------------------------------------------------------
            __append('<section id="global_statusmessage">\n      ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355515941552
            __attrs_140355515941552 = _static_140355540704128

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355515941024
            __default_140355515941024 = _DEFAULT_MARKER

            # <Value 'provider:plone.globalstatusmessage' (70:42)> -> __cache_140355491867856
            __token = 3032
            try:
                __zt_tmp = __attrs_140355515941552
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355491867856 = _static_140355540363392('provider', 'plone.globalstatusmessage', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.globalstatusmessage' (70:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70f3c2820> -> __condition
            __expression = __cache_140355491867856

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140355491867856
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n      ')
            if (__slot_global_statusmessage is None):

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355515941936
                __attrs_140355515941936 = _static_140355540704128

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n      </div>')
            else:
                __slot_global_statusmessage(__stream, econtext.copy(), rcontext)
            __append('\n    </section>\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa710ab8d30> name=None at 7fa710ab8cd0> -> __attrs_140355515944000
            __attrs_140355515944000 = _static_140355515944240

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div id="viewlet-above-content">')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355515942032
            __default_140355515942032 = _DEFAULT_MARKER

            # <Value 'provider:plone.abovecontent' (75:59)> -> __cache_140355515943088
            __token = 3211
            try:
                __zt_tmp = __attrs_140355515944000
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355515943088 = _static_140355540363392('provider', 'plone.abovecontent', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.abovecontent' (75:59)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa710ab80d0> -> __condition
            __expression = __cache_140355515943088

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140355515943088
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('</div>\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa710ab89d0> name=None at 7fa710ab88e0> -> __attrs_140355484737008
            __attrs_140355484737008 = _static_140355515943376

            # <article ... (0:0)
            # --------------------------------------------------------
            __append('<article id="portal-column-content">\n\n      ')
            if (__slot_content is None):

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355484734464
                __attrs_140355484734464 = _static_140355540704128
                __append('\n\n      ')
                __token = None
                render_content(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                __append('\n\n      ')
            else:
                __slot_content(__stream, econtext.copy(), rcontext)
            __append('\n    </article>\n\n    ')
            if (__slot_column_one_slot is None):

                # <Static value=<ast.Dict object at 0x7fa70ecf57f0> name=None at 7fa70ecf5760> -> __attrs_140355484734416
                __attrs_140355484734416 = _static_140355484735472

                # <Value 'sl' (130:26)> -> __condition
                __token = 5052
                try:
                    __zt_tmp = __attrs_140355484734416
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('path', 'sl', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append('<aside id="portal-column-one">\n      ')
                    if (__slot_portlets_one_slot is None):

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355484698512
                        __attrs_140355484698512 = _static_140355540704128
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537279584
                        __attrs_140355537279584 = _static_140355540704128

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355537279296
                        __default_140355537279296 = _DEFAULT_MARKER

                        # <Value 'provider:plone.leftcolumn' (132:38)> -> __cache_140355484699712
                        __token = 5150
                        try:
                            __zt_tmp = __attrs_140355537279584
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355484699712 = _static_140355540363392('provider', 'plone.leftcolumn', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value 'provider:plone.leftcolumn' (132:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70ececd90> -> __condition
                        __expression = __cache_140355484699712

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140355484699712
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n      ')
                    else:
                        __slot_portlets_one_slot(__stream, econtext.copy(), rcontext)
                    __append('\n    </aside>')
            else:
                __slot_column_one_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')
            if (__slot_column_two_slot is None):

                # <Static value=<ast.Dict object at 0x7fa70ecece80> name=None at 7fa70ececaf0> -> __attrs_140355537279440
                __attrs_140355537279440 = _static_140355484700288

                # <Value 'sr' (138:26)> -> __condition
                __token = 5325
                try:
                    __zt_tmp = __attrs_140355537279440
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('path', 'sr', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:

                    # <aside ... (0:0)
                    # --------------------------------------------------------
                    __append('<aside id="portal-column-two">\n      ')
                    if (__slot_portlets_two_slot is None):

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537277712
                        __attrs_140355537277712 = _static_140355540704128
                        __append('\n        ')

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355537280304
                        __attrs_140355537280304 = _static_140355540704128

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355537280736
                        __default_140355537280736 = _DEFAULT_MARKER

                        # <Value 'provider:plone.rightcolumn' (140:38)> -> __cache_140355537280496
                        __token = 5423
                        try:
                            __zt_tmp = __attrs_140355537280304
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355537280496 = _static_140355540363392('provider', 'plone.rightcolumn', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value 'provider:plone.rightcolumn' (140:38)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa711f11430> -> __condition
                        __expression = __cache_140355537280496

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140355537280496
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n      ')
                    else:
                        __slot_portlets_two_slot(__stream, econtext.copy(), rcontext)
                    __append('\n    </aside>')
            else:
                __slot_column_two_slot(__stream, econtext.copy(), rcontext)
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa711f11be0> name=None at 7fa711f11e50> -> __attrs_140355537280832
            __attrs_140355537280832 = _static_140355537279968
            __previous_i18n_domain_140355484721216 = __i18n_domain
            __i18n_domain = 'plone'

            # <footer ... (0:0)
            # --------------------------------------------------------
            __append('<footer id="portal-footer-wrapper">\n      ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355484724048
            __attrs_140355484724048 = _static_140355540704128

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355484724528
            __default_140355484724528 = _DEFAULT_MARKER

            # <Value 'provider:plone.portalfooter' (145:34)> -> __cache_140355484721888
            __token = 5586
            try:
                __zt_tmp = __attrs_140355484724048
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355484721888 = _static_140355540363392('provider', 'plone.portalfooter', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'provider:plone.portalfooter' (145:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70ecf26a0> -> __condition
            __expression = __cache_140355484721888

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div />')
            else:
                __content = __cache_140355484721888
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n    </footer>')
            __i18n_domain = __previous_i18n_domain_140355484721216
            __append('\n\n  </body>')
            if (__backup_body_class_140355519632720 is __marker):
                del econtext['body_class']
            else:
                econtext['body_class'] = __backup_body_class_140355519632720
            if (__backup_sr_140355525233872 is __marker):
                del econtext['sr']
            else:
                econtext['sr'] = __backup_sr_140355525233872
            if (__backup_sl_140355526603392 is __marker):
                del econtext['sl']
            else:
                econtext['sl'] = __backup_sl_140355526603392
            if (__backup_isRTL_140355526548688 is __marker):
                del econtext['isRTL']
            else:
                econtext['isRTL'] = __backup_isRTL_140355526548688
            __append('\n</html>')
            __i18n_domain = __previous_i18n_domain_140355491092368
            if (__backup_ajax_load_140355528711760 is __marker):
                del econtext['ajax_load']
            else:
                econtext['ajax_load'] = __backup_ajax_load_140355528711760
            if (__backup_ajax_include_head_140355523196000 is __marker):
                del econtext['ajax_include_head']
            else:
                econtext['ajax_include_head'] = __backup_ajax_include_head_140355523196000
            if (__backup_site_properties_140355522096528 is __marker):
                del econtext['site_properties']
            else:
                econtext['site_properties'] = __backup_site_properties_140355522096528
            if (__backup_checkPermission_140355523086512 is __marker):
                del econtext['checkPermission']
            else:
                econtext['checkPermission'] = __backup_checkPermission_140355523086512
            if (__backup_portal_url_140355521774784 is __marker):
                del econtext['portal_url']
            else:
                econtext['portal_url'] = __backup_portal_url_140355521774784
            if (__backup_dummy_140355519296656 is __marker):
                del econtext['dummy']
            else:
                econtext['dummy'] = __backup_dummy_140355519296656
            if (__backup_view_140355522096816 is __marker):
                del econtext['view']
            else:
                econtext['view'] = __backup_view_140355522096816
            if (__backup_lang_140355519500240 is __marker):
                del econtext['lang']
            else:
                econtext['lang'] = __backup_lang_140355519500240
            if (__backup_plone_layout_140355521331456 is __marker):
                del econtext['plone_layout']
            else:
                econtext['plone_layout'] = __backup_plone_layout_140355521331456
            if (__backup_icons_140355527191904 is __marker):
                del econtext['icons']
            else:
                econtext['icons'] = __backup_icons_140355527191904
            if (__backup_plone_view_140355521945312 is __marker):
                del econtext['plone_view']
            else:
                econtext['plone_view'] = __backup_plone_view_140355521945312
            if (__backup_context_state_140355526549264 is __marker):
                del econtext['context_state']
            else:
                econtext['context_state'] = __backup_context_state_140355526549264
            if (__backup_portal_state_140355521278256 is __marker):
                del econtext['portal_state']
            else:
                econtext['portal_state'] = __backup_portal_state_140355521278256
            __append('\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise


    def render_content(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_content_description = econtext['__slot_content_description'].pop()
        except:
            __slot_content_description = None

        try:
            __slot_body = econtext['__slot_body'].pop()
        except:
            __slot_body = None

        try:
            __slot_main = econtext['__slot_main'].pop()
        except:
            __slot_main = None

        try:
            __slot_content_title = econtext['__slot_content_title'].pop()
        except:
            __slot_content_title = None

        try:
            __slot_content_core = econtext['__slot_content_core'].pop()
        except:
            __slot_content_core = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355484735712
            __attrs_140355484735712 = _static_140355540704128
            __append('\n\n        ')
            if (__slot_body is None):

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355484734512
                __attrs_140355484734512 = _static_140355540704128
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x7fa712020730> name=None at 7fa712020b80> -> __attrs_140355538390224
                __attrs_140355538390224 = _static_140355538388784

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n\n            ')
                if (__slot_main is None):

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355538390704
                    __attrs_140355538390704 = _static_140355540704128
                    __append('\n\n              ')

                    # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355538388064
                    __attrs_140355538388064 = _static_140355540704128

                    # <header ... (0:0)
                    # --------------------------------------------------------
                    __append('<header>\n\n                ')

                    # <Static value=<ast.Dict object at 0x7fa7120261c0> name=None at 7fa712026f70> -> __attrs_140355538413120
                    __attrs_140355538413120 = _static_140355538411968

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-above-content-title">')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355538415232
                    __default_140355538415232 = _DEFAULT_MARKER

                    # <Value 'provider:plone.abovecontenttitle' (91:77)> -> __cache_140355538389792
                    __token = 3606
                    try:
                        __zt_tmp = __attrs_140355538413120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355538389792 = _static_140355540363392('provider', 'plone.abovecontenttitle', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.abovecontenttitle' (91:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa712020f40> -> __condition
                    __expression = __cache_140355538389792

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355538389792
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n                ')
                    if (__slot_content_title is None):

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355538414560
                        __attrs_140355538414560 = _static_140355540704128
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355538412208
                        __attrs_140355538412208 = _static_140355540704128

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355538415136
                        __default_140355538415136 = _DEFAULT_MARKER

                        # <Value 'context/@@title' (94:45)> -> __cache_140355538413360
                        __token = 3747
                        try:
                            __zt_tmp = __attrs_140355538412208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355538413360 = _static_140355540363392('path', 'context/@@title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value 'context/@@title' (94:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa712026310> -> __condition
                        __expression = __cache_140355538413360

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <h1 ... (0:0)
                            # --------------------------------------------------------
                            __append('<h1 />')
                        else:
                            __content = __cache_140355538413360
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                ')
                    else:
                        __slot_content_title(__stream, econtext.copy(), rcontext)
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x7fa70f3d0790> name=None at 7fa70f3d09d0> -> __attrs_140355491922752
                    __attrs_140355491922752 = _static_140355491923856

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-title">')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355491925488
                    __default_140355491925488 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontenttitle' (97:77)> -> __cache_140355538412592
                    __token = 3876
                    try:
                        __zt_tmp = __attrs_140355491922752
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355538412592 = _static_140355540363392('provider', 'plone.belowcontenttitle', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontenttitle' (97:77)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa712026490> -> __condition
                    __expression = __cache_140355538412592

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355538412592
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n                ')
                    if (__slot_content_description is None):

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355491923712
                        __attrs_140355491923712 = _static_140355540704128
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355491923136
                        __attrs_140355491923136 = _static_140355540704128

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355491922992
                        __default_140355491922992 = _DEFAULT_MARKER

                        # <Value 'context/@@description' (100:44)> -> __cache_140355491923808
                        __token = 4028
                        try:
                            __zt_tmp = __attrs_140355491923136
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355491923808 = _static_140355540363392('path', 'context/@@description', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value 'context/@@description' (100:44)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70f3d0580> -> __condition
                        __expression = __cache_140355491923808

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <p ... (0:0)
                            # --------------------------------------------------------
                            __append('<p />')
                        else:
                            __content = __cache_140355491923808
                            __content = __convert(__content)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                ')
                    else:
                        __slot_content_description(__stream, econtext.copy(), rcontext)
                    __append('\n\n                ')

                    # <Static value=<ast.Dict object at 0x7fa710999250> name=None at 7fa7109993d0> -> __attrs_140355514769264
                    __attrs_140355514769264 = _static_140355514765904

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-description">')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355514767728
                    __default_140355514767728 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontentdescription' (103:83)> -> __cache_140355491922704
                    __token = 4175
                    try:
                        __zt_tmp = __attrs_140355514769264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355491922704 = _static_140355540363392('provider', 'plone.belowcontentdescription', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontentdescription' (103:83)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70f3d0af0> -> __condition
                    __expression = __cache_140355491922704

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355491922704
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n              </header>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7fa710999550> name=None at 7fa710999670> -> __attrs_140355514766768
                    __attrs_140355514766768 = _static_140355514766672

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-above-content-body">')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355514765520
                    __default_140355514765520 = _DEFAULT_MARKER

                    # <Value 'provider:plone.abovecontentbody' (107:74)> -> __cache_140355514768544
                    __token = 4318
                    try:
                        __zt_tmp = __attrs_140355514766768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355514768544 = _static_140355540363392('provider', 'plone.abovecontentbody', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.abovecontentbody' (107:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa710999c70> -> __condition
                    __expression = __cache_140355514768544

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355514768544
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7fa710999460> name=None at 7fa710999400> -> __attrs_140355514765376
                    __attrs_140355514765376 = _static_140355514766432

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="content-core">\n                ')
                    if (__slot_content_core is None):

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355529470064
                        __attrs_140355529470064 = _static_140355540704128

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355529473424
                        __default_140355529473424 = _DEFAULT_MARKER

                        # <Value 'nothing' (110:68)> -> __cache_140355529470256
                        __token = 4461
                        try:
                            __zt_tmp = __attrs_140355529470064
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355529470256 = _static_140355540363392('path', 'nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value 'nothing' (110:68)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa71179fd30> -> __condition
                        __expression = __cache_140355529470256

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n                  Page body text\n                ')
                        else:
                            __content = __cache_140355529470256
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                    else:
                        __slot_content_core(__stream, econtext.copy(), rcontext)
                    __append('\n              </div>\n\n              ')

                    # <Static value=<ast.Dict object at 0x7fa71179fa60> name=None at 7fa71179fc10> -> __attrs_140355529470304
                    __attrs_140355529470304 = _static_140355529472608

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div id="viewlet-below-content-body">')

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355529472320
                    __default_140355529472320 = _DEFAULT_MARKER

                    # <Value 'provider:plone.belowcontentbody' (115:74)> -> __cache_140355529470400
                    __token = 4630
                    try:
                        __zt_tmp = __attrs_140355529470304
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140355529470400 = _static_140355540363392('provider', 'plone.belowcontentbody', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                    # <BinOp left=<Value 'provider:plone.belowcontentbody' (115:74)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa71179f220> -> __condition
                    __expression = __cache_140355529470400

                    # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        pass
                    else:
                        __content = __cache_140355529470400
                        __content = __convert(__content)
                        if (__content is not None):
                            __append(__content)
                    __append('</div>\n\n            ')
                else:
                    __slot_main(__stream, econtext.copy(), rcontext)
                __append('\n            ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355529471648
                __attrs_140355529471648 = _static_140355540704128

                # <footer ... (0:0)
                # --------------------------------------------------------
                __append('<footer>\n              ')

                # <Static value=<ast.Dict object at 0x7fa70ecec3a0> name=None at 7fa70ecec100> -> __attrs_140355484698368
                __attrs_140355484698368 = _static_140355484697504

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="viewlet-below-content">')

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355484698656
                __default_140355484698656 = _DEFAULT_MARKER

                # <Value 'provider:plone.belowcontent' (119:69)> -> __cache_140355484697024
                __token = 4787
                try:
                    __zt_tmp = __attrs_140355484698368
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140355484697024 = _static_140355540363392('provider', 'plone.belowcontent', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                # <BinOp left=<Value 'provider:plone.belowcontent' (119:69)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70ececf40> -> __condition
                __expression = __cache_140355484697024

                # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140355484697024
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n            </footer>\n          </article>\n        ')
            else:
                __slot_body(__stream, econtext.copy(), rcontext)
            __append('\n      ')
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
            render_master(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_master': render_master, 'render_content': render_content, 'render': render, }