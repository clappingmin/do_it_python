from flask import Flask,request,render_template,send_from_directory,redirect,url_for
import os

app = Flask(__name__)

UPLOAD_DIRECTORY = os.path.dirname(__file__)+'/files'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

@app.route('/') #첫번째 페이지
def index():
    return render_template('index.html')

@app.route('/resume', methods=['GET','POST'])
def upload():
    result = request.form
    return render_template('resume.html',result=result)

@app.route('/fileupload')
def fileupload():
    return render_template('list.html')

@app.route('/fileupload', methods=['GET','POST'])
def upload_file():
    if request.method=='POST':
        f=request.files['file'] #내부의 file은 upload.html의 file
        dirname=os.path.dirname(__file__)+'/files/'+f.filename
        #print(dirname)
        f.save(dirname)
    return redirect('/files')

@app.route('/files')
def list_files():
    files=[]
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    #return jsonify(files)
    return render_template('list.html',files=files)

@app.route('/files/<path:path>')
def get_file(path):
    return send_from_directory(UPLOAD_DIRECTORY,path,as_attachment=True)


if __name__ =='__main__':
    app.run(debug=True,port=8879)