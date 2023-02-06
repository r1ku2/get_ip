from flask import Flask, render_template, request, make_response
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/hoge")
def hoge_hoge():
    a = request.url
    return "<p>hoge, hoge!</p>" + str(a)

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
