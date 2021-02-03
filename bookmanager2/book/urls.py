
from django.urls import path
from book.views import shop
urlpatterns = [
    path('<city_id>/<res_id>/', shop),
]