import mysql.connector as pysql
mydb = pysql.connect(host="localhost",user="root",password="1234",database="practical")
mycursor=mydb.cursor()
mycursor.execute("delete from student where Name ='John'")
mydb.commit()
print("Record deleted...")
mydb.close()