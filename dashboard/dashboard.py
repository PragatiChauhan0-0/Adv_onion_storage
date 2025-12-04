# serial_comm.py
import serial
import threading

from flask import Flask, render_template

app = Flask(__name__)

# connect to adruino - read data from serial port

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


# Serial communication setup
PORT = "COM7" 
BAUD = 9600

ser = serial.Serial(PORT, BAUD, timeout=1)

latest_data = {"temp": None, "hum": None, "gas": None}

def listen_serial():
    global latest_data
    while True:
        line = ser.readline().decode().strip()
        if line:
            # Example: "TEMP:25.3,HUM:68,GAS:12"
            parts = line.split(',')
            for p in parts:
                key, value = p.split(':')
                latest_data[key.lower()] = float(value)

threading.Thread(target=listen_serial, daemon=True).start()

def send_command(target, value):
    # Example send: "FAN:150\n"
    ser.write(f"{target}:{value}\n".encode())

if __name__ == '__main__':
    app.run(debug=True)