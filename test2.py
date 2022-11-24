import mysql.connector as conn

mydb = conn.connect(host="localhost",user="root",passwd="Likith@97" )
cur = mydb.cursor()
#s="create table likithdb.likithdetails(employee_id int(10) , emp_name varchar(80) , emp_mailid varchar(20) , employee_salary int(6) , emp_attendence int(3))"
#cur.execute(s)

q1= cur.execute("select * from likithdb.likithdetails")
print(q1)


