from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    Age=request.form.get("Age")
    return render_template("hello.html", name=name,Age=Age)

if __name__=='__main__':
    app.run(debug=True)