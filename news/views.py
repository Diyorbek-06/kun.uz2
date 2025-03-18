from django.shortcuts import render
from .models import Category, News, Sponsor

def index(request):
    ctg = Category.objects.all()
    news = News.objects.all().order_by('-date')
    news_lasts = News.objects.all().order_by('-date')
    news_uzb = News.objects.filter(category__name="O'zbekiston").order_by('-date')
    news_jah = News.objects.filter(category__name="Jahon").order_by('-date')
    news_sport = News.objects.filter(category__name="Sport").order_by('-date')
    news_fan = News.objects.filter(category__name="Fan-texnika").order_by('-date')
    sponsor = Sponsor.objects.all()
    context = {
        'ctg': ctg,
        'news': news,
        'news_lasts': news_lasts[:5],
        'news_uzb': news_uzb,
        'news_jah': news_jah,
        'news_sport': news_sport,
        'news_fan': news_fan,
        'sponsor': sponsor,
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, '404.html')

def detail(request):
    return render(request, 'single_page.html')

def contact(request):
    return render(request, 'contact.html')

def error_page(request):
    return render(request, '404.html')
