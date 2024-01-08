from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("home.html", message = "Hello Multicolor World! I hope you like this amazing and uselessly long rainbow sentence :)")

if __name__ == "__main__":
    app.run()
    
