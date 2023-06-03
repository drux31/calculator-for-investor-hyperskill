# write your code here
from sqlalchemy import select, case, cast, Float, func, and_
from Stage2 import Companies, Financial, engine, Session

def cmp_by_nd_ebitda():
    # getting the session
    session = Session(bind=engine)

    xpr = case((and_(
                    Financial.net_debt.is_not(None),
                    Financial.ebitda.is_not(None),
                    Financial.ebitda > 0
                    ), func.round((Financial.net_debt / Financial.ebitda), 2)
                ), else_ = 0.0).label("ND_EBITDA")
    #getting the financial
    stmt_f = select(Financial.ticker, xpr).order_by(xpr.desc()).limit(10)

    #printing top ten comapnies
    print('TICKER', 'ND/EBITDA')
    for f in session.execute(stmt_f):
        print(f[0], f[1])


def cmp_by_ROE():
    # getting the session
    session = Session(bind=engine)

    xpr = case((and_(
        Financial.net_profit.is_not(None),
        Financial.equity.is_not(None),
        Financial.equity > 0
    ), func.round((Financial.net_profit / Financial.equity), 2)
    ), else_=0.0).label("ROE")
    # getting the financial
    stmt_f = select(Financial.ticker, xpr).order_by(xpr.desc()).limit(10)

    # printing top ten comapnies
    print('TICKER', 'ROE')
    for f in session.execute(stmt_f):
        print(f[0], f[1])


def cmp_by_ROA():
    # getting the session
    session = Session(bind=engine)

    xpr = case((and_(
        Financial.net_profit.is_not(None),
        Financial.assets.is_not(None),
        Financial.assets > 0
    ), func.round((Financial.net_profit / Financial.assets), 2)
    ), else_=0.0).label("ROA")
    # getting the financial
    stmt_f = select(Financial.ticker, xpr).order_by(xpr.desc()).limit(10)

    # printing top ten comapnies
    print('TICKER', 'ROA')
    for f in session.execute(stmt_f):
        print(f[0], f[1])

'''

            if (f.net_profit != None and f.equity != None and f.equity > 0):
                ROE = round(f.net_profit/f.equity, 2)

            if (f.net_profit != None and f.assets != None and f.assets > 0):
                ROA = round(f.net_profit/f.assets, 2)
[
    (and_(
        (agreement.approving_official_id.is_not(None)),
        (approver.current_flag == 'Y'),
        (approver.inactive_date.is_(None)),
        (approver.organizationalstat == 'EMPLOYEE'),
        or_(
            (participatingIc.ic_nihsac == func.substr(approver.nihsac, 1, 3)),
            (externalPeoplePrimaryApprover.id.is_not(None))
        )
    ), 'Y')
],
else_ = 'N'
) 
'''