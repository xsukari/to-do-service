from flask import Flask

app = Flask(__name__)

@app.route("/api/test")
def test():
    return "flask api test"