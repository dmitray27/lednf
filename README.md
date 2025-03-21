# Web-Based Remote Control of LED and Relay via ESP32 over Wi-Fi. A system that allows real-time control of connected devices through a browser interface. [![Live Demo](https://img.shields.io/badge/Live_Demo-Timeweb_Cloud-blue)](https://dmitray27-lednf-9cec.twc1.net/)

A project for remote control of LED and Relay  via ESP32 microcontroller and a Flask-based web interface hosted on Timeweb Cloud.

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://python.org)
[![ESP32](https://img.shields.io/badge/ESP32-v4.4.1-green?logo=espressif)](https://espressif.com)
[![License](https://img.shields.io/badge/License-MIT-red)](https://opensource.org/licenses/MIT)
[![Last Commit](https://img.shields.io/github/last-commit/dmitray27/lednf)](https://github.com/dmitray27/lednf/commits/main)

## 🌐 Live Demo
**Web Interface**: [https://dmitray27-lednf-9cec.twc1.net/](https://dmitray27-lednf-9cec.twc1.net/)

## 🚀 Features
- Real-time control of LED and Relay via a web interface
- Secure HTTPS connection
- REST API for third-party integrations
- Auto-refreshing status updates (no page reload)
- Action logging (ON/OFF events)

## 🛠 Technologies
| Component       | Technologies               |
|-----------------|----------------------------|
| Microcontroller | ESP32 (C++, Arduino IDE)    |
| Backend         | Python Flask               |
| Frontend        | HTML5, JavaScript    |
| Hosting         | Timeweb Cloud      |
| Security        | HTTPS, Rate Limiting       |

## 📦 Installation

### Hardware Requirements
1. **ESP32** (any variant)
2. Relay module Songle SRD-03VDC-SL-C and similar models
3. LED (any color)
4. 220Ω Resistor
5. Breadboard and jumper wires

### Software Setup
1. Clone the repository:
```bash
git clone https://github.com/dmitray27/lednf.git
cd lednf 
```
2. Install Flask dependencies:

```bash 
pip install -r requirements.txt
```

3. Start the server:
```bash 
python app.py  # For development
# For production:
gunicorn --bind 0.0.0.0:80 app:app
```

## 🖥 Web Interface Preview

Web Interface

## 🌍 Deployment

On Timeweb Cloud server.

<!-- ## Пин-аут ESP32

| Компонент    | GPIO  | Назначение          |
|--------------|-------|---------------------|
| Светодиод    | GPIO2 | Индикация состояния |
| Реле         | GPIO4 | Управление нагрузкой |-->


