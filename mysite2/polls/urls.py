from django.urls import path
from polls.views import index
from . import views
urlpatterns = [
    path('',index),
    path('<int:question_id>/',views.detail,name='detail'),
    path('<int:question_id>/results/',views.results,name='results'),
    path('<int:question_id>/vote/',views.vote,name='vote')
]