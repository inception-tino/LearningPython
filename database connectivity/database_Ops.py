import mysql.connector

#configuration
db_config ={
    'host' : 'localhost',
    'user' : "root",
    'password' : 'root',
    'database' : 'Aug13'
}

#connection establishment

conn = mysql.connector.connect(**db_config)
cursor = conn.cursor( )

def display():
    sqlQuery = "select * from users"
    cursor.execute(sqlQuery)
    res = cursor.fetchall()
    for rec in res:
        print(rec)

def search():
    id = input("Enter the id you want to search = ")
    sqlQuery = "select * from users where id = %s"
    cursor.execute(sqlQuery, (id,))
    res = cursor.fetchone()
    print(res)

def insertData():
    name = input("Enter the name = ")
    email = input("Enter the email = ")
    sqlQuery = "insert into users(name,email) values (%s,%s)"
    cursor.execute(sqlQuery, (name,email))
    conn.commit()
def updateData():
    id = input("Enter the id you want to update = ")
    ch = int(input("1 Update Name 2 Update Email 3 Update name and email = "))
    if ch == 1:
        name = input("Enter the name = ")
        sqlQuery = "update users set name = %s where id = %s"
        cursor.execute(sqlQuery, (name, id))
        print("Successfully updated")
    elif ch == 2:
        email = input("Enter the email = ")
        sqlQuery = "update users set email = %s where id = %s"
        cursor.execute(sqlQuery, (email, id))
        print("Successfully updated")
    elif ch == 3:
        name = input("Enter the name = ")
        email = input("Enter the email = ")
        sqlQuery = "update users set name=%s,email = %s where id = %s"
        cursor.execute(sqlQuery, (name, email, id))
        print("Successfully updated")
    else:
        print("Invalid choice")
    conn.commit()

def deleteData():
    id = input("Enter the id you want to delete = ")
    sqlQuery = "delete from users where id = %s"
    cursor.execute(sqlQuery, (id,))
    conn.commit()

while True:
    print("1 Create record 2 Update record 3 Delete record 4 Display record 5 Search 6 Exit ")
    ch = int(input("Enter the choice "))
    match ch:
        case 1: insertData()
        case 2: updateData()
        case 3: deleteData()
        case 4: display()
        case 5: search()
        case 6: break
        case _: print("Invalid ")