
def view_cust():    
    import sqlite3
    connection = sqlite3.connect('dp_customerscopy.db')
    cursor = connection.cursor()
    colums = ['name', 'city', 'state', 'phone', 'Email']
    print(f"{'id'} {'name':<25} {'city':<26} {'state':<18} {'phone':<24} {'Email'}")
    print("------------------------------------------------------------------------------------------------------------------")
    rows = cursor.execute("SELECT customer_id, name, city, state, phone, email FROM Customers").fetchall()

    for row in rows:
        print(f'{row[0]} {row[1]:<25} {row[2]:<27} {row[3]:<15} {(row[4] if row [4] != None else "None"):<20} {(row[5] if row [5] != None else "None")}')

    while True:
        customer_id = input("Enter a ID to view customer or press 'Enter' to return to Main Menu:\n ")
       
        if customer_id == '':
            break
        else:
            rows = cursor.execute(f"SELECT customer_id, name, city, state, phone, email FROM Customers WHERE customer_id ='{customer_id}'").fetchall()
            for row in rows:
                print(f"{'ID'} {'Name':<25} {'City':<26} {'State':<18} {'Phone':<24} {'Email'}")
                print("------------------------------------------------------------------------------------------------------------------")
                print(f'{row[0]} {row[1]:<25} {row[2]:<27} {row[3]:<15} {(row[4] if row [4] != None else "None"):<20} {(row[5] if row [5] != None else "None")}')
     
        
        connection.commit()


    
