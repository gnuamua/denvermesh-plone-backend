# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.z3cform-4.3.2-py3.9.egg/plone/app/z3cform/templates/widget.pt'

__tokens = {320: ('nocall:context', 6, 14), 348: (' python:widget.erro', 7, 12), 387: ("s python:error and ' error' or ", 8, 17), 439: ("es python: (None, '', [], ('', '', '', '00', '00', ''), ('', '', '", 9, 17), 525: ("ass python: (widget.value in empty_values) and ' empty' o", 10, 15), 12: ("mb-3 field fieldname-${python:widget.name} widget-mode-${python:widget.mode}${error_class}${empty_class} ${python: getattr(widget, 'wrapper_css_class', '')}", 1, 12), 35: ('python:widget.name', 1, 35), 69: ('python:widget.mode', 1, 69), 90: ('error_class', 1, 90), 104: ('empty_class', 1, 104), 119: ("python: getattr(widget, 'wrapper_css_class', '')", 1, 119), 179: ('formfield-${python:widget.id}', 2, 9), 191: ('python:widget.id', 2, 21), 272: ('${widget/name}', 4, 21), 274: ('widget/name', 4, 23), 709: ("python: widget.mode == 'input' and widget.label", 16, 24), 664: ('${python:widget.id}', 15, 14), 666: ('python:widget.id', 15, 16), 785: ('python:widget.label', 18, 23), 932: ('python:widget.required', 24, 25), 1095: ("python: widget.mode == 'display' and widget.label", 29, 20), 1173: ('python:widget.label', 31, 23), 1337: ('python:widget.render()', 38, 32), 1433: ("python: getattr(widget, 'description', widget.field.description)", 43, 21), 1530: ("python:description and widget.mode == 'input'", 45, 22), 1607: ('description', 46, 30), 1697: ('error', 52, 22), 1734: ('python:error.render() or False', 53, 30)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140362872771776 = {'class': 'form-text', }
_static_140362863383600 = {'type': 'text', }
_static_140362863367312 = {'class': 'widget-label form-label d-block', }
_static_140362863369040 = {'class': 'required', 'title': 'Required', }
_static_140362943909360 = {}
_static_140362863194656 = {'class': 'form-label', 'for': '${python:widget.id}', }
_static_140362943564240 = __C2ZContextWrapper
_static_140362943564528 = __compile_zt_expr
_static_140362872812784 = {'class': "mb-3 field fieldname-${python:widget.name} widget-mode-${python:widget.mode}${error_class}${empty_class} ${python: getattr(widget, 'wrapper_css_class', '')}", 'id': 'formfield-${python:widget.id}', 'data-fieldname': '${widget/name}', }

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

    def render_widget_wrapper(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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
            __slot_widget = econtext['__slot_widget'].pop()
        except:
            __slot_widget = None

        try:
            getname = econtext.get_name
            get = econtext.get

            # <Static value=<ast.Dict object at 0x7fa8c72c74f0> name=None at 7fa8c72c7bb0> -> __attrs_140362863198160
            __attrs_140362863198160 = _static_140362872812784
            __backup_widget_140362872998592 = get('widget', __marker)

            # <Value 'nocall:context' (6:14)> -> __value
            __token = 320
            try:
                __zt_tmp = __attrs_140362863198160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('nocall', 'context', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['widget'] = __value
            __backup_error_140362872888816 = get('error', __marker)

            # <Value 'python:widget.error' (7:12)> -> __value
            __token = 348
            try:
                __zt_tmp = __attrs_140362863198160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('python', 'widget.error', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['error'] = __value
            __backup_error_class_140362872812208 = get('error_class', __marker)

            # <Value "python:error and ' error' or ''" (8:17)> -> __value
            __token = 387
            try:
                __zt_tmp = __attrs_140362863198160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('python', "error and ' error' or ''", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['error_class'] = __value
            __backup_empty_values_140362873186240 = get('empty_values', __marker)

            # <Value "python: (None, '', [], ('', '', '', '00', '00', ''), ('', '', ''))" (9:17)> -> __value
            __token = 439
            try:
                __zt_tmp = __attrs_140362863198160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('python', " (None, '', [], ('', '', '', '00', '00', ''), ('', '', ''))", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['empty_values'] = __value
            __backup_empty_class_140362873186384 = get('empty_class', __marker)

            # <Value "python: (widget.value in empty_values) and ' empty' or ''" (10:15)> -> __value
            __token = 525
            try:
                __zt_tmp = __attrs_140362863198160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('python', " (widget.value in empty_values) and ' empty' or ''", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['empty_class'] = __value
            __previous_i18n_domain_140362863197104 = __i18n_domain
            __i18n_domain = 'plone'

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div')

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872814128
            __default_140362872814128 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution "mb-3 field fieldname-${python:widget.name} widget-mode-${python:widget.mode}${error_class}${empty_class} ${python: getattr(widget, 'wrapper_css_class', '')}" (1:12)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c72c73a0> -> __attr_class
            __token = 12
            __token = 35
            try:
                __zt_tmp = __attrs_140362863198160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class = _static_140362943564528('python', 'widget.name', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 69
            try:
                __zt_tmp = __attrs_140362863198160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_67 = _static_140362943564528('python', 'widget.mode', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_class_67 = __quote(__attr_class_67, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 90
            try:
                __zt_tmp = __attrs_140362863198160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_88 = _static_140362943564528('path', 'error_class', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_class_88 = __quote(__attr_class_88, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 104
            try:
                __zt_tmp = __attrs_140362863198160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_102 = _static_140362943564528('path', 'empty_class', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_class_102 = __quote(__attr_class_102, '"', '&quot;', None, _DEFAULT_MARKER)
            __token = 119
            try:
                __zt_tmp = __attrs_140362863198160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_class_117 = _static_140362943564528('python', " getattr(widget, 'wrapper_css_class', '')", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_class_117 = __quote(__attr_class_117, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_class = ('%s%s%s%s%s%s%s%s' % ('mb-3 field fieldname-', (__attr_class if (__attr_class is not None) else ''), ' widget-mode-', (__attr_class_67 if (__attr_class_67 is not None) else ''), (__attr_class_88 if (__attr_class_88 is not None) else ''), (__attr_class_102 if (__attr_class_102 is not None) else ''), ' ', (__attr_class_117 if (__attr_class_117 is not None) else ''), ))
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

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872812160
            __default_140362872812160 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution 'formfield-${python:widget.id}' (2:9)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c72c73d0> -> __attr_id
            __token = 179
            __token = 191
            try:
                __zt_tmp = __attrs_140362863198160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_id = _static_140362943564528('python', 'widget.id', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_id = __quote(__attr_id, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_id = ('%s%s' % ('formfield-', (__attr_id if (__attr_id is not None) else ''), ))
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

            # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872813264
            __default_140362872813264 = _DEFAULT_MARKER

            # <Interpolation value=<Substitution '${widget/name}' (4:21)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c72c7d60> -> __attr_data_fieldname
            __token = 272
            __token = 274
            try:
                __zt_tmp = __attrs_140362863198160
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_data_fieldname = _static_140362943564528('path', 'widget/name', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            __attr_data_fieldname = __quote(__attr_data_fieldname, '"', '&quot;', None, _DEFAULT_MARKER)
            __attr_data_fieldname = __attr_data_fieldname
            if (__attr_data_fieldname is None):
                pass
            else:
                if (__attr_data_fieldname is _DEFAULT_MARKER):
                    __attr_data_fieldname = None
                else:
                    __tt = type(__attr_data_fieldname)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __attr_data_fieldname = str(__attr_data_fieldname)
                    else:
                        if (__tt is bytes):
                            __attr_data_fieldname = decode(__attr_data_fieldname)
                        else:
                            if (__tt is not str):
                                try:
                                    __attr_data_fieldname = __attr_data_fieldname.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__attr_data_fieldname)
                                    __attr_data_fieldname = (str(__attr_data_fieldname) if (__attr_data_fieldname is __converted) else __converted)
                                else:
                                    __attr_data_fieldname = __attr_data_fieldname()
            if (__attr_data_fieldname is not None):
                __append((' data-fieldname="%s"' % __attr_data_fieldname))
            __append(' >\n  ')

            # <Static value=<ast.Dict object at 0x7fa8c699b220> name=None at 7fa8c699b700> -> __attrs_140362863195856
            __attrs_140362863195856 = _static_140362863194656

            # <Value "python: widget.mode == 'input' and widget.label" (16:24)> -> __condition
            __token = 709
            try:
                __zt_tmp = __attrs_140362863195856
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140362943564528('python', " widget.mode == 'input' and widget.label", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            if __condition:

                # <label ... (0:0)
                # --------------------------------------------------------
                __append('<label class="form-label"')

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362863196336
                __default_140362863196336 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '${python:widget.id}' (15:14)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7fa8c699b0d0> -> __attr_for
                __token = 664
                __token = 666
                try:
                    __zt_tmp = __attrs_140362863195856
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_for = _static_140362943564528('python', 'widget.id', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
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
                __append(' >\n    ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362863368128
                __attrs_140362863368128 = _static_140362943909360

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362863367936
                __default_140362863367936 = _DEFAULT_MARKER

                # <Value 'python:widget.label' (18:23)> -> __cache_140362863369712
                __token = 785
                try:
                    __zt_tmp = __attrs_140362863368128
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140362863369712 = _static_140362943564528('python', 'widget.label', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:widget.label' (18:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c69c56a0> -> __condition
                __expression = __cache_140362863369712

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span >label</span>')
                else:
                    __content = __cache_140362863369712
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7fa8c69c5b50> name=None at 7fa8c69c5a00> -> __attrs_140362863370048
                __attrs_140362863370048 = _static_140362863369040

                # <Value 'python:widget.required' (24:25)> -> __condition
                __token = 932
                try:
                    __zt_tmp = __attrs_140362863370048
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140362943564528('python', 'widget.required', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="required"')

                    # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362863368800
                    __default_140362863368800 = _DEFAULT_MARKER

                    # <Translate msgid='title_required' node=<ast.Constant object at 0x7fa8c69c5cd0> at 7fa8c69c5550> -> __attr_title
                    __attr_title = 'Required'
                    __attr_title = translate('title_required', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append(' ></span>')
                __append('\n  </label>')
            __append('\n  ')

            # <Static value=<ast.Dict object at 0x7fa8c69c5490> name=None at 7fa8c69c51f0> -> __attrs_140362863385856
            __attrs_140362863385856 = _static_140362863367312

            # <Value "python: widget.mode == 'display' and widget.label" (29:20)> -> __condition
            __token = 1095
            try:
                __zt_tmp = __attrs_140362863385856
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140362943564528('python', " widget.mode == 'display' and widget.label", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            if __condition:

                # <b ... (0:0)
                # --------------------------------------------------------
                __append('<b class="widget-label form-label d-block" >\n    ')

                # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362863386192
                __attrs_140362863386192 = _static_140362943909360

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362863386384
                __default_140362863386384 = _DEFAULT_MARKER

                # <Value 'python:widget.label' (31:23)> -> __cache_140362863385136
                __token = 1173
                try:
                    __zt_tmp = __attrs_140362863386192
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140362863385136 = _static_140362943564528('python', 'widget.label', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:widget.label' (31:23)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c69c99d0> -> __condition
                __expression = __cache_140362863385136

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span >label</span>')
                else:
                    __content = __cache_140362863385136
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('\n  </b>')
            __append('\n\n  ')
            if (__slot_widget is None):

                # <Static value=<ast.Dict object at 0x7fa8c69c9430> name=None at 7fa8c69c9520> -> __attrs_140362872771824
                __attrs_140362872771824 = _static_140362863383600

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362863383504
                __default_140362863383504 = _DEFAULT_MARKER

                # <Value 'python:widget.render()' (38:32)> -> __cache_140362863382688
                __token = 1337
                try:
                    __zt_tmp = __attrs_140362872771824
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140362863382688 = _static_140362943564528('python', 'widget.render()', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:widget.render()' (38:32)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c69c97c0> -> __condition
                __expression = __cache_140362863382688

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="text" />')
                else:
                    __content = __cache_140362863382688
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            else:
                __slot_widget(__stream, econtext.copy(), rcontext)
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7fa8c72bd4c0> name=None at 7fa8c72bdf70> -> __attrs_140362872773936
            __attrs_140362872773936 = _static_140362872771776
            __backup_description_140362873183056 = get('description', __marker)

            # <Value "python: getattr(widget, 'description', widget.field.description)" (43:21)> -> __value
            __token = 1433
            try:
                __zt_tmp = __attrs_140362872773936
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140362943564528('python', " getattr(widget, 'description', widget.field.description)", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            econtext['description'] = __value

            # <Value "python:description and widget.mode == 'input'" (45:22)> -> __condition
            __token = 1530
            try:
                __zt_tmp = __attrs_140362872773936
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140362943564528('python', "description and widget.mode == 'input'", econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-text" >')

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872771056
                __default_140362872771056 = _DEFAULT_MARKER

                # <Value 'description' (46:30)> -> __cache_140362872773888
                __token = 1607
                try:
                    __zt_tmp = __attrs_140362872773936
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140362872773888 = _static_140362943564528('path', 'description', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                # <BinOp left=<Value 'description' (46:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c72bd7f0> -> __condition
                __expression = __cache_140362872773888

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('\n      help text\n  ')
                else:
                    __content = __cache_140362872773888
                    __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('</div>')
            if (__backup_description_140362873183056 is __marker):
                del econtext['description']
            else:
                econtext['description'] = __backup_description_140362873183056
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7fa8cb694df0> name=None at 7fa8cb694e50> -> __attrs_140362872915424
            __attrs_140362872915424 = _static_140362943909360

            # <Value 'error' (52:22)> -> __condition
            __token = 1697
            try:
                __zt_tmp = __attrs_140362872915424
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140362943564528('path', 'error', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))
            if __condition:

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __default_140362872772832
                __default_140362872772832 = _DEFAULT_MARKER

                # <Value 'python:error.render() or False' (53:30)> -> __cache_140362872770864
                __token = 1734
                try:
                    __zt_tmp = __attrs_140362872915424
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140362872770864 = _static_140362943564528('python', 'error.render() or False', econtext=econtext)(_static_140362943564240(econtext, __zt_tmp))

                # <BinOp left=<Value 'python:error.render() or False' (53:30)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa8cb731f70> at 7fa8c72bd5e0> -> __condition
                __expression = __cache_140362872770864

                # <Symbol value=<DEFAULT> at 7fa8cb731f70> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div >\n        Error\n  </div>')
                else:
                    __content = __cache_140362872770864
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
            __append('\n\n</div>')
            __i18n_domain = __previous_i18n_domain_140362863197104
            if (__backup_empty_class_140362873186384 is __marker):
                del econtext['empty_class']
            else:
                econtext['empty_class'] = __backup_empty_class_140362873186384
            if (__backup_empty_values_140362873186240 is __marker):
                del econtext['empty_values']
            else:
                econtext['empty_values'] = __backup_empty_values_140362873186240
            if (__backup_error_class_140362872812208 is __marker):
                del econtext['error_class']
            else:
                econtext['error_class'] = __backup_error_class_140362872812208
            if (__backup_error_140362872888816 is __marker):
                del econtext['error']
            else:
                econtext['error'] = __backup_error_140362872888816
            if (__backup_widget_140362872998592 is __marker):
                del econtext['widget']
            else:
                econtext['widget'] = __backup_widget_140362872998592
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
            render_widget_wrapper(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_widget_wrapper': render_widget_wrapper, 'render': render, }