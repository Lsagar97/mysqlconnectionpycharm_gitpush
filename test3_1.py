import mysql.connector as conn
mydb=conn.connect(host="localhost",username="root",passwd="Likith@97")
cursor=mydb.cursor()
ls="insert into likithdb.likithdetails values(101,'likith','likith@gamil.com',100,30)"
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
cursor.execute(ls)
mydb.commit()  ##like iam commiting changes or asigned vales in table
cursor.execute("select * from likithdb.likithdetails")
for i in cursor.fetchall():
    print(i)


    liki
