# write your code here
import csv
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Float
from sqlalchemy.orm import sessionmaker, Query, declarative_base
from collections import defaultdict

# Creating the engine for the connection
engine = create_engine('sqlite:///investor.db', echo=False)
Session = sessionmaker(bind=engine)

Base = declarative_base()


class Companies(Base):
    __tablename__ = 'companies'
    ticker = Column(String(30), primary_key=True)
    name = Column(String(30))
    sector = Column(String(30))


class Financial(Base):
    __tablename__ = 'financial'
    ticker = Column(String(30), primary_key=True)
    ebitda = Column(Float)
    sales = Column(Float)
    net_profit = Column(Float)
    market_price = Column(Float)
    net_debt = Column(Float)
    assets = Column(Float)
    equity = Column(Float)
    cash_equivalents = Column(Float)
    liabilities = Column(Float)


def create_db(reader1, reader2):
    # Create the new table
    Base.metadata.create_all(engine)

    # data insertion
    session = Session()
    for comp, vals in reader1.items():
        # print(vals)
        session.merge(Companies(ticker=vals['ticker'], name=vals['name'], sector=vals['sector']))

    for f, vals in reader2.items():
        # print(f[0]['ticker'])
        session.merge(Financial(ticker=vals['ticker'],
                              ebitda=vals['ebitda'],
                              sales=vals['sales'],
                              net_profit=vals['net_profit'],
                              market_price=vals['market_price'],
                              net_debt=vals['net_debt'],
                              assets=vals['assets'],
                              equity=vals['equity'],
                              cash_equivalents=vals['cash_equivalents'],
                              liabilities=vals['liabilities']
                              ))
    session.commit()


def store_data():
    dict_companies = defaultdict(dict)
    dict_financial = defaultdict(dict)
    count = 0
    with open("../../companies.csv") as company:
        companies_file_reader = csv.DictReader(company, delimiter=",")
        for line in companies_file_reader:
            if line['ticker'] == '':
                line['ticker'] = None
            if line['name'] == '':
                line['name'] = None
            if line['sector'] == '':
                line['sector'] = None
            # print(line)
            dict_companies[count] = {'ticker': line['ticker'], 'name': line['name'], 'sector': line['sector']}
            count += 1

    # print(dict_companies)
    count = 0
    with open("../../financial.csv") as fin:
        financial_file_reader = csv.DictReader(fin, delimiter=",")
        for line in financial_file_reader:
            if line['ticker'] == '':
                line['ticker'] = None
            if line['ebitda'] == '':
                line['ebitda'] = None
            if line['sales'] == '':
                line['sales'] = None
            if line['net_profit'] == '':
                line['net_profit'] = None
            if line['market_price'] == '':
                line['market_price'] = None
            if line['net_debt'] == '':
                line['net_debt'] = None
            if line['assets'] == '':
                line['assets'] = None
            if line['equity'] == '':
                line['equity'] = None
            if line['cash_equivalents'] == '':
                line['cash_equivalents'] = None
            if line['liabilities'] == '':
                line['liabilities'] = None
            dict_financial[count] = dict(line)
            count += 1
    # print(dict_financial)
    create_db(dict_companies, dict_financial)
    #print('Database created successfully!')
