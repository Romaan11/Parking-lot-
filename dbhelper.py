import sqlite3
import datetime

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

def create_table():
    cursor.execute(
        '''
        create table if not exists parking(
        id integer primary key,
        driver_name text not null,
        vehicle_type text not null,
        vehicle_num integer not null,
        parking_start_time date,
        end_time date,
        total_price float null
        )
       
        '''
    )
    conn.commit()
    print("Table has been created successfully!")

def insert_query():
    driver_name = input("Enter the name of the driver: ")
    while True:
        print("""Enter the vehicle type
          1. Two Wheeler
          2. Four Wheeler""")
        vehicle_type_option = int(input("Enter the type of the vehicle: "))
        if vehicle_type_option == 1:
            vehicle_type = "Two Wheeler"
            break
        elif vehicle_type_option == 2:
            vehicle_type = "Four Wheeler"
            break
        else:
            print("Invalid option")
            print("Enter the correct option")

    parking_start_time = datetime.datetime.now()
    vehicle_num = int(input("Enter the vehicle number: "))
    details = (driver_name,vehicle_type,vehicle_num,parking_start_time)

    cursor.execute("insert into parking (driver_name,vehicle_type,vehicle_num,parking_start_time) values (?,?,?,?)",details)
    conn.commit()
    cursor.execute(f"select * from parking where vehicle_num == {vehicle_num}")
    rows = cursor.fetchall()[0]
    print("Your slips")

    with open(rows[3] + ".txt",mode="w") as file:
        file.write(f"id: {rows[0]}\n")
        file.write(f"driver_name: {rows[1]}\n")
        file.write(f"vehicle_type: {rows[2]}\n")
        file.write(f"vehicle_type: {rows[4]}\n")


def display_all():
    cursor.execute("select * from parking")

    rows = cursor.fetchall()
    print("All records")
    print("(id|driver_name|vehicle_type|vehicle_num|parking_start_time)")
    for row in rows:
        print(row,"\t")

def exit_parking():

    ending_time = datetime.datetime.now()

    id = int(input("Enter your id: "))
    cursor.execute("update parking set end_time = (?) where id = (?)",(ending_time,id ))
    conn.commit()
    cursor.execute("select parking_start_time from parking where id = (?)", (id))
    
    rows = cursor.fetchall()
    starting_time = rows[0][0]
    format = '%Y-%m-%d %H:%M:%S.%f'
    start_time = datetime.datetime.strptime(starting_time,format)

    actual_time = (ending_time - start_time)
    print(actual_time)

