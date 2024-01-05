import mysql.connector

con = mysql.connector.connection

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="weather1"
)
cursor = con.cursor()


def registerUser(data):
    try:
        cursor.execute('INSERT INTO users (username, email, password, location) VALUES (%s, %s, %s, %s)', data)
        con.commit()
        return True
    except:
        return False

def loginUser(data):
    try:
        cursor.execute('SELECT * FROM users WHERE username = %s and password = %s', data)
        return cursor.fetchone()
    except:
        return

def addCity(data):
    try:
        cursor.execute("UPDATE users SET city1 = %s, city2 = %s, city3 = %s WHERE id =  %s", data)
        con.commit()
        return True
    except:
        return False