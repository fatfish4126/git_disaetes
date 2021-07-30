from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template("form.html")

@app.route('/<name>')
def hello(name):
    return "Hello" + name + "!!!" 

if __name__=="__main__":
    app.run()