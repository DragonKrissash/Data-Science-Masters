from mysql import connector as cnt
db=cnt.connect(
    host='Local',
    user='user',
    password='pass',
    port=3000
)
cur=db.cursor()
cur.execute('insert into pw.employee values(2,"sudhanshu",25000)')
cur.execute('insert into pw.employee values(3,"sudhanshu",25000)')
cur.execute('insert into pw.employee values(4,"sudhanshu",25000)')
cur.execute('insert into pw.employee values(5,"sudhanshu",25000)')
db.commit()
db.close()