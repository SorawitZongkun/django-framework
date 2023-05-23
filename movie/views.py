from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def page_a(request):
    # name_movie = 'Dragon Ball'
    # return HttpResponse(name_movie)
    return render(request, 'page_a.html')


def page_b(request):
    return render(request, 'page_b.html')


def page_c(request):
    return render(request, 'page_c.html')
