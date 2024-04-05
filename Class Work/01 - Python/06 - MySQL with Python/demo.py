import mysql.connector 
db=mysql.connector.connect(
    host='Local',
    user='user',
    password='pass',
    port=3000
)
cursor=db.cursor()
cursor.execute('USE student_registration')
cursor.execute('SELECT * FROM student_data')
for x in  cursor:
    print (x)
db.close()