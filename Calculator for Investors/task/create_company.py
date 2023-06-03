# write your code here
from Stage2 import Companies, Financial, engine, Session

# create a company
def create_company():
    print("Enter ticker (in the format of 'MOON'): ")
    ticker = input()

    print("Enter company (in the format of 'Moon Corp'): ")
    company = input()

    print("Enter industries (in the format of 'Technology'): ")
    industries = input()

    print("Enter ebitda (in the format of '987654321'): ")
    ebitda = input()

    print("Enter sales (in the format of '987654321'): ")
    sales = input()

    print("Enter net profit (in the format of '987654321'): ")
    net_profit = input()

    print("Enter market price (in the format of '987654321'): ")
    market_price = input()

    print("Enter net debt (in the format of '987654321'): ")
    net_debt = input()

    print("Enter assets (in the format of '987654321'): ")
    assets = input()

    print("Enter equity (in the format of '987654321'): ")
    equity = input()

    print("Enter cash equivalents (in the format of '987654321'): ")
    cash_equivalent = input()

    print("Enter liabilities (in the format of '987654321'): ")
    liabilities = input()

    # data insertion
    session = Session(bind=engine, autoflush=False)
    #creating company object
    stmt_company = Companies(ticker=ticker, name=company, sector=industries)

    stmt_financial = Financial(ticker=ticker,
                               ebitda = float(ebitda) if len(ebitda) > 0 else None,
                               sales = float(sales) if len(sales) > 0 else None,
                               net_profit = float(net_profit) if len(net_profit) > 0 else None,
                               market_price = float(market_price) if len(market_price) > 0 else None,
                               net_debt = float(net_debt) if len(ebitda) > 0 else None,
                               assets = float(assets) if len(assets) > 0 else None,
                               equity = float(equity) if len(equity) > 0 else None,
                               cash_equivalents = float(cash_equivalent) if len(cash_equivalent) > 0 else None,
                               liabilities = float(liabilities) if len(liabilities) > 0 else None)

    session.add_all([stmt_company, stmt_financial])
    session.commit()

