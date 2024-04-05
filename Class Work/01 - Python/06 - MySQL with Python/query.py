from mysql import connector as cnt
db=cnt.connect(
    host='Local',
    user='user',
    password='pass',
    port=3000
)
cur = db.cursor()
cur.execute('SELECT name,salary FROM pw.employee')
for i in cur:
    print(i)
db.close()