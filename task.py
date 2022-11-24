import mysql.connector as conn
#import csvkit
import pandas as pd

pd.read_csv("D:/testcsv.csv")



mydb = conn.connect(host="localhost",user='root',passwd='Likith@97')
cur = mydb.cursor()
#s =  'create table likithdb.attributedataset(Dress_ID int(15),Style varchar(20),Price varchar(20),Rating float(2),Size varchar(5),Season varchar(8),Neckline varchar(10),Sleeevline varchar(15),waiseline varchar(15), Material varchar(15), FabricType varchar(15), Decoration varchar(15), Pattern_type varchar(15),recommendation int(2))'
#cur.execute(s)


###tried here not succeded but went to jupyter notebook file name (my task for sql to upload bulk csv)



#cur.execute("select * from likithdb.attributedatasetcsv")
l =[]
#for i in cur.fetchall():
    #l.append(i)
  #  print(l,type(l[0]))
cur.execute("select attributedatasetcsv.Dress_ID from likithdb.attributedatasetcsv left join likithdb.dresssales on attributedatasetcsv.Dress_ID = dresssales.Dress_ID")
#cur.execute("select attributedatasetcsv.Size from likithdb.attributedatasetcsv")
for i in cur.fetchall():
    l.append(i)
    #print(i,l.index(i)) #to count no of data's
    print(i,l.index(i))
#print(l.count("1006032852"))
#print(l)
#t=(1,2,3,4,4,4,5,6)
#print(t.count(4))
#print(l.count())))