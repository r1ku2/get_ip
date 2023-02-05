import os
from flask import Flask, render_template
import random

app = Flask(__name__)
a = random.random()
@app.route('/')
def hello_world():
    return render_template('index.html', test=a)

if __name__ == '__main__':
    app.run()
