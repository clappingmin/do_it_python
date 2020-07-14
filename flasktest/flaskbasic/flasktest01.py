from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html') #html 문서 호출

@app.route('/cakes')
def cakes():
    return "cheese cakes!"

@app.route('/user/<username>') #user밑에 username이름으로 가져옴
def show_user_profile(username):
    return 'User %s'%username

@app.route('/user/<username>/<int:age>')
def show_user_profile_age(username,age):
    return 'Username %s, 나이 %d'%(username,age)




if __name__ =='__main__':
    app.run(debug = True,port = 8889)