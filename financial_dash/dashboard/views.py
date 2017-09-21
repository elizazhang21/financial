from django.shortcuts import render
from django.http import HttpResponse
from .constants import logger
from .methodology.get_dashboard import (
    get_balance_analysis
)


def dashboard_index(request):
    return render(request, 'dashboard_index.html')
