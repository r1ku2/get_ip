from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    c = dict(request.headers)
    return c

@app.route("/xfor")
def get_xfor():
    a = request.headers["X-Forwarded-For"]
    if a != None:
        return "<p>X-Forwarded-For</p>" + str(a)
    return "<p> None </p>"

if __name__ == '__main__':
    app.run()
