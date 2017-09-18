from django.shortcuts import render
from django.http import HttpResponse


def dashboard_index(request):
    return HttpResponse('dashboard index page')
