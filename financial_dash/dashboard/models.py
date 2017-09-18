from django.db import models


class BalanceCNY(models.Model):
    observation_date = models.DateField(blank=True, null=True)
    account = models.CharField(max_length=99, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'balance_cny'


class BalanceUSD(models.Model):
    observation_date = models.DateField(blank=True, null=True)
    account = models.CharField(max_length=99, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'balance_usd'


class InvestmentCNY(models.Model):
    observation_date = models.DateField(blank=True, null=True)
    account = models.CharField(max_length=99, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investment_cny'


class InvestmentUSD(models.Model):
    observation_date = models.DateField(blank=True, null=True)
    account = models.CharField(max_length=99, blank=True, null=True)
    balance = models.FloatField(blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investment_usd'


class DailyTransaction(models.Model):
    txn_date = models.DateField(blank=True, null=True)
    bank_acct = models.CharField(max_length=99, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=99, blank=True, null=True)
    txn_category = models.CharField(max_length=99, blank=True, null=True)
    description = models.CharField(max_length=99, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'daily_transaction'


class InvestmentTransfer(models.Model):
    txn_date = models.DateField(blank=True, null=True)
    bank_acct = models.CharField(max_length=99, blank=True, null=True)
    inv_acct = models.CharField(max_length=99, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=99, blank=True, null=True)
    description = models.CharField(max_length=99, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'investment_transfer'


class Income(models.Model):
    txn_date = models.DateField(blank=True, null=True)
    bank_acct = models.CharField(max_length=99, blank=True, null=True)
    gross_income = models.FloatField(blank=True, null=True)
    tax_paid = models.FloatField(blank=True, null=True)
    net_income = models.FloatField(blank=True, null=True)
    currency = models.CharField(max_length=99, blank=True, null=True)
    description = models.CharField(max_length=99, blank=True, null=True)
    last_update = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'income'
