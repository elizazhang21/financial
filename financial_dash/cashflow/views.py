from django.shortcuts import render
from django.http import HttpResponse

from .constants import logger


def cashflow_index(request):
    return HttpResponse('Hello world!')
