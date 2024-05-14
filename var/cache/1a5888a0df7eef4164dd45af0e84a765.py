# -*- coding: utf-8 -*-
__filename = 'manage_users'

__tokens = {27: ('here/manage_page_header', 1, 27), 92: ('string:ZODB Users', 3, 27), 138: ('here/manage_tabs', 4, 27), 224: ('request/adding | nothing', 7, 25), 274: (" python: not adding and request.get('user_id')\n                                            and request.get('passwd'", 8, 24), 417: ("g python: not adding and not passwd\n                                             and request.get('user_id", 10, 25), 550: ('ng python: not adding and not passwd\n                               and not updat', 12, 24), 679: ('browsing', 16, 22), 879: ('context/@@csrf_token/token', 22, 32), 1292: ('here/listUserInfo', 36, 28), 1454: ('info/user_id', 40, 39), 1646: ('string:?user_id=${info/user_id}', 47, 34), 1705: ('info/user_id', 48, 26), 1849: ('string:?user_id=${info/user_id}&amp;pass', 53, 33), 1992: ('info/login_name', 57, 47), 2403: ('adding', 75, 22), 2439: ("request/user_id | python:''", 76, 27), 2497: (" request/login_name | python:'", 77, 29), 2696: ('context/@@csrf_token/token', 84, 31), 2974: ('here/manage_widgets/macros/authentication_widgets', 97, 27), 2974: ('here/manage_widgets/macros/authentication_widgets', 97, 27), 3203: ('passwd', 109, 22), 3239: ('request/user_id', 110, 27), 3279: (' python:here.getUserInfo( user_id ', 111, 23), 3344: ('e info/login_na', 112, 28), 3488: ('string:?user_id=${user_id}', 116, 52), 3699: ('context/@@csrf_token/token', 121, 31), 3940: ('user_id', 130, 34), 3994: ('user_id', 131, 42), 4165: ('login_name', 140, 45), 4791: ('updating', 173, 22), 4829: ('request/user_id', 174, 27), 4869: (' python:here.getUserInfo(user_id', 175, 23), 4932: ('e info/login_na', 176, 28), 5073: ('string:?user_id=${user_id}&amp;pass', 180, 43), 5284: ('context/@@csrf_token/token', 185, 31), 5525: ('user_id', 194, 34), 5579: ('user_id', 195, 42), 5812: ('login_name', 205, 34), 6043: ('here/manage_page_footer', 222, 27)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140141461552288 = {'type': 'submit', 'value': ' Update User ', 'class': 'btn btn-primary', }
_static_140141462163264 = {'class': 'form-controls', }
_static_140141462160960 = {'type': 'text', 'name': 'login_name', 'size': '40', 'class': 'form-control', 'value': 'login_name', }
_static_140141600654336 = {'class': 'form-label', }
_static_140141461865232 = {'class': 'form-label', }
_static_140141462124432 = {'type': 'hidden', 'name': 'user_id', 'class': 'form-control', 'value': 'user_id', }
_static_140141461647760 = {'class': 'form-label', }
_static_140141461663808 = {'class': 'table table-sm', }
_static_140141461955776 = {'type': 'hidden', 'name': 'csrf_token', 'value': 'context/@@csrf_token/token', }
_static_140141461291408 = {'action': 'manage_updateUser', 'method': 'POST', }
_static_140141461293184 = {'href': '?user_id=XXX&amp;passwd=1', }
_static_140141462137200 = {'type': 'submit', 'value': ' Update Password ', 'class': 'btn btn-primary', }
_static_140141462006560 = {'class': 'form-controls', }
_static_140141462005648 = {'type': 'password', 'name': 'confirm', 'size': '20', 'value': 'confirm', 'class': 'form-control', }
_static_140141461896880 = {'class': 'form-label', }
_static_140141461987440 = {'type': 'password', 'name': 'password', 'size': '20', 'value': 'password', 'class': 'form-control', }
_static_140141461853616 = {'class': 'form-label', }
_static_140141461855968 = {'class': 'form-control', }
_static_140141462059088 = {'class': 'form-label', }
_static_140141461783024 = {'class': 'form-label', }
_static_140141461885856 = {'type': 'hidden', 'name': 'user_id', 'class': 'form-control', 'value': 'user_id', }
_static_140141461791312 = {'class': 'form-label', }
_static_140141461762928 = {'class': 'table table-sm', }
_static_140141461765952 = {'type': 'hidden', 'name': 'csrf_token', 'value': 'context/@@csrf_token/token', }
_static_140141452399664 = {'action': 'manage_updateUserPassword', 'method': 'POST', }
_static_140141461771984 = {'href': '?user_id=XXX', }
_static_140141462322096 = {'type': 'submit', 'value': ' Add User ', 'class': 'btn btn-primary', }
_static_140141462064624 = {'class': 'form-controls', }
_static_140141462061168 = 'authentication_widgets'
_static_140141462428880 = {'type': 'text', 'name': 'user_id', 'size': '20', 'class': 'form-control', }
_static_140141462340464 = {'class': 'form-label', }
_static_140141462342960 = {'scope': 'row', }
_static_140141461697440 = {'class': 'table table-sm', }
_static_140141461698064 = {'type': 'hidden', 'name': 'csrf_token', 'value': 'context/@@csrf_token/token', }
_static_140141462209200 = {'action': 'manage_addUser', 'method': 'POST', }
_static_140141462306240 = {'type': 'submit', 'name': 'manage_removeUsers:method', 'class': 'btn btn-primary zmi-patch', 'value': ' Remove Users ', }
_static_140141462303360 = {'type': 'hidden', 'name': 'user_ids:list:default', 'value': '', }
_static_140141461972880 = {'class': 'form-group zmi-controls', }
_static_140141462803888 = {'class': 'form-text', }
_static_140141461974416 = {'href': '?passwd=1', 'class': 'form-text', }
_static_140141462226784 = {'href': '?user_id=foo', 'class': 'form-text', }
_static_140141461373472 = {'class': 'far fa-user', }
_static_140141461372992 = {'type': 'checkbox', 'name': 'user_ids:list', 'value': 'info/user_id', }
_static_140141461295312 = {'class': 'text-right', }
_static_140141452390608 = {'scope': 'col', }
_static_140141452393968 = {'scope': 'col', }
_static_140141452392144 = {'scope': 'col', }
_static_140141462797184 = {'scope': 'col', 'style': 'width:2em', }
_static_140141462797760 = {'class': 'text-right', 'scope': 'col', 'style': 'width:2em', }
_static_140141461362720 = {'class': 'table table-sm table-striped table-hover', }
_static_140141461978176 = {'type': 'hidden', 'name': 'csrf_token', 'value': 'context/@@csrf_token/token', }
_static_140141461928880 = {'action': '.', 'method': 'POST', 'id': 'users', }
_static_140141461929120 = {'href': '?adding=1', }
_static_140141461524048 = {'class': 'container-fluid', }
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

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461847536
            __attrs_140141461847536 = _static_140141533420656

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461847440
            __default_140141461847440 = _DEFAULT_MARKER

            # <Value 'here/manage_page_header' (1:27)> -> __cache_140141461847776
            __token = 27
            try:
                __zt_tmp = __attrs_140141461847536
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141461847776 = _static_140141533071728('path', 'here/manage_page_header', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_header' (1:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0d38b0> -> __condition
            __expression = __cache_140141461847776

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Header</h1>')
            else:
                __content = __cache_140141461847776
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462105680
            __attrs_140141462105680 = _static_140141533420656
            __backup_form_title_140141461844608 = get('form_title', __marker)

            # <Value 'string:ZODB Users' (3:27)> -> __value
            __token = 92
            try:
                __zt_tmp = __attrs_140141462105680
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('string', 'ZODB Users', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['form_title'] = __value

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462105152
            __default_140141462105152 = _DEFAULT_MARKER

            # <Value 'here/manage_tabs' (4:27)> -> __cache_140141462102128
            __token = 138
            try:
                __zt_tmp = __attrs_140141462105680
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141462102128 = _static_140141533071728('path', 'here/manage_tabs', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_tabs' (4:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a112760> -> __condition
            __expression = __cache_140141462102128

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h2 ... (0:0)
                # --------------------------------------------------------
                __append('<h2> TABS </h2>')
            else:
                __content = __cache_140141462102128
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            if (__backup_form_title_140141461844608 is __marker):
                del econtext['form_title']
            else:
                econtext['form_title'] = __backup_form_title_140141461844608
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f753a084e50> name=None at 7f753a084c40> -> __attrs_140141461524240
            __attrs_140141461524240 = _static_140141461524048
            __backup_adding_140141461846288 = get('adding', __marker)

            # <Value 'request/adding | nothing' (7:25)> -> __value
            __token = 224
            try:
                __zt_tmp = __attrs_140141461524240
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('path', 'request/adding | nothing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['adding'] = __value
            __backup_passwd_140141461845664 = get('passwd', __marker)

            # <Value "python: not adding and request.get('user_id')\n                                            and request.get('passwd')" (8:24)> -> __value
            __token = 274
            try:
                __zt_tmp = __attrs_140141461524240
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('python', " not adding and request.get('user_id')\n                                            and request.get('passwd')", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['passwd'] = __value
            __backup_updating_140141462105584 = get('updating', __marker)

            # <Value "python: not adding and not passwd\n                                             and request.get('user_id')" (10:25)> -> __value
            __token = 417
            try:
                __zt_tmp = __attrs_140141461524240
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('python', " not adding and not passwd\n                                             and request.get('user_id')", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['updating'] = __value
            __backup_browsing_140141461521984 = get('browsing', __marker)

            # <Value 'python: not adding and not passwd\n                               and not updating' (12:24)> -> __value
            __token = 550
            try:
                __zt_tmp = __attrs_140141461524240
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140141533071728('python', ' not adding and not passwd\n                               and not updating', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            econtext['browsing'] = __value

            # <main ... (0:0)
            # --------------------------------------------------------
            __append('<main class="container-fluid">\n\n  ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461929216
            __attrs_140141461929216 = _static_140141533420656

            # <Value 'browsing' (16:22)> -> __condition
            __token = 679
            try:
                __zt_tmp = __attrs_140141461929216
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140141533071728('path', 'browsing', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461928928
                __attrs_140141461928928 = _static_140141533420656

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3> Current Users ')

                # <Static value=<ast.Dict object at 0x7f753a0e7ca0> name=None at 7f753a0e7e20> -> __attrs_140141461926096
                __attrs_140141461926096 = _static_140141461929120

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a href="?adding=1">(Add a user)</a></h3>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f753a0e7bb0> name=None at 7f753a0e7f40> -> __attrs_140141461975104
                __attrs_140141461975104 = _static_140141461928880

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form action="." method="POST" id="users">\n    ')

                # <Static value=<ast.Dict object at 0x7f753a0f3c40> name=None at 7f753a0f32b0> -> __attrs_140141461360848
                __attrs_140141461360848 = _static_140141461978176

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="csrf_token"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461975776
                __default_140141461975776 = _DEFAULT_MARKER

                # <Substitution 'context/@@csrf_token/token' (22:32)> -> __attr_value
                __token = 879
                try:
                    __zt_tmp = __attrs_140141461360848
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'context/@@csrf_token/token', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n\n    ')

                # <Static value=<ast.Dict object at 0x7f753a05d820> name=None at 7f753a05d850> -> __attrs_140141461362960
                __attrs_140141461362960 = _static_140141461362720

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-sm table-striped table-hover">\n     ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461361952
                __attrs_140141461361952 = _static_140141533420656

                # <thead ... (0:0)
                # --------------------------------------------------------
                __append('<thead>\n       ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461362240
                __attrs_140141461362240 = _static_140141533420656

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n        ')

                # <Static value=<ast.Dict object at 0x7f753a1bbdc0> name=None at 7f753a1bb3a0> -> __attrs_140141462796368
                __attrs_140141462796368 = _static_140141462797760

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th class="text-right" scope="col" style="width:2em"></th>\n        ')

                # <Static value=<ast.Dict object at 0x7f753a1bbb80> name=None at 7f753a1bb460> -> __attrs_140141462797664
                __attrs_140141462797664 = _static_140141462797184

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="col" style="width:2em"></th>\n        ')

                # <Static value=<ast.Dict object at 0x7f75397cf6d0> name=None at 7f75397cf820> -> __attrs_140141452393056
                __attrs_140141452393056 = _static_140141452392144

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="col"> User ID </th>\n        ')

                # <Static value=<ast.Dict object at 0x7f75397cfdf0> name=None at 7f75397cfca0> -> __attrs_140141452390560
                __attrs_140141452390560 = _static_140141452393968

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="col"></th>\n        ')

                # <Static value=<ast.Dict object at 0x7f75397cf0d0> name=None at 7f75397cfd30> -> __attrs_140141599842064
                __attrs_140141599842064 = _static_140141452390608

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="col"> Login Name </th>\n       </tr>\n     </thead>\n\n     ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461298048
                __attrs_140141461298048 = _static_140141533420656

                # <tbody ... (0:0)
                # --------------------------------------------------------
                __append('<tbody>\n       ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461296272
                __attrs_140141461296272 = _static_140141533420656
                __backup_info_140141461926720 = get('info', __marker)

                # <Value 'here/listUserInfo' (36:28)> -> __iterator
                __token = 1292
                try:
                    __zt_tmp = __attrs_140141461296272
                except get('NameError', NameError):
                    __zt_tmp = None

                __iterator = _static_140141533071728('path', 'here/listUserInfo', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                (__iterator, ____index_140141461297328, ) = getname('repeat')('info', __iterator)
                econtext['info'] = None
                for __item in __iterator:
                    econtext['info'] = __item

                    # <tr ... (0:0)
                    # --------------------------------------------------------
                    __append('<tr>\n        ')

                    # <Static value=<ast.Dict object at 0x7f753a04d0d0> name=None at 7f753a04dac0> -> __attrs_140141461298960
                    __attrs_140141461298960 = _static_140141461295312

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td class="text-right">\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a060040> name=None at 7f753a0608e0> -> __attrs_140141461374288
                    __attrs_140141461374288 = _static_140141461372992

                    # <input ... (0:0)
                    # --------------------------------------------------------
                    __append('<input type="checkbox" name="user_ids:list"')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461376496
                    __default_140141461376496 = _DEFAULT_MARKER

                    # <Substitution 'info/user_id' (40:39)> -> __attr_value
                    __token = 1454
                    try:
                        __zt_tmp = __attrs_140141461374288
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_value = _static_140141533071728('path', 'info/user_id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                    if (__attr_value is not None):
                        __append((' value="%s"' % __attr_value))
                    __append(' />\n        </td>\n        ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461374096
                    __attrs_140141461374096 = _static_140141533420656

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a060220> name=None at 7f753a060160> -> __attrs_140141461376688
                    __attrs_140141461376688 = _static_140141461373472

                    # <i ... (0:0)
                    # --------------------------------------------------------
                    __append('<i class="far fa-user" />\n        </td>\n        ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462228368
                    __attrs_140141462228368 = _static_140141533420656

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a130760> name=None at 7f753a130190> -> __attrs_140141462228416
                    __attrs_140141462228416 = _static_140141462226784

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462227552
                    __default_140141462227552 = _DEFAULT_MARKER

                    # <Substitution 'string:?user_id=${info/user_id}' (47:34)> -> __attr_href
                    __token = 1646
                    try:
                        __zt_tmp = __attrs_140141462228416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140141533071728('string', '?user_id=${info/user_id}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?user_id=foo', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' class="form-text" >')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462225056
                    __default_140141462225056 = _DEFAULT_MARKER

                    # <Value 'info/user_id' (48:26)> -> __cache_140141462225152
                    __token = 1705
                    try:
                        __zt_tmp = __attrs_140141462228416
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141462225152 = _static_140141533071728('path', 'info/user_id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'info/user_id' (48:26)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1305e0> -> __condition
                    __expression = __cache_140141462225152

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('USER_ID')
                    else:
                        __content = __cache_140141462225152
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</a>\n        </td>\n        ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461973840
                    __attrs_140141461973840 = _static_140141533420656

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n         ')

                    # <Static value=<ast.Dict object at 0x7f753a0f2d90> name=None at 7f753a0f2370> -> __attrs_140141461973312
                    __attrs_140141461973312 = _static_140141461974416

                    # <a ... (0:0)
                    # --------------------------------------------------------
                    __append('<a')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461974560
                    __default_140141461974560 = _DEFAULT_MARKER

                    # <Substitution 'string:?user_id=${info/user_id}&passwd=1' (53:33)> -> __attr_href
                    __token = 1849
                    try:
                        __zt_tmp = __attrs_140141461973312
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __attr_href = _static_140141533071728('string', '?user_id=${info/user_id}&passwd=1', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                    __attr_href = __quote(__attr_href, '"', '&quot;', '?passwd=1', _DEFAULT_MARKER)
                    if (__attr_href is not None):
                        __append((' href="%s"' % __attr_href))
                    __append(' class="form-text" >Password</a>\n        </td>\n        ')

                    # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461974176
                    __attrs_140141461974176 = _static_140141533420656

                    # <td ... (0:0)
                    # --------------------------------------------------------
                    __append('<td>\n          ')

                    # <Static value=<ast.Dict object at 0x7f753a1bd5b0> name=None at 7f753a1bde50> -> __attrs_140141462803024
                    __attrs_140141462803024 = _static_140141462803888

                    # <span ... (0:0)
                    # --------------------------------------------------------
                    __append('<span class="form-text">')

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462805328
                    __default_140141462805328 = _DEFAULT_MARKER

                    # <Value 'info/login_name' (57:47)> -> __cache_140141462806000
                    __token = 1992
                    try:
                        __zt_tmp = __attrs_140141462803024
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __cache_140141462806000 = _static_140141533071728('path', 'info/login_name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                    # <BinOp left=<Value 'info/login_name' (57:47)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a1bd7f0> -> __condition
                    __expression = __cache_140141462806000

                    # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                    __value = _DEFAULT_MARKER
                    __condition = (__expression is __value)
                    if __condition:
                        __append('\n            LOGIN_NAME\n          ')
                    else:
                        __content = __cache_140141462806000
                        __content = __quote(__content, None, '\xad', None, None)
                        if (__content is not None):
                            __append(__content)
                    __append('</span>\n        </td>\n       </tr>')
                    ____index_140141461297328 -= 1
                    if (____index_140141461297328 > 0):
                        __append('\n       ')
                if (__backup_info_140141461926720 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_140141461926720
                __append('\n\n    </tbody>\n    </table>\n\n    ')

                # <Static value=<ast.Dict object at 0x7f753a0f2790> name=None at 7f753a04d160> -> __attrs_140141462306048
                __attrs_140141462306048 = _static_140141461972880

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-group zmi-controls">\n      ')

                # <Static value=<ast.Dict object at 0x7f753a143280> name=None at 7f753a1432b0> -> __attrs_140141462303792
                __attrs_140141462303792 = _static_140141462303360

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="user_ids:list:default" value="" />\n      ')

                # <Static value=<ast.Dict object at 0x7f753a143dc0> name=None at 7f753a143100> -> __attrs_140141461310768
                __attrs_140141461310768 = _static_140141462306240

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="submit" name="manage_removeUsers:method" class="btn btn-primary zmi-patch" value=" Remove Users " />\n    </div>\n  </form>\n\n  </div>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461309088
            __attrs_140141461309088 = _static_140141533420656

            # <Value 'adding' (75:22)> -> __condition
            __token = 2403
            try:
                __zt_tmp = __attrs_140141461309088
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140141533071728('path', 'adding', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n  ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461307456
                __attrs_140141461307456 = _static_140141533420656
                __backup_user_id_140141461522608 = get('user_id', __marker)

                # <Value "request/user_id | python:''" (76:27)> -> __value
                __token = 2439
                try:
                    __zt_tmp = __attrs_140141461307456
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', "request/user_id | python:''", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['user_id'] = __value
                __backup_login_name_140141461928016 = get('login_name', __marker)

                # <Value "request/login_name | python:''" (77:29)> -> __value
                __token = 2497
                try:
                    __zt_tmp = __attrs_140141461307456
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', "request/login_name | python:''", econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['login_name'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462211648
                __attrs_140141462211648 = _static_140141533420656

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3> Add a User </h3>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f753a12c2b0> name=None at 7f753a12c5e0> -> __attrs_140141462211264
                __attrs_140141462211264 = _static_140141462209200

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form action="manage_addUser" method="POST">\n  ')

                # <Static value=<ast.Dict object at 0x7f753a0af610> name=None at 7f753a12cdc0> -> __attrs_140141461697968
                __attrs_140141461697968 = _static_140141461698064

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="csrf_token"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461696720
                __default_140141461696720 = _DEFAULT_MARKER

                # <Substitution 'context/@@csrf_token/token' (84:31)> -> __attr_value
                __token = 2696
                try:
                    __zt_tmp = __attrs_140141461697968
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'context/@@csrf_token/token', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n\n  ')

                # <Static value=<ast.Dict object at 0x7f753a0af3a0> name=None at 7f753a0aff70> -> __attrs_140141461700176
                __attrs_140141461700176 = _static_140141461697440

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-sm">\n\n   ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462340416
                __attrs_140141462340416 = _static_140141533420656

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x7f753a14cd30> name=None at 7f753a14c820> -> __attrs_140141462340944
                __attrs_140141462340944 = _static_140141462342960

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th scope="row">\n     ')

                # <Static value=<ast.Dict object at 0x7f753a14c370> name=None at 7f753a14c580> -> __attrs_140141532724960
                __attrs_140141532724960 = _static_140141462340464

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">User ID:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462429648
                __attrs_140141462429648 = _static_140141533420656

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n     ')

                # <Static value=<ast.Dict object at 0x7f753a161cd0> name=None at 7f753a161d30> -> __attrs_140141462061456
                __attrs_140141462061456 = _static_140141462428880

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="text" name="user_id" size="20" class="form-control" />\n    </td>\n   </tr>\n\n   ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462061360
                __attrs_140141462061360 = _static_140141533420656
                __backup_macroname_140141486334144 = get('macroname', __marker)

                # <Static value=<ast.Constant object at 0x7f753a108070> name=None at 7f753a108f10> -> __value
                __value = _static_140141462061168
                econtext['macroname'] = __value

                # <Value 'here/manage_widgets/macros/authentication_widgets' (97:27)> -> __macro
                __token = 2974
                try:
                    __zt_tmp = __attrs_140141462061360
                except get('NameError', NameError):
                    __zt_tmp = None

                __macro = _static_140141533071728('path', 'here/manage_widgets/macros/authentication_widgets', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __token = 2974
                __m = __macro.include
                __m(__stream, econtext.copy(), rcontext, __i18n_domain)
                econtext.update(rcontext)
                if (__backup_macroname_140141486334144 is __marker):
                    del econtext['macroname']
                else:
                    econtext['macroname'] = __backup_macroname_140141486334144
                __append('\n\n  </table>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f753a108df0> name=None at 7f753a1083d0> -> __attrs_140141462063232
                __attrs_140141462063232 = _static_140141462064624

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-controls">\n    ')

                # <Static value=<ast.Dict object at 0x7f753a147bb0> name=None at 7f753a1479a0> -> __attrs_140141462319696
                __attrs_140141462319696 = _static_140141462322096

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="submit" value=" Add User " class="btn btn-primary" />\n  </div>\n  </form>\n\n  </div>')
                if (__backup_login_name_140141461928016 is __marker):
                    del econtext['login_name']
                else:
                    econtext['login_name'] = __backup_login_name_140141461928016
                if (__backup_user_id_140141461522608 is __marker):
                    del econtext['user_id']
                else:
                    econtext['user_id'] = __backup_user_id_140141461522608
                __append('\n  </div>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462320080
            __attrs_140141462320080 = _static_140141533420656

            # <Value 'passwd' (109:22)> -> __condition
            __token = 3203
            try:
                __zt_tmp = __attrs_140141462320080
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140141533071728('path', 'passwd', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n  ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462323008
                __attrs_140141462323008 = _static_140141533420656
                __backup_user_id_140141461928784 = get('user_id', __marker)

                # <Value 'request/user_id' (110:27)> -> __value
                __token = 3239
                try:
                    __zt_tmp = __attrs_140141462323008
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'request/user_id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['user_id'] = __value
                __backup_info_140141461927008 = get('info', __marker)

                # <Value 'python:here.getUserInfo( user_id )' (111:23)> -> __value
                __token = 3279
                try:
                    __zt_tmp = __attrs_140141462323008
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', 'here.getUserInfo( user_id )', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['info'] = __value
                __backup_login_name_140141461364400 = get('login_name', __marker)

                # <Value 'info/login_name' (112:28)> -> __value
                __token = 3344
                try:
                    __zt_tmp = __attrs_140141462323008
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'info/login_name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['login_name'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461773328
                __attrs_140141461773328 = _static_140141533420656

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3> Update User Password ')

                # <Static value=<ast.Dict object at 0x7f753a0c16d0> name=None at 7f753a0c1250> -> __attrs_140141461773808
                __attrs_140141461773808 = _static_140141461771984

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461772272
                __default_140141461772272 = _DEFAULT_MARKER

                # <Substitution 'string:?user_id=${user_id}' (116:52)> -> __attr_href
                __token = 3488
                try:
                    __zt_tmp = __attrs_140141461773808
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140141533071728('string', '?user_id=${user_id}', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '?user_id=XXX', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >(update user)</a></h3>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f75397d1430> name=None at 7f75397d1f70> -> __attrs_140141461765568
                __attrs_140141461765568 = _static_140141452399664

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form action="manage_updateUserPassword" method="POST">\n  ')

                # <Static value=<ast.Dict object at 0x7f753a0bff40> name=None at 7f753a0bf9d0> -> __attrs_140141461763840
                __attrs_140141461763840 = _static_140141461765952

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="csrf_token"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461764128
                __default_140141461764128 = _DEFAULT_MARKER

                # <Substitution 'context/@@csrf_token/token' (121:31)> -> __attr_value
                __token = 3699
                try:
                    __zt_tmp = __attrs_140141461763840
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'context/@@csrf_token/token', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n  ')

                # <Static value=<ast.Dict object at 0x7f753a0bf370> name=None at 7f753a0bfe50> -> __attrs_140141461793664
                __attrs_140141461793664 = _static_140141461762928

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-sm">\n\n   ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461792752
                __attrs_140141461792752 = _static_140141533420656

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461791168
                __attrs_140141461791168 = _static_140141533420656

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>\n     ')

                # <Static value=<ast.Dict object at 0x7f753a0c6250> name=None at 7f753a0c6670> -> __attrs_140141461888832
                __attrs_140141461888832 = _static_140141461791312

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">User ID:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461888016
                __attrs_140141461888016 = _static_140141533420656

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n     ')

                # <Static value=<ast.Dict object at 0x7f753a0dd3a0> name=None at 7f753a0dd760> -> __attrs_140141461886096
                __attrs_140141461886096 = _static_140141461885856

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="user_id" class="form-control"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461885472
                __default_140141461885472 = _DEFAULT_MARKER

                # <Substitution 'user_id' (130:34)> -> __attr_value
                __token = 3940
                try:
                    __zt_tmp = __attrs_140141461886096
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'user_id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n     ')

                # <Static value=<ast.Dict object at 0x7f753a0c41f0> name=None at 7f753a0c4be0> -> __attrs_140141461786432
                __attrs_140141461786432 = _static_140141461783024

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461786384
                __default_140141461786384 = _DEFAULT_MARKER

                # <Value 'user_id' (131:42)> -> __cache_140141461784320
                __token = 3994
                try:
                    __zt_tmp = __attrs_140141461786432
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140141461784320 = _static_140141533071728('path', 'user_id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                # <BinOp left=<Value 'user_id' (131:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a0c4730> -> __condition
                __expression = __cache_140141461784320

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('USER_ID')
                else:
                    __content = __cache_140141461784320
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n    </td>\n   </tr>\n\n   ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461784128
                __attrs_140141461784128 = _static_140141533420656

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462060960
                __attrs_140141462060960 = _static_140141533420656

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>\n     ')

                # <Static value=<ast.Dict object at 0x7f753a107850> name=None at 7f753a107c40> -> __attrs_140141462059712
                __attrs_140141462059712 = _static_140141462059088

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">Login name:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462057840
                __attrs_140141462057840 = _static_140141533420656

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n      ')

                # <Static value=<ast.Dict object at 0x7f753a0d5ee0> name=None at 7f753a0d5dc0> -> __attrs_140141461854720
                __attrs_140141461854720 = _static_140141461855968

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-control">')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461854288
                __default_140141461854288 = _DEFAULT_MARKER

                # <Value 'login_name' (140:45)> -> __cache_140141462060288
                __token = 4165
                try:
                    __zt_tmp = __attrs_140141461854720
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140141462060288 = _static_140141533071728('path', 'login_name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                # <BinOp left=<Value 'login_name' (140:45)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a107ee0> -> __condition
                __expression = __cache_140141462060288

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append(' Login ')
                else:
                    __content = __cache_140141462060288
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n    </td>\n   </tr>\n\n   ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461855392
                __attrs_140141461855392 = _static_140141533420656

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461855104
                __attrs_140141461855104 = _static_140141533420656

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>\n     ')

                # <Static value=<ast.Dict object at 0x7f753a0d55b0> name=None at 7f753a0d5df0> -> __attrs_140141461990032
                __attrs_140141461990032 = _static_140141461853616

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">Password:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461990704
                __attrs_140141461990704 = _static_140141533420656

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n     ')

                # <Static value=<ast.Dict object at 0x7f753a0f6070> name=None at 7f753a0f62b0> -> __attrs_140141461897168
                __attrs_140141461897168 = _static_140141461987440

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="password" name="password" size="20" value="password" class="form-control" />\n    </td>\n   </tr>\n\n   ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461895632
                __attrs_140141461895632 = _static_140141533420656

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461893184
                __attrs_140141461893184 = _static_140141533420656

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>\n     ')

                # <Static value=<ast.Dict object at 0x7f753a0dfeb0> name=None at 7f753a0df7f0> -> __attrs_140141461897120
                __attrs_140141461897120 = _static_140141461896880

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">Confirm password:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462006944
                __attrs_140141462006944 = _static_140141533420656

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n     ')

                # <Static value=<ast.Dict object at 0x7f753a0fa790> name=None at 7f753a0fa3d0> -> __attrs_140141462005504
                __attrs_140141462005504 = _static_140141462005648

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="password" name="confirm" size="20" value="confirm" class="form-control" />\n    </td>\n   </tr>\n\n\n  </table>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f753a0fab20> name=None at 7f753a0fa400> -> __attrs_140141462137872
                __attrs_140141462137872 = _static_140141462006560

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-controls">\n    ')

                # <Static value=<ast.Dict object at 0x7f753a11a970> name=None at 7f753a11a460> -> __attrs_140141462135328
                __attrs_140141462135328 = _static_140141462137200

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="submit" value=" Update Password " class="btn btn-primary" />\n  </div>\n  </form>\n\n  </div>')
                if (__backup_login_name_140141461364400 is __marker):
                    del econtext['login_name']
                else:
                    econtext['login_name'] = __backup_login_name_140141461364400
                if (__backup_info_140141461927008 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_140141461927008
                if (__backup_user_id_140141461928784 is __marker):
                    del econtext['user_id']
                else:
                    econtext['user_id'] = __backup_user_id_140141461928784
                __append('\n  </div>')
            __append('\n\n  ')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462138256
            __attrs_140141462138256 = _static_140141533420656

            # <Value 'updating' (173:22)> -> __condition
            __token = 4791
            try:
                __zt_tmp = __attrs_140141462138256
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140141533071728('path', 'updating', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
            if __condition:

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div>\n  ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462114608
                __attrs_140141462114608 = _static_140141533420656
                __backup_user_id_140141462797952 = get('user_id', __marker)

                # <Value 'request/user_id' (174:27)> -> __value
                __token = 4829
                try:
                    __zt_tmp = __attrs_140141462114608
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'request/user_id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['user_id'] = __value
                __backup_info_140141452392288 = get('info', __marker)

                # <Value 'python:here.getUserInfo(user_id)' (175:23)> -> __value
                __token = 4869
                try:
                    __zt_tmp = __attrs_140141462114608
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('python', 'here.getUserInfo(user_id)', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['info'] = __value
                __backup_login_name_140141461296128 = get('login_name', __marker)

                # <Value 'info/login_name' (176:28)> -> __value
                __token = 4932
                try:
                    __zt_tmp = __attrs_140141462114608
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140141533071728('path', 'info/login_name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                econtext['login_name'] = __value

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div >\n  ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462115328
                __attrs_140141462115328 = _static_140141533420656

                # <h3 ... (0:0)
                # --------------------------------------------------------
                __append('<h3> Update User ')

                # <Static value=<ast.Dict object at 0x7f753a04c880> name=None at 7f753a04c250> -> __attrs_140141461291936
                __attrs_140141461291936 = _static_140141461293184

                # <a ... (0:0)
                # --------------------------------------------------------
                __append('<a')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461294816
                __default_140141461294816 = _DEFAULT_MARKER

                # <Substitution 'string:?user_id=${user_id}&passwd=1' (180:43)> -> __attr_href
                __token = 5073
                try:
                    __zt_tmp = __attrs_140141461291936
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_href = _static_140141533071728('string', '?user_id=${user_id}&passwd=1', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_href = __quote(__attr_href, '"', '&quot;', '?user_id=XXX&amp;passwd=1', _DEFAULT_MARKER)
                if (__attr_href is not None):
                    __append((' href="%s"' % __attr_href))
                __append(' >(change password)</a></h3>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f753a04c190> name=None at 7f753a04c820> -> __attrs_140141461956832
                __attrs_140141461956832 = _static_140141461291408

                # <form ... (0:0)
                # --------------------------------------------------------
                __append('<form action="manage_updateUser" method="POST">\n  ')

                # <Static value=<ast.Dict object at 0x7f753a0ee4c0> name=None at 7f753a0eeac0> -> __attrs_140141461664528
                __attrs_140141461664528 = _static_140141461955776

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="csrf_token"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461665392
                __default_140141461665392 = _DEFAULT_MARKER

                # <Substitution 'context/@@csrf_token/token' (185:31)> -> __attr_value
                __token = 5284
                try:
                    __zt_tmp = __attrs_140141461664528
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'context/@@csrf_token/token', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n  ')

                # <Static value=<ast.Dict object at 0x7f753a0a7040> name=None at 7f753a0a72b0> -> __attrs_140141461665296
                __attrs_140141461665296 = _static_140141461663808

                # <table ... (0:0)
                # --------------------------------------------------------
                __append('<table class="table table-sm">\n\n   ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461649488
                __attrs_140141461649488 = _static_140141533420656

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461650160
                __attrs_140141461650160 = _static_140141533420656

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>\n     ')

                # <Static value=<ast.Dict object at 0x7f753a0a3190> name=None at 7f753a0a3c70> -> __attrs_140141462122848
                __attrs_140141462122848 = _static_140141461647760

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">User ID:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462123424
                __attrs_140141462123424 = _static_140141533420656

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n     ')

                # <Static value=<ast.Dict object at 0x7f753a117790> name=None at 7f753a117430> -> __attrs_140141462123088
                __attrs_140141462123088 = _static_140141462124432

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="hidden" name="user_id" class="form-control"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462124720
                __default_140141462124720 = _DEFAULT_MARKER

                # <Substitution 'user_id' (194:34)> -> __attr_value
                __token = 5525
                try:
                    __zt_tmp = __attrs_140141462123088
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'user_id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n     ')

                # <Static value=<ast.Dict object at 0x7f753a0d8310> name=None at 7f753b858070> -> __attrs_140141461866816
                __attrs_140141461866816 = _static_140141461865232

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141486506960
                __default_140141486506960 = _DEFAULT_MARKER

                # <Value 'user_id' (195:42)> -> __cache_140141462122944
                __token = 5579
                try:
                    __zt_tmp = __attrs_140141461866816
                except get('NameError', NameError):
                    __zt_tmp = None

                __cache_140141462122944 = _static_140141533071728('path', 'user_id', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

                # <BinOp left=<Value 'user_id' (195:42)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a117a90> -> __condition
                __expression = __cache_140141462122944

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
                __value = _DEFAULT_MARKER
                __condition = (__expression is __value)
                if __condition:
                    __append('USER_ID')
                else:
                    __content = __cache_140141462122944
                    __content = __quote(__content, None, '\xad', None, None)
                    if (__content is not None):
                        __append(__content)
                __append('</div>\n    </td>\n   </tr>\n\n   ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461867728
                __attrs_140141461867728 = _static_140141533420656

                # <tr ... (0:0)
                # --------------------------------------------------------
                __append('<tr>\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461866240
                __attrs_140141461866240 = _static_140141533420656

                # <th ... (0:0)
                # --------------------------------------------------------
                __append('<th>\n     ')

                # <Static value=<ast.Dict object at 0x7f7542534400> name=None at 7f7542534460> -> __attrs_140141484386288
                __attrs_140141484386288 = _static_140141600654336

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-label">Login name:</div>\n    </th>\n    ')

                # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141462162400
                __attrs_140141462162400 = _static_140141533420656

                # <td ... (0:0)
                # --------------------------------------------------------
                __append('<td>\n     ')

                # <Static value=<ast.Dict object at 0x7f753a120640> name=None at 7f753a120610> -> __attrs_140141462161728
                __attrs_140141462161728 = _static_140141462160960

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="text" name="login_name" size="40" class="form-control"')

                # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141462163168
                __default_140141462163168 = _DEFAULT_MARKER

                # <Substitution 'login_name' (205:34)> -> __attr_value
                __token = 5812
                try:
                    __zt_tmp = __attrs_140141462161728
                except get('NameError', NameError):
                    __zt_tmp = None

                __attr_value = _static_140141533071728('path', 'login_name', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))
                __attr_value = __quote(__attr_value, '"', '&quot;', None, _DEFAULT_MARKER)
                if (__attr_value is not None):
                    __append((' value="%s"' % __attr_value))
                __append(' />\n    </td>\n   </tr>\n\n  </table>\n\n  ')

                # <Static value=<ast.Dict object at 0x7f753a120f40> name=None at 7f753a1203d0> -> __attrs_140141462608528
                __attrs_140141462608528 = _static_140141462163264

                # <div ... (0:0)
                # --------------------------------------------------------
                __append('<div class="form-controls">\n    ')

                # <Static value=<ast.Dict object at 0x7f753a08bca0> name=None at 7f753a08be20> -> __attrs_140141461550032
                __attrs_140141461550032 = _static_140141461552288

                # <input ... (0:0)
                # --------------------------------------------------------
                __append('<input type="submit" value=" Update User " class="btn btn-primary" />\n  </div>\n  </form>\n\n  </div>')
                if (__backup_login_name_140141461296128 is __marker):
                    del econtext['login_name']
                else:
                    econtext['login_name'] = __backup_login_name_140141461296128
                if (__backup_info_140141452392288 is __marker):
                    del econtext['info']
                else:
                    econtext['info'] = __backup_info_140141452392288
                if (__backup_user_id_140141462797952 is __marker):
                    del econtext['user_id']
                else:
                    econtext['user_id'] = __backup_user_id_140141462797952
                __append('\n  </div>')
            __append('\n\n</main>')
            if (__backup_browsing_140141461521984 is __marker):
                del econtext['browsing']
            else:
                econtext['browsing'] = __backup_browsing_140141461521984
            if (__backup_updating_140141462105584 is __marker):
                del econtext['updating']
            else:
                econtext['updating'] = __backup_updating_140141462105584
            if (__backup_passwd_140141461845664 is __marker):
                del econtext['passwd']
            else:
                econtext['passwd'] = __backup_passwd_140141461845664
            if (__backup_adding_140141461846288 is __marker):
                del econtext['adding']
            else:
                econtext['adding'] = __backup_adding_140141461846288
            __append('\n\n')

            # <Static value=<ast.Dict object at 0x7f753e515c70> name=None at 7f753e515cd0> -> __attrs_140141461552816
            __attrs_140141461552816 = _static_140141533420656

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __default_140141461552720
            __default_140141461552720 = _DEFAULT_MARKER

            # <Value 'here/manage_page_footer' (222:27)> -> __cache_140141461551184
            __token = 6043
            try:
                __zt_tmp = __attrs_140141461552816
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140141461551184 = _static_140141533071728('path', 'here/manage_page_footer', econtext=econtext)(_static_140141533071440(econtext, __zt_tmp))

            # <BinOp left=<Value 'here/manage_page_footer' (222:27)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7f753e5b3df0> at 7f753a08bf70> -> __condition
            __expression = __cache_140141461551184

            # <Symbol value=<DEFAULT> at 7f753e5b3df0> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:

                # <h1 ... (0:0)
                # --------------------------------------------------------
                __append('<h1>Footer</h1>')
            else:
                __content = __cache_140141461551184
                __content = __convert(__content)
                if (__content is not None):
                    __append(__content)
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }