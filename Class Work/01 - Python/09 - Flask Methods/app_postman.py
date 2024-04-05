from flask import Flask,request,render_template,redirect,jsonify
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('./index.html')

def math_opr(a,b,opr):
    if opr == 'add':
        return a+b
    elif opr == 'subtract':
        return abs(a-b)
    elif opr=='divide':
        return a/b
    elif opr=='multiply':
        return a*b
    else:
        return 'wrong!'


@app.route('/math',methods=['POST'])
def math():
    if request.method=='POST':
        num1=int(request.json['num1'])
        num2=int(request.json['num2'])
        opr=request.json['operation']
        print(num1,num2,opr)
        result=math_opr(num1,num2,opr)
    return jsonify(result)


if __name__=='__main__':
    app.run(host='localhost',port=4000)