from django.contrib import admin
from . import models


class BalanceCNY(admin.ModelAdmin):
    list_display = ('observation_date', 'account', 'balance')
    search_fields = ['observation_date']
admin.site.register(models.BalanceCNY, BalanceCNY)


class BalanceUSD(admin.ModelAdmin):
    list_display = ('observation_date', 'account', 'balance')
    search_fields = ['observation_date']
admin.site.register(models.BalanceUSD, BalanceUSD)


class InvestmentCNY(admin.ModelAdmin):
    list_display = ('observation_date', 'account', 'balance')
    search_fields = ['observation_date']
admin.site.register(models.InvestmentCNY, InvestmentCNY)


class InvestmentUSD(admin.ModelAdmin):
    list_display = ('observation_date', 'account', 'balance')
    search_fields = ['observation_date']
admin.site.register(models.InvestmentUSD, InvestmentUSD)


class DailyTransaction(admin.ModelAdmin):
    list_display = ('txn_date', 'amount', 'currency', 'txn_category', 'description')
    search_fields = ['txn_date', 'txn_category']
admin.site.register(models.DailyTransaction, DailyTransaction)


class InvestmentTransfer(admin.ModelAdmin):
    list_display = ('txn_date', 'inv_acct', 'amount')
    search_fields = ['txn_date', 'inv_acct']
admin.site.register(models.InvestmentTransfer, InvestmentTransfer)


class Income(admin.ModelAdmin):
    list_display = ('txn_date', 'bank_acct', 'net_income', 'description')
    search_fields = ['txn_date']
admin.site.register(models.Income, Income)
