from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

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
    app.run(host='0.0.0.0', port=port, debug=True)
