import mysql.connector as conn

mydb = conn.connect(host = "localhost", user = "root",passwd = "Likith@97")
cursor = mydb.cursor()
s="create table likith123.likithdetails1(employee_id int(10) , emp_name varchar(80) , emp_mailid varchar(20) , employee_salary int(6) , emp_attendence int(3)"
cursor.execute(s)

mydb.commit()
