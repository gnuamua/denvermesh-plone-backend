# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.batching-2.0.6-py3.9.egg/plone/batching/batchnavigation.pt'

__tokens = {132: ('view/batch|nothing', 4, 29), 207: ('batch', 6, 32), 284: ('batch/multiple_pages', 10, 22), 395: ('nothing', 16, 28), 519: ('batch/has_previous', 20, 25), 622: ('python:view.make_link(batch.previouspage)', 24, 18), 885: ('batch/pagesize', 32, 31), 1085: ('nothing', 41, 28), 1203: ('batch/show_link_to_first', 45, 25), 1312: ('python:view.make_link(1)', 49, 18), 1407: ('nothing', 54, 28), 1543: ('batch/second_page_not_in_navlist', 58, 25), 1651: ('nothing', 63, 28), 1819: ('batch/previous_pages', 67, 33), 1960: ('python:view.make_link(pagenumber)', 72, 18), 1902: ('pagenumber', 70, 24), 2063: ('nothing', 77, 28), 2213: ('batch/navlist', 82, 25), 2295: ('batch/pagenumber', 85, 27), 2459: ('nothing', 92, 28), 2623: ('batch/next_pages', 96, 33), 2760: ('python:view.make_link(pagenumber)', 101, 18), 2702: ('pagenumber', 99, 24), 2863: ('nothing', 106, 28), 2999: ('batch/before_last_page_not_in_navlist', 110, 25), 3130: ('nothing', 115, 28), 3246: ('batch/show_link_to_last', 119, 25), 3394: ('python:view.make_link(batch.lastpage)', 124, 18), 3332: ('batch/lastpage', 122, 24), 3501: ('nothing', 129, 28), 3617: ('batch/has_next', 133, 25), 3716: ('python:view.make_link(batch.nextpage)', 137, 18), 3920: ('batch/next_item_count', 144, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140141461845952 = {'aria-hidden': 'true', }
_static_140141461847200 = {'class': 'label', }
_static_140141461927200 = {'class': 'page-link', 'href': 'python:view.make_link(batch.nextpage)', }
_static_140141461852800 = {'class': 'page-item next', }
_static_140141461855632 = {'class': 'page-link', 'href': 'python:view.make_link(batch.lastpage)', }
_static_140141461791984 = {'class': 'page-item last', }
_static_140141461793520 = {'class': 'page-link', }
_static_140141461772944 = {'class': 'page-item disabled', }
_static_140141461771696 = {'class': 'page-link', 'href': 'python:view.make_link(pagenumber)', }
_static_140141461783456 = {'class': 'page-item', }
_static_140141462428496 = {'class': 'sr-only', }
_static_140141452419808 = {'class': 'page-link', }
_static_140141461700032 = {'class': 'page-item active', 'aria-current': 'page', }
_static_140141461696576 = {'class': 'page-link', 'href': 'python:view.make_link(pagenumber)', }
_static_140141462007040 = {'class': 'page-item', }
_static_140141461764848 = {'class': 'page-item disabled', }
_static_140141461990032 = {'class': 'page-link', 'href': 'python:view.make_link(1)', }
_static_140141461990464 = {'class': 'first page-item', }
_static_140141461894672 = {'class': 'label', }
_static_140141461893616 = {'aria-hidden': 'true', }
_static_140141525033168 = {'class': 'page-link', 'href': 'python:view.make_link(batch.previouspage)', }
_static_140141462796992 = {'class': 'page-item previous', }
_static_140141462665056 = {'class': 'pagination', }
_static_140141462665248 = {'class': 'd-flex justify-content-center', }
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

    def render_navigation(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462665392
            __attrs_140141462665392 = _static_140141533420656
            __backup_batch_140141452373488 = get('batch', __marker)

            # <Value 'view/batch|nothing' (4:29)> -> __value
            __token = 132
            try:
                __zt_tmp = __attrs_140141462665392
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('path', 'view/batch|nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['batch'] = __value

            # <Value 'batch' (6:32)> -> __condition
            __token = 207
            try:
                __zt_tmp = __attrs_140141462665392
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140141533071728('path', 'batch', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            if __condition:
                __append('\n\n  ')

                # <Static value=<ast.Dict object at 0x7f753a19b820> name=None at 7f753a19b070> -> __attrs_140141462665488
                __attrs_140141462665488 = _static_140141462665248

                # <Value 'batch/multiple_pages' (10:22)> -> __condition
                __token = 284
                try:
                    __zt_tmp = __attrs_140141462665488
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('path', 'batch/multiple_pages', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:
                    __previous_i18n_domain_140141462667168 = __i18n_domain
                    __i18n_domain = 'plone'

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append('<nav class="d-flex justify-content-center" >\n\n    ')

                    # <Static value=<ast.Dict object at 0x7f753a19b760> name=None at 7f753a19bb50> -> __attrs_140141462797232
                    __attrs_140141462797232 = _static_140141462665056

                    # <ul ... (0:0)
                    # --------------------------------------------------------
                    __append('<ul class="pagination">\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462797424
                    __attrs_140141462797424 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462797520
                    __default_140141462797520 = _DEFAULT_MARKER

                    # <Value 'nothing' (16:28)> -> __cache_140141462795552
                    __token = 395
                    try:
                        __zt_tmp = __attrs_140141462797424
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141462795552 = _static_140141533071728('path', 'nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (16:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1bbeb0> -> __condition
                    __expression = __cache_140141462795552

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Previous page -->\n      ')
                    else:
                        __content = __cache_140141462795552
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f753a1bbac0> name=None at 7f753a1bb9d0> -> __attrs_140141462797904
                    __attrs_140141462797904 = _static_140141462796992

                    # <Value 'batch/has_previous' (20:25)> -> __condition
                    __token = 519
                    try:
                        __zt_tmp = __attrs_140141462797904
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('path', 'batch/has_previous', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item previous" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f753dd160d0> name=None at 7f753dd164c0> -> __attrs_140141461895344
                        __attrs_140141461895344 = _static_140141525033168

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141525036432
                        __default_140141525036432 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(batch.previouspage)' (24:18)> -> __attr_href
                        __token = 622
                        try:
                            __zt_tmp = __attrs_140141461895344
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140141533071728('python', 'view.make_link(batch.previouspage)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n          ')

                        # <Static value=<ast.Dict object at 0x7f753a0df1f0> name=None at 7f753a0df070> -> __attrs_140141461896448
                        __attrs_140141461896448 = _static_140141461893616

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span aria-hidden="true">&lt;</span>\n          ')

                        # <Static value=<ast.Dict object at 0x7f753a0df610> name=None at 7f753a0df4f0> -> __attrs_140141461895008
                        __attrs_140141461895008 = _static_140141461894672

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_140141462745376_number = ''
                        __stream_140141461895920 = []
                        __append_140141461895920 = __stream_140141461895920.append
                        __append_140141461895920('\n            Previous\n            ')
                        __stream_140141462745376_number = []
                        __append_140141462745376_number = __stream_140141462745376_number.append

                        # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461987680
                        __attrs_140141461987680 = _static_140141533420656

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461989264
                        __default_140141461989264 = _DEFAULT_MARKER

                        # <Value 'batch/pagesize' (32:31)> -> __cache_140141461893520
                        __token = 885
                        try:
                            __zt_tmp = __attrs_140141461987680
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140141461893520 = _static_140141533071728('path', 'batch/pagesize', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                        # <BinOp left=<Value 'batch/pagesize' (32:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0f6d60> -> __condition
                        __expression = __cache_140141461893520

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append_140141462745376_number('n')
                        else:
                            __content = __cache_140141461893520
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140141462745376_number(__content)
                        __append_140141461895920('${number}')
                        __stream_140141462745376_number = ''.join(__stream_140141462745376_number)
                        __append_140141461895920('\n             items\n          ')
                        __msgid_140141461895920 = __re_whitespace(''.join(__stream_140141461895920)).strip()
                        if 'batch_previous_x_items':
                            __append(translate('batch_previous_x_items', mapping={'number': __stream_140141462745376_number, }, default=__msgid_140141461895920, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n        </a>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461989360
                    __attrs_140141461989360 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461990128
                    __default_140141461990128 = _DEFAULT_MARKER

                    # <Value 'nothing' (41:28)> -> __cache_140141461987536
                    __token = 1085
                    try:
                        __zt_tmp = __attrs_140141461989360
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141461987536 = _static_140141533071728('path', 'nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (41:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0f63a0> -> __condition
                    __expression = __cache_140141461987536

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- First page -->\n      ')
                    else:
                        __content = __cache_140141461987536
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f753a0f6c40> name=None at 7f753a0f62e0> -> __attrs_140141461988736
                    __attrs_140141461988736 = _static_140141461990464

                    # <Value 'batch/show_link_to_first' (45:25)> -> __condition
                    __token = 1203
                    try:
                        __zt_tmp = __attrs_140141461988736
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('path', 'batch/show_link_to_first', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="first page-item" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f753a0f6a90> name=None at 7f753a0f6100> -> __attrs_140141461763792
                        __attrs_140141461763792 = _static_140141461990032

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461763936
                        __default_140141461763936 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(1)' (49:18)> -> __attr_href
                        __token = 1312
                        try:
                            __zt_tmp = __attrs_140141461763792
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140141533071728('python', 'view.make_link(1)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >1</a>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461763888
                    __attrs_140141461763888 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461765520
                    __default_140141461765520 = _DEFAULT_MARKER

                    # <Value 'nothing' (54:28)> -> __cache_140141461766048
                    __token = 1407
                    try:
                        __zt_tmp = __attrs_140141461763888
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141461766048 = _static_140141533071728('path', 'nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (54:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0bffd0> -> __condition
                    __expression = __cache_140141461766048

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Ellipsis after first item -->\n      ')
                    else:
                        __content = __cache_140141461766048
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f753a0bfaf0> name=None at 7f753a0bfd00> -> __attrs_140141462005264
                    __attrs_140141462005264 = _static_140141461764848

                    # <Value 'batch/second_page_not_in_navlist' (58:25)> -> __condition
                    __token = 1543
                    try:
                        __zt_tmp = __attrs_140141462005264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('path', 'batch/second_page_not_in_navlist', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item disabled" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462004544
                        __attrs_140141462004544 = _static_140141533420656

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span>...</span>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462005744
                    __attrs_140141462005744 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462004160
                    __default_140141462004160 = _DEFAULT_MARKER

                    # <Value 'nothing' (63:28)> -> __cache_140141462006800
                    __token = 1651
                    try:
                        __zt_tmp = __attrs_140141462005744
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141462006800 = _static_140141533071728('path', 'nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (63:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0faa90> -> __condition
                    __expression = __cache_140141462006800

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Pagelist with links to previous pages for quick navigation -->\n      ')
                    else:
                        __content = __cache_140141462006800
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f753a0fad00> name=None at 7f753e2a2130> -> __attrs_140141532723616
                    __attrs_140141532723616 = _static_140141462007040
                    __backup_pagenumber_140141462666208 = get('pagenumber', __marker)

                    # <Value 'batch/previous_pages' (67:33)> -> __iterator
                    __token = 1819
                    try:
                        __zt_tmp = __attrs_140141532723616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140141533071728('path', 'batch/previous_pages', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    (__iterator, ____index_140141532723136, ) = getname('repeat')('pagenumber', __iterator)
                    econtext['pagenumber'] = None
                    for __item in __iterator:
                        econtext['pagenumber'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f753a0af040> name=None at 7f753a0af2b0> -> __attrs_140141461697248
                        __attrs_140141461697248 = _static_140141461696576

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461699696
                        __default_140141461699696 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(pagenumber)' (72:18)> -> __attr_href
                        __token = 1960
                        try:
                            __zt_tmp = __attrs_140141461697248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140141533071728('python', 'view.make_link(pagenumber)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461696624
                        __default_140141461696624 = _DEFAULT_MARKER

                        # <Value 'pagenumber' (70:24)> -> __cache_140141461697872
                        __token = 1902
                        try:
                            __zt_tmp = __attrs_140141461697248
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140141461697872 = _static_140141533071728('path', 'pagenumber', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                        # <BinOp left=<Value 'pagenumber' (70:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0af610> -> __condition
                        __expression = __cache_140141461697872

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140141461697872
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>\n      </li>')
                        ____index_140141532723136 -= 1
                        if (____index_140141532723136 > 0):
                            __append('\n      ')
                    if (__backup_pagenumber_140141462666208 is __marker):
                        del econtext['pagenumber']
                    else:
                        econtext['pagenumber'] = __backup_pagenumber_140141462666208
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461697440
                    __attrs_140141461697440 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461699408
                    __default_140141461699408 = _DEFAULT_MARKER

                    # <Value 'nothing' (77:28)> -> __cache_140141461696672
                    __token = 2063
                    try:
                        __zt_tmp = __attrs_140141461697440
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141461696672 = _static_140141533071728('path', 'nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (77:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0afee0> -> __condition
                    __expression = __cache_140141461696672

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Active page -->\n      ')
                    else:
                        __content = __cache_140141461696672
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f753a0afdc0> name=None at 7f753a0afcd0> -> __attrs_140141452420768
                    __attrs_140141452420768 = _static_140141461700032

                    # <Value 'batch/navlist' (82:25)> -> __condition
                    __token = 2213
                    try:
                        __zt_tmp = __attrs_140141452420768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('path', 'batch/navlist', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item active" aria-current="page" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f75397d62e0> name=None at 7f75397d6430> -> __attrs_140141452419568
                        __attrs_140141452419568 = _static_140141452419808

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="page-link" >')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141452419184
                        __default_140141452419184 = _DEFAULT_MARKER

                        # <Value 'batch/pagenumber' (85:27)> -> __cache_140141452422064
                        __token = 2295
                        try:
                            __zt_tmp = __attrs_140141452419568
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140141452422064 = _static_140141533071728('path', 'batch/pagenumber', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                        # <BinOp left=<Value 'batch/pagenumber' (85:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f75397d6cd0> -> __condition
                        __expression = __cache_140141452422064

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140141452422064
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n        ')

                        # <Static value=<ast.Dict object at 0x7f753a161b50> name=None at 7f753a1617c0> -> __attrs_140141462428016
                        __attrs_140141462428016 = _static_140141462428496

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="sr-only" >')
                        __stream_140141462426720 = []
                        __append_140141462426720 = __stream_140141462426720.append
                        __msgid_140141462426720 = __re_whitespace(''.join(__stream_140141462426720)).strip()
                        if '(current)':
                            __append(translate('(current)', mapping=None, default=__msgid_140141462426720, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461784416
                    __attrs_140141461784416 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461784656
                    __default_140141461784656 = _DEFAULT_MARKER

                    # <Value 'nothing' (92:28)> -> __cache_140141461784752
                    __token = 2459
                    try:
                        __zt_tmp = __attrs_140141461784416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141461784752 = _static_140141533071728('path', 'nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (92:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0c48e0> -> __condition
                    __expression = __cache_140141461784752

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Pagelist with links to next pages for quick navigation -->\n      ')
                    else:
                        __content = __cache_140141461784752
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f753a0c43a0> name=None at 7f753a0c4400> -> __attrs_140141461784272
                    __attrs_140141461784272 = _static_140141461783456
                    __backup_pagenumber_140141462664768 = get('pagenumber', __marker)

                    # <Value 'batch/next_pages' (96:33)> -> __iterator
                    __token = 2623
                    try:
                        __zt_tmp = __attrs_140141461784272
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140141533071728('path', 'batch/next_pages', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    (__iterator, ____index_140141461782688, ) = getname('repeat')('pagenumber', __iterator)
                    econtext['pagenumber'] = None
                    for __item in __iterator:
                        econtext['pagenumber'] = __item

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f753a0c15b0> name=None at 7f753a0c4cd0> -> __attrs_140141461774192
                        __attrs_140141461774192 = _static_140141461771696

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461771840
                        __default_140141461771840 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(pagenumber)' (101:18)> -> __attr_href
                        __token = 2760
                        try:
                            __zt_tmp = __attrs_140141461774192
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140141533071728('python', 'view.make_link(pagenumber)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461786048
                        __default_140141461786048 = _DEFAULT_MARKER

                        # <Value 'pagenumber' (99:24)> -> __cache_140141461782880
                        __token = 2702
                        try:
                            __zt_tmp = __attrs_140141461774192
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140141461782880 = _static_140141533071728('path', 'pagenumber', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                        # <BinOp left=<Value 'pagenumber' (99:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0c4040> -> __condition
                        __expression = __cache_140141461782880

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140141461782880
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>\n      </li>')
                        ____index_140141461782688 -= 1
                        if (____index_140141461782688 > 0):
                            __append('\n      ')
                    if (__backup_pagenumber_140141462664768 is __marker):
                        del econtext['pagenumber']
                    else:
                        econtext['pagenumber'] = __backup_pagenumber_140141462664768
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461772176
                    __attrs_140141461772176 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461771600
                    __default_140141461771600 = _DEFAULT_MARKER

                    # <Value 'nothing' (106:28)> -> __cache_140141461771024
                    __token = 2863
                    try:
                        __zt_tmp = __attrs_140141461772176
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141461771024 = _static_140141533071728('path', 'nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (106:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0c12e0> -> __condition
                    __expression = __cache_140141461771024

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Ellipsis before last item -->\n      ')
                    else:
                        __content = __cache_140141461771024
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f753a0c1a90> name=None at 7f753a0c1e50> -> __attrs_140141461773568
                    __attrs_140141461773568 = _static_140141461772944

                    # <Value 'batch/before_last_page_not_in_navlist' (110:25)> -> __condition
                    __token = 2999
                    try:
                        __zt_tmp = __attrs_140141461773568
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('path', 'batch/before_last_page_not_in_navlist', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item disabled" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f753a0c6af0> name=None at 7f753a0c6ca0> -> __attrs_140141461791600
                        __attrs_140141461791600 = _static_140141461793520

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="page-link">...</span>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461794048
                    __attrs_140141461794048 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461794384
                    __default_140141461794384 = _DEFAULT_MARKER

                    # <Value 'nothing' (115:28)> -> __cache_140141461791840
                    __token = 3130
                    try:
                        __zt_tmp = __attrs_140141461794048
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141461791840 = _static_140141533071728('path', 'nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (115:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0c6430> -> __condition
                    __expression = __cache_140141461791840

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Last page -->\n      ')
                    else:
                        __content = __cache_140141461791840
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f753a0c64f0> name=None at 7f753a0c69a0> -> __attrs_140141461853856
                    __attrs_140141461853856 = _static_140141461791984

                    # <Value 'batch/show_link_to_last' (119:25)> -> __condition
                    __token = 3246
                    try:
                        __zt_tmp = __attrs_140141461853856
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('path', 'batch/show_link_to_last', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item last" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f753a0d5d90> name=None at 7f753a0d5e20> -> __attrs_140141461856016
                        __attrs_140141461856016 = _static_140141461855632

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461855488
                        __default_140141461855488 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(batch.lastpage)' (124:18)> -> __attr_href
                        __token = 3394
                        try:
                            __zt_tmp = __attrs_140141461856016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140141533071728('python', 'view.make_link(batch.lastpage)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461854432
                        __default_140141461854432 = _DEFAULT_MARKER

                        # <Value 'batch/lastpage' (122:24)> -> __cache_140141461853760
                        __token = 3332
                        try:
                            __zt_tmp = __attrs_140141461856016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140141461853760 = _static_140141533071728('path', 'batch/lastpage', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                        # <BinOp left=<Value 'batch/lastpage' (122:24)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0d5040> -> __condition
                        __expression = __cache_140141461853760

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            pass
                        else:
                            __content = __cache_140141461853760
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</a>\n      </li>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461929264
                    __attrs_140141461929264 = _static_140141533420656

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461929024
                    __default_140141461929024 = _DEFAULT_MARKER

                    # <Value 'nothing' (129:28)> -> __cache_140141461854816
                    __token = 3501
                    try:
                        __zt_tmp = __attrs_140141461929264
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141461854816 = _static_140141533071728('path', 'nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'nothing' (129:28)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0d5a90> -> __condition
                    __expression = __cache_140141461854816

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n        <!-- Next page -->\n      ')
                    else:
                        __content = __cache_140141461854816
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('\n      ')

                    # <Static value=<ast.Dict object at 0x7f753a0d5280> name=None at 7f753a0d57c0> -> __attrs_140141461927920
                    __attrs_140141461927920 = _static_140141461852800

                    # <Value 'batch/has_next' (133:25)> -> __condition
                    __token = 3617
                    try:
                        __zt_tmp = __attrs_140141461927920
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('path', 'batch/has_next', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:

                        # <li ... (0:0)
                        # --------------------------------------------------------
                        __append('<li class="page-item next" >\n        ')

                        # <Static value=<ast.Dict object at 0x7f753a0e7520> name=None at 7f753a0e7640> -> __attrs_140141461929408
                        __attrs_140141461929408 = _static_140141461927200

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="page-link"')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461925952
                        __default_140141461925952 = _DEFAULT_MARKER

                        # <Substitution 'python:view.make_link(batch.nextpage)' (137:18)> -> __attr_href
                        __token = 3716
                        try:
                            __zt_tmp = __attrs_140141461929408
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140141533071728('python', 'view.make_link(batch.nextpage)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n          ')

                        # <Static value=<ast.Dict object at 0x7f753a0d3ca0> name=None at 7f753a0d3cd0> -> __attrs_140141461844608
                        __attrs_140141461844608 = _static_140141461847200

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_140141462745824_number = ''
                        __stream_140141461846624 = []
                        __append_140141461846624 = __stream_140141461846624.append
                        __append_140141461846624('\n            Next\n            ')
                        __stream_140141462745824_number = []
                        __append_140141462745824_number = __stream_140141462745824_number.append

                        # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461845040
                        __attrs_140141461845040 = _static_140141533420656

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461845568
                        __default_140141461845568 = _DEFAULT_MARKER

                        # <Value 'batch/next_item_count' (144:31)> -> __cache_140141461844464
                        __token = 3920
                        try:
                            __zt_tmp = __attrs_140141461845040
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140141461844464 = _static_140141533071728('path', 'batch/next_item_count', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                        # <BinOp left=<Value 'batch/next_item_count' (144:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0d3e50> -> __condition
                        __expression = __cache_140141461844464

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append_140141462745824_number('n')
                        else:
                            __content = __cache_140141461844464
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140141462745824_number(__content)
                        __append_140141461846624('${number}')
                        __stream_140141462745824_number = ''.join(__stream_140141462745824_number)
                        __append_140141461846624('\n            items\n          ')
                        __msgid_140141461846624 = __re_whitespace(''.join(__stream_140141461846624)).strip()
                        if 'batch_next_x_items':
                            __append(translate('batch_next_x_items', mapping={'number': __stream_140141462745824_number, }, default=__msgid_140141461846624, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n          ')

                        # <Static value=<ast.Dict object at 0x7f753a0d37c0> name=None at 7f753a0d3040> -> __attrs_140141461844320
                        __attrs_140141461844320 = _static_140141461845952

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span aria-hidden="true">&gt;</span>\n        </a>\n      </li>')
                    __append('\n    </ul>\n\n  </nav>')
                    __i18n_domain = __previous_i18n_domain_140141462667168
                __append('\n\n')
            if (__backup_batch_140141452373488 is __marker):
                del econtext['batch']
            else:
                econtext['batch'] = __backup_batch_140141452373488
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
            __append('<!-- Navigation -->\n')
            __token = None
            render_navigation(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_navigation': render_navigation, 'render': render, }