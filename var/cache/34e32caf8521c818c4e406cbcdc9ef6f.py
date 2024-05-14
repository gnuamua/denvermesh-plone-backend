# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.z3cform-4.3.2-py3.9.egg/plone/app/z3cform/templates/image_input.pt'

__tokens = {38: ('view/download_url', 2, 20), 70: (' python: view.value is not Non', 3, 13), 115: ('n view/acti', 4, 12), 149: ('ge view/allow_nocha', 5, 19), 185: ('ype view/file_content_', 6, 12), 220: ('icon view/file', 7, 7), 251: ('ename view/fi', 8, 10), 311: ('view/id', 11, 10), 332: (' view/styl', 12, 12), 356: ('e view/tit', 13, 11), 379: ('ng view/l', 14, 9), 404: ('ick view/onc', 15, 11), 435: ('lick view/ondbl', 16, 13), 470: ('edown view/onmou', 17, 13), 504: ('ouseup view/on', 18, 10), 538: ('useover view/onm', 19, 11), 574: ('ousemove view/on', 20, 10), 609: ('nmouseout view/', 21, 8), 643: ('onkeypress view', 22, 7), 676: ('  onkeydown vi', 23, 5), 706: ('     onkeyup', 24, 2), 734: ('      onfocu', 25, 1), 761: ('\n       onb', 25, 28), 789: ('       onchan', 27, 0), 819: ('\n       reado', 27, 30), 850: ('\n       access', 28, 30), 881: ('y;\n       ons', 29, 30), 990: ('view/file_upload_id', 35, 18), 1048: ('up_id', 37, 25), 1076: ('${view/name}.file_upload_id', 39, 17), 1078: ('view/name', 39, 19), 1148: ('${up_id}', 41, 18), 1150: ('up_id', 41, 20), 1275: ('${view/value/filename}', 45, 8), 1277: ('view/value/filename', 45, 10), 1345: ("python:exists and download_url and action=='nochange'", 48, 23), 1439: ('download_url', 50, 14), 1497: ('view/thumb_tag', 52, 34), 1587: ('icon', 56, 24), 1654: (' doc_typ', 59, 14), 1634: ('icon', 58, 15), 1680: ('e filena', 60, 15), 1778: ('download_url', 65, 14), 1730: ('filename', 63, 20), 1885: ('doc_type', 69, 38), 1923: ('doc_type', 70, 27), 2055: ('view/file_size', 74, 21), 2110: ('sizekb', 76, 25), 2212: ('allow_nochange', 81, 24), 2402: ('string:${view/name}.action', 87, 20), 2447: (' string:${view/id}-nochang', 88, 17), 2497: ("k string:document.getElementById('${view/id}-input').disabled=tr", 89, 21), 2585: ("ed python:'checked' if action == 'nochange' else N", 90, 20), 2751: ('string:${view/id}-nochange', 95, 19), 2933: ('not:view/field/required', 101, 24), 3106: ('string:${view/name}.action', 107, 20), 3151: (' string:${view/id}-remov', 108, 17), 3199: ("k string:document.getElementById('${view/id}-input').disabled=tr", 109, 21), 3287: ("ed python:'checked' if action == 'remove' else N", 110, 20), 3451: ('string:${view/id}-remove', 115, 19), 3756: ('string:${view/name}.action', 126, 20), 3801: (' string:${view/id}-replac', 127, 17), 3850: ("k string:document.getElementById('${view/id}-input').disabled=fal", 128, 21), 3939: ("ed python:'checked' if action == 'replace' else N", 129, 20), 4104: ('string:${view/id}-replace', 134, 19), 4302: ('${view/accept|nothing}', 142, 17), 4304: ('view/accept|nothing', 142, 19), 4387: ('string:${view/id}-input', 145, 14), 4427: (' view/nam', 146, 15), 4457: ("d python:view.required and 'required' or No", 147, 18), 4517: ('ze view/s', 148, 13), 4547: ('led view/disa', 149, 16), 4582: ('ngth view/maxl', 150, 16), 4666: ('view/accept|nothing', 154, 22), 4800: ('${view/accept}', 158, 41), 4802: ('view/accept', 158, 43), 4895: ("python:allow_nochange and action != 'replace'", 162, 25), 4965: ("string:document.getElementById('${view/id}-input').disabled=true;", 163, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140362873233360 = {'type': 'text/javascript', }
_static_140362873232544 = {'class': 'form-text', }
_static_140362872694000 = {'class': 'form-control', 'accept': '${view/accept|nothing}', 'type': 'file', 'id': 'string:${view/id}-input', 'name': 'view/name', 'required': "python:view.required and 'required' or None", 'size': 'view/size', 'disabled': 'view/disabled', 'maxlength': 'view/maxlength', }
_static_140362873491520 = {'class': 'form-check-label', 'for': 'string:${view/id}-replace', }
_static_140362873269552 = {'class': 'form-check-input', 'type': 'radio', 'value': 'replace', 'name': 'string:${view/name}.action', 'id': 'string:${view/id}-replace', 'onclick': "string:document.getElementById('${view/id}-input').disabled=false", 'checked': "python:'checked' if action == 'replace' else None", }
_static_140362873269360 = {'class': 'form-check', }
_static_140362873537008 = {'class': 'form-check-label', 'for': 'string:${view/id}-remove', }
_static_140362873537680 = {'class': 'form-check-input', 'type': 'radio', 'value': 'remove', 'name': 'string:${view/name}.action', 'id': 'string:${view/id}-remove', 'onclick': "string:document.getElementById('${view/id}-input').disabled=true", 'checked': "python:'checked' if action == 'remove' else None", }
_static_140362873081040 = {'class': 'form-check', }
_static_140362873078160 = {'class': 'form-check-label', 'for': 'string:${view/id}-nochange', }
_static_140362872386752 = {'class': 'form-check-input', 'type': 'radio', 'value': 'nochange', 'name': 'string:${view/name}.action', 'id': 'string:${view/id}-nochange', 'onclick': "string:document.getElementById('${view/id}-input').disabled=true", 'checked': "python:'checked' if action == 'nochange' else None", }
_static_140362872691440 = {'class': 'form-check', }
_static_140362873144320 = {'class': 'discreet', }
_static_140362873043408 = {'href': 'download_url', }
_static_140362863294976 = {'alt': '', 'src': '', 'title': 'filename', }
_static_140362872748400 = {'href': 'download_url', }
_static_140362873193568 = {'name': '${view/name}.file_upload_id', 'type': 'hidden', 'value': '${up_id}', }
_static_140362943909360 = {}
_static_140362943564240 = __C2ZContextWrapper
_static_140362943564528 = __compile_zt_expr
_static_140362883329136 = {'id': 'view/id', 'style': 'view/style', 'title': 'view/title', 'lang': 'view/lang', 'onclick': 'view/onclick', 'ondblclick': 'view/ondblclick', 'onmousedown': 'view/onmousedown', 'onmouseup': 'view/onmouseup', 'onmouseover': 'view/onmouseover', 'onmousemove': 'view/onmousemove', 'onmouseout': 'view/onmouseout', 'onkeypress': 'view/onkeypress', 'onkeydown': 'view/onkeydown', 'onkeyup': 'view/onkeyup', 'onfocus': 'view/onfocus', 'onblur': 'view/onblur', 'onchange': 'view/onchange', 'readonly': 'view/readonly', 'accesskey': 'view/accesskey', 'onselect': 'view/onselect', }

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

            # <Static value=<ast.Dict object at 0x7fa8c7ccec70> name=None at 7fa8c7ccec40> -> __attrs_140362863508160
            __attrs_140362863508160 = _static_140362883329136
            __backup_download_url_140362872612272 = get('download_url', __marker)

            # <Value 'view/download_url' (2:20)> -> __value
            __token = 38
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('path', 'view/download_url', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['download_url'] = __value
            __backup_exists_140362872610976 = get('exists', __marker)

            # <Value 'python: view.value is not None' (3:13)> -> __value
            __token = 70
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('python', ' view.value is not None', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['exists'] = __value
            __backup_action_140362872614336 = get('action', __marker)

            # <Value 'view/action' (4:12)> -> __value
            __token = 115
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('path', 'view/action', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['action'] = __value
            __backup_allow_nochange_140362863509168 = get('allow_nochange', __marker)

            # <Value 'view/allow_nochange' (5:19)> -> __value
            __token = 149
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('path', 'view/allow_nochange', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['allow_nochange'] = __value
            __backup_doc_type_140362863506048 = get('doc_type', __marker)

            # <Value 'view/file_content_type' (6:12)> -> __value
            __token = 185
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('path', 'view/file_content_type', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['doc_type'] = __value
            __backup_icon_140362863509072 = get('icon', __marker)

            # <Value 'view/file_icon' (7:7)> -> __value
            __token = 220
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('path', 'view/file_icon', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['icon'] = __value
            __backup_filename_140362863507680 = get('filename', __marker)

            # <Value 'view/filename' (8:10)> -> __value
            __token = 251
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('path', 'view/filename', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['filename'] = __value
            __previous_i18n_domain_140362917344352 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362952419552
            __default_140362952419552 = _DEFAULT_MARKER

            # <Substitution 'view/id' (11:10)> -> __attr_id
            __token = 311
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140362943564528('path', 'view/id', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362883946864
            __default_140362883946864 = _DEFAULT_MARKER

            # <Substitution 'view/style' (12:12)> -> __attr_style
            __token = 332
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_style = _static_140362943564528('path', 'view/style', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_style = __quote(__attr_style, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_style is not None):
                __append((' style="%s"' % __attr_style))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362883944608
            __default_140362883944608 = _DEFAULT_MARKER

            # <Substitution 'view/title' (13:11)> -> __attr_title
            __token = 356
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_title = _static_140362943564528('path', 'view/title', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_title is not None):
                __append((' title="%s"' % __attr_title))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873168848
            __default_140362873168848 = _DEFAULT_MARKER

            # <Substitution 'view/lang' (14:9)> -> __attr_lang
            __token = 379
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_lang = _static_140362943564528('path', 'view/lang', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_lang = __quote(__attr_lang, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_lang is not None):
                __append((' lang="%s"' % __attr_lang))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873167984
            __default_140362873167984 = _DEFAULT_MARKER

            # <Substitution 'view/onclick' (15:11)> -> __attr_onclick
            __token = 404
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onclick = _static_140362943564528('path', 'view/onclick', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onclick is not None):
                __append((' onclick="%s"' % __attr_onclick))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873170240
            __default_140362873170240 = _DEFAULT_MARKER

            # <Substitution 'view/ondblclick' (16:13)> -> __attr_ondblclick
            __token = 435
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_ondblclick = _static_140362943564528('path', 'view/ondblclick', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_ondblclick = __quote(__attr_ondblclick, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_ondblclick is not None):
                __append((' ondblclick="%s"' % __attr_ondblclick))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873171248
            __default_140362873171248 = _DEFAULT_MARKER

            # <Substitution 'view/onmousedown' (17:13)> -> __attr_onmousedown
            __token = 470
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousedown = _static_140362943564528('path', 'view/onmousedown', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_onmousedown = __quote(__attr_onmousedown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousedown is not None):
                __append((' onmousedown="%s"' % __attr_onmousedown))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873169424
            __default_140362873169424 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseup' (18:10)> -> __attr_onmouseup
            __token = 504
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseup = _static_140362943564528('path', 'view/onmouseup', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_onmouseup = __quote(__attr_onmouseup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseup is not None):
                __append((' onmouseup="%s"' % __attr_onmouseup))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873170720
            __default_140362873170720 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseover' (19:11)> -> __attr_onmouseover
            __token = 538
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseover = _static_140362943564528('path', 'view/onmouseover', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_onmouseover = __quote(__attr_onmouseover, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseover is not None):
                __append((' onmouseover="%s"' % __attr_onmouseover))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873171680
            __default_140362873171680 = _DEFAULT_MARKER

            # <Substitution 'view/onmousemove' (20:10)> -> __attr_onmousemove
            __token = 574
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmousemove = _static_140362943564528('path', 'view/onmousemove', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_onmousemove = __quote(__attr_onmousemove, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmousemove is not None):
                __append((' onmousemove="%s"' % __attr_onmousemove))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873170288
            __default_140362873170288 = _DEFAULT_MARKER

            # <Substitution 'view/onmouseout' (21:8)> -> __attr_onmouseout
            __token = 609
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onmouseout = _static_140362943564528('path', 'view/onmouseout', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_onmouseout = __quote(__attr_onmouseout, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onmouseout is not None):
                __append((' onmouseout="%s"' % __attr_onmouseout))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873170672
            __default_140362873170672 = _DEFAULT_MARKER

            # <Substitution 'view/onkeypress' (22:7)> -> __attr_onkeypress
            __token = 643
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeypress = _static_140362943564528('path', 'view/onkeypress', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_onkeypress = __quote(__attr_onkeypress, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeypress is not None):
                __append((' onkeypress="%s"' % __attr_onkeypress))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873168176
            __default_140362873168176 = _DEFAULT_MARKER

            # <Substitution 'view/onkeydown' (23:5)> -> __attr_onkeydown
            __token = 676
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeydown = _static_140362943564528('path', 'view/onkeydown', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_onkeydown = __quote(__attr_onkeydown, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeydown is not None):
                __append((' onkeydown="%s"' % __attr_onkeydown))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362952403888
            __default_140362952403888 = _DEFAULT_MARKER

            # <Substitution 'view/onkeyup' (24:2)> -> __attr_onkeyup
            __token = 706
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onkeyup = _static_140362943564528('path', 'view/onkeyup', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_onkeyup = __quote(__attr_onkeyup, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onkeyup is not None):
                __append((' onkeyup="%s"' % __attr_onkeyup))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872613376
            __default_140362872613376 = _DEFAULT_MARKER

            # <Substitution 'view/onfocus' (25:1)> -> __attr_onfocus
            __token = 734
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onfocus = _static_140362943564528('path', 'view/onfocus', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_onfocus = __quote(__attr_onfocus, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onfocus is not None):
                __append((' onfocus="%s"' % __attr_onfocus))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872612752
            __default_140362872612752 = _DEFAULT_MARKER

            # <Substitution 'view/onblur' (25:28)> -> __attr_onblur
            __token = 761
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onblur = _static_140362943564528('path', 'view/onblur', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_onblur = __quote(__attr_onblur, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onblur is not None):
                __append((' onblur="%s"' % __attr_onblur))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872614000
            __default_140362872614000 = _DEFAULT_MARKER

            # <Substitution 'view/onchange' (27:0)> -> __attr_onchange
            __token = 789
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onchange = _static_140362943564528('path', 'view/onchange', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_onchange = __quote(__attr_onchange, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onchange is not None):
                __append((' onchange="%s"' % __attr_onchange))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362863506960
            __default_140362863506960 = _DEFAULT_MARKER

            # <Boolean 'view/readonly' (27:30)> -> __attr_readonly
            __token = 819
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_readonly = _static_140362943564528('path', 'view/readonly', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            if (__attr_readonly is _DEFAULT_MARKER):
                __attr_readonly = None
            else:
                if __attr_readonly:
                    __attr_readonly = 'readonly'
                else:
                    __attr_readonly = None
            if (__attr_readonly is not None):
                __append((' readonly="%s"' % __attr_readonly))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362863507776
            __default_140362863507776 = _DEFAULT_MARKER

            # <Substitution 'view/accesskey' (28:30)> -> __attr_accesskey
            __token = 850
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accesskey = _static_140362943564528('path', 'view/accesskey', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_accesskey = __quote(__attr_accesskey, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_accesskey is not None):
                __append((' accesskey="%s"' % __attr_accesskey))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362863507536
            __default_140362863507536 = _DEFAULT_MARKER

            # <Substitution 'view/onselect' (29:30)> -> __attr_onselect
            __token = 881
            try:
                __zt_tmp = __attrs_140362863508160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_onselect = _static_140362943564528('path', 'view/onselect', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_onselect = __quote(__attr_onselect, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_onselect is not None):
                __append((' onselect="%s"' % __attr_onselect))
            __append(' >\n  ')

            # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873195296
            __attrs_140362873195296 = _static_140362943909360
            __backup_up_id_140362863506480 = get('up_id', __marker)

            # <Value 'view/file_upload_id' (35:18)> -> __value
            __token = 990
            try:
                __zt_tmp = __attrs_140362873195296
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('path', 'view/file_upload_id', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['up_id'] = __value

            # <Value 'up_id' (37:25)> -> __condition
            __token = 1048
            try:
                __zt_tmp = __attrs_140362873195296
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140362943564528('path', 'up_id', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7fa8c7324460> name=None at 7fa8c73249d0> -> __attrs_140362872748448
                __attrs_140362872748448 = _static_140362873193568

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input')

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873196112
                __default_140362873196112 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${view/name}.file_upload_id' (39:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c7324820> -> __attr_name
                __token = 1076
                __token = 1078
                try:
                    __zt_tmp = __attrs_140362872748448
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140362943564528('path', 'view/name', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                __attr_name = ('%s%s' % ((__attr_name if (__attr_name is not None) else ''), '.file_upload_id', ))
                if (__attr_name is None):
                    pass
                else:
                    if (__attr_name is _DEFAULT_MARKER):
                        __attr_name = None
                    else:
                        __tt = type(__attr_name)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_name = str(__attr_name)
                        else:
                            if (__tt is bytes):
                                __attr_name = decode(__attr_name)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_name = __attr_name.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_name)
                                        __attr_name = (str(__attr_name) if (__attr_name is __converted) else __converted)
                                    else:
                                        __attr_name = __attr_name()
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))
                __append(' type="hidden"')

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873195200
                __default_140362873195200 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${up_id}' (41:18)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c73249a0> -> __attr_value
                __token = 1148
                __token = 1150
                try:
                    __zt_tmp = __attrs_140362872748448
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140362943564528('path', 'up_id', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
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
                __append(' />\n    ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872746912
                __attrs_140362872746912 = _static_140362943909360

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>\n      ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872746672
                __attrs_140362872746672 = _static_140362943909360
                __stream_140362872746432 = []
                __append_140362872746432 = __stream_140362872746432.append
                __append_140362872746432('Image already uploaded:')
                __msgid_140362872746432 = __re_whitespace(''.join(__stream_140362872746432)).strip()
                if 'image_already_uploaded':
                    __append(translate('image_already_uploaded', mapping=None, default=__msgid_140362872746432, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))

                # <Interpolation value=<Substitution '\n        ${view/value/filename}\n    ' (44:90)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c72b7a90> -> __content_140363024536688
                __token = 1275
                __token = 1277
                try:
                    __zt_tmp = __attrs_140362872746912
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140363024536688 = _static_140362943564528('path', 'view/value/filename', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __content_140363024536688 = __quote(__content_140363024536688, '\x00', '&#0;', None, None)
                __content_140363024536688 = ('%s%s%s' % ('\n        ', (__content_140363024536688 if (__content_140363024536688 is not None) else ''), '\n    ', ))
                if (__content_140363024536688 is None):
                    pass
                else:
                    if (__content_140363024536688 is None):
                        __content_140363024536688 = None
                    else:
                        __tt = type(__content_140363024536688)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140363024536688 = str(__content_140363024536688)
                        else:
                            if (__tt is bytes):
                                __content_140363024536688 = decode(__content_140363024536688)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140363024536688 = __content_140363024536688.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140363024536688)
                                        __content_140363024536688 = (str(__content_140363024536688) if (__content_140363024536688 is __converted) else __converted)
                                    else:
                                        __content_140363024536688 = __content_140363024536688()
                if (__content_140363024536688 is not None):
                    __append(__content_140363024536688)
                __append('</span>\n  ')
            if (__backup_up_id_140362863506480 is __marker):
                del econtext['up_id']
            else:
                econtext['up_id'] = __backup_up_id_140362863506480
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872747536
            __attrs_140362872747536 = _static_140362943909360

            # <Value "python:exists and download_url and action=='nochange'" (48:23)> -> __condition
            __token = 1345
            try:
                __zt_tmp = __attrs_140362872747536
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140362943564528('python', "exists and download_url and action=='nochange'", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            if __condition:

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span>\n    ')

                # <Static value=<ast.Dict object at 0x7fa8c72b7970> name=None at 7fa8c72b7760> -> __attrs_140362863295936
                __attrs_140362863295936 = _static_140362872748400

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362863292672
                __default_140362863292672 = _DEFAULT_MARKER

                # <Substitution 'download_url' (50:14)> -> __attr_href
                __token = 1439
                try:
                    __zt_tmp = __attrs_140362863295936
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140362943564528('path', 'download_url', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append('>\n      ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362863294592
                __attrs_140362863294592 = _static_140362943909360

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362863295024
                __default_140362863295024 = _DEFAULT_MARKER

                # <Value 'view/thumb_tag' (52:34)> -> __cache_140362863296464
                __token = 1497
                try:
                    __zt_tmp = __attrs_140362863294592
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140362863296464 = _static_140362943564528('path', 'view/thumb_tag', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                # <BinOp left=<Value 'view/thumb_tag' (52:34)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c69b3070> -> __condition
                __expression = __cache_140362863296464

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append('<img />')
                else:
                    __content = __cache_140362863296464
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n    </a>')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362863295216
                __attrs_140362863295216 = _static_140362943909360

                # <br ... (0:0)
                # --------------------------------------------------------
                __append('<br />\n    ')

                # <Static value=<ast.Dict object at 0x7fa8c69b3a00> name=None at 7fa8c69b3c10> -> __attrs_140362873041248
                __attrs_140362873041248 = _static_140362863294976

                # <Value 'icon' (56:24)> -> __condition
                __token = 1587
                try:
                    __zt_tmp = __attrs_140362873041248
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140362943564528('path', 'icon', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if __condition:

                    # <img ... (0:0)
                    # --------------------------------------------------------
                    __append('<img')

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873044032
                    __default_140362873044032 = _DEFAULT_MARKER

                    # <Substitution 'doc_type' (59:14)> -> __attr_alt
                    __token = 1654
                    try:
                        __zt_tmp = __attrs_140362873041248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_alt = _static_140362943564528('path', 'doc_type', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    __attr_alt = __quote(__attr_alt, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_alt is not None):
                        __append((' alt="%s"' % __attr_alt))

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873043168
                    __default_140362873043168 = _DEFAULT_MARKER

                    # <Substitution 'icon' (58:15)> -> __attr_src
                    __token = 1634
                    try:
                        __zt_tmp = __attrs_140362873041248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_src = _static_140362943564528('path', 'icon', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    __attr_src = __quote(__attr_src, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_src is not None):
                        __append((' src="%s"' % __attr_src))

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873043120
                    __default_140362873043120 = _DEFAULT_MARKER

                    # <Substitution 'filename' (60:15)> -> __attr_title
                    __token = 1680
                    try:
                        __zt_tmp = __attrs_140362873041248
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140362943564528('path', 'filename', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' />')
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7fa8c72ff9d0> name=None at 7fa8c72ffee0> -> __attrs_140362873144416
                __attrs_140362873144416 = _static_140362873043408

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873044848
                __default_140362873044848 = _DEFAULT_MARKER

                # <Substitution 'download_url' (65:14)> -> __attr_href
                __token = 1778
                try:
                    __zt_tmp = __attrs_140362873144416
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140362943564528('path', 'download_url', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >')

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873043600
                __default_140362873043600 = _DEFAULT_MARKER

                # <Value 'filename' (63:20)> -> __cache_140362873044560
                __token = 1730
                try:
                    __zt_tmp = __attrs_140362873144416
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140362873044560 = _static_140362943564528('path', 'filename', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                # <BinOp left=<Value 'filename' (63:20)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c72ff940> -> __condition
                __expression = __cache_140362873044560

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('Filename')
                else:
                    __content = __cache_140362873044560
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</a>\n    ')

                # <Static value=<ast.Dict object at 0x7fa8c7318400> name=None at 7fa8c73189a0> -> __attrs_140362873145808
                __attrs_140362873145808 = _static_140362873144320

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="discreet">\n      &mdash;')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873147200
                __attrs_140362873147200 = _static_140362943909360

                # <Value 'doc_type' (69:38)> -> __condition
                __token = 1885
                try:
                    __zt_tmp = __attrs_140362873147200
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140362943564528('path', 'doc_type', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if __condition:
                    __append('\n        ')

                    # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872691872
                    __attrs_140362872691872 = _static_140362943909360

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872688848
                    __default_140362872688848 = _DEFAULT_MARKER

                    # <Value 'doc_type' (70:27)> -> __cache_140362873144608
                    __token = 1923
                    try:
                        __zt_tmp = __attrs_140362872691872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140362873144608 = _static_140362943564528('path', 'doc_type', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                    # <BinOp left=<Value 'doc_type' (70:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c73182b0> -> __condition
                    __expression = __cache_140362873144608

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span >ContentType</span>')
                    else:
                        __content = __cache_140362873144608
                        __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append(',')
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872692208
                __attrs_140362872692208 = _static_140362943909360
                __backup_sizekb_140362873194384 = get('sizekb', __marker)

                # <Value 'view/file_size' (74:21)> -> __value
                __token = 2055
                try:
                    __zt_tmp = __attrs_140362872692208
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140362943564528('path', 'view/file_size', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                econtext['sizekb'] = __value

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872689280
                __default_140362872689280 = _DEFAULT_MARKER

                # <Value 'sizekb' (76:25)> -> __cache_140362872690960
                __token = 2110
                try:
                    __zt_tmp = __attrs_140362872692208
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140362872690960 = _static_140362943564528('path', 'sizekb', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                # <BinOp left=<Value 'sizekb' (76:25)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c72a92e0> -> __condition
                __expression = __cache_140362872690960

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span >100</span>')
                else:
                    __content = __cache_140362872690960
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                if (__backup_sizekb_140362873194384 is __marker):
                    del econtext['sizekb']
                else:
                    econtext['sizekb'] = __backup_sizekb_140362873194384
                __append('\n    </span>\n  </span>')
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872692496
            __attrs_140362872692496 = _static_140362943909360

            # <Value 'allow_nochange' (81:24)> -> __condition
            __token = 2212
            try:
                __zt_tmp = __attrs_140362872692496
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140362943564528('path', 'allow_nochange', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            if __condition:
                __append('\n    ')

                # <Static value=<ast.Dict object at 0x7fa8c72a9af0> name=None at 7fa8c72a9a60> -> __attrs_140362872388864
                __attrs_140362872388864 = _static_140362872691440

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-check">\n      ')

                # <Static value=<ast.Dict object at 0x7fa8c725f4c0> name=None at 7fa8c725fa00> -> __attrs_140362873080752
                __attrs_140362873080752 = _static_140362872386752

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-check-input" type="radio" value="nochange"')

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872387184
                __default_140362872387184 = _DEFAULT_MARKER

                # <Substitution 'string:${view/name}.action' (87:20)> -> __attr_name
                __token = 2402
                try:
                    __zt_tmp = __attrs_140362873080752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140362943564528('string', '${view/name}.action', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872387376
                __default_140362872387376 = _DEFAULT_MARKER

                # <Substitution 'string:${view/id}-nochange' (88:17)> -> __attr_id
                __token = 2447
                try:
                    __zt_tmp = __attrs_140362873080752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140362943564528('string', '${view/id}-nochange', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872386992
                __default_140362872386992 = _DEFAULT_MARKER

                # <Substitution "string:document.getElementById('${view/id}-input').disabled=true" (89:21)> -> __attr_onclick
                __token = 2497
                try:
                    __zt_tmp = __attrs_140362873080752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_onclick = _static_140362943564528('string', "document.getElementById('${view/id}-input').disabled=true", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_onclick is not None):
                    __append((' onclick="%s"' % __attr_onclick))

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872388384
                __default_140362872388384 = _DEFAULT_MARKER

                # <Boolean "python:'checked' if action == 'nochange' else None" (90:20)> -> __attr_checked
                __token = 2585
                try:
                    __zt_tmp = __attrs_140362873080752
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_checked = _static_140362943564528('python', "'checked' if action == 'nochange' else None", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if (__attr_checked is _DEFAULT_MARKER):
                    __attr_checked = None
                else:
                    if __attr_checked:
                        __attr_checked = 'checked'
                    else:
                        __attr_checked = None
                if (__attr_checked is not None):
                    __append((' checked="%s"' % __attr_checked))
                __append(' />\n      ')

                # <Static value=<ast.Dict object at 0x7fa8c7308190> name=None at 7fa8c73087c0> -> __attrs_140362873077824
                __attrs_140362873077824 = _static_140362873078160

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-check-label"')

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873080416
                __default_140362873080416 = _DEFAULT_MARKER

                # <Substitution 'string:${view/id}-nochange' (95:19)> -> __attr_for
                __token = 2751
                try:
                    __zt_tmp = __attrs_140362873077824
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_140362943564528('string', '${view/id}-nochange', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_for is not None):
                    __append((' for="%s"' % __attr_for))
                __append(' >')
                __stream_140362873079360 = []
                __append_140362873079360 = __stream_140362873079360.append
                __append_140362873079360('Keep existing image')
                __msgid_140362873079360 = __re_whitespace(''.join(__stream_140362873079360)).strip()
                if 'image_keep':
                    __append(translate('image_keep', mapping=None, default=__msgid_140362873079360, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n    </div>\n    ')

                # <Static value=<ast.Dict object at 0x7fa8c7308cd0> name=None at 7fa8c7308340> -> __attrs_140362873080176
                __attrs_140362873080176 = _static_140362873081040

                # <Value 'not:view/field/required' (101:24)> -> __condition
                __token = 2933
                try:
                    __zt_tmp = __attrs_140362873080176
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140362943564528('not', 'view/field/required', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-check" >\n      ')

                    # <Static value=<ast.Dict object at 0x7fa8c7378490> name=None at 7fa8c7378fd0> -> __attrs_140362873540368
                    __attrs_140362873540368 = _static_140362873537680

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input class="form-check-input" type="radio" value="remove"')

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873539600
                    __default_140362873539600 = _DEFAULT_MARKER

                    # <Substitution 'string:${view/name}.action' (107:20)> -> __attr_name
                    __token = 3106
                    try:
                        __zt_tmp = __attrs_140362873540368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_name = _static_140362943564528('string', '${view/name}.action', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_name is not None):
                        __append((' name="%s"' % __attr_name))

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873537392
                    __default_140362873537392 = _DEFAULT_MARKER

                    # <Substitution 'string:${view/id}-remove' (108:17)> -> __attr_id
                    __token = 3151
                    try:
                        __zt_tmp = __attrs_140362873540368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_id = _static_140362943564528('string', '${view/id}-remove', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_id is not None):
                        __append((' id="%s"' % __attr_id))

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873536768
                    __default_140362873536768 = _DEFAULT_MARKER

                    # <Substitution "string:document.getElementById('${view/id}-input').disabled=true" (109:21)> -> __attr_onclick
                    __token = 3199
                    try:
                        __zt_tmp = __attrs_140362873540368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_onclick = _static_140362943564528('string', "document.getElementById('${view/id}-input').disabled=true", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_onclick is not None):
                        __append((' onclick="%s"' % __attr_onclick))

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873537728
                    __default_140362873537728 = _DEFAULT_MARKER

                    # <Boolean "python:'checked' if action == 'remove' else None" (110:20)> -> __attr_checked
                    __token = 3287
                    try:
                        __zt_tmp = __attrs_140362873540368
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_checked = _static_140362943564528('python', "'checked' if action == 'remove' else None", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    if (__attr_checked is _DEFAULT_MARKER):
                        __attr_checked = None
                    else:
                        if __attr_checked:
                            __attr_checked = 'checked'
                        else:
                            __attr_checked = None
                    if (__attr_checked is not None):
                        __append((' checked="%s"' % __attr_checked))
                    __append(' />\n      ')

                    # <Static value=<ast.Dict object at 0x7fa8c73781f0> name=None at 7fa8c7378a90> -> __attrs_140362873269120
                    __attrs_140362873269120 = _static_140362873537008

                    # <label ... (0:0)
                    # --------------------------------------------------------
                    __append('<label class="form-check-label"')

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873268160
                    __default_140362873268160 = _DEFAULT_MARKER

                    # <Substitution 'string:${view/id}-remove' (115:19)> -> __attr_for
                    __token = 3451
                    try:
                        __zt_tmp = __attrs_140362873269120
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_for = _static_140362943564528('string', '${view/id}-remove', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                    __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_for is not None):
                        __append((' for="%s"' % __attr_for))
                    __append(' >')
                    __stream_140362873539936 = []
                    __append_140362873539936 = __stream_140362873539936.append
                    __append_140362873539936('Remove existing image')
                    __msgid_140362873539936 = __re_whitespace(''.join(__stream_140362873539936)).strip()
                    if 'image_remove':
                        __append(translate('image_remove', mapping=None, default=__msgid_140362873539936, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</label>\n    </div>')
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7fa8c7336c70> name=None at 7fa8c7336f10> -> __attrs_140362873269744
                __attrs_140362873269744 = _static_140362873269360

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-check">\n      ')

                # <Static value=<ast.Dict object at 0x7fa8c7336d30> name=None at 7fa8c7336e50> -> __attrs_140362873494544
                __attrs_140362873494544 = _static_140362873269552

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-check-input" type="radio" value="replace"')

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873494304
                __default_140362873494304 = _DEFAULT_MARKER

                # <Substitution 'string:${view/name}.action' (126:20)> -> __attr_name
                __token = 3756
                try:
                    __zt_tmp = __attrs_140362873494544
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_name = _static_140362943564528('string', '${view/name}.action', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_name is not None):
                    __append((' name="%s"' % __attr_name))

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873492144
                __default_140362873492144 = _DEFAULT_MARKER

                # <Substitution 'string:${view/id}-replace' (127:17)> -> __attr_id
                __token = 3801
                try:
                    __zt_tmp = __attrs_140362873494544
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_id = _static_140362943564528('string', '${view/id}-replace', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_id is not None):
                    __append((' id="%s"' % __attr_id))

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873492192
                __default_140362873492192 = _DEFAULT_MARKER

                # <Substitution "string:document.getElementById('${view/id}-input').disabled=false" (128:21)> -> __attr_onclick
                __token = 3850
                try:
                    __zt_tmp = __attrs_140362873494544
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_onclick = _static_140362943564528('string', "document.getElementById('${view/id}-input').disabled=false", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __attr_onclick = __quote(__attr_onclick, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_onclick is not None):
                    __append((' onclick="%s"' % __attr_onclick))

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873493248
                __default_140362873493248 = _DEFAULT_MARKER

                # <Boolean "python:'checked' if action == 'replace' else None" (129:20)> -> __attr_checked
                __token = 3939
                try:
                    __zt_tmp = __attrs_140362873494544
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_checked = _static_140362943564528('python', "'checked' if action == 'replace' else None", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if (__attr_checked is _DEFAULT_MARKER):
                    __attr_checked = None
                else:
                    if __attr_checked:
                        __attr_checked = 'checked'
                    else:
                        __attr_checked = None
                if (__attr_checked is not None):
                    __append((' checked="%s"' % __attr_checked))
                __append(' />\n      ')

                # <Static value=<ast.Dict object at 0x7fa8c736d040> name=None at 7fa8c736dac0> -> __attrs_140362873492672
                __attrs_140362873492672 = _static_140362873491520

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-check-label"')

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873494832
                __default_140362873494832 = _DEFAULT_MARKER

                # <Substitution 'string:${view/id}-replace' (134:19)> -> __attr_for
                __token = 4104
                try:
                    __zt_tmp = __attrs_140362873492672
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_140362943564528('string', '${view/id}-replace', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __attr_for = __quote(__attr_for, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_for is not None):
                    __append((' for="%s"' % __attr_for))
                __append(' >')
                __stream_140362873495168 = []
                __append_140362873495168 = __stream_140362873495168.append
                __append_140362873495168('Replace with new image')
                __msgid_140362873495168 = __re_whitespace(''.join(__stream_140362873495168)).strip()
                if 'image_replace':
                    __append(translate('image_replace', mapping=None, default=__msgid_140362873495168, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</label>\n    </div>\n  ')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7fa8c72aa4f0> name=None at 7fa8c72aa280> -> __attrs_140362873229376
            __attrs_140362873229376 = _static_140362872694000

            # <input ... (0:0)
            # --------------------------------------------------------
            __append('<input class="form-control"')

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872694192
            __default_140362872694192 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${view/accept|nothing}' (142:17)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c72aad00> -> __attr_accept
            __token = 4302
            __token = 4304
            try:
                __zt_tmp = __attrs_140362873229376
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_accept = _static_140362943564528('path', 'view/accept|nothing', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_accept = __quote(__attr_accept, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_accept = __attr_accept
            if (__attr_accept is None):
                pass
            else:
                if (__attr_accept is _DEFAULT_MARKER):
                    __attr_accept = None
                else:
                    __tt = type(__attr_accept)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_accept = str(__attr_accept)
                    else:
                        if (__tt is bytes):
                            __attr_accept = decode(__attr_accept)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_accept = __attr_accept.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_accept)
                                    __attr_accept = (str(__attr_accept) if (__attr_accept is __converted) else __converted)
                                else:
                                    __attr_accept = __attr_accept()
            if (__attr_accept is not None):
                __append((' accept="%s"' % __attr_accept))
            __append(' type="file"')

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872696496
            __default_140362872696496 = _DEFAULT_MARKER

            # <Substitution 'string:${view/id}-input' (145:14)> -> __attr_id
            __token = 4387
            try:
                __zt_tmp = __attrs_140362873229376
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140362943564528('string', '${view/id}-input', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_id is not None):
                __append((' id="%s"' % __attr_id))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872693760
            __default_140362872693760 = _DEFAULT_MARKER

            # <Substitution 'view/name' (146:15)> -> __attr_name
            __token = 4427
            try:
                __zt_tmp = __attrs_140362873229376
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_name = _static_140362943564528('path', 'view/name', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_name = __quote(__attr_name, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_name is not None):
                __append((' name="%s"' % __attr_name))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872695872
            __default_140362872695872 = _DEFAULT_MARKER

            # <Substitution "python:view.required and 'required' or None" (147:18)> -> __attr_required
            __token = 4457
            try:
                __zt_tmp = __attrs_140362873229376
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_required = _static_140362943564528('python', "view.required and 'required' or None", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_required = __quote(__attr_required, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_required is not None):
                __append((' required="%s"' % __attr_required))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872694048
            __default_140362872694048 = _DEFAULT_MARKER

            # <Substitution 'view/size' (148:13)> -> __attr_size
            __token = 4517
            try:
                __zt_tmp = __attrs_140362873229376
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_size = _static_140362943564528('path', 'view/size', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_size = __quote(__attr_size, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_size is not None):
                __append((' size="%s"' % __attr_size))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872694144
            __default_140362872694144 = _DEFAULT_MARKER

            # <Boolean 'view/disabled' (149:16)> -> __attr_disabled
            __token = 4547
            try:
                __zt_tmp = __attrs_140362873229376
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_disabled = _static_140362943564528('path', 'view/disabled', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            if (__attr_disabled is _DEFAULT_MARKER):
                __attr_disabled = None
            else:
                if __attr_disabled:
                    __attr_disabled = 'disabled'
                else:
                    __attr_disabled = None
            if (__attr_disabled is not None):
                __append((' disabled="%s"' % __attr_disabled))

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872693424
            __default_140362872693424 = _DEFAULT_MARKER

            # <Substitution 'view/maxlength' (150:16)> -> __attr_maxlength
            __token = 4582
            try:
                __zt_tmp = __attrs_140362873229376
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_maxlength = _static_140362943564528('path', 'view/maxlength', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_maxlength = __quote(__attr_maxlength, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_maxlength is not None):
                __append((' maxlength="%s"' % __attr_maxlength))
            __append(' />\n  ')

            # <Static value=<ast.Dict object at 0x7fa8c732dca0> name=None at 7fa8c732d400> -> __attrs_140362873230912
            __attrs_140362873230912 = _static_140362873232544

            # <Value 'view/accept|nothing' (154:22)> -> __condition
            __token = 4666
            try:
                __zt_tmp = __attrs_140362873230912
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140362943564528('path', 'view/accept|nothing', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-text" >')
                __stream_140362873827104_accepted_types = ''
                __stream_140362873231680 = []
                __append_140362873231680 = __stream_140362873231680.append
                __append_140362873231680('\n    Allowed types:\n    ')
                __stream_140362873827104_accepted_types = []
                __append_140362873827104_accepted_types = __stream_140362873827104_accepted_types.append

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362873231392
                __attrs_140362873231392 = _static_140362943909360

                # <Interpolation value=<Substitution '${view/accept}' (158:41)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c732d700> -> __content_140363024536688
                __token = 4800
                __token = 4802
                try:
                    __zt_tmp = __attrs_140362873231392
                except get('NameError', NameError):
                    __zt_tmp = None

                __content_140363024536688 = _static_140362943564528('path', 'view/accept', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                __content_140363024536688 = __quote(__content_140363024536688, '\x00', '&#0;', None, None)
                __content_140363024536688 = __content_140363024536688
                if (__content_140363024536688 is None):
                    pass
                else:
                    if (__content_140363024536688 is None):
                        __content_140363024536688 = None
                    else:
                        __tt = type(__content_140363024536688)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __content_140363024536688 = str(__content_140363024536688)
                        else:
                            if (__tt is bytes):
                                __content_140363024536688 = decode(__content_140363024536688)
                            else:
                                if (__tt is not str):
                                    try:
                                        __content_140363024536688 = __content_140363024536688.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__content_140363024536688)
                                        __content_140363024536688 = (str(__content_140363024536688) if (__content_140363024536688 is __converted) else __converted)
                                    else:
                                        __content_140363024536688 = __content_140363024536688()
                if (__content_140363024536688 is not None):
                    __append_140362873827104_accepted_types(__content_140363024536688)
                __append_140362873231680('${accepted_types}')
                __stream_140362873827104_accepted_types = ''.join(__stream_140362873827104_accepted_types)
                __append_140362873231680('.\n  ')
                __msgid_140362873231680 = __re_whitespace(''.join(__stream_140362873231680)).strip()
                if 'namedfile_accepted_types':
                    __append(translate('namedfile_accepted_types', mapping={'accepted_types': __stream_140362873827104_accepted_types, }, default=__msgid_140362873231680, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7fa8c732dfd0> name=None at 7fa8c732d730> -> __attrs_140362872324048
            __attrs_140362872324048 = _static_140362873233360

            # <Value "python:allow_nochange and action != 'replace'" (162:25)> -> __condition
            __token = 4895
            try:
                __zt_tmp = __attrs_140362872324048
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140362943564528('python', "allow_nochange and action != 'replace'", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            if __condition:

                # <script ... (0:0)
                # --------------------------------------------------------
                __append('<script type="text/javascript" >')

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362873230384
                __default_140362873230384 = _DEFAULT_MARKER

                # <Value "string:document.getElementById('${view/id}-input').disabled=true;" (163:23)> -> __cache_140362873231200
                __token = 4965
                try:
                    __zt_tmp = __attrs_140362872324048
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140362873231200 = _static_140362943564528('string', "document.getElementById('${view/id}-input').disabled=true;", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                # <BinOp left=<Value "string:document.getElementById('${view/id}-input').disabled=true;" (163:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c732da90> -> __condition
                __expression = __cache_140362873231200

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n  ')
                else:
                    __content = __cache_140362873231200
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</script>')
            __append('\n\n</div>')
            __i18n_domain = __previous_i18n_domain_140362917344352
            if (__backup_filename_140362863507680 is __marker):
                del econtext['filename']
            else:
                econtext['filename'] = __backup_filename_140362863507680
            if (__backup_icon_140362863509072 is __marker):
                del econtext['icon']
            else:
                econtext['icon'] = __backup_icon_140362863509072
            if (__backup_doc_type_140362863506048 is __marker):
                del econtext['doc_type']
            else:
                econtext['doc_type'] = __backup_doc_type_140362863506048
            if (__backup_allow_nochange_140362863509168 is __marker):
                del econtext['allow_nochange']
            else:
                econtext['allow_nochange'] = __backup_allow_nochange_140362863509168
            if (__backup_action_140362872614336 is __marker):
                del econtext['action']
            else:
                econtext['action'] = __backup_action_140362872614336
            if (__backup_exists_140362872610976 is __marker):
                del econtext['exists']
            else:
                econtext['exists'] = __backup_exists_140362872610976
            if (__backup_download_url_140362872612272 is __marker):
                del econtext['download_url']
            else:
                econtext['download_url'] = __backup_download_url_140362872612272
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }