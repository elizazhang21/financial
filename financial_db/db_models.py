import datetime
from sqlalchemy import Column, Integer, String, Float, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


# bank balance tables
class BalanceCNY(Base):
    __tablename__ = 'balance_cny'

    id = Column(Integer, primary_key=True, autoincrement=True)
    observation_date = Column(Date)
    account = Column(String)
    balance = Column(Float)
    last_update = Column(DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return "<CNY Balance on {}: {:.2f} of {}>".format(
            self.observation_date, self.balance, self.account
        )


class BalanceUSD(Base):
    __tablename__ = 'balance_usd'

    id = Column(Integer, primary_key=True, autoincrement=True)
    observation_date = Column(Date)
    account = Column(String)
    balance = Column(Float)
    last_update = Column(DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return "<USD Balance on {}: {:.2f} of {}>".format(
            self.observation_date, self.balance, self.account
        )


# investment balance tables
class InvestmentCNY(Base):
    __tablename__ = 'investment_cny'

    id = Column(Integer, primary_key=True, autoincrement=True)
    observation_date = Column(Date)
    account = Column(String)
    balance = Column(Float)
    last_update = Column(DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return "<CNY Investment on {}: {:.2f} of {}>".format(
            self.observation_date, self.balance, self.account
        )


class InvestmentUSD(Base):
    __tablename__ = 'investment_usd'

    id = Column(Integer, primary_key=True, autoincrement=True)
    observation_date = Column(Date)
    account = Column(String)
    balance = Column(Float)
    last_update = Column(DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return "<USD Investment on {}: {:.2f} of {}>".format(
            self.observation_date, self.balance, self.account
        )


# transaction entry tables
class DailyTransaction(Base):
    __tablename__ = 'daily_transaction'

    id = Column(Integer, primary_key=True, autoincrement=True)
    txn_date = Column(Date)
    bank_acct = Column(String)
    amount = Column(Float)
    currency = Column(String)
    txn_category = Column(String)
    description = Column(String)
    last_update = Column(DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return "<Transaction on {}: {} {:.2f} for {}>".format(
            self.txn_date, self.currency, self.amount, self.txn_category
        )


class InvestmentTransfer(Base):
    __tablename__ = 'investment_transfer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    txn_date = Column(Date)
    bank_acct = Column(String)
    inv_acct = Column(String)
    amount = Column(Float)
    currency = Column(String)
    description = Column(String)
    last_update = Column(DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        if amount < 0:
            return "<Transfer on {}: {:.2f} from {} to {}>".format(
                self.txn_date, self.amount, self.bank_acct, self.inv_acct
            )
        else:
            return "<Transfer on {}: {:.2f} from {} to {}>".format(
                self.txn_date, self.amount, self.inv_acct, self.bank_acct
            )


# income entries
class Income(Base):
    __tablename__ = 'income'

    id = Column(Integer, primary_key=True, autoincrement=True)
    txn_date = Column(Date)
    bank_acct = Column(String)
    gross_income = Column(Float)
    tax_paid = Column(Float)
    net_income = Column(Float)
    currency = Column(String)
    description = Column(String)
    last_update = Column(DateTime, default=datetime.datetime.utcnow())

    def __repr__(self):
        return "<Income on {}: {} {:.2f}>".format(
            self.observation_date, self.currency, self.net_income
        )


model_list = [
    BalanceCNY, BalanceUSD, InvestmentCNY, InvestmentUSD,
    DailyTransaction, InvestmentTransfer, Income
]
