# write your code here
from create_company import create_company
from Read import read_company, read_all
from Update import update_company
from Delete import delete_company
from ToptenCompanies import cmp_by_nd_ebitda, cmp_by_ROA, cmp_by_ROE
from Stage1 import main_menu, get_input, crud_menu, top_ten_menu
from Stage2 import store_data, engine
from sqlalchemy_utils.functions import database_exists
global option


def talking_number():
    print("Welcome to the Investor Program!\n")
    if not database_exists(engine.url):
        store_data()
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
                if crud_option < 0 or crud_option > 5:
                    print("Invalid option!")
                    print()
                    crud_menu()
                    option = get_input()
                elif crud_option ==1:
                    create_company()
                    print("Company created successfully!\n")

                    main_menu()
                    option = get_input()

                elif crud_option == 2:
                    read_company()
                    print()
                    main_menu()
                    option = get_input()

                elif crud_option == 3:
                    update_company()
                    print("Company updated successfully!")
                    print()
                    main_menu()
                    option = get_input()

                elif crud_option == 4:
                    delete_company()
                    print("Company deleted successfully!")
                    print()
                    main_menu()
                    option = get_input()
                elif crud_option == 5:
                    read_all()
                    print()
                    main_menu()
                    option = get_input()
                else:
                    main_menu()
                    option = get_input()

            elif option == 2:
                top_ten_menu()
                top_menu_option = get_input()
                if top_menu_option < 0 or top_menu_option > 3:
                    print("Invalid option!")
                    print()
                    main_menu()
                    option = get_input()
                elif top_menu_option == 1:
                    cmp_by_nd_ebitda()
                    print()
                    main_menu()
                    option = get_input()

                elif top_menu_option == 2:
                    cmp_by_ROE()
                    print()
                    main_menu()
                    option = get_input()

                elif top_menu_option == 3:
                    cmp_by_ROA()
                    print()
                    main_menu()
                    option = get_input()

                else:
                    main_menu()
                    option = get_input()

    print("Have a nice day!")


talking_number()
