# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/plone.app.layout-4.1.0-py3.9.egg/plone/app/layout/nextprevious/nextprevious.pt'

__tokens = {73: ('view/enabled|nothing', 3, 19), 120: (' view/isViewTemplate|nothin', 4, 25), 185: ('python:enabled and isViewTemplate', 6, 24), 300: ('view/site_url', 11, 26), 422: ('view/next', 16, 16), 452: (' view/previou', 17, 19), 503: ('python:previous is not None or next is not None', 19, 24), 696: ('previous', 24, 24), 748: ('previous/url', 26, 16), 1012: ('previous/title', 35, 29), 1240: ('next', 43, 24), 1288: ('next/url', 45, 16), 1500: ('next/title', 53, 29)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355448577088 = {'class': 'arrow', }
_static_140355448975520 = {'class': 'label', }
_static_140355449357792 = {'class': 'btn btn-sm btn-outline-secondary align-self-end next', 'title': 'Go to next item', 'href': 'next/url', }
_static_140355448530736 = {'class': 'label', }
_static_140355459606416 = {'class': 'arrow', }
_static_140355459396752 = {'class': 'btn btn-sm btn-outline-secondary align-self-start previous', 'title': 'Go to previous item', 'href': 'previous/url', }
_static_140355449423712 = {'class': 'pagination justify-content-between', }
_static_140355540704128 = {}
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355449027312 = {'id': 'section-next-prev', }

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

            # <Static value=<ast.Dict object at 0x7fa70cae7af0> name=None at 7fa70ca6c310> -> __attrs_140355449026160
            __attrs_140355449026160 = _static_140355449027312
            __backup_enabled_140355459448112 = get('enabled', __marker)

            # <Value 'view/enabled|nothing' (3:19)> -> __value
            __token = 73
            try:
                __zt_tmp = __attrs_140355449026160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/enabled|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['enabled'] = __value
            __backup_isViewTemplate_140355449107936 = get('isViewTemplate', __marker)

            # <Value 'view/isViewTemplate|nothing' (4:25)> -> __value
            __token = 120
            try:
                __zt_tmp = __attrs_140355449026160
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('path', 'view/isViewTemplate|nothing', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['isViewTemplate'] = __value

            # <Value 'python:enabled and isViewTemplate' (6:24)> -> __condition
            __token = 185
            try:
                __zt_tmp = __attrs_140355449026160
            except get('NameError', NameError):
                __zt_tmp = None

            __condition = _static_140355540363392('python', 'enabled and isViewTemplate', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            if __condition:
                __previous_i18n_domain_140355449423136 = __i18n_domain
                __i18n_domain = 'plone'

                # <section ... (0:0)
                # --------------------------------------------------------
                __append('<section id="section-next-prev" >\n\n  ')

                # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449424336
                __attrs_140355449424336 = _static_140355540704128
                __backup_portal_url_140355449422128 = get('portal_url', __marker)

                # <Value 'view/site_url' (11:26)> -> __value
                __token = 300
                try:
                    __zt_tmp = __attrs_140355449424336
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'view/site_url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['portal_url'] = __value
                __append('\n\n    ')

                # <Static value=<ast.Dict object at 0x7fa70cb48760> name=None at 7fa70cb48b50> -> __attrs_140355449639312
                __attrs_140355449639312 = _static_140355449423712
                __backup_next_140355449425680 = get('next', __marker)

                # <Value 'view/next' (16:16)> -> __value
                __token = 422
                try:
                    __zt_tmp = __attrs_140355449639312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'view/next', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['next'] = __value
                __backup_previous_140355449423328 = get('previous', __marker)

                # <Value 'view/previous' (17:19)> -> __value
                __token = 452
                try:
                    __zt_tmp = __attrs_140355449639312
                except get('NameError', NameError):
                    __zt_tmp = None

                __value = _static_140355540363392('path', 'view/previous', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                econtext['previous'] = __value

                # <Value 'python:previous is not None or next is not None' (19:24)> -> __condition
                __token = 503
                try:
                    __zt_tmp = __attrs_140355449639312
                except get('NameError', NameError):
                    __zt_tmp = None

                __condition = _static_140355540363392('python', 'previous is not None or next is not None', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                if __condition:

                    # <nav ... (0:0)
                    # --------------------------------------------------------
                    __append('<nav class="pagination justify-content-between" >\n\n      ')

                    # <Static value=<ast.Dict object at 0x7fa70d4cb490> name=None at 7fa70d4cb310> -> __attrs_140355459607952
                    __attrs_140355459607952 = _static_140355459396752

                    # <Value 'previous' (24:24)> -> __condition
                    __token = 696
                    try:
                        __zt_tmp = __attrs_140355459607952
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('path', 'previous', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-sm btn-outline-secondary align-self-start previous"')

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459607712
                        __default_140355459607712 = _DEFAULT_MARKER

                        # <Translate msgid='title_previous_item' node=<ast.Constant object at 0x7fa70d4cbfd0> at 7fa70d4cb940> -> __attr_title
                        __attr_title = 'Go to previous item'
                        __attr_title = translate('title_previous_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459608432
                        __default_140355459608432 = _DEFAULT_MARKER

                        # <Substitution 'previous/url' (26:16)> -> __attr_href
                        __token = 748
                        try:
                            __zt_tmp = __attrs_140355459607952
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140355540363392('path', 'previous/url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n        ')

                        # <Static value=<ast.Dict object at 0x7fa70d4fe790> name=None at 7fa70d4fedf0> -> __attrs_140355448529584
                        __attrs_140355448529584 = _static_140355459606416

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="arrow"></span>\n        ')

                        # <Static value=<ast.Dict object at 0x7fa70ca6e730> name=None at 7fa70ca6eb50> -> __attrs_140355448530256
                        __attrs_140355448530256 = _static_140355448530736

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_140355449112384_itemtitle = ''
                        __stream_140355448531840 = []
                        __append_140355448531840 = __stream_140355448531840.append
                        __append_140355448531840('\n              Previous:\n          ')
                        __stream_140355449112384_itemtitle = []
                        __append_140355449112384_itemtitle = __stream_140355449112384_itemtitle.append

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449461152
                        __attrs_140355449461152 = _static_140355540704128

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449462112
                        __default_140355449462112 = _DEFAULT_MARKER

                        # <Value 'previous/title' (35:29)> -> __cache_140355449459856
                        __token = 1012
                        try:
                            __zt_tmp = __attrs_140355449461152
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355449459856 = _static_140355540363392('path', 'previous/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value 'previous/title' (35:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70cb48970> -> __condition
                        __expression = __cache_140355449459856

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_140355449112384_itemtitle('<span ></span>')
                        else:
                            __content = __cache_140355449459856
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140355449112384_itemtitle(__content)
                        __append_140355448531840('${itemtitle}')
                        __stream_140355449112384_itemtitle = ''.join(__stream_140355449112384_itemtitle)
                        __append_140355448531840('\n        ')
                        __msgid_140355448531840 = __re_whitespace(''.join(__stream_140355448531840)).strip()
                        if 'label_previous_item':
                            __append(translate('label_previous_item', mapping={'itemtitle': __stream_140355449112384_itemtitle, }, default=__msgid_140355448531840, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n      </a>')
                    __append('\n\n      ')

                    # <Static value=<ast.Dict object at 0x7fa70cb385e0> name=None at 7fa70cb38ee0> -> __attrs_140355449358224
                    __attrs_140355449358224 = _static_140355449357792

                    # <Value 'next' (43:24)> -> __condition
                    __token = 1240
                    try:
                        __zt_tmp = __attrs_140355449358224
                    except get('NameError', NameError):
                        __zt_tmp = None

                    __condition = _static_140355540363392('path', 'next', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                    if __condition:

                        # <a ... (0:0)
                        # --------------------------------------------------------
                        __append('<a class="btn btn-sm btn-outline-secondary align-self-end next"')

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449358896
                        __default_140355449358896 = _DEFAULT_MARKER

                        # <Translate msgid='title_next_item' node=<ast.Constant object at 0x7fa70cb38a00> at 7fa70cb38af0> -> __attr_title
                        __attr_title = 'Go to next item'
                        __attr_title = translate('title_next_item', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
                        if (__attr_title is not None):
                            __append((' title="%s"' % __attr_title))

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355449357024
                        __default_140355449357024 = _DEFAULT_MARKER

                        # <Substitution 'next/url' (45:16)> -> __attr_href
                        __token = 1288
                        try:
                            __zt_tmp = __attrs_140355449358224
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __attr_href = _static_140355540363392('path', 'next/url', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
                        __attr_href = __quote(__attr_href, '"', '&quot;', None, _DEFAULT_MARKER)
                        if (__attr_href is not None):
                            __append((' href="%s"' % __attr_href))
                        __append(' >\n        ')

                        # <Static value=<ast.Dict object at 0x7fa70cadb0a0> name=None at 7fa70cadb640> -> __attrs_140355448978496
                        __attrs_140355448978496 = _static_140355448975520

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="label" >')
                        __stream_140355449112832_itemtitle = ''
                        __stream_140355448978400 = []
                        __append_140355448978400 = __stream_140355448978400.append
                        __append_140355448978400('\n              Next:\n          ')
                        __stream_140355449112832_itemtitle = []
                        __append_140355449112832_itemtitle = __stream_140355449112832_itemtitle.append

                        # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355448574448
                        __attrs_140355448574448 = _static_140355540704128

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355448574880
                        __default_140355448574880 = _DEFAULT_MARKER

                        # <Value 'next/title' (53:29)> -> __cache_140355448574688
                        __token = 1500
                        try:
                            __zt_tmp = __attrs_140355448574448
                        except get('NameError', NameError):
                            __zt_tmp = None

                        __cache_140355448574688 = _static_140355540363392('path', 'next/title', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

                        # <BinOp left=<Value 'next/title' (53:29)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70ca79160> -> __condition
                        __expression = __cache_140355448574688

                        # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
                        __value = _DEFAULT_MARKER
                        __condition = (__expression is __value)
                        if __condition:

                            # <span ... (0:0)
                            # --------------------------------------------------------
                            __append_140355449112832_itemtitle('<span ></span>')
                        else:
                            __content = __cache_140355448574688
                            __content = __quote(__content, None, '\xad', None, None)
                            if (__content is not None):
                                __append_140355449112832_itemtitle(__content)
                        __append_140355448978400('${itemtitle}')
                        __stream_140355449112832_itemtitle = ''.join(__stream_140355449112832_itemtitle)
                        __append_140355448978400('\n        ')
                        __msgid_140355448978400 = __re_whitespace(''.join(__stream_140355448978400)).strip()
                        if 'label_next_item':
                            __append(translate('label_next_item', mapping={'itemtitle': __stream_140355449112832_itemtitle, }, default=__msgid_140355448978400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
                        __append('</span>\n        ')

                        # <Static value=<ast.Dict object at 0x7fa70ca79c40> name=None at 7fa70ca793d0> -> __attrs_140355448575168
                        __attrs_140355448575168 = _static_140355448577088

                        # <span ... (0:0)
                        # --------------------------------------------------------
                        __append('<span class="arrow"></span>\n      </a>')
                    __append('\n\n\n    </nav>')
                if (__backup_previous_140355449423328 is __marker):
                    del econtext['previous']
                else:
                    econtext['previous'] = __backup_previous_140355449423328
                if (__backup_next_140355449425680 is __marker):
                    del econtext['next']
                else:
                    econtext['next'] = __backup_next_140355449425680
                __append('\n\n  ')
                if (__backup_portal_url_140355449422128 is __marker):
                    del econtext['portal_url']
                else:
                    econtext['portal_url'] = __backup_portal_url_140355449422128
                __append('\n\n</section>')
                __i18n_domain = __previous_i18n_domain_140355449423136
            if (__backup_isViewTemplate_140355449107936 is __marker):
                del econtext['isViewTemplate']
            else:
                econtext['isViewTemplate'] = __backup_isViewTemplate_140355449107936
            if (__backup_enabled_140355459448112 is __marker):
                del econtext['enabled']
            else:
                econtext['enabled'] = __backup_enabled_140355459448112
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }