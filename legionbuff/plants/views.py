from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('страница')


def categories(request, cat_id):
    return HttpResponse(f'<h1>Категории</h1><p>id: {cat_id}</p>')


def categories_by_slug(request, cat_slug):
    return HttpResponse(f'<h1>Категории</h1><p>slug: {cat_slug}</p>')


def archive(request, year):
    return HttpResponse(f'<h1>Архив по годам</h1><p>id: {year}</p>')
