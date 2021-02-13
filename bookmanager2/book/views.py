from django.http import HttpResponse
from django.shortcuts import render
import json
# Create your views here.
from book.models import BookInfo
from book.models import PeopleInfo
# BookInfo.objects.filter(peopleinfo__id__='1')
# BookInfo(
#     name='Django',
#     pub_date='2020-1-2',
#     readcount=0,
#     commentcount=10
#
# )
# BookInfo.objects.filter(pk=1).update(name='gao')
# BookInfo.objects.filter(pk=4).delete()
# BookInfo.objects.filter(name__contains='天')
# BookInfo.objects.filter(name__endswith='部')
# BookInfo.objects.filter(name__isnull=True)
# BookInfo.objects.filter(pk__in=[1,3,5])
# BookInfo.objects.filter(pk__gt=3)
# BookInfo.objects.filter(pub_date__year__gt=1980)
# from django.db.models import F
# BookInfo.objects.filter(commentcount__gt=F('readcount'))
# from django.db.models import Q
# BookInfo.objects.filter(~Q(id=3))
# BookInfo.objects.filter(Q(id=1)|Q(id=3))
# BookInfo.objects.aggregate(Sum('commentcount'))
# from django.db.models import Sum
# book=BookInfo.objects.get(id=1)
# book.peopleinfo_set.filter(name='郭靖')
# # 查询图书，要求图书人物为"郭靖"
# # 查询图书，要求图书中人物的描述包含"八"
# BookInfo.objects.filter(peopleinfo__description__contains='八')


def cookie(request):
    cookie_name=request.GET.get('username')
    psd=request.GET.get('password')
    set_cookie=HttpResponse('123')
    set_cookie.set_cookie('name',cookie_name,max_age=3600)
    set_cookie.set_cookie('password',psd)

    return set_cookie

def get_cookie(request):
    avc=request.COOKIES.get('name')
    print(avc)
    return HttpResponse('高旭桉')
def register(request):
    #前端form表单发送post请求给后端传递前端数据，后端通过request.Post拿到数据 是字典形式的数据
    data=request.POST
    print(data)
    return HttpResponse('1233')
def json_name(request):
    #前端发送json数据给后台，后台通过request.body拿到json数据 是byte类型 需要利用decode()转化为json数据形式 ，再利用(先 import json）json.load可以转化为字典形式
    data=request.body
    data2=json.loads(data.decode())
    #通过request.META可以拿到请求头的信息  字典形式
    print(request.META)

    return HttpResponse('json')
def shop(request,city_id):
    return HttpResponse('12')
def set_session(request):
    username=request.GET.get('username')
    user_id=1
    request.session['id_name']=user_id
    request.session['id_username']=username
    return HttpResponse('session')
def get_session(request):
    a=request.session.get('id_name')
    b = request.session.get('id_username')
    content='{},{}'.format(a,b)
    return HttpResponse(content)
from django.views import View
class login(View):
    def get(self,request):
        return HttpResponse('get')
    def post(self,request):
        return HttpResponse('post')
from django.contrib.auth.mixins import LoginRequiredMixin
class OrderView(LoginRequiredMixin,View):
    def get(self,request):
        return HttpResponse('get')
    def post(self,request):
        return HttpResponse('post')


