from flask import Flask, render_template, request
from src.utils import *

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/start')
def insert():
    open_waste_slot()

    return render_template('insert.html')


@app.route('/waste/pick-type')
def pick_type():
    close_waste_slot()

    return render_template('type.html')


@app.route('/confirmation', methods=['POST'])
def confirmation():
    waste_type = request.form['type']

    process_waste(waste_type)
    return render_template('confirmation.html')


if __name__ == "__main__":
    app.run(debug=True)
