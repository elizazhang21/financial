from django.shortcuts import render, redirect


def index(request):
    return redirect('dashboard_index', permanent=True)
