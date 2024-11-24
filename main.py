import dbhelper

while True:    

    print("Select operation you wanna perform:\n 1.Create table\n 2.Insert into table\n 3.Display all records\n 4.Exit ")
    operation =int(input("Enter the option:"))

    if(operation == 1):
        dbhelper.create_table()
    elif(operation == 2):
        dbhelper.insert_query()
    elif(operation == 3):
        dbhelper.display_all()
    elif(operation == 4):
        dbhelper.exit_parking()    
    else:   
        print("Invalid Option")
        print("Enter the correct option")