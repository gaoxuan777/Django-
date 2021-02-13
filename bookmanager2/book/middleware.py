from django.utils.deprecation import MiddlewareMixin
class TestMiddleWare(MiddlewareMixin):
    def process_request(self,request):
        print('111')
    def process_response(self,request,response):
        print('222')
        return response