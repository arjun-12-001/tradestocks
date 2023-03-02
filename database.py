import psycopg2 as pg
conn = pg.connect(
   database="postgres", user='postgres', password='12345678', host='127.0.0.1', port= '5433'
)
#Setting auto commit false
conn.autocommit = True


# Creating a cursor object using the cursor() method  
cursor = conn.cursor()

def insertion():
    conn = pg.connect(database="postgres", user='postgres', password='12345678', host='127.0.0.1', port= '5433')
    user = input("enter username : ")
    passwd = input("enter password : ")
    cursor.execute("INSERT INTO account(usernames, passwords)values(%s,%s)",(user,passwd))
    # Commit your changes in the database
    conn.commit()
    print("Records inserted........")
    # Closing the connection
    conn.close()

def selected():
    conn = pg.connect(database="postgres", user='postgres', password='12345678', host='127.0.0.1', port= '5433')
    cursor.execute("select * from account")
    conn.commit()
    rows = cursor.fetchall()
    conn.close()
    return rows

def check(userID):
    conn = pg.connect(database="postgres", user='postgres', password='12345678', host='127.0.0.1', port= '5433')
    cursor = conn.cursor()
    cursor.execute("select passwords from account where usernames =%s",(userID,))
    conn.commit()
    val = cursor.fetchone()
    conn.close()
    return val[0]