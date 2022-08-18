
def search_cust():
    import sqlite3
    connection = sqlite3.connect('dp_customerscopy.db')
    cursor = connection.cursor()
    search_term = input('Enter a name you want to search: ')
    rows = cursor.execute(f"SELECT customer_id, name, city, state, phone, email FROM Customers WHERE name LIKE'%{search_term}%'").fetchall()
    for row in rows:
        print(f"{'ID'} {'name':<25} {'city':<26} {'state':<18} {'phone':<24} {'Email'}")
        print("------------------------------------------------------------------------------------------------------------------")
        print(f'{row[0]} {row[1]:<25} {row[2]:<27} {row[3]:<15} {(row[4] if row [4] != None else "None"):<20} {(row[5] if row [5] != None else "None")}')

    while True:
        customer_id = input("Enter a ID to view customer: ")
        rows = cursor.execute(f"SELECT customer_id, name, street_address, city, state, postal_code, phone, email FROM Customers WHERE customer_id ='{customer_id}'").fetchall()
        cust_name = cursor.execute(f"SELECT name FROM Customers WHERE customer_id = '{customer_id}'").fetchone()
        for row in rows:
            print(f"{'ID'} {'Name':<25} {'Street Address':<26} {'City':<15} {'State':<8} {'Postal Code':<22} {'Phone':<15} {'Email'}")
            print("------------------------------------------------------------------------------------------------------------------")
            print(f'{row[0]} {row[1]:<25} {(row[2] if row [2] != None else "None"):<27} {row[3]:<15} {row[4]:<10} {(row[5] if row [5] != None else "None"):<20} {(row[6] if row [6] != None else "None"):<10} {(row[7] if row [7] != None else "None")}')
        user_input = input("To update field, enter the first letter of the field.\nTo delete this record, type 'Delete'.\nTo return to the main menu, press 'ENTER' \n")
        if user_input.capitalize() == 'N':
            update_name = input("Enter new name: ")
            cursor.execute(f"UPDATE Customers SET name = '{update_name}' WHERE customer_id = '{customer_id}'")
            print("Success: Name has been updated!")
        elif user_input.capitalize() == 'S':
            update_street = input("Enter a new Street Address: ")
            cursor.execute(f"UPDATE Customers SET name = '{update_street}' WHERE customer_id = '{customer_id}'")
            print("Success: Street Address has been updated!")
        elif user_input.capitalize() == 'C':
            update_city = input("Enter a new city: ")
            update_pocode = input("Enter new postal code: ")
            cursor.execute(f"UPDATE Customers SET name = '{update_city}', postal_code = '{update_pocode}' WHERE customer_id = '{customer_id}'")
            print("Success: City has been updated!")
        elif user_input.capitalize() == 'S':
            update_state = input("Enter a new state: ")
            cursor.execute(f"UPDATE Customers SET name = '{update_state}' WHERE customer_id = '{customer_id}'")
            print("Success: State has been updated!")
        elif user_input.capitalize() == 'P':
            update_phone = input("Enter a new phone number: ")
            cursor.execute(f"UPDATE Customers SET name = '{update_phone}' WHERE customer_id = '{customer_id}'")
            print("Success: Phone has been updated!")
        elif user_input.capitalize() == "E":
            update_email = input("Enter a new email: ")
            cursor.execute(f"UPDATE Customers SET name = '{update_email}' WHERE customer_id = '{customer_id}'")
            print("Success: Email has been updated!")
        elif user_input.upper() == "DELETE":
            user_action = input(f"Are you sure you want to DELETE customer #{customer_id}{cust_name} --- (Y/N)?: ")
            if user_action.capitalize() == 'Y':
                cursor.execute(f"DELETE FROM Customers WHERE customer_id = '{customer_id}'")
                print("Success: User was deleted!")

            elif user_action.capitalize() == 'N':
                break

        elif user_input == '':
            break
        elif user_input.upper() != 'N''S''C''S''P''E''DELETE''':
            print("Please enter a valid command!")
            # for line in lines:
        break



    connection.commit()


