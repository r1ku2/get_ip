import os
from flask import Flask, render_template

app = Flask(__name__)
a = 1+1
@app.route('/')
def hello_world():
    return render_template('index.html', test=a)

@app.route("/hello")
def hello_world():
    return "Hello world"

if __name__ == '__main__':
    app.run()
