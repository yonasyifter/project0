from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/more")
def more():
    return render_template("more.html")
@app.route("/index", methods=["GET","POST"])
def index():
    name=request.form.get('name')
    age=request.form.get('age')
    if age <21:
        return render_template("index.html",name=name)
    else:
        return render_template('error.html')

if __name__=="__main__":
    app.run(debug=True)