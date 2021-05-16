from flask import  Flask
from flask import render_template
from pynput.keyboard import Key, Controller
import time
import sys

print('ok')

keyboard = Controller()


app = Flask(__name__)

@app.route("/")
def hello_world():
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.tab)
    # time.sleep(0.5)
        keyboard.release(Key.tab)
    return  render_template('index.html')
