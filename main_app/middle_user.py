# coding=utf-8
"""
中间键
"""
from urllib import request

from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin


class Middle(MiddlewareMixin):

    @staticmethod
    def check_ip(ips):
        check_ip_url = 'http://api.ipify.org/'
        handler = request.ProxyHandler(ips)
        opener = request.build_opener(handler)
        try:
            ip = opener.open(check_ip_url, timeout=3).read().decode('utf-8')
            if '117.136.38.177' != ip:
                return True
        except:
            return False
    """
    强制登录
    """

    def process_request(self, request):
        """
        拦截view之前的请求
        如果没有login标志就进行拦截
        :param request:
        :return:
        """
        # 登录等操作返回False跳过验证
        print('lanjie', request.path.split('/')[-2])
        paths = request.path.split('/')[-2] not in ['api.ipify.org', 'username_verify', 'ajax_verify', 'login_page', 'login_logic',
                                                    'register', 'register_logic', 'verify_code']
        if paths:
            if request.session.get('name'):
                print(request.META.get('REMOTE_ADDR'))
                flag = self.check_ip({'http': request.META.get('HTTP_HOST')})
                print(flag)
                if flag:
                    pass
            else:
                print('拦截请求：%s' % request.path)
                return redirect('login_page')

    def process_response(self, request, response):
        """
        持续返回响应
        :param request:
        :param response:
        :return:
        """
        print("response:", self.__dict__, request, response)
        return response


if __name__ == '__main__':
    Middle.check_ip({'http': '117.136.38.177:8000'})