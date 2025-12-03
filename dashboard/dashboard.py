from flask import Flask, render_template

app = Flask(__name__)

# connect to adruino - read data from serial port

@app.route('/')
def index():
    return render_template('home.html')