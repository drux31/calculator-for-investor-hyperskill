# write your code here
from sqlalchemy import update, select
from Stage2 import Companies, Financial, engine, Session

def update_company():
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
        #Get the company
        #company = select(Companies).where(Companies.name == cmp_list[int(num)].name)
        ticker = cmp_list[int(num)].ticker
        #get the finance
        stmt_f = select(Financial).where(Financial.ticker == ticker)
        #c_finance = session.scalars(stmt_f).one()
        for c_finance in session.scalars(stmt_f):
            #Update everything
            #ebitda
            print("Enter ebitda (in the format of '987654321'): ")
            ed = input()
            c_finance.ebitda = float(ed) if len(ed) > 0 else None

            #sales
            print("Enter sales (in the format of '987654321'): ")
            sa = input()
            c_finance.sales = float(sa) if len(sa) > 0 else None

            #net_profit
            print("Enter net profit (in the format of '987654321'): ")
            np = input()
            c_finance.net_profit = float(np) if len(np) > 0 else None

            #market_price
            print("Enter market price (in the format of '987654321'): ")
            mp = input()
            c_finance.market_price = float(mp) if len(mp) > 0 else None

            #net_debt
            print("Enter net debt (in the format of '987654321'): ")
            nd = input()
            c_finance.net_debt = float(nd) if len(nd) > 0 else None

            #assets
            print("Enter assets (in the format of '987654321'): ")
            ass = input()
            c_finance.assets = float(ass) if len(ass) > 0 else None

            #equity
            print("Enter equity (in the format of '987654321'): ")
            eq = input()
            c_finance.equity = float(eq) if len(eq) > 0 else None

            #cash_equivalents
            print("Enter cash equivalents (in the format of '987654321'): ")
            ce = input()
            c_finance.cash_equivalents = float(ce) if len(ce) > 0 else None

            #liabilities
            print("Enter liabilities (in the format of '987654321'): ")
            li = input()
            c_finance.liabilities = float(li) if len(li) > 0 else None

    session.commit()