import os
from flask import Flask, render_template, request
import random
import requests

app = Flask(__name__)
url = "https://www.php.net/manual/ja/function.apache-response-headers.php"

response = requests.head(url)
a =response.headers

@app.route('/')
def hello_world():
    url_2 = request.url
    response_2 = requests.head(url_2)
    b =response_2.headers
    return render_template('index.html', test=a, test_2=b)


if __name__ == '__main__':
    app.run()
