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

def lstm_data(future,name):
    conn = pg.connect(database="postgres", user='postgres', password='12345678', host='127.0.0.1', port= '5433')
    for i in future:
        cursor.execute("INSERT INTO LSTMdata(price, compID)values(%s,%s)",(i,name))
        # Commit your changes in the database
        conn.commit()
        print("Records inserted........")
    # Closing the connection
    conn.close()

def delete_pred():
    pass

def capital():
    conn = pg.connect(database="postgres", user='postgres', password='12345678', host='127.0.0.1', port= '5433')
    cursor = conn.cursor()
    cursor.execute("select * from cash")
    conn.commit()
    val = cursor.fetchone()
    cap = val[0]
    inv = val[1]
    print("Transaction Retrieved...")
    conn.close()
    print(cap,inv)
    return cap,inv

def holdings():
    conn = pg.connect(database="postgres", user='postgres', password='12345678', host='127.0.0.1', port= '5433')
    cursor = conn.cursor()
    cursor.execute("select * from holdings")
    conn.commit()
    val = cursor.fetchone()
    conn.close()
    return val

def sell(qty,comp,choice):
    conn = pg.connect(database="postgres", user='postgres', password='12345678', host='127.0.0.1', port= '5433')
    cursor = conn.cursor()
    if choice == 'all':
        cursor.execute("DELETE from holdings")
        conn.commit()
        print("all positions sold")
        conn.close()

    elif choice == "some":
        cursor.execute(f"UPDATE holdings set quantity={qty} WHERE equity = {comp}")
        conn.commit()
        print(f"sold {qty} positions")
        conn.close()
        
def profits(last,quantity,comp):
    prof = last*quantity
    conn = pg.connect(database="postgres", user='postgres', password='12345678', host='127.0.0.1', port= '5433')
    cursor = conn.cursor()
    cursor.execute("select * from cash")
    conn.commit()
    vals = cursor.fetchone()
    gain = prof-vals[1]
    cursor.execute("INSERT INTO profits(GainLoss) VALUES (%s)",(gain,))
    conn.commit()
    # cursor.execute(f"UPDATE cash set money=money+{vals[1]}+{gain} WHERE equity = {comp}")
    # conn.commit()
    # cursor.execute(f"UPDATE cash set invested={prof}-invested WHERE equity = {comp}")
    # conn.commit()
    conn.close()
    print(gain)

def count_positions():
    conn = pg.connect(database="postgres", user='postgres', password='12345678', host='127.0.0.1', port= '5433')
    cursor = conn.cursor()
    cursor.execute("select count(*) from holdings")
    conn.commit()
    val = cursor.fetchone()
    conn.close()
    return val[0]

def buy_new(tick,values,last_price):
    conn = pg.connect(database="postgres", user='postgres', password='12345678', host='127.0.0.1', port= '5433')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO holdings (equity, quantity, price) VALUES (%s, %s, %s)", (tick, values, last_price))
    conn.commit()
    print("Updated Database with new Buy Order")
    conn.close()
