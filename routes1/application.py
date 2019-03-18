from flask import Flask

app = Flask(__name__)

@app.route("/<string:name>/",defaults={'name':'world'})
def hello(name):
    return "Hello, {}!".format(name)

if __name__=="__main__":
    app.run(debug=True)