from django.shortcuts import render
from django.http import HttpResponse

from .constants import logger
from .methodology.get_dashboard import (
    get_balance_analysis, get_investment_analysis, get_transaction_analysis)
from .methodology.get_visualization import (
    get_txn_plot)


def dashboard_index(request):
    bal_dict = get_balance_analysis()
    inv_dict = get_investment_analysis()
    txn_dict, txn_hist_plot = get_transaction_analysis()

    txn_plot = get_txn_plot(txn_dict['category'])
    txn_plot_detail = get_txn_plot(txn_dict['category_detail'])

    return render(request, 'dashboard_index.html', {
            'bal': bal_dict,
            'inv': inv_dict,
            'txn': txn_dict,
            'txn_plot': txn_plot,
            'txn_plot_detail': txn_plot_detail,
            'txn_hist_plot': txn_hist_plot,
        })
