from django.shortcuts import render

#Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import news
from app.models import *


def latest_news(request, c_slug, news_slug):
    try:
        new = news.objects.get(cat__slug=c_slug, slug=news_slug)
    except Exception as e:
        raise e
    return render(request, 'news.html', {'news': new})

