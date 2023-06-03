# write your code here
from sqlalchemy import select
from Stage2 import Companies, Financial, engine, Session


def read_company():
    print("Enter company name:")
    cname = input()

    # getting the session
    session = Session(bind=engine)

    # getting the list of the companies from the database
    stmt_companies = select(Companies).where(Companies.name.like('%' + cname + '%'))

    # listing the companies
    result = session.scalars(stmt_companies)

    cmp_list = []
    for cmp in result:
        cmp_list.append(cmp)

    if len(cmp_list) == 0:
        print("Company not found!")
    else:
        for (i, cm) in enumerate(cmp_list):
            print(i, cm.name)

        print("Enter company number:")
        num = input()

        c_ticker = cmp_list[int(num)].ticker
        stmt_fin = select(Financial).where(Financial.ticker == c_ticker)

        print(c_ticker, cmp_list[int(num)].name)
        for f in session.scalars(stmt_fin):
            PE = None
            PS = None
            PB = None
            ND_EBITDA = None
            ROE = None
            ROA = None
            LA = None

            if (f.market_price != None and f.net_profit != None and f.net_profit > 0):
                PE = round(f.market_price/f.net_profit, 2)

            if (f.market_price != None and f.sales != None and f.sales > 0):
                PS = round(f.market_price/f.sales, 2)

            if (f.market_price != None and f.assets != None and f.assets > 0):
                PB = round(f.market_price/f.assets, 2)

            if (f.net_debt != None and f.ebitda != None and f.ebitda > 0):
                ND_EBITDA = round(f.net_debt/f.ebitda, 2)

            if (f.net_profit != None and f.equity != None and f.equity > 0):
                ROE = round(f.net_profit/f.equity, 2)

            if (f.net_profit != None and f.assets != None and f.assets > 0):
                ROA = round(f.net_profit/f.assets, 2)

            if (f.liabilities != None and f.assets != None and f.assets > 0):
                LA = round(f.liabilities/f.assets, 2)

            print('P/E = ' + str(PE))
            print('P/S = ' + str(PS))
            print('P/B = ' + str(PB))
            print('ND/EBITDA = ' + str(ND_EBITDA))
            print('ROE = ' + str(ROE))
            print('ROA = ' + str(ROA))
            print('L/A = ' + str(LA))

def read_all():
    # getting the session
    session = Session(bind=engine, autoflush=False)

    # getting the list of the companies from the database
    stmt_c = select(Companies).order_by(Companies.ticker)
    print("COMPANY LIST")
    for c in session.scalars(stmt_c):
        print(c.ticker, c.name, c.sector)

    #session.close()