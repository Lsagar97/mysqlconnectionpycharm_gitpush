import mysql.connector as conn

mydb = conn.connect(host="localhost",username="root",passwd="Likith@97")
cursor = mydb.cursor()

#cursor.execute("insert into likithdb.likithdetails values(101 , 'likith', 'likith@gmail.com',100,30)")
#mydb.commit()
cursor.execute("select * from likith123.bank_details")
for i in cursor.fetchall():
    print(i)


    likith