
import view_db
import search_db
import add_db


while True:
    print("**** Customer Database ****")
    action = str(input("[1] View All Customers\n[2] Search Customers\n[3] Add a New Customer\n[Q] Quit\n"))

    if action == "1":
        view_db.view_cust()

    if action == "2":
        search_db.search_cust()

    if action == "3":
        add_db.add_customer()

    if action.capitalize() == "Q":
        print("GoodBye!")
        break
