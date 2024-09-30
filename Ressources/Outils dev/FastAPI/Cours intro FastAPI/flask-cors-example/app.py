from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    try:
        response = requests.get("http://127.0.0.1:8000/product/all")
        message = response.text
    except Exception as error:
        message = error

    return render_template("home.html", message = message)

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=12345)