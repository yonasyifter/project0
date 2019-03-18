from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('new.html')
@app.route('/index',methods=['POST'])
def newe():
    name=request.form.get('name')
    return render_template('index.html',name=name)

if __name__=='__main__':
    app.run(debug=True)