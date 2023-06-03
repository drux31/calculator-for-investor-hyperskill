
def main_menu():
    # Main menu
    print("MAIN MENU")
    print("0 Exit")
    print("1 CRUD operations")
    print("2 Show top ten companies by criteria")
    print()


def crud_menu():
    print("CRUD MENU")
    print("0 Back")
    print("1 Create a company")
    print("2 Read a company")
    print("3 Update a company")
    print("4 Delete a company")
    print("5 List all companies")
    print()


def top_ten_menu():
    print("TOP TEN MENU")
    print("0 Back")
    print("1 List by ND/EBITDA")
    print("2 List by ROE")
    print("3 List by ROA")
    print()


def get_input():
    print("Enter an option: ")
    test = input()
    if test.isdigit():
        return int(test)
    else:
        return -1


