from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/') #바로 호출했을 때
def index():
    return render_template('form_input.html')

@app.route('/login',methods=['POST'])
def login():
    result = request.form
    return render_template('form_result_test.html',result=result)



if __name__ == '__main__':
    app.run(debug=True,port=8089)

# html에서
# <!--for문 쓸때 {% %} 사용 데이터는 {{}}-->
# <!--flasktest03 12번째줄의 앞의 result-->