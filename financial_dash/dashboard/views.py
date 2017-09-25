from django.shortcuts import render
from django.http import HttpResponse
from .constants import logger
from .methodology.get_dashboard import (
    get_balance_analysis, get_investment_analysis, get_transaction_analysis
)


def dashboard_index(request):
    bal_dict = get_balance_analysis()
    inv_dict = get_investment_analysis()
    txn_dict = get_transaction_analysis()
    return render(request, 'dashboard_index.html', {
            'bal': bal_dict,
            'inv': inv_dict,
            'txn': txn_dict,
        })
