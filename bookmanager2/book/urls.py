
from django.urls import path
from book.views import cookie,get_cookie,register,json_name,shop
from django.urls.converters import register_converter
'''转换器的使用方法
1.定义转换器'''

class MobileConvert:
    regex = '1[3-9]\d{9}'


    def to_python(self, value):
        return value
# 2.注册转换器
register_converter(MobileConvert,'phone')

urlpatterns = [
    path('set_cookie/',cookie),
    path('get_cookie/',get_cookie),
    path('register/',register),
    path('json/',json_name),
    path('<phone:city_id>/',shop)
]