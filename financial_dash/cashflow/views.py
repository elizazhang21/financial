from django.shortcuts import render
from django.http import HttpResponse

from .constants import logger

from .methodology.get_cashflow import get_cashflow
from .methodology.get_visualization import (
    get_cap_growth_plot, get_constitution_plot)


def cashflow_index(request):
    # get cashflow data
    cf_data = get_cashflow(
        annual_income=125000, monthly_rent=2000, monthly_expense=1200, monthly_consumption=500, annual_return=0.07, periods=20)

    # format plot data
    plot_cap_growth = get_cap_growth_plot(cf_data['cap_growth'])
    plot_cons_pre = get_constitution_plot(cf_data['cons_pre_tax'])
    plot_cons_post = get_constitution_plot(cf_data['cons_post_tax'])

    # combine render data
    render_data = {
        'tax': cf_data['tax'],
        'disposable': cf_data['disposable'],
        'cons_pre_tax': cf_data['cons_pre_tax'].to_dict('record'),
        'plot_cap_growth': plot_cap_growth,
        'plot_cons_pre': plot_cons_pre,
        'plot_cons_post': plot_cons_post,
    }

    return render(request, 'cashflow_index.html', render_data)
