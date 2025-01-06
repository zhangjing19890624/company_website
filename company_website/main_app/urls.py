from django.urls import path
from .views import hello,news_list,news_detail

urlpatterns = [
    path('hello/', hello,name='hello'),
    path('news/', news_list,name='news_list'),
    path('news/<slug:slug>/', news_detail,name='news_detail'),
]