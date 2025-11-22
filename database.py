import sqlite3

connection = sqlite3.connect("feeback.db")
cursor = connection.cursor()

cmd = """
    CREATE TABLE IF NOT EXISTS FEEDBACK(
        id integer primary key AUTOINCREMENT,
        fullname text not null,
        usn varchar(10) not null,
        contact varchar(10) not null,
        email text not null,
        message text not null
    )
"""

cursor.execute(cmd)
connection.commit()

cmd = "INSERT INTO FEEDBACK(fullname, usn, contact, email, message)values(?,?,?,?,?)"

#cursor.execute(cmd,('Nishan','abcd123','9380719446','nishankamath@gmail.com','This is a good time to learn DevpOps!'))
connection.commit()

f = cursor.execute("SELECT * FROM FEEDBACK").fetchall()
print(f)

r = cursor.execute("select * from FEEDBACK where fullname = ?",('Nishan',)).fetchall()
print(r)



connection.close()