from flask import Flask,request
app=Flask(__name__)

@app.route("/")
def home():
    return '<h1>Hello World!</h1>'

@app.route("/2")
def home2():
    return '<h1>Hello World2!</h1>'

@app.route("/3")
def home3():
    return '<h1>Hello World3!</h1>'

@app.route("/test")
def home4():
    data=request.args.get('x')
    return 'this is the data from my url {}'.format(data)

if __name__=='__main__':
    app.run(host='localhost',port=4000)