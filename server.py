import os
from flask import Flask, render_template, request
import random
import requests

app = Flask(__name__)
url = "https://www.php.net/manual/ja/function.apache-response-headers.php"

response = requests.head(url)
a =response.headers
b = 1
@app.route('/')
def hello_world():
    return render_template('index.html', test=a, test_2=b)


if __name__ == '__main__':
    app.run()
