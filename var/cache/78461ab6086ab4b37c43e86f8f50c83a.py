# -*- coding: utf-8 -*-
__filename = 'manage_main'

__tokens = {31: ('here/manage_page_header', 1, 31), 89: ('here/manage_tabs', 3, 29), 238: ("python:getattr(here.aq_explicit, 'has_order_support', 0)", 7, 38), 318: (' modules/AccessControl/getSecurityManage', 8, 22), 392: ("t python: 'position' if has_order_support else 'i", 9, 31), 467: ("ey python:request.get('skey',default_so", 10, 22), 532: ("key python:request.get('rkey','a", 11, 21), 594: ("_alt python:'desc' if rkey=='asc' else ", 12, 24), 666: ('lt_up rkey_alt', 13, 26), 705: ('   obs python: here.manage_get_sortedObjects(sortkey = skey, revkey ', 14, 17), 801: (' my_url string:${context/absolute_url}/man', 15, 19), 905: ('string:${request/URL1}/', 17, 31), 962: ('obs', 19, 30), 1057: ('obs', 20, 89), 1120: ("python:'thead-light sorted_%s'%(request.get('rkey',''))", 21, 57), 1550: ('string:Sort ${rkey_alt_up} by meta-type', 29, 39), 1628: (' string:${my_url}?skey=meta_type&rkey=${rkey_alt', 30, 37), 1716: ("s python:skey=='meta_type' and 'zmi-sort_key' or No", 31, 37), 2066: ('string:Sort ${rkey_alt_up} by name', 39, 39), 2139: (' string:${my_url}?skey=id&rkey=${rkey_alt', 40, 37), 2220: ("s python:skey=='id' and 'zmi-sort_key' or No", 41, 37), 2879: ('string:Sort ${rkey_alt_up} by size', 52, 39), 2952: (' string:${my_url}?skey=get_size&rkey=${rkey_alt', 53, 37), 3039: ("s python:skey=='get_size' and 'zmi-sort_key' or No", 54, 37), 3451: ('string:Sort ${rkey_alt_up} by modification date', 63, 39), 3537: (' string:${my_url}?skey=_p_mtime&rkey=${rkey_alt', 64, 37), 3624: ("s python:skey=='_p_mtime' and 'zmi-sort_key' or No", 65, 37), 3906: ('obs', 74, 34), 3944: ('nocall:ob_dict/obj', 75, 32), 4178: ('ob_dict/id', 77, 104), 4519: (' ob/meta_type | defaul', 81, 122), 4491: ('ob/zmi_icon | default', 81, 94), 4598: ('ob/meta_type | default', 82, 53), 4765: ("python:'%s/manage_workspace'%(ob_dict['quoted_id'])", 86, 40), 4856: ('ob_dict/id', 87, 37), 4989: ('ob/wl_isLocked | nothing', 88, 111), 5163: ('ob/title|nothing', 91, 74), 5228: ('ob/title', 92, 46), 5390: ('python:here.compute_size(ob)', 96, 76), 5522: ('python:here.last_modified(ob)', 98, 81), 5737: ("python:sm.checkPermission('Delete objects', context)", 106, 23), 5806: ('obs', 106, 92), 5883: ('not:context/dontAllowCopyAndPaste|nothing', 108, 37), 6160: ('delete_allowed', 110, 121), 6415: ('here/cb_dataValid', 112, 125), 6587: ('delete_allowed', 114, 122), 6741: ("python:sm.checkPermission('Import/Export objects', context)", 115, 135), 6856: ("python: has_order_support and sm.checkPermission('Manage properties', context)", 117, 50), 7050: ('python:range(1,min(5,len(obs)))', 119, 38), 7096: ('val', 119, 84), 7142: ('python:range(5,len(obs),5)', 120, 38), 7183: ('val', 120, 79), 8444: ('not:obs', 146, 26), 8558: ('here/title_or_id', 148, 57), 8662: ('not:context/dontAllowCopyAndPaste|nothing', 151, 35), 8824: ('here/cb_dataValid', 152, 118), 9000: ("python:sm.checkPermission('Import/Export objects', context)", 154, 128), 12921: ('here/manage_page_footer', 281, 31)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140141461659072 = {'class': 'zmi-typename_show', }
_static_140141462783648 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_importExportForm:method', 'value': 'Import/Export', }
_static_140141462764416 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'manage_pasteObjects:method', 'value': 'Paste', }
_static_140141461454704 = {'class': 'form-group', }
_static_140141461904976 = {'class': 'alert alert-info mt-4 mb-4', }
_static_140141461903968 = {'class': 'fas fa-arrow-down', 'style': 'border-bottom: 0.2rem solid silver;', }
_static_140141462742208 = {'type': 'submit', 'name': 'manage_move_objects_to_bottom:method', 'value': 'Move to bottom', 'title': 'Move selected items to bottom', 'class': 'btn btn-primary', }
_static_140141462051952 = {'class': 'fas fa-arrow-up', 'style': 'border-top: 0.2rem solid silver;', }
_static_140141462752608 = {'type': 'submit', 'name': 'manage_move_objects_to_top:method', 'value': 'Move to top', 'title': 'Move selected items to top', 'class': 'btn btn-primary ml-2 mr-2', }
_static_140141462749584 = {'class': 'fas fa-arrow-down', }
_static_140141462032736 = {'type': 'submit', 'name': 'manage_move_objects_down:method', 'value': 'Move down', 'title': 'Move selected items down', 'class': 'btn btn-primary rounded-right', }
_static_140141475652272 = {'class': 'fas fa-arrow-up', }
_static_140141452456288 = {'type': 'submit', 'name': 'manage_move_objects_up:method', 'value': 'Move up', 'title': 'Move selected items up', 'class': 'btn btn-primary', }
_static_140141452458640 = {'class': 'input-group-append', }
_static_140141478770000 = {'class': 'form-control btn btn-primary', 'name': 'delta:int', }
_static_140141518189952 = {'class': 'input-group', }
_static_140141463004160 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_importExportForm:method', 'value': 'Import/Export', }
_static_140141471928816 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_delObjects:method', 'value': 'Delete', }
_static_140141462024832 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_pasteObjects:method', 'value': 'Paste', }
_static_140141462026656 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_copyObjects:method', 'value': 'Copy', }
_static_140141452371328 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_cutObjects:method', 'value': 'Cut', }
_static_140141452373776 = {'class': 'btn btn-primary mr-2', 'type': 'submit', 'name': 'manage_renameForm:method', 'value': 'Rename', }
_static_140141471597712 = {'class': 'input-group', }
_static_140141461245712 = {'class': 'form-group form-inline zmi-controls', }
_static_140141462359152 = {'class': 'text-right zmi-object-date hidden-xs pl-3', }
_static_140141461616960 = {'class': 'text-right zmi-object-size hidden-xs', }
_static_140141461884160 = {'class': 'zmi-object-title hidden-xs', }
_static_140141461510560 = {'class': 'fa fa-lock', }
_static_140141461615856 = {'class': 'badge badge-warning', 'title': 'This item has been locked by WebDAV', }
_static_140141471585088 = {'href': "python:'%s/manage_workspace'%(ob_dict['quoted_id'])", }
_static_140141472031216 = {'class': 'zmi-object-id', }
_static_140141472031792 = {'class': 'sr-only', }
_static_140141461325664 = {'title': 'Broken object', 'class': 'fas fa-ban text-danger', }
_static_140141461327632 = {'class': 'zmi-object-type', 'onclick': "$(this).prev().children('input').trigger('click')", }
_static_140141471999696 = {'type': 'checkbox', 'class': 'checkbox-list-item', 'name': 'ids:list', 'onclick': 'event.stopPropagation();select_objectitem($(this));', 'value': 'ob_dict/id', }
_static_140141461245280 = {'class': 'zmi-object-check text-right', 'onclick': "$(this).children('input').trigger('click');", }
_static_140141461299552 = {'class': 'fa fa-sort', }
_static_140141472841888 = {'title': 'Sort Ascending by Modification Date', 'href': '?skey=_p_mtime&rkey=asc', 'class': "python:skey=='_p_mtime' and 'zmi-sort_key' or None", }
_static_140141472810560 = {'scope': 'col', 'class': 'zmi-object-date text-right hidden-xs', }
_static_140141472786320 = {'class': 'fa fa-sort', }
_static_140141472417392 = {'title': 'Sort Ascending by File-Size', 'href': '?skey=get_size&rkey=asc', 'class': "python:skey=='get_size' and 'zmi-sort_key' or None", }
_static_140141461598560 = {'scope': 'col', 'class': 'zmi-object-size text-right hidden-xs', }
_static_140141461599664 = {'id': 'tablefilter', 'name': 'obj_ids:tokens', 'type': 'text', 'title': 'Filter object list by entering a name. Pressing the Enter key starts recursive search.', }
_static_140141461897520 = {'class': 'fa fa-search tablefilter', 'onclick': "$('#tablefilter').focus()", }
_static_140141461897808 = {'class': 'fa fa-sort', }
_static_140141461462320 = {'title': 'Sort Ascending by Name', 'href': '?skey=id&rkey=asc', 'class': "python:skey=='id' and 'zmi-sort_key' or None", }
_static_140141461461792 = {'scope': 'col', 'class': 'zmi-object-id', }
_static_140141461462608 = {'class': 'fa fa-sort', }
_static_140141461480736 = {'title': 'Sort Ascending by Meta-Type', 'href': '?skey=meta_type&rkey=asc', 'class': "python:skey=='meta_type' and 'zmi-sort_key' or None", }
_static_140141461480016 = {'scope': 'col', 'class': 'zmi-object-type', }
_static_140141462134256 = {'type': 'checkbox', 'id': 'checkAll', 'onclick': 'checkbox_all();', }
_static_140141462130752 = {'scope': 'col', 'class': 'zmi-object-check text-right', }
_static_140141462250112 = {'class': 'thead-light', }
_static_140141462250544 = {'class': 'table table-striped table-hover table-sm objectItems', }
_static_140141461511232 = {'id': 'objectItems', 'name': 'objectItems', 'method': 'post', 'action': 'string:${request/URL1}/', }
_static_140141462666688 = {'class': 'container-fluid', }
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

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462667216
            __attrs_140141462667216 = _static_140141533420656

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141487099616
            __default_140141487099616 = _DEFAULT_MARKER

            # <Value 'here/manage_page_header' (1:31)> -> __cache_140141462561216
            __token = 31
            try:
                __zt_tmp = __attrs_140141462667216
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462561216 = _static_140141533071728('path', 'here/manage_page_header', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_header' (1:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a182dc0> -> __condition
            __expression = __cache_140141462561216

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140141462561216
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462664624
            __attrs_140141462664624 = _static_140141533420656

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462665536
            __default_140141462665536 = _DEFAULT_MARKER

            # <Value 'here/manage_tabs' (3:29)> -> __cache_140141462665056
            __token = 89
            try:
                __zt_tmp = __attrs_140141462664624
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462665056 = _static_140141533071728('path', 'here/manage_tabs', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_tabs' (3:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a19b820> -> __condition
            __expression = __cache_140141462665056

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140141462665056
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f753a19bdc0> name=None at 7f753a19b730> -> __attrs_140141461508496
            __attrs_140141461508496 = _static_140141462666688

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n  ')

            # <Static value=<ast.Dict object at 0x7f753a081c40> name=None at 7f753a081d60> -> __attrs_140141462701152
            __attrs_140141462701152 = _static_140141461511232
            __backup_has_order_support_140141461947344 = get('has_order_support', __marker)

            # <Value "python:getattr(here.aq_explicit, 'has_order_support', 0)" (7:38)> -> __value
            __token = 238
            try:
                __zt_tmp = __attrs_140141462701152
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('python', "getattr(here.aq_explicit, 'has_order_support', 0)", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['has_order_support'] = __value
            __backup_sm_140141462563712 = get('sm', __marker)

            # <Value 'modules/AccessControl/getSecurityManager' (8:22)> -> __value
            __token = 318
            try:
                __zt_tmp = __attrs_140141462701152
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('path', 'modules/AccessControl/getSecurityManager', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['sm'] = __value
            __backup_default_sort_140141461511040 = get('default_sort', __marker)

            # <Value "python: 'position' if has_order_support else 'id'" (9:31)> -> __value
            __token = 392
            try:
                __zt_tmp = __attrs_140141462701152
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('python', " 'position' if has_order_support else 'id'", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['default_sort'] = __value
            __backup_skey_140141462700672 = get('skey', __marker)

            # <Value "python:request.get('skey',default_sort)" (10:22)> -> __value
            __token = 467
            try:
                __zt_tmp = __attrs_140141462701152
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('python', "request.get('skey',default_sort)", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['skey'] = __value
            __backup_rkey_140141462703984 = get('rkey', __marker)

            # <Value "python:request.get('rkey','asc')" (11:21)> -> __value
            __token = 532
            try:
                __zt_tmp = __attrs_140141462701152
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('python', "request.get('rkey','asc')", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['rkey'] = __value
            __backup_rkey_alt_140141462703216 = get('rkey_alt', __marker)

            # <Value "python:'desc' if rkey=='asc' else 'asc'" (12:24)> -> __value
            __token = 594
            try:
                __zt_tmp = __attrs_140141462701152
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('python', "'desc' if rkey=='asc' else 'asc'", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['rkey_alt'] = __value
            __backup_rkey_alt_up_140141462701488 = get('rkey_alt_up', __marker)

            # <Value 'rkey_alt/upper' (13:26)> -> __value
            __token = 666
            try:
                __zt_tmp = __attrs_140141462701152
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('path', 'rkey_alt/upper', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['rkey_alt_up'] = __value
            __backup_obs_140141462703312 = get('obs', __marker)

            # <Value 'python: here.manage_get_sortedObjects(sortkey = skey, revkey = rkey)' (14:17)> -> __value
            __token = 705
            try:
                __zt_tmp = __attrs_140141462701152
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('python', ' here.manage_get_sortedObjects(sortkey = skey, revkey = rkey)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['obs'] = __value
            __backup_my_url_140141462703648 = get('my_url', __marker)

            # <Value 'string:${context/absolute_url}/manage_main' (15:19)> -> __value
            __token = 801
            try:
                __zt_tmp = __attrs_140141462701152
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('string', '${context/absolute_url}/manage_main', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['my_url'] = __value

            # <form ... (0:0)
            # --------------------------------------------------------
            __append('<form id="objectItems" name="objectItems" method="post"')

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462701008
            __default_140141462701008 = _DEFAULT_MARKER

            # <Substitution 'string:${request/URL1}/' (17:31)> -> __attr_action
            __token = 905
            try:
                __zt_tmp = __attrs_140141462701152
            except get('NameError', NameError):
                __zt_tmp = None

            __attr_action = _static_140141533071728('string', '${request/URL1}/', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            __attr_action = __quote(__attr_action, '"', '&quot;', None, _DEFAULT_MARKER)
            if (__attr_action is not None):
                __append((' action="%s"' % __attr_action))
            __append('>\n\n    ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462688864
            __attrs_140141462688864 = _static_140141533420656

            # <Value 'obs' (19:30)> -> __condition
            __token = 962
            try:
                __zt_tmp = __attrs_140141462688864
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140141533071728('path', 'obs', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f753a136430> name=None at 7f753a1366a0> -> __attrs_140141462252320
                __attrs_140141462252320 = _static_140141462250544

                # <Value 'obs' (20:89)> -> __condition
                __token = 1057
                try:
                    __zt_tmp = __attrs_140141462252320
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('path', 'obs', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <table ... (0:0)
                    # --------------------------------------------------------
                    __append('<table class="table table-striped table-hover table-sm objectItems">\n        ')

                    # <Static value=<ast.Dict object at 0x7f753a136280> name=None at 7f753a136c70> -> __attrs_140141462251504
                    __attrs_140141462251504 = _static_140141462250112

                    # <thead ... (0:0)
                    # --------------------------------------------------------
                    __append('<thead')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462253184
                    __default_140141462253184 = _DEFAULT_MARKER

                    # <Substitution "python:'thead-light sorted_%s'%(request.get('rkey',''))" (21:57)> -> __attr_class
                    __token = 1120
                    try:
                        __zt_tmp = __attrs_140141462251504
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140141533071728('python', "'thead-light sorted_%s'%(request.get('rkey',''))", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', 'thead-light', _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n          ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462253088
                    __attrs_140141462253088 = _static_140141533420656

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n            ')

                    # <Static value=<ast.Dict object at 0x7f753a119040> name=None at 7f753a119ca0> -> __attrs_140141462132624
                    __attrs_140141462132624 = _static_140141462130752

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-check text-right">\n              ')

                    # <Static value=<ast.Dict object at 0x7f753a119df0> name=None at 7f753a119430> -> __attrs_140141462132144
                    __attrs_140141462132144 = _static_140141462134256

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" id="checkAll" onclick="checkbox_all();" />\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x7f753a07a250> name=None at 7f753a07abb0> -> __attrs_140141461480592
                    __attrs_140141461480592 = _static_140141461480016

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-type">\n              ')

                    # <Static value=<ast.Dict object at 0x7f753a07a520> name=None at 7f753a07a4c0> -> __attrs_140141461482080
                    __attrs_140141461482080 = _static_140141461480736

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461479824
                    __default_140141461479824 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by meta-type' (29:39)> -> __attr_title
                    __token = 1550
                    try:
                        __zt_tmp = __attrs_140141461482080
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140141533071728('string', 'Sort ${rkey_alt_up} by meta-type', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Meta-Type', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461483424
                    __default_140141461483424 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=meta_type&rkey=${rkey_alt}' (30:37)> -> __attr_href
                    __token = 1628
                    try:
                        __zt_tmp = __attrs_140141461482080
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140141533071728('string', '${my_url}?skey=meta_type&rkey=${rkey_alt}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=meta_type&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461483184
                    __default_140141461483184 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='meta_type' and 'zmi-sort_key' or None" (31:37)> -> __attr_class
                    __token = 1716
                    try:
                        __zt_tmp = __attrs_140141461482080
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140141533071728('python', "skey=='meta_type' and 'zmi-sort_key' or None", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                ')

                    # <Static value=<ast.Dict object at 0x7f753a075e50> name=None at 7f753a0758b0> -> __attrs_140141461460496
                    __attrs_140141461460496 = _static_140141461462608

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x7f753a075b20> name=None at 7f753a075fd0> -> __attrs_140141461462368
                    __attrs_140141461462368 = _static_140141461461792

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-id">\n              ')

                    # <Static value=<ast.Dict object at 0x7f753a075d30> name=None at 7f753a0754c0> -> __attrs_140141461898432
                    __attrs_140141461898432 = _static_140141461462320

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461461648
                    __default_140141461461648 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by name' (39:39)> -> __attr_title
                    __token = 2066
                    try:
                        __zt_tmp = __attrs_140141461898432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140141533071728('string', 'Sort ${rkey_alt_up} by name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Name', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461900496
                    __default_140141461900496 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=id&rkey=${rkey_alt}' (40:37)> -> __attr_href
                    __token = 2139
                    try:
                        __zt_tmp = __attrs_140141461898432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140141533071728('string', '${my_url}?skey=id&rkey=${rkey_alt}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=id&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461897424
                    __default_140141461897424 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='id' and 'zmi-sort_key' or None" (41:37)> -> __attr_class
                    __token = 2220
                    try:
                        __zt_tmp = __attrs_140141461898432
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140141533071728('python', "skey=='id' and 'zmi-sort_key' or None", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                Name\n                ')

                    # <Static value=<ast.Dict object at 0x7f753a0e0250> name=None at 7f753a0e0340> -> __attrs_140141461898912
                    __attrs_140141461898912 = _static_140141461897808

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n              ')

                    # <Static value=<ast.Dict object at 0x7f753a0e0130> name=None at 7f753a0e0a30> -> __attrs_140141461601632
                    __attrs_140141461601632 = _static_140141461897520

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-search tablefilter" onclick="$(\'#tablefilter\').focus()"></i>\n              ')

                    # <Static value=<ast.Dict object at 0x7f753a0975b0> name=None at 7f753a097700> -> __attrs_140141461598272
                    __attrs_140141461598272 = _static_140141461599664

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input id="tablefilter" name="obj_ids:tokens" type="text" title="Filter object list by entering a name. Pressing the Enter key starts recursive search." />\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x7f753a097160> name=None at 7f753a097280> -> __attrs_140141461598320
                    __attrs_140141461598320 = _static_140141461598560

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-size text-right hidden-xs">\n              ')

                    # <Static value=<ast.Dict object at 0x7f753aae8670> name=None at 7f753aae83d0> -> __attrs_140141473489872
                    __attrs_140141473489872 = _static_140141472417392

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141472318320
                    __default_140141472318320 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by size' (52:39)> -> __attr_title
                    __token = 2879
                    try:
                        __zt_tmp = __attrs_140141473489872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140141533071728('string', 'Sort ${rkey_alt_up} by size', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by File-Size', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141473035984
                    __default_140141473035984 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=get_size&rkey=${rkey_alt}' (53:37)> -> __attr_href
                    __token = 2952
                    try:
                        __zt_tmp = __attrs_140141473489872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140141533071728('string', '${my_url}?skey=get_size&rkey=${rkey_alt}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=get_size&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141472663584
                    __default_140141472663584 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='get_size' and 'zmi-sort_key' or None" (54:37)> -> __attr_class
                    __token = 3039
                    try:
                        __zt_tmp = __attrs_140141473489872
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140141533071728('python', "skey=='get_size' and 'zmi-sort_key' or None", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                Size\n                ')

                    # <Static value=<ast.Dict object at 0x7f753ab42790> name=None at 7f753ab42eb0> -> __attrs_140141472810608
                    __attrs_140141472810608 = _static_140141472786320

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n            </th>\n            ')

                    # <Static value=<ast.Dict object at 0x7f753ab48640> name=None at 7f753aaaf970> -> __attrs_140141472200832
                    __attrs_140141472200832 = _static_140141472810560

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th scope="col" class="zmi-object-date text-right hidden-xs">\n              ')

                    # <Static value=<ast.Dict object at 0x7f753ab500a0> name=None at 7f753ab500d0> -> __attrs_140141461300128
                    __attrs_140141461300128 = _static_140141472841888

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141471915744
                    __default_140141471915744 = _DEFAULT_MARKER

                    # <Substitution 'string:Sort ${rkey_alt_up} by modification date' (63:39)> -> __attr_title
                    __token = 3451
                    try:
                        __zt_tmp = __attrs_140141461300128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140141533071728('string', 'Sort ${rkey_alt_up} by modification date', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', 'Sort Ascending by Modification Date', _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141471549808
                    __default_140141471549808 = _DEFAULT_MARKER

                    # <Substitution 'string:${my_url}?skey=_p_mtime&rkey=${rkey_alt}' (64:37)> -> __attr_href
                    __token = 3537
                    try:
                        __zt_tmp = __attrs_140141461300128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140141533071728('string', '${my_url}?skey=_p_mtime&rkey=${rkey_alt}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?skey=_p_mtime&rkey=asc', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141471551440
                    __default_140141471551440 = _DEFAULT_MARKER

                    # <Substitution "python:skey=='_p_mtime' and 'zmi-sort_key' or None" (65:37)> -> __attr_class
                    __token = 3624
                    try:
                        __zt_tmp = __attrs_140141461300128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140141533071728('python', "skey=='_p_mtime' and 'zmi-sort_key' or None", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n                Last Modified\n                ')

                    # <Static value=<ast.Dict object at 0x7f753a04e160> name=None at 7f753a04e700> -> __attrs_140141461301088
                    __attrs_140141461301088 = _static_140141461299552

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="fa fa-sort"></i>\n              </a>\n            </th>\n          </tr>\n        </thead>\n        ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461300032
                    __attrs_140141461300032 = _static_140141533420656

                    # <tbody ... (0:0)
                    # --------------------------------------------------------
                    __append('<tbody>\n          ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461301184
                    __attrs_140141461301184 = _static_140141533420656
                    __backup_ob_dict_140141462251072 = get('ob_dict', __marker)

                    # <Value 'obs' (74:34)> -> __iterator
                    __token = 3906
                    try:
                        __zt_tmp = __attrs_140141461301184
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140141533071728('path', 'obs', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    (__iterator, ____index_140141461302384, ) = getname('repeat')('ob_dict', __iterator)
                    econtext['ob_dict'] = None
                    for __item in __iterator:
                        econtext['ob_dict'] = __item

                        # <tr ... (0:0)
                        # --------------------------------------------------------
                        __append('<tr>\n            ')

                        # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461243840
                        __attrs_140141461243840 = _static_140141533420656
                        __backup_ob_140141462251120 = get('ob', __marker)

                        # <Value 'nocall:ob_dict/obj' (75:32)> -> __value
                        __token = 3944
                        try:
                            __zt_tmp = __attrs_140141461243840
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140141533071728('nocall', 'ob_dict/obj', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        econtext['ob'] = __value
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x7f753a040d60> name=None at 7f753a040550> -> __attrs_140141471999840
                        __attrs_140141471999840 = _static_140141461245280

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="zmi-object-check text-right" onclick="$(this).children(\'input\').trigger(\'click\');">\n                ')

                        # <Static value=<ast.Dict object at 0x7f753aa826d0> name=None at 7f753aa822b0> -> __attrs_140141472001184
                        __attrs_140141472001184 = _static_140141471999696

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input type="checkbox" class="checkbox-list-item" name="ids:list"                   onclick="event.stopPropagation();select_objectitem($(this));"')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141472001376
                        __default_140141472001376 = _DEFAULT_MARKER

                        # <Substitution 'ob_dict/id' (77:104)> -> __attr_value
                        __token = 4178
                        try:
                            __zt_tmp = __attrs_140141472001184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_value = _static_140141533071728('path', 'ob_dict/id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_value is not None):
                            __append((' value="%s"' % __attr_value))
                        __append(' />\n              </td>\n              ')

                        # <Static value=<ast.Dict object at 0x7f753a054f10> name=None at 7f753a054cd0> -> __attrs_140141461327248
                        __attrs_140141461327248 = _static_140141461327632

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="zmi-object-type" onclick="$(this).prev().children(\'input\').trigger(\'click\')">\n                ')

                        # <Static value=<ast.Dict object at 0x7f753a054760> name=None at 7f753a054d00> -> __attrs_140141472033472
                        __attrs_140141472033472 = _static_140141461325664

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461326144
                        __default_140141461326144 = _DEFAULT_MARKER

                        # <Substitution 'ob/meta_type | default' (81:122)> -> __attr_title
                        __token = 4519
                        try:
                            __zt_tmp = __attrs_140141472033472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_title = _static_140141533071728('path', 'ob/meta_type | default', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        __attr_title = __quote(__attr_title, '"', '&quot;', 'Broken object', _DEFAULT_MARKER)
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461326912
                        __default_140141461326912 = _DEFAULT_MARKER

                        # <Substitution 'ob/zmi_icon | default' (81:94)> -> __attr_class
                        __token = 4491
                        try:
                            __zt_tmp = __attrs_140141472033472
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_class = _static_140141533071728('path', 'ob/zmi_icon | default', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        __attr_class = __quote(__attr_class, '"', '&quot;', 'fas fa-ban text-danger', _DEFAULT_MARKER)
                        if (__attr_class is not None):
                            __append((' class="%s"' % __attr_class))
                        __append('>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f753aa8a430> name=None at 7f753aa8aa90> -> __attrs_140141472034528
                        __attrs_140141472034528 = _static_140141472031792

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="sr-only">')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141472034336
                        __default_140141472034336 = _DEFAULT_MARKER

                        # <Value 'ob/meta_type | default' (82:53)> -> __cache_140141472030832
                        __token = 4598
                        try:
                            __zt_tmp = __attrs_140141472034528
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140141472030832 = _static_140141533071728('path', 'ob/meta_type | default', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                        # <BinOp left=<Value 'ob/meta_type | default' (82:53)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753aa8a5b0> -> __condition
                        __expression = __cache_140141472030832

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Broken object')
                        else:
                            __content = __cache_140141472030832
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</span>\n                </i>\n              </td>\n              ')

                        # <Static value=<ast.Dict object at 0x7f753aa8a1f0> name=None at 7f753aa8a3d0> -> __attrs_140141471757792
                        __attrs_140141471757792 = _static_140141472031216

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="zmi-object-id">\n                ')

                        # <Static value=<ast.Dict object at 0x7f753aa1d340> name=None at 7f753aa1dfd0> -> __attrs_140141461616816
                        __attrs_140141461616816 = _static_140141471585088

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141471586384
                        __default_140141471586384 = _DEFAULT_MARKER

                        # <Substitution "python:'%s/manage_workspace'%(ob_dict['quoted_id'])" (86:40)> -> __attr_href
                        __token = 4765
                        try:
                            __zt_tmp = __attrs_140141461616816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140141533071728('python', "'%s/manage_workspace'%(ob_dict['quoted_id'])", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append('>\n                  ')

                        # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461616096
                        __attrs_140141461616096 = _static_140141533420656

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461618304
                        __default_140141461618304 = _DEFAULT_MARKER

                        # <Value 'ob_dict/id' (87:37)> -> __cache_140141461618208
                        __token = 4856
                        try:
                            __zt_tmp = __attrs_140141461616096
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140141461618208 = _static_140141533071728('path', 'ob_dict/id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                        # <BinOp left=<Value 'ob_dict/id' (87:37)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a09b400> -> __condition
                        __expression = __cache_140141461618208

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span>Id</span>')
                        else:
                            __content = __cache_140141461618208
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f753a09b4f0> name=None at 7f753a1a1e80> -> __attrs_140141462702400
                        __attrs_140141462702400 = _static_140141461615856

                        # <Value 'ob/wl_isLocked | nothing' (88:111)> -> __condition
                        __token = 4989
                        try:
                            __zt_tmp = __attrs_140141462702400
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140141533071728('path', 'ob/wl_isLocked | nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="badge badge-warning" title="This item has been locked by WebDAV">\n                    ')

                            # <Static value=<ast.Dict object at 0x7f753a0819a0> name=None at 7f753a081c10> -> __attrs_140141461509744
                            __attrs_140141461509744 = _static_140141461510560

                            # <i ... (0:0)
                            # --------------------------------------------------------
                            __append('<i class="fa fa-lock"></i>\n                  </span>')
                        __append('\n                  ')

                        # <Static value=<ast.Dict object at 0x7f753a0dcd00> name=None at 7f753a0dc5b0> -> __attrs_140141461884784
                        __attrs_140141461884784 = _static_140141461884160

                        # <Value 'ob/title|nothing' (91:74)> -> __condition
                        __token = 5163
                        try:
                            __zt_tmp = __attrs_140141461884784
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140141533071728('path', 'ob/title|nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append('<span class="zmi-object-title hidden-xs">\n                    &nbsp;(')

                            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461616672
                            __attrs_140141461616672 = _static_140141533420656

                            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461615184
                            __default_140141461615184 = _DEFAULT_MARKER

                            # <Value 'ob/title' (92:46)> -> __cache_140141461946528
                            __token = 5228
                            try:
                                __zt_tmp = __attrs_140141461616672
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140141461946528 = _static_140141533071728('path', 'ob/title', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                            # <BinOp left=<Value 'ob/title' (92:46)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0ecf70> -> __condition
                            __expression = __cache_140141461946528

                            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:

                                # <span ... (0:0)
                                # --------------------------------------------------------
                                __append('<span></span>')
                            else:
                                __content = __cache_140141461946528
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append(')\n                  </span>')
                        __append('\n                </a>\n              </td>\n              ')

                        # <Static value=<ast.Dict object at 0x7f753a09b940> name=None at 7f753a09b7c0> -> __attrs_140141462357184
                        __attrs_140141462357184 = _static_140141461616960

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="text-right zmi-object-size hidden-xs">')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461616768
                        __default_140141461616768 = _DEFAULT_MARKER

                        # <Value 'python:here.compute_size(ob)' (96:76)> -> __cache_140141461884112
                        __token = 5390
                        try:
                            __zt_tmp = __attrs_140141462357184
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140141461884112 = _static_140141533071728('python', 'here.compute_size(ob)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                        # <BinOp left=<Value 'python:here.compute_size(ob)' (96:76)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a09b070> -> __condition
                        __expression = __cache_140141461884112

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              ')
                        else:
                            __content = __cache_140141461884112
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</td>\n              ')

                        # <Static value=<ast.Dict object at 0x7f753a150c70> name=None at 7f753a150700> -> __attrs_140141462358576
                        __attrs_140141462358576 = _static_140141462359152

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="text-right zmi-object-date hidden-xs pl-3">')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462356704
                        __default_140141462356704 = _DEFAULT_MARKER

                        # <Value 'python:here.last_modified(ob)' (98:81)> -> __cache_140141462357424
                        __token = 5522
                        try:
                            __zt_tmp = __attrs_140141462358576
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140141462357424 = _static_140141533071728('python', 'here.last_modified(ob)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                        # <BinOp left=<Value 'python:here.last_modified(ob)' (98:81)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1501f0> -> __condition
                        __expression = __cache_140141462357424

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('\n              ')
                        else:
                            __content = __cache_140141462357424
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</td>\n            ')
                        if (__backup_ob_140141462251120 is __marker):
                            del econtext['ob']
                        else:
                            econtext['ob'] = __backup_ob_140141462251120
                        __append('\n          </tr>')
                        ____index_140141461302384 -= 1
                        if (____index_140141461302384 > 0):
                            __append('\n          ')
                    if (__backup_ob_dict_140141462251072 is __marker):
                        del econtext['ob_dict']
                    else:
                        econtext['ob_dict'] = __backup_ob_dict_140141462251072
                    __append('\n        </tbody>\n      </table>')
                __append('\n\n      ')

                # <Static value=<ast.Dict object at 0x7f753a040f10> name=None at 7f753a040520> -> __attrs_140141471600112
                __attrs_140141471600112 = _static_140141461245712
                __backup_delete_allowed_140141462688480 = get('delete_allowed', __marker)

                # <Value "python:sm.checkPermission('Delete objects', context)" (106:23)> -> __value
                __token = 5737
                try:
                    __zt_tmp = __attrs_140141471600112
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', "sm.checkPermission('Delete objects', context)", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['delete_allowed'] = __value

                # <Value 'obs' (106:92)> -> __condition
                __token = 5806
                try:
                    __zt_tmp = __attrs_140141471600112
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('path', 'obs', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="form-group form-inline zmi-controls">\n        ')

                    # <Static value=<ast.Dict object at 0x7f753aa20490> name=None at 7f753aa20100> -> __attrs_140141471597424
                    __attrs_140141471597424 = _static_140141471597712

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="input-group">\n          ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462834336
                    __attrs_140141462834336 = _static_140141533420656

                    # <Value 'not:context/dontAllowCopyAndPaste|nothing' (108:37)> -> __condition
                    __token = 5883
                    try:
                        __zt_tmp = __attrs_140141462834336
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('not', 'context/dontAllowCopyAndPaste|nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f75397caf10> name=None at 7f75397ca760> -> __attrs_140141452372576
                        __attrs_140141452372576 = _static_140141452373776

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_renameForm:method" value="Rename" />\n            ')

                        # <Static value=<ast.Dict object at 0x7f75397ca580> name=None at 7f75397ca7f0> -> __attrs_140141462024304
                        __attrs_140141462024304 = _static_140141452371328

                        # <Value 'delete_allowed' (110:121)> -> __condition
                        __token = 6160
                        try:
                            __zt_tmp = __attrs_140141462024304
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140141533071728('path', 'delete_allowed', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input class="btn btn-primary mr-2" type="submit" name="manage_cutObjects:method" value="Cut" />')
                        __append('\n            ')

                        # <Static value=<ast.Dict object at 0x7f753a0ff9a0> name=None at 7f753a0ffc70> -> __attrs_140141462026992
                        __attrs_140141462026992 = _static_140141462026656

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_copyObjects:method" value="Copy" />\n            ')

                        # <Static value=<ast.Dict object at 0x7f753a0ff280> name=None at 7f753a0ffb80> -> __attrs_140141462853568
                        __attrs_140141462853568 = _static_140141462024832

                        # <Value 'here/cb_dataValid' (112:125)> -> __condition
                        __token = 6415
                        try:
                            __zt_tmp = __attrs_140141462853568
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140141533071728('path', 'here/cb_dataValid', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input class="btn btn-primary mr-2" type="submit" name="manage_pasteObjects:method" value="Paste" />')
                        __append('\n          ')
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f753aa711f0> name=None at 7f753aa71f40> -> __attrs_140141462852416
                    __attrs_140141462852416 = _static_140141471928816

                    # <Value 'delete_allowed' (114:122)> -> __condition
                    __token = 6587
                    try:
                        __zt_tmp = __attrs_140141462852416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('path', 'delete_allowed', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_delObjects:method" value="Delete" />')
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a1ee400> name=None at 7f753a1ee940> -> __attrs_140141518191536
                    __attrs_140141518191536 = _static_140141463004160

                    # <Value "python:sm.checkPermission('Import/Export objects', context)" (115:135)> -> __condition
                    __token = 6741
                    try:
                        __zt_tmp = __attrs_140141518191536
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('python', "sm.checkPermission('Import/Export objects', context)", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary mr-2" type="submit" name="manage_importExportForm:method" value="Import/Export" />')
                    __append('\n\n          ')

                    # <Static value=<ast.Dict object at 0x7f753d68f580> name=None at 7f753d68f790> -> __attrs_140141478594832
                    __attrs_140141478594832 = _static_140141518189952

                    # <Value "python: has_order_support and sm.checkPermission('Manage properties', context)" (117:50)> -> __condition
                    __token = 6856
                    try:
                        __zt_tmp = __attrs_140141478594832
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('python', " has_order_support and sm.checkPermission('Manage properties', context)", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="input-group">\n            ')

                        # <Static value=<ast.Dict object at 0x7f753b0f7550> name=None at 7f753b0f7ee0> -> __attrs_140141486038608
                        __attrs_140141486038608 = _static_140141478770000

                        # <select ... (0:0)
                        # --------------------------------------------------------
                        __append('<select class="form-control btn btn-primary" name="delta:int">\n              ')

                        # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141452459264
                        __attrs_140141452459264 = _static_140141533420656
                        __backup_val_140141461651616 = get('val', __marker)

                        # <Value 'python:range(1,min(5,len(obs)))' (119:38)> -> __iterator
                        __token = 7050
                        try:
                            __zt_tmp = __attrs_140141452459264
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140141533071728('python', 'range(1,min(5,len(obs)))', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        (__iterator, ____index_140141452459648, ) = getname('repeat')('val', __iterator)
                        econtext['val'] = None
                        for __item in __iterator:
                            econtext['val'] = __item

                            # <option ... (0:0)
                            # --------------------------------------------------------
                            __append('<option>')

                            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141478844688
                            __default_140141478844688 = _DEFAULT_MARKER

                            # <Value 'val' (119:84)> -> __cache_140141478845984
                            __token = 7096
                            try:
                                __zt_tmp = __attrs_140141452459264
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140141478845984 = _static_140141533071728('path', 'val', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                            # <BinOp left=<Value 'val' (119:84)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753b1096d0> -> __condition
                            __expression = __cache_140141478845984

                            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140141478845984
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</option>')
                            ____index_140141452459648 -= 1
                            if (____index_140141452459648 > 0):
                                __append('\n              ')
                        if (__backup_val_140141461651616 is __marker):
                            del econtext['val']
                        else:
                            econtext['val'] = __backup_val_140141461651616
                        __append('\n              ')

                        # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141452458208
                        __attrs_140141452458208 = _static_140141533420656
                        __backup_val_140141461302912 = get('val', __marker)

                        # <Value 'python:range(5,len(obs),5)' (120:38)> -> __iterator
                        __token = 7142
                        try:
                            __zt_tmp = __attrs_140141452458208
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __iterator = _static_140141533071728('python', 'range(5,len(obs),5)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        (__iterator, ____index_140141452456192, ) = getname('repeat')('val', __iterator)
                        econtext['val'] = None
                        for __item in __iterator:
                            econtext['val'] = __item

                            # <option ... (0:0)
                            # --------------------------------------------------------
                            __append('<option>')

                            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141452456144
                            __default_140141452456144 = _DEFAULT_MARKER

                            # <Value 'val' (120:79)> -> __cache_140141452459696
                            __token = 7183
                            try:
                                __zt_tmp = __attrs_140141452458208
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140141452459696 = _static_140141533071728('path', 'val', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                            # <BinOp left=<Value 'val' (120:79)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f75397dfd60> -> __condition
                            __expression = __cache_140141452459696

                            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140141452459696
                                __content = __quote(__content, None, '\xad', None, None)
                                if (__content is not None):
                                    __append(__content)
                            __append('</option>')
                            ____index_140141452456192 -= 1
                            if (____index_140141452456192 > 0):
                                __append('\n              ')
                        if (__backup_val_140141461302912 is __marker):
                            del econtext['val']
                        else:
                            econtext['val'] = __backup_val_140141461302912
                        __append('\n            </select>\n            ')

                        # <Static value=<ast.Dict object at 0x7f75397dfa90> name=None at 7f75397dfb50> -> __attrs_140141452457248
                        __attrs_140141452457248 = _static_140141452458640

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div class="input-group-append">\n              ')

                        # <Static value=<ast.Dict object at 0x7f75397df160> name=None at 7f75397df970> -> __attrs_140141475651936
                        __attrs_140141475651936 = _static_140141452456288

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_up:method" value="Move up"                 title="Move selected items up" class="btn btn-primary">\n                ')

                        # <Static value=<ast.Dict object at 0x7f753adfe2b0> name=None at 7f753adfea90> -> __attrs_140141462032976
                        __attrs_140141462032976 = _static_140141475652272

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-up"></i>\n              </button>\n              ')

                        # <Static value=<ast.Dict object at 0x7f753a101160> name=None at 7f753a101ca0> -> __attrs_140141462753232
                        __attrs_140141462753232 = _static_140141462032736

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_down:method" value="Move down"                 title="Move selected items down" class="btn btn-primary rounded-right">\n                ')

                        # <Static value=<ast.Dict object at 0x7f753a1b0190> name=None at 7f753a1b07c0> -> __attrs_140141462752080
                        __attrs_140141462752080 = _static_140141462749584

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-down"></i>\n              </button>\n            </div>\n            ')

                        # <Static value=<ast.Dict object at 0x7f753a1b0d60> name=None at 7f753a1b01c0> -> __attrs_140141462750976
                        __attrs_140141462750976 = _static_140141462752608

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_to_top:method" value="Move to top"               title="Move selected items to top" class="btn btn-primary ml-2 mr-2">\n              ')

                        # <Static value=<ast.Dict object at 0x7f753a105c70> name=None at 7f753a105790> -> __attrs_140141462050464
                        __attrs_140141462050464 = _static_140141462051952

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-up" style="border-top: 0.2rem solid silver;"></i>\n            </button>\n            ')

                        # <Static value=<ast.Dict object at 0x7f753a1ae4c0> name=None at 7f753a1ae3a0> -> __attrs_140141463015968
                        __attrs_140141463015968 = _static_140141462742208

                        # <button ... (0:0)
                        # --------------------------------------------------------
                        __append('<button type="submit" name="manage_move_objects_to_bottom:method" value="Move to bottom"                title="Move selected items to bottom" class="btn btn-primary">\n              ')

                        # <Static value=<ast.Dict object at 0x7f753a0e1a60> name=None at 7f753a0e1670> -> __attrs_140141461904448
                        __attrs_140141461904448 = _static_140141461903968

                        # <i ... (0:0)
                        # --------------------------------------------------------
                        __append('<i class="fas fa-arrow-down" style="border-bottom: 0.2rem solid silver;"></i>\n            </button>\n          </div>')
                    __append('\n        </div>\n\n      </div>')
                if (__backup_delete_allowed_140141462688480 is __marker):
                    del econtext['delete_allowed']
                else:
                    econtext['delete_allowed'] = __backup_delete_allowed_140141462688480
                __append('\n    ')
            __append('\n\n    ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141471599776
            __attrs_140141471599776 = _static_140141533420656

            # <Value 'not:obs' (146:26)> -> __condition
            __token = 8444
            try:
                __zt_tmp = __attrs_140141471599776
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140141533071728('not', 'obs', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            if __condition:
                __append('\n      ')

                # <Static value=<ast.Dict object at 0x7f753a0e1e50> name=None at 7f753a0e1550> -> __attrs_140141461454032
                __attrs_140141461454032 = _static_140141461904976

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="alert alert-info mt-4 mb-4">\n        There are currently no items in ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461451392
                __attrs_140141461451392 = _static_140141533420656

                # <em ... (0:0)
                # --------------------------------------------------------
                __append('<em>')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461453216
                __default_140141461453216 = _DEFAULT_MARKER

                # <Value 'here/title_or_id' (148:57)> -> __cache_140141461451920
                __token = 8558
                try:
                    __zt_tmp = __attrs_140141461451392
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140141461451920 = _static_140141533071728('path', 'here/title_or_id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                # <BinOp left=<Value 'here/title_or_id' (148:57)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a073a60> -> __condition
                __expression = __cache_140141461451920

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140141461451920
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</em>.\n      </div>\n      ')

                # <Static value=<ast.Dict object at 0x7f753a073f70> name=None at 7f753a073c70> -> __attrs_140141461452784
                __attrs_140141461452784 = _static_140141461454704

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-group">\n        ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462782400
                __attrs_140141462782400 = _static_140141533420656

                # <Value 'not:context/dontAllowCopyAndPaste|nothing' (151:35)> -> __condition
                __token = 8662
                try:
                    __zt_tmp = __attrs_140141462782400
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('not', 'context/dontAllowCopyAndPaste|nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:
                    __append('\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a1b3b80> name=None at 7f753a1b3940> -> __attrs_140141484581840
                    __attrs_140141484581840 = _static_140141462764416

                    # <Value 'here/cb_dataValid' (152:118)> -> __condition
                    __token = 8824
                    try:
                        __zt_tmp = __attrs_140141484581840
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('path', 'here/cb_dataValid', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:

                        # <input ... (0:0)
                        # --------------------------------------------------------
                        __append('<input class="btn btn-primary" type="submit" name="manage_pasteObjects:method" value="Paste" />')
                    __append('\n        ')
                __append('\n        ')

                # <Static value=<ast.Dict object at 0x7f753a1b86a0> name=None at 7f753a1b8250> -> __attrs_140141461657632
                __attrs_140141461657632 = _static_140141462783648

                # <Value "python:sm.checkPermission('Import/Export objects', context)" (154:128)> -> __condition
                __token = 9000
                try:
                    __zt_tmp = __attrs_140141461657632
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('python', "sm.checkPermission('Import/Export objects', context)", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input class="btn btn-primary" type="submit" name="manage_importExportForm:method" value="Import/Export" />')
                __append('\n      </div>\n    ')
            __append('\n  </form>')
            if (__backup_my_url_140141462703648 is __marker):
                del econtext['my_url']
            else:
                econtext['my_url'] = __backup_my_url_140141462703648
            if (__backup_obs_140141462703312 is __marker):
                del econtext['obs']
            else:
                econtext['obs'] = __backup_obs_140141462703312
            if (__backup_rkey_alt_up_140141462701488 is __marker):
                del econtext['rkey_alt_up']
            else:
                econtext['rkey_alt_up'] = __backup_rkey_alt_up_140141462701488
            if (__backup_rkey_alt_140141462703216 is __marker):
                del econtext['rkey_alt']
            else:
                econtext['rkey_alt'] = __backup_rkey_alt_140141462703216
            if (__backup_rkey_140141462703984 is __marker):
                del econtext['rkey']
            else:
                econtext['rkey'] = __backup_rkey_140141462703984
            if (__backup_skey_140141462700672 is __marker):
                del econtext['skey']
            else:
                econtext['skey'] = __backup_skey_140141462700672
            if (__backup_default_sort_140141461511040 is __marker):
                del econtext['default_sort']
            else:
                econtext['default_sort'] = __backup_default_sort_140141461511040
            if (__backup_sm_140141462563712 is __marker):
                del econtext['sm']
            else:
                econtext['sm'] = __backup_sm_140141462563712
            if (__backup_has_order_support_140141461947344 is __marker):
                del econtext['has_order_support']
            else:
                econtext['has_order_support'] = __backup_has_order_support_140141461947344
            __append('\n\n</main>\n\n\n')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461453552
            __attrs_140141461453552 = _static_140141533420656

            # <script ... (0:0)
            # --------------------------------------------------------
            __append('<script>\n  // +++++++++++++++++++++++++++\n  // Item  Selection\n  // +++++++++++++++++++++++++++\n  function checkbox_all() {\n    var checkboxes = document.getElementsByClassName(\'checkbox-list-item\');\n    // Toggle Highlighting CSS-Class\n    if (document.getElementById(\'checkAll\').checked) {\n      $(\'table.objectItems tbody tr\').addClass(\'checked\');\n    } else {\n      $(\'table.objectItems tbody tr\').removeClass(\'checked\');\n    };\n    // Set Checkbox like checkAll-Box\n    for (i = 0; i < checkboxes.length; i++) {\n      checkboxes[i].checked = document.getElementById(\'checkAll\').checked;\n    }\n  };\n\n  function zmicontrols_visible() {\n    var zmicontrols = $(\'form#objectItems .zmi-controls\');\n    var zmicontrols_top = zmicontrols.offset().top;\n    var zmicontrols_bottom = zmicontrols_top + zmicontrols.outerHeight();\n    var viewport_top = $(window).scrollTop();\n    var viewport_bottom = viewport_top + $(window).height();\n    return zmicontrols_bottom > viewport_top && zmicontrols_top < viewport_bottom;\n  };\n\n  function select_objectitem(ob) {\n    ob.parent().parent().toggleClass(\'checked\');\n    if ( !zmicontrols_visible() ) {\n      $(\'form#objectItems\').addClass(\'selected\');\n    }\n    // Anything selected?\n    var checkboxes = document.getElementsByClassName(\'checkbox-list-item\');\n    var selected = false;\n    for (i = 0; i < checkboxes.length; i++) {\n      if ( checkboxes[i].checked ) {\n        selected = true;\n        break;\n      }\n    }\n    if ( !selected ) {\n      $(\'form#objectItems\').removeClass(\'selected\');\n      console.log(\'form#objectItems removed .selected\');\n    }\n  };\n\n\n  $(function () {\n\n    // +++++++++++++++++++++++++++\n    // Icon Tooltips\n    // +++++++++++++++++++++++++++\n    $(\'td.zmi-object-type i\').tooltip({\n      \'placement\': \'top\'\n    });\n\n    // +++++++++++++++++++++++++++\n    // Tablefilter/Search Element\n    // +++++++++++++++++++++++++++\n\n    function isModifierKeyPressed(event) {\n      return event.altKey ||\n        event.ctrlKey ||\n        event.metaKey;\n    }\n\n    $(document).keypress(function (event) {\n\n      if (isModifierKeyPressed(event)) {\n        return; // ignore\n      }\n\n      // Set Focus to Tablefilter only when Modal Dialog is not Shown\n      if (!$(\'#zmi-modal\').hasClass(\'show\')) {\n        $(\'#tablefilter\').focus();\n        // Prevent Submitting a form by hitting Enter\n        // https://stackoverflow.com/questions/895171/prevent-users-from-submitting-a-form-by-hitting-enter\n        if (event.which == 13) {\n          event.preventDefault();\n          return false;\n        };\n      };\n    })\n\n    $(\'#tablefilter\').keyup(function (event) {\n\n      if (isModifierKeyPressed(event)) {\n        return; // ignore\n      }\n\n      var tablefilter = $(this).val();\n      if (event.which == 13) {\n        if (1 === $(\'tbody tr:visible\').length) {\n          window.location.href = $(\'tbody tr:visible a\').attr(\'href\');\n        } else {\n          window.location.href = \'manage_findForm?btn_submit=Find&search_sub:int=1&obj_ids%3Atokens=\' + tablefilter;\n        }\n        event.preventDefault();\n      };\n      $(\'table.objectItems\').find("tbody tr").hide();\n      $(\'table.objectItems\').find("tbody tr td.zmi-object-id a:contains(" + tablefilter + ")").closest(\'tbody tr\').show();\n    });\n\n    // +++++++++++++++++++++++++++\n    // OBJECTIST SORTING: Show skey=meta_type\n    // +++++++++++++++++++++++++++\n    let searchParams = new URLSearchParams(window.location.search);\n    if (searchParams.get(\'skey\') == \'meta_type\') {\n      $(\'td.zmi-object-type i\').each(function () {\n        $(this).parent().parent().find(\'td.zmi-object-id\').prepend(\'')

            # <Static value=<ast.Dict object at 0x7f753a0a5dc0> name=None at 7f753a0a5e20> -> __attrs_140141461656576
            __attrs_140141461656576 = _static_140141461659072

            # <span ... (0:0)
            # --------------------------------------------------------
            __append('<span class="zmi-typename_show">\' + $(this).text() + \'</span>\')\n      });\n      $(\'th.zmi-object-id\').addClass(\'zmi-typename_show\');\n    }\n\n  });\n\n</script>\n\n')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141471565904
            __attrs_140141471565904 = _static_140141533420656

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141471563840
            __default_140141471563840 = _DEFAULT_MARKER

            # <Value 'here/manage_page_footer' (281:31)> -> __cache_140141462394336
            __token = 12921
            try:
                __zt_tmp = __attrs_140141471565904
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462394336 = _static_140141533071728('path', 'here/manage_page_footer', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_footer' (281:31)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a159c40> -> __condition
            __expression = __cache_140141462394336

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140141462394336
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }