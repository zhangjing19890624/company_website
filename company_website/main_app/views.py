from django.shortcuts import render, get_object_or_404
from .models import News, NewsType

# Create your views here.
def hello(request):
    return render(request, 'hello.html', {'message': 'hello world12'})

def news_list(request):
    #获取新闻列表信息
    news = News.objects.all()
    return render(request, 'news_list.html', {'news': news})

def news_detail(request, slug):
    #获取新闻详情信息
    news = get_object_or_404(News, slug=slug)
    return render(request, 'news_detail.html', {'news': news})
