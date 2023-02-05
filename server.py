import os
from flask import Flask, render_template
import random
import requests

app = Flask(__name__)
url = "https://www.php.net/manual/ja/function.apache-response-headers.php"
response = requests.head(url)
print(response.headers)
a =. response.headers

@app.route('/')
def hello_world():
    return render_template('index.html', test=a)

if __name__ == '__main__':
    app.run()
