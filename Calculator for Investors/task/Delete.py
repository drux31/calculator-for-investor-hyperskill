# write your code here
from sqlalchemy import update, select
from Stage2 import Companies, Financial, engine, Session

def delete_company():
    print("Enter company name:")
    cname = input()

    # getting the session
    session = Session(bind=engine, autoflush=False)

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
        # Get the company
        ticker = cmp_list[int(num)].ticker
        stmt_c = select(Companies).where(Companies.ticker == ticker)
        stmt_f = select(Financial).where(Financial.ticker == ticker)

        #deleting the finance
        for f in session.scalars(stmt_f):
            session.delete(f)

        #deleting the company
        for c in session.scalars(stmt_c):
            session.delete(c)

    session.commit()