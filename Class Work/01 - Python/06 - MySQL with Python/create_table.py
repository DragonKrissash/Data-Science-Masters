from mysql import connector as cnt
db=cnt.connect(
    host='Local',
    user='user',
    password='pass',
    port=3000
)
cur=db.cursor()
cur.execute('CREATE TABLE if not exists test.employee(id INT UNIQUE PRIMARY KEY, name VARCHAR(50),salary INT);')
db.close()