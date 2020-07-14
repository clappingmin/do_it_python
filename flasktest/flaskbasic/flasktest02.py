from flask import Flask,request, render_template

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/method/',methods=['GET','POST']) #요청값 처리 위에 app선언한거 따라감 안적으면 기본 get방식
def login(): #이름은 보통 url에 맞춤
    if request.method =='POST': #넘어오는 방식이 POST면
        return 'Post'
    else :
        return 'Get'

@app.route('/login') #http://127.0.0.1:8889/login?name=tnals
def login1(): #함수 이름은 무조건 달아야한다. get 방식
    user = request.args.get('name')
    return 'User %s'%user   

@app.route('/login',methods=['POST']) #얘는 같아도 되는데
def login2():                         #함수이름은 달라야 한다.
    username = request.form['username']
    pw = request.form['password'] #딕셔너리
    return 'Username: %s, pw: %s'%(username,pw)

if __name__=='__main__': #자기파일에서 호출되면 name이 들어가고 다른곳에서 호출되면 name에 파일명이 들어감 
    app.run(debug = True,port=8889)