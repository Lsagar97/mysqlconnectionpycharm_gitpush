import mysql.connector as conn
mydb = conn.connect(host = "localhost",username="root",passwd="Likith@97")
cursor=mydb.cursor()
cursor.execute("select employee_id,emp_mailid from likithdb.likithdetails")
l=[]
for i in cursor.fetchall():
    l.append(i)
print(l,type(l[0]))
