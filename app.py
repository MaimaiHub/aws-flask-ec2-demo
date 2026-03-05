from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='text-align:center;padding:70px 0;'>Hello World!!!</h1>", 200

app.run(host="0.0.0.0", port=5000)
