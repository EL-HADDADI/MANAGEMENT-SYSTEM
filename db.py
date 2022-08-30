import sqlite3

def connect():

    try:
        con = sqlite3.connect("data/student_records.db")
        print("connected")
        con.commit()

    except:
        print("failed to connect")
        con.close()

def insertRecord(regno,fname,lname,gender,dob,course):
    try:
        con = sqlite3.connect("data/student_records.db")
        cur = con.cursor()
        cur.execute("INSERT INTO student_data VALUES(?,?,?,?,?,?)",(regno,fname,lname,gender,dob,course))
        con.commit()
        print("registered")

    except:
        print("failed")

    
        



