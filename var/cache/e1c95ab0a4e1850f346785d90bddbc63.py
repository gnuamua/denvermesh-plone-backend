# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/Products.CMFPlone-6.0.11-py3.9.egg/Products/CMFPlone/controlpanel/browser/usergroups_usersoverview.pt'

__tokens = {413: ('string:@@usergroup-userprefs', 12, 28), 466: (" python:request.get('showAll', '') and not view.newSearch and 'y", 13, 23), 553: ("h python:modules['Products.CMFPlone'].Bat", 14, 20), 619: ("rt python:0 if showAll or view.newSearch else request.get('b_start'", 15, 21), 710: ('ize python:showAll and len(view.searchResults) o', 16, 19), 788: ('oles view/portal_', 17, 24), 833: ('l_url context/port', 18, 21), 1017: ('context/global_statusmessage/macros/portal_message', 27, 30), 1017: ('context/global_statusmessage/macros/portal_message', 27, 30), 1346: ("python:icons.tag('people', tag_alt='Inherited from Group')", 33, 92), 1601: ('view/show_users_listing_warning', 41, 26), 2229: ("python:'form.button.FindAll' in request.keys()", 54, 34), 2315: (' view/searchResult', 55, 38), 2366: ('h python:Batch(portal_users, b_size, int(b_start), orphan=', 56, 30), 2465: ("ys python:['searchstring','_authenticato", 57, 37), 2543: ('ers view/many_u', 58, 33), 2162: ('string:$portal_url/$template_id', 53, 37), 2780: ('{\n                "actionOptions": {\n                  "redirectOnResponse": true,\n                  "redirectToUrl": "${portal_url}/@@usergroup-userprefs"\n                }\n              }', 64, 35), 2901: ('portal_url', 67, 38), 3005: ('string:${portal_url}/@@new-user', 70, 34), 3494: ('view/searchString', 79, 40), 4135: ('not:many_users', 95, 33), 4352: ('portal_users', 99, 36), 4547: ('portal_roles', 102, 61), 4579: ('portal_role', 102, 93), 4973: ('batch', 108, 41), 5024: ('repeat/user/odd', 109, 43), 5083: (' user/useri', 110, 42), 5141: ('y python:view.makeQuery(userid=useri', 111, 44), 5228: ("python:oddrow and 'odd' or 'even'", 112, 46), 5423: ('string:$portal_url/@@user-information?${userquery}', 116, 52), 5527: (' useri', 117, 52), 5569: ('${user/fullname}', 118, 32), 5571: ('user/fullname', 118, 34), 5611: ('(${user/login})', 118, 74), 5614: ('user/login', 118, 77), 5762: ('userid', 120, 95), 5908: ('portal_roles', 124, 52), 5982: ("python:user['roles'][portal_role]['inherited']", 125, 59), 6087: (" python:user['roles'][portal_role]['explicit'", 126, 57), 6190: ("d python:user['roles'][portal_role]['canAssign", 127, 55), 6512: ('not:inherited', 132, 50), 6584: ('portal_role', 133, 57), 6643: (" python:'checked' if explicit else nothin", 134, 46), 6733: ("d python:default if enabled else 'disable", 135, 46), 6998: ('python:inherited', 139, 50), 7073: ('portal_role', 140, 57), 7142: ('inherited', 141, 53), 7176: ("python:icons.tag('people', tag_alt='Inherited from Group')", 141, 87), 7642: ('userid', 152, 55), 7704: (' string:Reset password of user ${user/fullname', 153, 54), 7809: ("d python:user['can_set_password'] and default or 'disable", 154, 56), 8257: ('userid', 162, 63), 8327: (' string:Remove user ${user/fullname', 163, 62), 8429: ("d python:user['can_delete'] and default or 'disable", 164, 64), 8610: ('not:batch', 168, 37), 8663: ('view/searchString', 169, 41), 8857: ('not:view/searchString', 172, 48), 8924: ('many_users', 173, 43), 9257: ('not:many_users', 179, 43), 9716: ('context/batch_macros/macros/navigation', 190, 32), 9716: ('context/batch_macros/macros/navigation', 190, 32), 9901: ("python:modules['ZTUtils'].make_query", 194, 30), 9970: (' batchformkeys|nothin', 195, 31), 10030: ('s python:keys and dict([(key, request.form[key]) for key in keys if key in request]) or request.fo', 196, 36), 10160: ('rl batch_base_url | string:${context/absolute_url}/${template_', 197, 28), 9834: ('python:batch.next or batch.previous', 193, 30), 10266: ("python: '%s?%s' % (url, mq( linkparams, {'showAll':'y'} ))", 198, 38), 10581: ('b_start', 205, 39), 10687: ('showAll', 208, 39), 10729: ('batch', 210, 30), 11096: ('context/@@authenticator/authenticator', 222, 40), 261: ('context/prefs_main_template/macros/master', 6, 23), 261: ('context/prefs_main_template/macros/master', 6, 23)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from collections import deque as _deque
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140141461453936 = {'class': 'btn btn-primary', 'type': 'submit', 'name': 'form.button.Modify', 'value': 'Save', }
_static_140141461658400 = {'class': 'btn-group', }
_static_140141461657920 = {'type': 'hidden', 'value': '', 'name': 'showAll', }
_static_140141461599616 = {'type': 'hidden', 'value': 'b_start', 'name': 'b_start', }
_static_140141461599904 = {'href': "python: '%s?%s' % (url, mq( linkparams, {'showAll':'y'} ))", }
_static_140141461618496 = {'class': 'showAllSearchResults', }
_static_140141462357808 = 'navigation'
_static_140141461615376 = {'class': 'discreet', 'style': 'text-align:center; font-size: 100%;', }
_static_140141462357424 = {'class': 'discreet', 'style': 'text-align:center; font-size: 100%;', }
_static_140141452373728 = {'style': 'text-align:center;', }
_static_140141462025072 = {'type': 'checkbox', 'class': 'noborder notify', 'name': 'delete:list', 'value': '', 'title': 'string:Remove user ${user/fullname}', 'disabled': "python:user['can_delete'] and default or 'disabled'", }
_static_140141462026080 = {'class': 'listingCheckbox table-danger', }
_static_140141472033424 = {'type': 'checkbox', 'class': 'noborder', 'name': 'users.resetpassword:records', 'value': '', 'title': 'string:Reset password of user ${user/fullname}', 'disabled': "python:user['can_set_password'] and default or 'disabled'", }
_static_140141471999312 = {'class': 'listingCheckbox table-warning', }
_static_140141472000368 = {'type': 'hidden', 'name': 'users.roles:list:records', 'value': 'Manager', }
_static_140141462317760 = {'type': 'checkbox', 'class': 'noborder', 'name': 'users.roles:list:records', 'value': 'Manager', 'checked': "python:'checked' if explicit else nothing", 'disabled': "python:default if enabled else 'disabled'", }
_static_140141461325280 = {'class': 'listingCheckbox', }
_static_140141461301232 = {'type': 'hidden', 'name': 'users.id:records', 'value': 'userid', }
_static_140141461300800 = {'class': 'text-muted', }
_static_140141472974016 = {'href': '@@user-i0nformation', 'title': 'userid', }
_static_140141471596896 = {'class': 'text-start', }
_static_140141462834336 = {'class': "python:oddrow and 'odd' or 'even'", }
_static_140141471915360 = {'class': 'rotate table-danger', }
_static_140141472150912 = {'class': 'rotate table-warning', }
_static_140141473035936 = {'class': 'rotate', }
_static_140141473506064 = {'class': 'text-start', }
_static_140141486021600 = {'class': 'table table-responsive table-bordered table-striped text-center', 'summary': 'User Listing', }
_static_140141475671008 = {'type': 'submit', 'class': 'searchButton btn btn-secondary', 'name': 'form.button.FindAll', 'value': 'Show all', }
_static_140141486036160 = {'type': 'submit', 'class': 'searchButton btn btn-primary', 'name': 'form.button.Search', 'value': 'Search', }
_static_140141452457344 = {'class': 'form-control quickSearch', 'id': 'quickSearch', 'aria-labelledby': 'quickSearchLabel', 'type': 'text', 'name': 'searchstring', 'value': '', }
_static_140141462103424 = {'class': 'input-group-text', 'id': 'quickSearchLabel', }
_static_140141462104816 = {'class': 'pat-plone-modal me-3 btn btn-success ', 'id': 'add-user', 'data-pat-plone-modal': '{\n                "actionOptions": {\n                  "redirectOnResponse": true,\n                  "redirectToUrl": "${portal_url}/@@usergroup-userprefs"\n                }\n              }', 'href': 'string:${portal_url}/@@new-user', }
_static_140141462171712 = {'class': 'mb-3 input-group', }
_static_140141462173632 = {'type': 'hidden', 'name': 'form.submitted', 'value': '1', }
_static_140141462035616 = {'action': '', 'class': 'pat-formautofocus', 'name': 'users_search', 'method': 'post', }
_static_140141462099280 = {'class': 'alert alert-warn', 'role': 'status', }
_static_140141462100624 = {'class': 'autotabs', }
_static_140141462750832 = {'id': 'content-core', }
_static_140141462752848 = {'class': 'text-muted mt-2', }
_static_140141462051664 = 'portal_message'
_static_140141462050464 = {'class': 'documentFirstHeading', }
_static_140141473457296 = {'id': 'content', }
_static_140141533071440 = __C2ZContextWrapper
_static_140141533071728 = __compile_zt_expr
_static_140141462355152 = 'master'
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

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462354288
            __attrs_140141462354288 = _static_140141533420656
            __previous_i18n_domain_140141462353328 = __i18n_domain
            __i18n_domain = 'plone'
            __backup_macroname_140141512771904 = get('macroname', __marker)

            # <Static value=<ast.Constant object at 0x7f753a14fcd0> name=None at 7f753a14f280> -> __value
            __value = _static_140141462355152
            econtext['macroname'] = __value

            def __fill_prefs_configlet_main(__stream, econtext, rcontext, __i18n_domain=__i18n_domain, __i18n_context=__i18n_context):
                getname = econtext.get_name
                get = econtext.get

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462355776
                __attrs_140141462355776 = _static_140141533420656
                __backup_template_id_140141462184336 = get('template_id', __marker)

                # <Value 'string:@@usergroup-userprefs' (12:28)> -> __value
                __token = 413
                try:
                    __zt_tmp = __attrs_140141462355776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('string', '@@usergroup-userprefs', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['template_id'] = __value
                __backup_showAll_140141462187936 = get('showAll', __marker)

                # <Value "python:request.get('showAll', '') and not view.newSearch and 'y'" (13:23)> -> __value
                __token = 466
                try:
                    __zt_tmp = __attrs_140141462355776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', "request.get('showAll', '') and not view.newSearch and 'y'", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['showAll'] = __value
                __backup_Batch_140141462187552 = get('Batch', __marker)

                # <Value "python:modules['Products.CMFPlone'].Batch" (14:20)> -> __value
                __token = 553
                try:
                    __zt_tmp = __attrs_140141462355776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', "modules['Products.CMFPlone'].Batch", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['Batch'] = __value
                __backup_b_start_140141462187744 = get('b_start', __marker)

                # <Value "python:0 if showAll or view.newSearch else request.get('b_start',0)" (15:21)> -> __value
                __token = 619
                try:
                    __zt_tmp = __attrs_140141462355776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', "0 if showAll or view.newSearch else request.get('b_start',0)", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['b_start'] = __value
                __backup_b_size_140141462184288 = get('b_size', __marker)

                # <Value 'python:showAll and len(view.searchResults) or 20' (16:19)> -> __value
                __token = 710
                try:
                    __zt_tmp = __attrs_140141462355776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', 'showAll and len(view.searchResults) or 20', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['b_size'] = __value
                __backup_portal_roles_140141462184144 = get('portal_roles', __marker)

                # <Value 'view/portal_roles' (17:24)> -> __value
                __token = 788
                try:
                    __zt_tmp = __attrs_140141462355776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'view/portal_roles', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['portal_roles'] = __value
                __backup_portal_url_140141461552432 = get('portal_url', __marker)

                # <Value 'context/portal_url' (18:21)> -> __value
                __token = 833
                try:
                    __zt_tmp = __attrs_140141462355776
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'context/portal_url', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7f753abe6490> name=None at 7f753abe6430> -> __attrs_140141461892160
                __attrs_140141461892160 = _static_140141473457296

                # <article ... (0:0)
                # --------------------------------------------------------
                __append('<article id="content">\n\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462052096
                __attrs_140141462052096 = _static_140141533420656

                # <header ... (0:0)
                # --------------------------------------------------------
                __append('<header>\n\n        ')

                # <Static value=<ast.Dict object at 0x7f753a1056a0> name=None at 7f753a105910> -> __attrs_140141462050704
                __attrs_140141462050704 = _static_140141462050464

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1 class="documentFirstHeading">')
                __stream_140141462051232 = []
                __append_140141462051232 = __stream_140141462051232.append
                __append_140141462051232('Users')
                __msgid_140141462051232 = __re_whitespace(''.join(__stream_140141462051232)).strip()
                if __msgid_140141462051232:
                    __append(translate(__msgid_140141462051232, mapping=None, default=__msgid_140141462051232, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</h1>\n\n        ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462051856
                __attrs_140141462051856 = _static_140141533420656
                __backup_macroname_140141487142592 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x7f753a105b50> name=None at 7f753a1051f0> -> __value
                __value = _static_140141462051664
                econtext['macroname'] = __value

                # <Value 'context/global_statusmessage/macros/portal_message' (27:30)> -> __macro
                __token = 1017
                try:
                    __zt_tmp = __attrs_140141462051856
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140141533071728('path', 'context/global_statusmessage/macros/portal_message', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __token = 1017
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140141487142592 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140141487142592
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f753a1b0e50> name=None at 7f753a1b0d90> -> __attrs_140141462752224
                __attrs_140141462752224 = _static_140141462752848

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="text-muted mt-2">')
                __stream_140141485083776_image_link_icon = ''
                __stream_140141462750496 = []
                __append_140141462750496 = __stream_140141462750496.append
                __append_140141462750496('\n              Note that roles set here apply directly to a user.\n              The symbol ')
                __stream_140141485083776_image_link_icon = []
                __append_140141485083776_image_link_icon = __stream_140141485083776_image_link_icon.append

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462753232
                __attrs_140141462753232 = _static_140141533420656

                # <span ... (0:0)
                # --------------------------------------------------------
                __append_140141485083776_image_link_icon('<span>')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462751408
                __attrs_140141462751408 = _static_140141533420656

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462752032
                __default_140141462752032 = _DEFAULT_MARKER

                # <Value "python:icons.tag('people', tag_alt='Inherited from Group')" (33:92)> -> __cache_140141462750448
                __token = 1346
                try:
                    __zt_tmp = __attrs_140141462751408
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140141462750448 = _static_140141533071728('python', "icons.tag('people', tag_alt='Inherited from Group')", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                # <BinOp left=<Value "python:icons.tag('people', tag_alt='Inherited from Group')" (33:92)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1b0d00> -> __condition
                __expression = __cache_140141462750448

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    pass
                else:
                    __content = __cache_140141462750448
                    __content = __convert(__content)
                    if (__content is not None):
                        __append_140141485083776_image_link_icon(__content)
                __append_140141485083776_image_link_icon('</span>')
                __append_140141462750496('${image_link_icon}')
                __stream_140141485083776_image_link_icon = ''.join(__stream_140141485083776_image_link_icon)
                __append_140141462750496('\n              indicates a role inherited from membership in a group.\n        ')
                __msgid_140141462750496 = __re_whitespace(''.join(__stream_140141462750496)).strip()
                if 'user_roles_note':
                    __append(translate('user_roles_note', mapping={'image_link_icon': __stream_140141485083776_image_link_icon, }, default=__msgid_140141462750496, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</div>\n      </header>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f753a1b0670> name=None at 7f753a1b0d60> -> __attrs_140141462783456
                __attrs_140141462783456 = _static_140141462750832

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div id="content-core">\n\n      ')

                # <Static value=<ast.Dict object at 0x7f753a111a90> name=None at 7f753a111b50> -> __attrs_140141462101536
                __attrs_140141462101536 = _static_140141462100624

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="autotabs">\n        ')

                # <Static value=<ast.Dict object at 0x7f753a111550> name=None at 7f753a111640> -> __attrs_140141462100960
                __attrs_140141462100960 = _static_140141462099280

                # <Value 'view/show_users_listing_warning' (41:26)> -> __condition
                __token = 1601
                try:
                    __zt_tmp = __attrs_140141462100960
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('path', 'view/show_users_listing_warning', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <p ... (0:0)
                    # --------------------------------------------------------
                    __append('<p class="alert alert-warn" role="status">\n          ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462034512
                    __attrs_140141462034512 = _static_140141533420656

                    # <strong ... (0:0)
                    # --------------------------------------------------------
                    __append('<strong>')
                    __stream_140141462100672 = []
                    __append_140141462100672 = __stream_140141462100672.append
                    __append_140141462100672('Note')
                    __msgid_140141462100672 = __re_whitespace(''.join(__stream_140141462100672)).strip()
                    if __msgid_140141462100672:
                        __append(translate(__msgid_140141462100672, mapping=None, default=__msgid_140141462100672, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</strong>\n          ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462035040
                    __attrs_140141462035040 = _static_140141533420656

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span>')
                    __stream_140141462033360 = []
                    __append_140141462033360 = __stream_140141462033360.append
                    __append_140141462033360('Some or all of your PAS user source\n          plugins do not allow listing of users, so you may not see\n          the users defined by those plugins unless doing a specific\n          search.')
                    __msgid_140141462033360 = __re_whitespace(''.join(__stream_140141462033360)).strip()
                    if 'description_pas_users_listing':
                        __append(translate('description_pas_users_listing', mapping=None, default=__msgid_140141462033360, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</span>\n        </p>')
                __append('\n\n        ')

                # <Static value=<ast.Dict object at 0x7f753a101ca0> name=None at 7f753a101fa0> -> __attrs_140141462454768
                __attrs_140141462454768 = _static_140141462035616
                __backup_findAll_140141461550752 = get('findAll', __marker)

                # <Value "python:'form.button.FindAll' in request.keys()" (54:34)> -> __value
                __token = 2229
                try:
                    __zt_tmp = __attrs_140141462454768
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', "'form.button.FindAll' in request.keys()", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['findAll'] = __value
                __backup_portal_users_140141461550896 = get('portal_users', __marker)

                # <Value 'view/searchResults' (55:38)> -> __value
                __token = 2315
                try:
                    __zt_tmp = __attrs_140141462454768
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'view/searchResults', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['portal_users'] = __value
                __backup_batch_140141461550608 = get('batch', __marker)

                # <Value 'python:Batch(portal_users, b_size, int(b_start), orphan=1)' (56:30)> -> __value
                __token = 2366
                try:
                    __zt_tmp = __attrs_140141462454768
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', 'Batch(portal_users, b_size, int(b_start), orphan=1)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['batch'] = __value
                __backup_batchformkeys_140141462380704 = get('batchformkeys', __marker)

                # <Value "python:['searchstring','_authenticator']" (57:37)> -> __value
                __token = 2465
                try:
                    __zt_tmp = __attrs_140141462454768
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', "['searchstring','_authenticator']", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['batchformkeys'] = __value
                __backup_many_users_140141462676288 = get('many_users', __marker)

                # <Value 'view/many_users' (58:33)> -> __value
                __token = 2543
                try:
                    __zt_tmp = __attrs_140141462454768
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'view/many_users', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['many_users'] = __value

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462035424
                __default_140141462035424 = _DEFAULT_MARKER

                # <Substitution 'string:$portal_url/$template_id' (53:37)> -> __attr_action
                __token = 2162
                try:
                    __zt_tmp = __attrs_140141462454768
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_action = _static_140141533071728('string', '$portal_url/$template_id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_action = __quote(__attr_action, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_action is not None):
                    __append((' action="%s"' % __attr_action))
                __append(' class="pat-formautofocus" name="users_search" method="post">\n          ')

                # <Static value=<ast.Dict object at 0x7f753a1237c0> name=None at 7f753a123e20> -> __attrs_140141462174592
                __attrs_140141462174592 = _static_140141462173632

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="form.submitted" value="1" />\n\n\n        ')

                # <Static value=<ast.Dict object at 0x7f753a123040> name=None at 7f753a1238b0> -> __attrs_140141462172768
                __attrs_140141462172768 = _static_140141462171712

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="mb-3 input-group">\n          ')

                # <Static value=<ast.Dict object at 0x7f753a112af0> name=None at 7f753a112cd0> -> __attrs_140141462105344
                __attrs_140141462105344 = _static_140141462104816

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a class="pat-plone-modal me-3 btn btn-success " id="add-user"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462105008
                __default_140141462105008 = _DEFAULT_MARKER

                # <Interpolation value=<Substitution '{\n                "actionOptions": {\n                  "redirectOnResponse": true,\n                  "redirectToUrl": "${portal_url}/@@usergroup-userprefs"\n                }\n              }' (64:35)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f753a1121c0> -> __attr_data_pat_plone_modal
                __token = 2780
                __token = 2901
                try:
                    __zt_tmp = __attrs_140141462105344
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_data_pat_plone_modal = _static_140141533071728('path', 'portal_url', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_data_pat_plone_modal = __quote(__attr_data_pat_plone_modal, "'", '&#39;', None, _DEFAULT_MARKER)
                __attr_data_pat_plone_modal = ('%s%s%s' % ('{\n                "actionOptions": {\n                  "redirectOnResponse": true,\n                  "redirectToUrl": "', (__attr_data_pat_plone_modal if (__attr_data_pat_plone_modal is not None) else ''), '/@@usergroup-userprefs"\n                }\n              }', ))
                if (__attr_data_pat_plone_modal is None):
                    pass
                else:
                    if (__attr_data_pat_plone_modal is _DEFAULT_MARKER):
                        __attr_data_pat_plone_modal = None
                    else:
                        __tt = type(__attr_data_pat_plone_modal)
                        if ((__tt is int) or (__tt is float) or (__tt is int)):
                            __attr_data_pat_plone_modal = str(__attr_data_pat_plone_modal)
                        else:
                            if (__tt is bytes):
                                __attr_data_pat_plone_modal = decode(__attr_data_pat_plone_modal)
                            else:
                                if (__tt is not str):
                                    try:
                                        __attr_data_pat_plone_modal = __attr_data_pat_plone_modal.__html__
                                    except get('AttributeError', AttributeError):
                                        __converted = convert(__attr_data_pat_plone_modal)
                                        __attr_data_pat_plone_modal = (str(__attr_data_pat_plone_modal) if (__attr_data_pat_plone_modal is __converted) else __converted)
                                    else:
                                        __attr_data_pat_plone_modal = __attr_data_pat_plone_modal()
                if (__attr_data_pat_plone_modal is not None):
                    __append((" data-pat-plone-modal='%s'" % __attr_data_pat_plone_modal))

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462105152
                __default_140141462105152 = _DEFAULT_MARKER

                # <Substitution 'string:${portal_url}/@@new-user' (70:34)> -> __attr_href
                __token = 3005
                try:
                    __zt_tmp = __attrs_140141462105344
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140141533071728('string', '${portal_url}/@@new-user', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append('>')
                __stream_140141462105920 = []
                __append_140141462105920 = __stream_140141462105920.append
                __append_140141462105920('Add New User')
                __msgid_140141462105920 = __re_whitespace(''.join(__stream_140141462105920)).strip()
                if 'label_add_new_user':
                    __append(translate('label_add_new_user', mapping=None, default=__msgid_140141462105920, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</a>\n          ')

                # <Static value=<ast.Dict object at 0x7f753a112580> name=None at 7f753a112550> -> __attrs_140141452459120
                __attrs_140141452459120 = _static_140141462103424

                # <span ... (0:0)
                # --------------------------------------------------------
                __append('<span class="input-group-text" id="quickSearchLabel">')
                __stream_140141462103040 = []
                __append_140141462103040 = __stream_140141462103040.append
                __append_140141462103040('User Search')
                __msgid_140141462103040 = __re_whitespace(''.join(__stream_140141462103040)).strip()
                if 'label_user_search':
                    __append(translate('label_user_search', mapping=None, default=__msgid_140141462103040, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</span>\n          ')

                # <Static value=<ast.Dict object at 0x7f75397df580> name=None at 7f75397df3a0> -> __attrs_140141452456912
                __attrs_140141452456912 = _static_140141452457344

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input class="form-control quickSearch" id="quickSearch" aria-labelledby="quickSearchLabel" type="text" name="searchstring"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141452458832
                __default_140141452458832 = _DEFAULT_MARKER

                # <Substitution 'view/searchString' (79:40)> -> __attr_value
                __token = 3494
                try:
                    __zt_tmp = __attrs_140141452456912
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'view/searchString', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n          ')

                # <Static value=<ast.Dict object at 0x7f753b7e54c0> name=None at 7f753b7e5b50> -> __attrs_140141478770000
                __attrs_140141478770000 = _static_140141486036160

                # <button ... (0:0)
                # --------------------------------------------------------
                __append('<button type="submit" class="searchButton btn btn-primary" name="form.button.Search"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141478846272
                __default_140141478846272 = _DEFAULT_MARKER

                # <Translate msgid='label_search' node=<ast.Constant object at 0x7f753b1097f0> at 7f753b109c70> -> __attr_value
                __attr_value = 'Search'
                __attr_value = translate('label_search', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' >')
                __stream_140141478846368 = []
                __append_140141478846368 = __stream_140141478846368.append
                __append_140141478846368('Search')
                __msgid_140141478846368 = __re_whitespace(''.join(__stream_140141478846368)).strip()
                if __msgid_140141478846368:
                    __append(translate(__msgid_140141478846368, mapping=None, default=__msgid_140141478846368, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                __append('</button>\n\n          ')

                # <Static value=<ast.Dict object at 0x7f753ae02be0> name=None at 7f753ae02910> -> __attrs_140141475653424
                __attrs_140141475653424 = _static_140141475671008

                # <Value 'not:many_users' (95:33)> -> __condition
                __token = 4135
                try:
                    __zt_tmp = __attrs_140141475653424
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('not', 'many_users', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button type="submit" class="searchButton btn btn-secondary" name="form.button.FindAll"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141475652944
                    __default_140141475652944 = _DEFAULT_MARKER

                    # <Translate msgid='label_showall' node=<ast.Constant object at 0x7f753adfe910> at 7f753adfe6d0> -> __attr_value
                    __attr_value = 'Show all'
                    __attr_value = translate('label_showall', default=__attr_value, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' >')
                    __stream_140141475670480 = []
                    __append_140141475670480 = __stream_140141475670480.append
                    __append_140141475670480('Show all')
                    __msgid_140141475670480 = __re_whitespace(''.join(__stream_140141475670480)).strip()
                    if 'label_showall':
                        __append(translate('label_showall', mapping=None, default=__msgid_140141475670480, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>')
                __append('\n        </div>\n          ')

                # <Static value=<ast.Dict object at 0x7f753b7e1be0> name=None at 7f753b7e16a0> -> __attrs_140141478593968
                __attrs_140141478593968 = _static_140141486021600

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-responsive table-bordered table-striped text-center" summary="User Listing">\n              ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141518190528
                __attrs_140141518190528 = _static_140141533420656

                # <Value 'portal_users' (99:36)> -> __condition
                __token = 4352
                try:
                    __zt_tmp = __attrs_140141518190528
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('path', 'portal_users', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <thead ... (0:0)
                    # --------------------------------------------------------
                    __append('<thead>\n                ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141518189136
                    __attrs_140141518189136 = _static_140141533420656

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n                  ')

                    # <Static value=<ast.Dict object at 0x7f753abf2310> name=None at 7f753abf25e0> -> __attrs_140141473525136
                    __attrs_140141473525136 = _static_140141473506064

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th  class="text-start">')
                    __stream_140141518189088 = []
                    __append_140141518189088 = __stream_140141518189088.append
                    __append_140141518189088('User name')
                    __msgid_140141518189088 = __re_whitespace(''.join(__stream_140141518189088)).strip()
                    if 'listingheader_user_name':
                        __append(translate('listingheader_user_name', mapping=None, default=__msgid_140141518189088, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</th>\n                  ')

                    # <Static value=<ast.Dict object at 0x7f753ab7f6a0> name=None at 7f753ab7f220> -> __attrs_140141472811040
                    __attrs_140141472811040 = _static_140141473035936
                    __backup_portal_role_140141463016016 = get('portal_role', __marker)

                    # <Value 'portal_roles' (102:61)> -> __iterator
                    __token = 4547
                    try:
                        __zt_tmp = __attrs_140141472811040
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140141533071728('path', 'portal_roles', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    (__iterator, ____index_140141472810656, ) = getname('repeat')('portal_role', __iterator)
                    econtext['portal_role'] = None
                    for __item in __iterator:
                        econtext['portal_role'] = __item

                        # <th ... (0:0)
                        # --------------------------------------------------------
                        __append('<th class="rotate">')

                        # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141472786224
                        __attrs_140141472786224 = _static_140141533420656

                        # <div ... (0:0)
                        # --------------------------------------------------------
                        __append('<div>')

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141472809552
                        __default_140141472809552 = _DEFAULT_MARKER

                        # <Value 'portal_role' (102:93)> -> __cache_140141472812528
                        __token = 4579
                        try:
                            __zt_tmp = __attrs_140141472786224
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140141472812528 = _static_140141533071728('path', 'portal_role', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                        # <BinOp left=<Value 'portal_role' (102:93)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753ab48580> -> __condition
                        __expression = __cache_140141472812528

                        # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:
                            __append('Role')
                        else:
                            __content = __cache_140141472812528
                            __content = translate(__content, default=None, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append(__content)
                        __append('</div></th>')
                        ____index_140141472810656 -= 1
                        if (____index_140141472810656 > 0):
                            __append('\n                  ')
                    if (__backup_portal_role_140141463016016 is __marker):
                        del econtext['portal_role']
                    else:
                        econtext['portal_role'] = __backup_portal_role_140141463016016
                    __append('\n                  ')

                    # <Static value=<ast.Dict object at 0x7f753aaa7580> name=None at 7f753aaa7700> -> __attrs_140141472286416
                    __attrs_140141472286416 = _static_140141472150912

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th class="rotate table-warning">')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141472200496
                    __attrs_140141472200496 = _static_140141533420656

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>')
                    __stream_140141472285792 = []
                    __append_140141472285792 = __stream_140141472285792.append
                    __append_140141472285792('Reset Password')
                    __msgid_140141472285792 = __re_whitespace(''.join(__stream_140141472285792)).strip()
                    if 'listingheader_reset_password':
                        __append(translate('listingheader_reset_password', mapping=None, default=__msgid_140141472285792, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</div></th>\n                  ')

                    # <Static value=<ast.Dict object at 0x7f753aa6dd60> name=None at 7f753aaaf970> -> __attrs_140141471928528
                    __attrs_140141471928528 = _static_140141471915360

                    # <th ... (0:0)
                    # --------------------------------------------------------
                    __append('<th class="rotate table-danger">')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462854096
                    __attrs_140141462854096 = _static_140141533420656

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>')
                    __stream_140141462852080 = []
                    __append_140141462852080 = __stream_140141462852080.append
                    __append_140141462852080('Remove')
                    __msgid_140141462852080 = __re_whitespace(''.join(__stream_140141462852080)).strip()
                    if 'listingheader_remove':
                        __append(translate('listingheader_remove', mapping=None, default=__msgid_140141462852080, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</div></th>\n                </tr>\n              </thead>')
                __append('\n              ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141463004544
                __attrs_140141463004544 = _static_140141533420656

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append('<tbody>\n                  ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141471669312
                __attrs_140141471669312 = _static_140141533420656
                __backup_user_140141462759456 = get('user', __marker)

                # <Value 'batch' (108:41)> -> __iterator
                __token = 4973
                try:
                    __zt_tmp = __attrs_140141471669312
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140141533071728('path', 'batch', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                (__iterator, ____index_140141462833808, ) = getname('repeat')('user', __iterator)
                econtext['user'] = None
                for __item in __iterator:
                    econtext['user'] = __item
                    __append('\n                    ')

                    # <Static value=<ast.Dict object at 0x7f753a1c4ca0> name=None at 7f753a1c4340> -> __attrs_140141471584608
                    __attrs_140141471584608 = _static_140141462834336
                    __backup_oddrow_140141462759120 = get('oddrow', __marker)

                    # <Value 'repeat/user/odd' (109:43)> -> __value
                    __token = 5024
                    try:
                        __zt_tmp = __attrs_140141471584608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140141533071728('path', 'repeat/user/odd', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    econtext['oddrow'] = __value
                    __backup_userid_140141463015920 = get('userid', __marker)

                    # <Value 'user/userid' (110:42)> -> __value
                    __token = 5083
                    try:
                        __zt_tmp = __attrs_140141471584608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140141533071728('path', 'user/userid', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    econtext['userid'] = __value
                    __backup_userquery_140141462298240 = get('userquery', __marker)

                    # <Value 'python:view.makeQuery(userid=userid)' (111:44)> -> __value
                    __token = 5141
                    try:
                        __zt_tmp = __attrs_140141471584608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __value = _static_140141533071728('python', 'view.makeQuery(userid=userid)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    econtext['userquery'] = __value

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141471756592
                    __default_140141471756592 = _DEFAULT_MARKER

                    # <Substitution "python:oddrow and 'odd' or 'even'" (112:46)> -> __attr_class
                    __token = 5228
                    try:
                        __zt_tmp = __attrs_140141471584608
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_class = _static_140141533071728('python', "oddrow and 'odd' or 'even'", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_class = __quote(__attr_class, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_class is not None):
                        __append((' class="%s"' % __attr_class))
                    __append('>\n\n                        ')

                    # <Static value=<ast.Dict object at 0x7f753aa20160> name=None at 7f753aa20f40> -> __attrs_140141471597712
                    __attrs_140141471597712 = _static_140141471596896

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="text-start">\n                            ')

                    # <Static value=<ast.Dict object at 0x7f753ab704c0> name=None at 7f753ab701c0> -> __attrs_140141461302240
                    __attrs_140141461302240 = _static_140141472974016

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141471551296
                    __default_140141471551296 = _DEFAULT_MARKER

                    # <Substitution 'string:$portal_url/@@user-information?${userquery}' (116:52)> -> __attr_href
                    __token = 5423
                    try:
                        __zt_tmp = __attrs_140141461302240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140141533071728('string', '$portal_url/@@user-information?${userquery}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '@@user-i0nformation', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141471547792
                    __default_140141471547792 = _DEFAULT_MARKER

                    # <Substitution 'userid' (117:52)> -> __attr_title
                    __token = 5527
                    try:
                        __zt_tmp = __attrs_140141461302240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140141533071728('path', 'userid', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))
                    __append('>')

                    # <Interpolation value=<Substitution '\n                                ${user/fullname} ' (117:61)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f753a04eee0> -> __content_140141614154928
                    __token = 5569
                    __token = 5571
                    try:
                        __zt_tmp = __attrs_140141461302240
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140141614154928 = _static_140141533071728('path', 'user/fullname', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __content_140141614154928 = __quote(__content_140141614154928, '\x00', '&#0;', None, None)
                    __content_140141614154928 = ('%s%s%s' % ('\n                                ', (__content_140141614154928 if (__content_140141614154928 is not None) else ''), ' ', ))
                    if (__content_140141614154928 is None):
                        pass
                    else:
                        if (__content_140141614154928 is None):
                            __content_140141614154928 = None
                        else:
                            __tt = type(__content_140141614154928)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140141614154928 = str(__content_140141614154928)
                            else:
                                if (__tt is bytes):
                                    __content_140141614154928 = decode(__content_140141614154928)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140141614154928 = __content_140141614154928.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140141614154928)
                                            __content_140141614154928 = (str(__content_140141614154928) if (__content_140141614154928 is __converted) else __converted)
                                        else:
                                            __content_140141614154928 = __content_140141614154928()
                    if (__content_140141614154928 is not None):
                        __append(__content_140141614154928)

                    # <Static value=<ast.Dict object at 0x7f753a04e640> name=None at 7f753a04e250> -> __attrs_140141461303152
                    __attrs_140141461303152 = _static_140141461300800

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="text-muted">')

                    # <Interpolation value=<Substitution '(${user/login})' (118:74)> braces_required=True translation=False default='"?"' default_marker='"?"' at 7f753a04e490> -> __content_140141614154928
                    __token = 5611
                    __token = 5614
                    try:
                        __zt_tmp = __attrs_140141461303152
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __content_140141614154928 = _static_140141533071728('path', 'user/login', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __content_140141614154928 = __quote(__content_140141614154928, '\x00', '&#0;', None, None)
                    __content_140141614154928 = ('%s%s%s' % ('(', (__content_140141614154928 if (__content_140141614154928 is not None) else ''), ')', ))
                    if (__content_140141614154928 is None):
                        pass
                    else:
                        if (__content_140141614154928 is None):
                            __content_140141614154928 = None
                        else:
                            __tt = type(__content_140141614154928)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_140141614154928 = str(__content_140141614154928)
                            else:
                                if (__tt is bytes):
                                    __content_140141614154928 = decode(__content_140141614154928)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_140141614154928 = __content_140141614154928.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_140141614154928)
                                            __content_140141614154928 = (str(__content_140141614154928) if (__content_140141614154928 is __converted) else __converted)
                                        else:
                                            __content_140141614154928 = __content_140141614154928()
                    if (__content_140141614154928 is not None):
                        __append(__content_140141614154928)
                    __append('</span>\n                            </a>\n                            ')

                    # <Static value=<ast.Dict object at 0x7f753a04e7f0> name=None at 7f753a04e130> -> __attrs_140141461302768
                    __attrs_140141461302768 = _static_140141461301232

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="hidden" name="users.id:records"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461302480
                    __default_140141461302480 = _DEFAULT_MARKER

                    # <Substitution 'userid' (120:95)> -> __attr_value
                    __token = 5762
                    try:
                        __zt_tmp = __attrs_140141461302768
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'userid', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n                        </td>\n\n                        ')

                    # <Static value=<ast.Dict object at 0x7f753a0545e0> name=None at 7f753a054250> -> __attrs_140141461325616
                    __attrs_140141461325616 = _static_140141461325280
                    __backup_portal_role_140141471564800 = get('portal_role', __marker)

                    # <Value 'portal_roles' (124:52)> -> __iterator
                    __token = 5908
                    try:
                        __zt_tmp = __attrs_140141461325616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __iterator = _static_140141533071728('path', 'portal_roles', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    (__iterator, ____index_140141461324224, ) = getname('repeat')('portal_role', __iterator)
                    econtext['portal_role'] = None
                    for __item in __iterator:
                        econtext['portal_role'] = __item

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td class="listingCheckbox">\n                          ')

                        # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461327632
                        __attrs_140141461327632 = _static_140141533420656
                        __backup_inherited_140141485994336 = get('inherited', __marker)

                        # <Value "python:user['roles'][portal_role]['inherited']" (125:59)> -> __value
                        __token = 5982
                        try:
                            __zt_tmp = __attrs_140141461327632
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140141533071728('python', "user['roles'][portal_role]['inherited']", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        econtext['inherited'] = __value
                        __backup_explicit_140141485997168 = get('explicit', __marker)

                        # <Value "python:user['roles'][portal_role]['explicit']" (126:57)> -> __value
                        __token = 6087
                        try:
                            __zt_tmp = __attrs_140141461327632
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140141533071728('python', "user['roles'][portal_role]['explicit']", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        econtext['explicit'] = __value
                        __backup_enabled_140141485997984 = get('enabled', __marker)

                        # <Value "python:user['roles'][portal_role]['canAssign']" (127:55)> -> __value
                        __token = 6190
                        try:
                            __zt_tmp = __attrs_140141461327632
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __value = _static_140141533071728('python', "user['roles'][portal_role]['canAssign']", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        econtext['enabled'] = __value
                        __append('\n                            ')

                        # <Static value=<ast.Dict object at 0x7f753a146ac0> name=None at 7f753a146220> -> __attrs_140141472001232
                        __attrs_140141472001232 = _static_140141462317760

                        # <Value 'not:inherited' (132:50)> -> __condition
                        __token = 6512
                        try:
                            __zt_tmp = __attrs_140141472001232
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140141533071728('not', 'inherited', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="checkbox" class="noborder" name="users.roles:list:records"')

                            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461243120
                            __default_140141461243120 = _DEFAULT_MARKER

                            # <Substitution 'portal_role' (133:57)> -> __attr_value
                            __token = 6584
                            try:
                                __zt_tmp = __attrs_140141472001232
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140141533071728('path', 'portal_role', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', 'Manager', _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))

                            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461243264
                            __default_140141461243264 = _DEFAULT_MARKER

                            # <Boolean "python:'checked' if explicit else nothing" (134:46)> -> __attr_checked
                            __token = 6643
                            try:
                                __zt_tmp = __attrs_140141472001232
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_checked = _static_140141533071728('python', "'checked' if explicit else nothing", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                            if (__attr_checked is _DEFAULT_MARKER):
                                __attr_checked = None
                            else:
                                if __attr_checked:
                                    __attr_checked = 'checked'
                                else:
                                    __attr_checked = None
                            if (__attr_checked is not None):
                                __append((' checked="%s"' % __attr_checked))

                            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141472001712
                            __default_140141472001712 = _DEFAULT_MARKER

                            # <Boolean "python:default if enabled else 'disabled'" (135:46)> -> __attr_disabled
                            __token = 6733
                            try:
                                __zt_tmp = __attrs_140141472001232
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_disabled = _static_140141533071728('python', "default if enabled else 'disabled'", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                            if (__attr_disabled is _DEFAULT_MARKER):
                                __attr_disabled = None
                            else:
                                if __attr_disabled:
                                    __attr_disabled = 'disabled'
                                else:
                                    __attr_disabled = None
                            if (__attr_disabled is not None):
                                __append((' disabled="%s"' % __attr_disabled))
                            __append(' />')
                        __append('\n                            ')

                        # <Static value=<ast.Dict object at 0x7f753aa82970> name=None at 7f753aa828e0> -> __attrs_140141471999744
                        __attrs_140141471999744 = _static_140141472000368

                        # <Value 'python:inherited' (139:50)> -> __condition
                        __token = 6998
                        try:
                            __zt_tmp = __attrs_140141471999744
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140141533071728('python', 'inherited', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        if __condition:

                            # <input ... (0:0)
                            # --------------------------------------------------------
                            __append('<input type="hidden" name="users.roles:list:records"')

                            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141472001088
                            __default_140141472001088 = _DEFAULT_MARKER

                            # <Substitution 'portal_role' (140:57)> -> __attr_value
                            __token = 7073
                            try:
                                __zt_tmp = __attrs_140141471999744
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __attr_value = _static_140141533071728('path', 'portal_role', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                            __attr_value = __quote(__attr_value, '"', '&quot;', 'Manager', _DEFAULT_MARKER)
                            if (__attr_value is not None):
                                __append((' value="%s"' % __attr_value))
                            __append(' />')
                        __append('\n                            ')

                        # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141472032416
                        __attrs_140141472032416 = _static_140141533420656

                        # <Value 'inherited' (141:53)> -> __condition
                        __token = 7142
                        try:
                            __zt_tmp = __attrs_140141472032416
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140141533071728('path', 'inherited', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        if __condition:

                            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141472033184
                            __default_140141472033184 = _DEFAULT_MARKER

                            # <Value "python:icons.tag('people', tag_alt='Inherited from Group')" (141:87)> -> __cache_140141471998304
                            __token = 7176
                            try:
                                __zt_tmp = __attrs_140141472032416
                            except get('NameError', NameError):
                                __zt_tmp = None

                            __cache_140141471998304 = _static_140141533071728('python', "icons.tag('people', tag_alt='Inherited from Group')", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                            # <BinOp left=<Value "python:icons.tag('people', tag_alt='Inherited from Group')" (141:87)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753aa822e0> -> __condition
                            __expression = __cache_140141471998304

                            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                            __value = _DEFAULT_MARKER
                            __condition = (__expression is __value)
                            if __condition:
                                pass
                            else:
                                __content = __cache_140141471998304
                                __content = __convert(__content)
                                if (__content is not None):
                                    __append(__content)
                        __append('\n\n                          ')
                        if (__backup_enabled_140141485997984 is __marker):
                            del econtext['enabled']
                        else:
                            econtext['enabled'] = __backup_enabled_140141485997984
                        if (__backup_explicit_140141485997168 is __marker):
                            del econtext['explicit']
                        else:
                            econtext['explicit'] = __backup_explicit_140141485997168
                        if (__backup_inherited_140141485994336 is __marker):
                            del econtext['inherited']
                        else:
                            econtext['inherited'] = __backup_inherited_140141485994336
                        __append('\n\n                        </td>')
                        ____index_140141461324224 -= 1
                        if (____index_140141461324224 > 0):
                            __append('\n                        ')
                    if (__backup_portal_role_140141471564800 is __marker):
                        del econtext['portal_role']
                    else:
                        econtext['portal_role'] = __backup_portal_role_140141471564800
                    __append('\n\n                        ')

                    # <Static value=<ast.Dict object at 0x7f753aa82550> name=None at 7f753aa822b0> -> __attrs_140141472030880
                    __attrs_140141472030880 = _static_140141471999312

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="listingCheckbox table-warning">\n                          ')

                    # <Static value=<ast.Dict object at 0x7f753aa8aa90> name=None at 7f753aa8aa60> -> __attrs_140141462024592
                    __attrs_140141462024592 = _static_140141472033424

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" class="noborder" name="users.resetpassword:records"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141472031936
                    __default_140141472031936 = _DEFAULT_MARKER

                    # <Substitution 'userid' (152:55)> -> __attr_value
                    __token = 7642
                    try:
                        __zt_tmp = __attrs_140141462024592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'userid', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462024496
                    __default_140141462024496 = _DEFAULT_MARKER

                    # <Substitution 'string:Reset password of user ${user/fullname}' (153:54)> -> __attr_title
                    __token = 7704
                    try:
                        __zt_tmp = __attrs_140141462024592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140141533071728('string', 'Reset password of user ${user/fullname}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462025168
                    __default_140141462025168 = _DEFAULT_MARKER

                    # <Boolean "python:user['can_set_password'] and default or 'disabled'" (154:56)> -> __attr_disabled
                    __token = 7809
                    try:
                        __zt_tmp = __attrs_140141462024592
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_disabled = _static_140141533071728('python', "user['can_set_password'] and default or 'disabled'", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if (__attr_disabled is _DEFAULT_MARKER):
                        __attr_disabled = None
                    else:
                        if __attr_disabled:
                            __attr_disabled = 'disabled'
                        else:
                            __attr_disabled = None
                    if (__attr_disabled is not None):
                        __append((' disabled="%s"' % __attr_disabled))
                    __append(' />\n                        </td>\n\n                        ')

                    # <Static value=<ast.Dict object at 0x7f753a0ff760> name=None at 7f753a0ff7c0> -> __attrs_140141462028096
                    __attrs_140141462028096 = _static_140141462026080

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="listingCheckbox table-danger">\n                          ')

                    # <Static value=<ast.Dict object at 0x7f753a0ff370> name=None at 7f753a0ff700> -> __attrs_140141452371760
                    __attrs_140141452371760 = _static_140141462025072

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" class="noborder notify" name="delete:list"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141452370224
                    __default_140141452370224 = _DEFAULT_MARKER

                    # <Substitution 'userid' (162:63)> -> __attr_value
                    __token = 8257
                    try:
                        __zt_tmp = __attrs_140141452371760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'userid', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141452373680
                    __default_140141452373680 = _DEFAULT_MARKER

                    # <Substitution 'string:Remove user ${user/fullname}' (163:62)> -> __attr_title
                    __token = 8327
                    try:
                        __zt_tmp = __attrs_140141452371760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_title = _static_140141533071728('string', 'Remove user ${user/fullname}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_title = __quote(__attr_title, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_title is not None):
                        __append((' title="%s"' % __attr_title))

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141452371904
                    __default_140141452371904 = _DEFAULT_MARKER

                    # <Boolean "python:user['can_delete'] and default or 'disabled'" (164:64)> -> __attr_disabled
                    __token = 8429
                    try:
                        __zt_tmp = __attrs_140141452371760
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_disabled = _static_140141533071728('python', "user['can_delete'] and default or 'disabled'", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if (__attr_disabled is _DEFAULT_MARKER):
                        __attr_disabled = None
                    else:
                        if __attr_disabled:
                            __attr_disabled = 'disabled'
                        else:
                            __attr_disabled = None
                    if (__attr_disabled is not None):
                        __append((' disabled="%s"' % __attr_disabled))
                    __append(' />\n                        </td>\n                    </tr>')
                    if (__backup_userquery_140141462298240 is __marker):
                        del econtext['userquery']
                    else:
                        econtext['userquery'] = __backup_userquery_140141462298240
                    if (__backup_userid_140141463015920 is __marker):
                        del econtext['userid']
                    else:
                        econtext['userid'] = __backup_userid_140141463015920
                    if (__backup_oddrow_140141462759120 is __marker):
                        del econtext['oddrow']
                    else:
                        econtext['oddrow'] = __backup_oddrow_140141462759120
                    __append('\n                  ')
                    ____index_140141462833808 -= 1
                    if (____index_140141462833808 > 0):
                        __append('')
                if (__backup_user_140141462759456 is __marker):
                    del econtext['user']
                else:
                    econtext['user'] = __backup_user_140141462759456
                __append('\n                  ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462024832
                __attrs_140141462024832 = _static_140141533420656

                # <Value 'not:batch' (168:37)> -> __condition
                __token = 8610
                try:
                    __zt_tmp = __attrs_140141462024832
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('not', 'batch', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n                      ')

                    # <Static value=<ast.Dict object at 0x7f75397caee0> name=None at 7f75397ca970> -> __attrs_140141452371616
                    __attrs_140141452371616 = _static_140141452373728

                    # <Value 'view/searchString' (169:41)> -> __condition
                    __token = 8663
                    try:
                        __zt_tmp = __attrs_140141452371616
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('path', 'view/searchString', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:

                        # <td ... (0:0)
                        # --------------------------------------------------------
                        __append('<td style="text-align:center;">')
                        __stream_140141452371808 = []
                        __append_140141452371808 = __stream_140141452371808.append
                        __append_140141452371808('No matches')
                        __msgid_140141452371808 = __re_whitespace(''.join(__stream_140141452371808)).strip()
                        if 'text_nomatches':
                            __append(translate('text_nomatches', mapping=None, default=__msgid_140141452371808, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</td>')
                    __append('\n                      ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462356128
                    __attrs_140141462356128 = _static_140141533420656

                    # <Value 'not:view/searchString' (172:48)> -> __condition
                    __token = 8857
                    try:
                        __zt_tmp = __attrs_140141462356128
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140141533071728('not', 'view/searchString', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    if __condition:
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x7f753a1505b0> name=None at 7f753a150b50> -> __attrs_140141462358816
                        __attrs_140141462358816 = _static_140141462357424

                        # <Value 'many_users' (173:43)> -> __condition
                        __token = 8924
                        try:
                            __zt_tmp = __attrs_140141462358816
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140141533071728('path', 'many_users', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        if __condition:

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append('<td class="discreet" style="text-align:center; font-size: 100%;">')
                            __stream_140141462357520 = []
                            __append_140141462357520 = __stream_140141462357520.append
                            __append_140141462357520('\n                            Enter a username to search for\n                        ')
                            __msgid_140141462357520 = __re_whitespace(''.join(__stream_140141462357520)).strip()
                            if 'text_no_user_searchstring':
                                __append(translate('text_no_user_searchstring', mapping=None, default=__msgid_140141462357520, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</td>')
                        __append('\n                        ')

                        # <Static value=<ast.Dict object at 0x7f753a09b310> name=None at 7f753a09b640> -> __attrs_140141461618016
                        __attrs_140141461618016 = _static_140141461615376

                        # <Value 'not:many_users' (179:43)> -> __condition
                        __token = 9257
                        try:
                            __zt_tmp = __attrs_140141461618016
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __condition = _static_140141533071728('not', 'many_users', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                        if __condition:

                            # <td ... (0:0)
                            # --------------------------------------------------------
                            __append('<td class="discreet" style="text-align:center; font-size: 100%;">')
                            __stream_140141462358192 = []
                            __append_140141462358192 = __stream_140141462358192.append
                            __append_140141462358192("\n                            Enter a username to search for, or click 'Show All'\n                        ")
                            __msgid_140141462358192 = __re_whitespace(''.join(__stream_140141462358192)).strip()
                            if 'text_no_user_searchstring_largesite':
                                __append(translate('text_no_user_searchstring_largesite', mapping=None, default=__msgid_140141462358192, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                            __append('</td>')
                        __append('\n                      ')
                    __append('\n                  </tr>')
                __append('\n              </tbody>\n          </table>\n\n          ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461618544
                __attrs_140141461618544 = _static_140141533420656
                __backup_macroname_140141514937984 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x7f753a150730> name=None at 7f753a150df0> -> __value
                __value = _static_140141462357808
                econtext['macroname'] = __value

                # <Value 'context/batch_macros/macros/navigation' (190:32)> -> __macro
                __token = 9716
                try:
                    __zt_tmp = __attrs_140141461618544
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140141533071728('path', 'context/batch_macros/macros/navigation', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __token = 9716
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140141514937984 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140141514937984
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x7f753a09bf40> name=None at 7f753a09bfa0> -> __attrs_140141461617248
                __attrs_140141461617248 = _static_140141461618496
                __backup_mq_140141462758640 = get('mq', __marker)

                # <Value "python:modules['ZTUtils'].make_query" (194:30)> -> __value
                __token = 9901
                try:
                    __zt_tmp = __attrs_140141461617248
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', "modules['ZTUtils'].make_query", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['mq'] = __value
                __backup_keys_140141462759648 = get('keys', __marker)

                # <Value 'batchformkeys|nothing' (195:31)> -> __value
                __token = 9970
                try:
                    __zt_tmp = __attrs_140141461617248
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'batchformkeys|nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['keys'] = __value
                __backup_linkparams_140141462296080 = get('linkparams', __marker)

                # <Value 'python:keys and dict([(key, request.form[key]) for key in keys if key in request]) or request.form' (196:36)> -> __value
                __token = 10030
                try:
                    __zt_tmp = __attrs_140141461617248
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', 'keys and dict([(key, request.form[key]) for key in keys if key in request]) or request.form', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['linkparams'] = __value
                __backup_url_140141462760320 = get('url', __marker)

                # <Value 'batch_base_url | string:${context/absolute_url}/${template_id}' (197:28)> -> __value
                __token = 10160
                try:
                    __zt_tmp = __attrs_140141461617248
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'batch_base_url | string:${context/absolute_url}/${template_id}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['url'] = __value

                # <Value 'python:batch.next or batch.previous' (193:30)> -> __condition
                __token = 9834
                try:
                    __zt_tmp = __attrs_140141461617248
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('python', 'batch.next or batch.previous', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="showAllSearchResults">\n              ')

                    # <Static value=<ast.Dict object at 0x7f753a0976a0> name=None at 7f753a0979a0> -> __attrs_140141461600000
                    __attrs_140141461600000 = _static_140141461599904

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461601104
                    __default_140141461601104 = _DEFAULT_MARKER

                    # <Substitution "python: '%s?%s' % (url, mq( linkparams, {'showAll':'y'} ))" (198:38)> -> __attr_href
                    __token = 10266
                    try:
                        __zt_tmp = __attrs_140141461600000
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140141533071728('python', " '%s?%s' % (url, mq( linkparams, {'showAll':'y'} ))", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append('>')
                    __stream_140141461600768 = []
                    __append_140141461600768 = __stream_140141461600768.append
                    __append_140141461600768('\n                  Show all search results\n              ')
                    __msgid_140141461600768 = __re_whitespace(''.join(__stream_140141461600768)).strip()
                    if 'description_pas_show_all_search_results':
                        __append(translate('description_pas_show_all_search_results', mapping=None, default=__msgid_140141461600768, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</a>\n          </div>')
                if (__backup_url_140141462760320 is __marker):
                    del econtext['url']
                else:
                    econtext['url'] = __backup_url_140141462760320
                if (__backup_linkparams_140141462296080 is __marker):
                    del econtext['linkparams']
                else:
                    econtext['linkparams'] = __backup_linkparams_140141462296080
                if (__backup_keys_140141462759648 is __marker):
                    del econtext['keys']
                else:
                    econtext['keys'] = __backup_keys_140141462759648
                if (__backup_mq_140141462758640 is __marker):
                    del econtext['mq']
                else:
                    econtext['mq'] = __backup_mq_140141462758640
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x7f753a097580> name=None at 7f753a0974f0> -> __attrs_140141461656240
                __attrs_140141461656240 = _static_140141461599616

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461601584
                __default_140141461601584 = _DEFAULT_MARKER

                # <Substitution 'b_start' (205:39)> -> __attr_value
                __token = 10581
                try:
                    __zt_tmp = __attrs_140141461656240
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'b_start', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', 'b_start', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' name="b_start"/>\n\n          ')

                # <Static value=<ast.Dict object at 0x7f753a0a5940> name=None at 7f753a0a5f10> -> __attrs_140141461658832
                __attrs_140141461658832 = _static_140141461657920

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461659552
                __default_140141461659552 = _DEFAULT_MARKER

                # <Substitution 'showAll' (208:39)> -> __attr_value
                __token = 10687
                try:
                    __zt_tmp = __attrs_140141461658832
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'showAll', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', '', _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' name="showAll"/>\n\n          ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461658016
                __attrs_140141461658016 = _static_140141533420656

                # <Value 'batch' (210:30)> -> __condition
                __token = 10729
                try:
                    __zt_tmp = __attrs_140141461658016
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140141533071728('path', 'batch', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                if __condition:

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div>\n\n            ')

                    # <Static value=<ast.Dict object at 0x7f753a0a5b20> name=None at 7f753aa28bb0> -> __attrs_140141461453600
                    __attrs_140141461453600 = _static_140141461658400

                    # <div ... (0:0)
                    # --------------------------------------------------------
                    __append('<div class="btn-group">\n              ')

                    # <Static value=<ast.Dict object at 0x7f753a073c70> name=None at 7f753a0731c0> -> __attrs_140141461453024
                    __attrs_140141461453024 = _static_140141461453936

                    # <button ... (0:0)
                    # --------------------------------------------------------
                    __append('<button class="btn btn-primary" type="submit" name="form.button.Modify" value="Save" >')
                    __stream_140141461452976 = []
                    __append_140141461452976 = __stream_140141461452976.append
                    __append_140141461452976('Apply changes')
                    __msgid_140141461452976 = __re_whitespace(''.join(__stream_140141461452976)).strip()
                    if 'label_apply_changes':
                        __append(translate('label_apply_changes', mapping=None, default=__msgid_140141461452976, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                    __append('</button>\n            </div>\n          </div>')
                __append('\n\n          ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462775792
                __attrs_140141462775792 = _static_140141533420656

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461453840
                __default_140141461453840 = _DEFAULT_MARKER

                # <Value 'context/@@authenticator/authenticator' (222:40)> -> __cache_140141461451728
                __token = 11096
                try:
                    __zt_tmp = __attrs_140141462775792
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140141461451728 = _static_140141533071728('path', 'context/@@authenticator/authenticator', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                # <BinOp left=<Value 'context/@@authenticator/authenticator' (222:40)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a073ee0> -> __condition
                __expression = __cache_140141461451728

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input />')
                else:
                    __content = __cache_140141461451728
                    __content = __convert(__content)
                    if (__content is not None):
                        __append(__content)
                __append('\n\n        </form>')
                if (__backup_many_users_140141462676288 is __marker):
                    del econtext['many_users']
                else:
                    econtext['many_users'] = __backup_many_users_140141462676288
                if (__backup_batchformkeys_140141462380704 is __marker):
                    del econtext['batchformkeys']
                else:
                    econtext['batchformkeys'] = __backup_batchformkeys_140141462380704
                if (__backup_batch_140141461550608 is __marker):
                    del econtext['batch']
                else:
                    econtext['batch'] = __backup_batch_140141461550608
                if (__backup_portal_users_140141461550896 is __marker):
                    del econtext['portal_users']
                else:
                    econtext['portal_users'] = __backup_portal_users_140141461550896
                if (__backup_findAll_140141461550752 is __marker):
                    del econtext['findAll']
                else:
                    econtext['findAll'] = __backup_findAll_140141461550752
                __append('\n      </div>\n    </div>\n\n  </article>\n\n')
                if (__backup_portal_url_140141461552432 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_140141461552432
                if (__backup_portal_roles_140141462184144 is __marker):
                    del econtext['portal_roles']
                else:
                    econtext['portal_roles'] = __backup_portal_roles_140141462184144
                if (__backup_b_size_140141462184288 is __marker):
                    del econtext['b_size']
                else:
                    econtext['b_size'] = __backup_b_size_140141462184288
                if (__backup_b_start_140141462187744 is __marker):
                    del econtext['b_start']
                else:
                    econtext['b_start'] = __backup_b_start_140141462187744
                if (__backup_Batch_140141462187552 is __marker):
                    del econtext['Batch']
                else:
                    econtext['Batch'] = __backup_Batch_140141462187552
                if (__backup_showAll_140141462187936 is __marker):
                    del econtext['showAll']
                else:
                    econtext['showAll'] = __backup_showAll_140141462187936
                if (__backup_template_id_140141462184336 is __marker):
                    del econtext['template_id']
                else:
                    econtext['template_id'] = __backup_template_id_140141462184336
            _slots = econtext['__slot_prefs_configlet_main'] = _deque((__fill_prefs_configlet_main, ))

            # <Value 'context/prefs_main_template/macros/master' (6:23)> -> __macro
            __token = 261
            try:
                __zt_tmp = __attrs_140141462354288
            except get('NameError', NameError):
                __zt_tmp = None

            __macro = _static_140141533071728('path', 'context/prefs_main_template/macros/master', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            __token = 261
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_140141512771904 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_140141512771904
            __i18n_domain = __previous_i18n_domain_140141462353328
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }