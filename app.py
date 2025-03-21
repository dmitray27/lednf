# Патчинг gevent должен быть выполнен ПЕРВЫМ
from gevent import monkey
monkey.patch_all()

from flask import Flask, render_template, request, jsonify
from datetime import datetime
import requests
import json
import os
import logging
# from flask_cors import CORS
app = Flask(__name__)
# CORS(app)
# Текущее состояние светодиода (по умолчанию выключен)
led_status = False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control_led():
    global led_status
    action = request.json.get('action')
    if action == 'on':
        led_status = True
    elif action == 'off':
        led_status = False
    return jsonify({'status': 'success', 'led_status': led_status})

@app.route('/get_led_status')
def get_led_status():
    return jsonify({'led_status': led_status})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port , debug=True)
