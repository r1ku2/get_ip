from flask import Flask, request

@app.route("/")
def hello_world():
    c = dict(request.headers)
    return c

@app.route("/xfor")
def get_xfor():
    a = request.headers["X-forwarded-For"]
    if a != None:
        return "<p>hoge, hoge!</p>" + str(a)
    return "<p> None </p>"

if __name__ == '__main__':
    app.run()
