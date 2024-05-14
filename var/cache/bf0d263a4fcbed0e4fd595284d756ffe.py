# -*- coding: utf-8 -*-
__filename = '/home/gnuamua/radio/denverMesh/backend/eggs/Products.CMFPlone-6.0.11-py3.9.egg/Products/CMFPlone/browser/templates/footer.pt'

__tokens = {860: ('nocall:modules/DateTime.DateTime', 20, 30), 921: (' python:DateTime(', 21, 27), 963: ('python:myTime.year()', 22, 22)}

from Products.PageTemplates.engine import _compile_zt_expr as __compile_zt_expr
from Products.PageTemplates.engine import _C2ZContextWrapper as __C2ZContextWrapper
from sys import exc_info as _exc_info
from chameleon.tales import DEFAULT_MARKER as _DEFAULT_MARKER

_static_140355448509872 = {'xmlns': 'http://www.w3.org/1999/xhtml', 'xml:lang': 'en', 'lang': 'en', }
_static_140355492193184 = {'href': 'http://creativecommons.org/licenses/GPL/2.0/', }
_static_140355449288640 = {'href': 'http://plone.org/foundation', }
_static_140355540363104 = __C2ZContextWrapper
_static_140355540363392 = __compile_zt_expr
_static_140355482644592 = {'title': 'Copyright', }
_static_140355482646464 = {'href': 'http://plone.org', }
_static_140355540704128 = {}
_static_140355492173568 = {'class': 'card-body', }
_static_140355448512416 = {'class': 'card card-classic', 'id': 'portal-footer-signature', }

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

    def render_portlet(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
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

            # <Static value=<ast.Dict object at 0x7fa70ca69fa0> name=None at 7fa70ca69850> -> __attrs_140355492175152
            __attrs_140355492175152 = _static_140355448512416

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card card-classic" id="portal-footer-signature">\n\n    ')

            # <Static value=<ast.Dict object at 0x7fa70f40d700> name=None at 7fa70f40d430> -> __attrs_140355492173952
            __attrs_140355492173952 = _static_140355492173568

            # <div ... (0:0)
            # --------------------------------------------------------
            __append('<div class="card-body">\n      ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449131744
            __attrs_140355449131744 = _static_140355540704128
            __stream_140355448713504_plonecms = ''
            __stream_140355448713504_plonefoundation = ''
            __stream_140355448713504_copyright = ''
            __stream_140355448713504_current_year = ''
            __stream_140355482648384 = []
            __append_140355482648384 = __stream_140355482648384.append
            __append_140355482648384('\n      The\n      ')
            __stream_140355448713504_plonecms = []
            __append_140355448713504_plonecms = __stream_140355448713504_plonecms.append

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355482646752
            __attrs_140355482646752 = _static_140355540704128
            __append_140355448713504_plonecms('\n           ')

            # <Static value=<ast.Dict object at 0x7fa70eaf77c0> name=None at 7fa70eaf7760> -> __attrs_140355482647904
            __attrs_140355482647904 = _static_140355482646464

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140355448713504_plonecms('<a href="http://plone.org">')
            __stream_140355482648192 = []
            __append_140355482648192 = __stream_140355482648192.append
            __append_140355482648192('Plone')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459508976
            __attrs_140355459508976 = _static_140355540704128

            # <sup ... (0:0)
            # --------------------------------------------------------
            __append_140355482648192('<sup>&reg;</sup> Open Source CMS/WCM')
            __msgid_140355482648192 = __re_whitespace(''.join(__stream_140355482648192)).strip()
            if 'label_plone_cms':
                __append_140355448713504_plonecms(translate('label_plone_cms', mapping=None, default=__msgid_140355482648192, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_140355448713504_plonecms('</a>\n      ')
            __append_140355482648384('${plonecms}')
            __stream_140355448713504_plonecms = ''.join(__stream_140355448713504_plonecms)
            __append_140355482648384('\n      is\n      ')
            __stream_140355448713504_copyright = []
            __append_140355448713504_copyright = __stream_140355448713504_copyright.append

            # <Static value=<ast.Dict object at 0x7fa70eaf7070> name=None at 7fa70eaf7c10> -> __attrs_140355459508784
            __attrs_140355459508784 = _static_140355482644592

            # <abbr ... (0:0)
            # --------------------------------------------------------
            __append_140355448713504_copyright('<abbr')

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459509552
            __default_140355459509552 = _DEFAULT_MARKER

            # <Translate msgid='title_copyright' node=<ast.Constant object at 0x7fa70d4e6ac0> at 7fa70d4e6dc0> -> __attr_title
            __attr_title = 'Copyright'
            __attr_title = translate('title_copyright', default=__attr_title, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language'))
            if (__attr_title is not None):
                __append_140355448713504_copyright((' title="%s"' % __attr_title))
            __append_140355448713504_copyright('>&copy;</abbr>')
            __append_140355482648384('${copyright}')
            __stream_140355448713504_copyright = ''.join(__stream_140355448713504_copyright)
            __append_140355482648384('\n      2000-')
            __stream_140355448713504_current_year = []
            __append_140355448713504_current_year = __stream_140355448713504_current_year.append

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355459509648
            __attrs_140355459509648 = _static_140355540704128
            __backup_DateTime_140355492175392 = get('DateTime', __marker)

            # <Value 'nocall:modules/DateTime.DateTime' (20:30)> -> __value
            __token = 860
            try:
                __zt_tmp = __attrs_140355459509648
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('nocall', 'modules/DateTime.DateTime', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['DateTime'] = __value
            __backup_myTime_140355492173520 = get('myTime', __marker)

            # <Value 'python:DateTime()' (21:27)> -> __value
            __token = 921
            try:
                __zt_tmp = __attrs_140355459509648
            except get('NameError', NameError):
                __zt_tmp = None

            __value = _static_140355540363392('python', 'DateTime()', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))
            econtext['myTime'] = __value

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __default_140355459508832
            __default_140355459508832 = _DEFAULT_MARKER

            # <Value 'python:myTime.year()' (22:22)> -> __cache_140355459508592
            __token = 963
            try:
                __zt_tmp = __attrs_140355459509648
            except get('NameError', NameError):
                __zt_tmp = None

            __cache_140355459508592 = _static_140355540363392('python', 'myTime.year()', econtext=econtext)(_static_140355540363104(econtext, __zt_tmp))

            # <BinOp left=<Value 'python:myTime.year()' (22:22)> op=<class 'chameleon.nodes.Is'> right=<Symbol value=<DEFAULT> at 7fa7122f4d00> at 7fa70d4e6220> -> __condition
            __expression = __cache_140355459508592

            # <Symbol value=<DEFAULT> at 7fa7122f4d00> -> __value
            __value = _DEFAULT_MARKER
            __condition = (__expression is __value)
            if __condition:
                pass
            else:
                __content = __cache_140355459508592
                __content = __quote(__content, None, '\xad', None, None)
                if (__content is not None):
                    __append_140355448713504_current_year(__content)
            if (__backup_myTime_140355492173520 is __marker):
                del econtext['myTime']
            else:
                econtext['myTime'] = __backup_myTime_140355492173520
            if (__backup_DateTime_140355492175392 is __marker):
                del econtext['DateTime']
            else:
                econtext['DateTime'] = __backup_DateTime_140355492175392
            __append_140355482648384('${current_year}')
            __stream_140355448713504_current_year = ''.join(__stream_140355448713504_current_year)
            __append_140355482648384('\n      by the\n      ')
            __stream_140355448713504_plonefoundation = []
            __append_140355448713504_plonefoundation = __stream_140355448713504_plonefoundation.append

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449288736
            __attrs_140355449288736 = _static_140355540704128
            __append_140355448713504_plonefoundation('\n           ')

            # <Static value=<ast.Dict object at 0x7fa70cb277c0> name=None at 7fa70cb27100> -> __attrs_140355449289744
            __attrs_140355449289744 = _static_140355449288640

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140355448713504_plonefoundation('<a href="http://plone.org/foundation">')
            __stream_140355449288400 = []
            __append_140355449288400 = __stream_140355449288400.append
            __append_140355449288400('Plone Foundation')
            __msgid_140355449288400 = __re_whitespace(''.join(__stream_140355449288400)).strip()
            if 'label_plone_foundation':
                __append_140355448713504_plonefoundation(translate('label_plone_foundation', mapping=None, default=__msgid_140355449288400, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_140355448713504_plonefoundation('</a>')
            __append_140355482648384('${plonefoundation}')
            __stream_140355448713504_plonefoundation = ''.join(__stream_140355448713504_plonefoundation)
            __append_140355482648384('\n      and friends.\n      ')
            __msgid_140355482648384 = __re_whitespace(''.join(__stream_140355482648384)).strip()
            if 'description_copyright':
                __append(translate('description_copyright', mapping={'current_year': __stream_140355448713504_current_year, 'copyright': __stream_140355448713504_copyright, 'plonefoundation': __stream_140355448713504_plonefoundation, 'plonecms': __stream_140355448713504_plonecms, }, default=__msgid_140355482648384, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n\n      ')

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449287200
            __attrs_140355449287200 = _static_140355540704128
            __stream_140355448713504_license = ''
            __stream_140355482645168 = []
            __append_140355482645168 = __stream_140355482645168.append
            __append_140355482645168('\n      Distributed under the\n           ')
            __stream_140355448713504_license = []
            __append_140355448713504_license = __stream_140355448713504_license.append

            # <Static value=<ast.Dict object at 0x7fa712255b80> name=None at 7fa712255be0> -> __attrs_140355449287632
            __attrs_140355449287632 = _static_140355540704128
            __append_140355448713504_license('\n                ')

            # <Static value=<ast.Dict object at 0x7fa70f4123a0> name=None at 7fa70f412880> -> __attrs_140355448397056
            __attrs_140355448397056 = _static_140355492193184

            # <a ... (0:0)
            # --------------------------------------------------------
            __append_140355448713504_license('<a href="http://creativecommons.org/licenses/GPL/2.0/">')
            __stream_140355492192992 = []
            __append_140355492192992 = __stream_140355492192992.append
            __append_140355492192992('GNU GPL license')
            __msgid_140355492192992 = __re_whitespace(''.join(__stream_140355492192992)).strip()
            if 'label_gnu_gpl_licence':
                __append_140355448713504_license(translate('label_gnu_gpl_licence', mapping=None, default=__msgid_140355492192992, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append_140355448713504_license('</a>')
            __append_140355482645168('${license}')
            __stream_140355448713504_license = ''.join(__stream_140355448713504_license)
            __append_140355482645168('.\n      ')
            __msgid_140355482645168 = __re_whitespace(''.join(__stream_140355482645168)).strip()
            if 'description_license':
                __append(translate('description_license', mapping={'license': __stream_140355448713504_license, }, default=__msgid_140355482645168, domain=__i18n_domain, context=__i18n_context, target_language=getname('target_language')))
            __append('\n    </div>\n\n  </div>')
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

            # <Static value=<ast.Dict object at 0x7fa70ca695b0> name=None at 7fa70ca69760> -> __attrs_140355448511072
            __attrs_140355448511072 = _static_140355448509872
            __previous_i18n_domain_140355448509584 = __i18n_domain
            __i18n_domain = 'plone'
            __append('\n\n  ')
            __token = None
            render_portlet(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            __append('\n\n')
            __i18n_domain = __previous_i18n_domain_140355448509584
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render_portlet': render_portlet, 'render': render, }