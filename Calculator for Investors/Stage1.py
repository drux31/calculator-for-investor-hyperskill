
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


global option

main_menu()
option = get_input()
# Check for option value
while option != 0:
    if option < 0 or option > 2:
        print("Invalid option!")
        print()
        main_menu()
        option = get_input()
    else:
        if option == 1:
            crud_menu()
            crud_option = get_input()
            if 5 < crud_option < 0:
                print("Invalid option!")
                print()
                main_menu()
                option = get_input()
            elif crud_option != 0:
                print("Not implemented!")
                print()
                main_menu()
                option = get_input()
            else:
                main_menu()
                option = get_input()

        elif option == 2:
            top_ten_menu()
            top_menu_option = get_input()
            if 3 < top_menu_option < 0:
                print("Invalid option!")
                print()
                main_menu()
                option = get_input()
            elif top_menu_option != 0:
                print("Not implemented!")
                print()
                main_menu()
                option = get_input()
            else:
                main_menu()
                option = get_input()

print("Have a nice day!")
