def add_customer():
    import sqlite3
    connection = sqlite3.connect('dp_customerscopy.db')
    cursor = connection.cursor()

    print("**** New Customer ****")
    print("Please fill out the form below to add a new Customer:")
    insert_info = "INSERT INTO Customers (name, street_address, city, state, postal_code, phone, email) VALUES (?,?,?,?,?,?,?)"
    while True:
        name = input('Enter customer name: ')
        address = input('Enter address: ')
        city = input('Enter city: ')
        state = input('Enter state: ')
        postal_code = input('Ener Postal code: ')
        phone = input('Enter phone number: ')
        email = input('Enter email: ')

        values = (name, address, city, state, postal_code, phone, email)
        cursor.execute(insert_info, values)
        print('Success: Customer was successfully added!')
        connection.commit()
        break