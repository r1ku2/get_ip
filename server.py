from flask import Flask, render_template, request, make_response
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    c = dict(request.headers)
    return c

@app.route("/xfor")
def hoge_hoge():
    a = request.headers["X-forwarded-For"]
    if a != None:
        return "<p>hoge, hoge!</p>" + str(a)
    return "<p> None </p>"

@app.route("/hello")
def hella_world():
    b = 1
    return render_template("index.html", test=b)

@app.route("/res")
def main():
    resp = make_response("OK")
    resp.headers["X-TEST-HEADER"] = "This is test header."
    return resp

if __name__ == "__main__":
    app.run()
