from django.shortcuts import render
from django.http import HttpResponse

from .constants import logger

from .methodology.get_cashflow import get_cashflow
from .methodology.get_visualization import (
    get_cap_growth_plot, get_constitution_plot)


def cashflow_index(request):
    # load cashflow index
    return render(request, 'cashflow_index.html')


def cashflow_panel(request):
    # parse GET parameters
    annual_income = float(request.GET['annual_income'])
    monthly_rent = float(request.GET['monthly_rent'])
    monthly_expense = float(request.GET['monthly_expense'])
    monthly_consumption = float(request.GET['monthly_consumption'])
    annual_return = float(request.GET['annual_return']) / 100
    n_periods = float(request.GET['n_periods'])

    # get cashflow data
    cf_data = get_cashflow(
        annual_income=annual_income,
        monthly_rent=monthly_rent,
        monthly_expense=monthly_expense,
        monthly_consumption=monthly_consumption,
        annual_return=annual_return,
        periods=n_periods)

    # format plot data
    plot_cap_growth = get_cap_growth_plot(cf_data['cap_growth'])
    plot_cons_pre = get_constitution_plot(cf_data['cons_pre_tax'])
    plot_cons_post = get_constitution_plot(cf_data['cons_post_tax'])

    # combine render data
    render_data = {
        'tax': cf_data['tax'],
        'disposable': cf_data['disposable'],
        'cons_pre_tax': cf_data['cons_pre_tax'].to_dict('record'),
        'cons_post_tax': cf_data['cons_post_tax'].to_dict('record'),
        'plot_cap_growth': plot_cap_growth,
        'plot_cons_pre': plot_cons_pre,
        'plot_cons_post': plot_cons_post,
    }

    return render(request, 'cashflow_panel.html', render_data)
