# Remote LED Control via ESP32 with Web Interface  
A project to control an LED remotely using an ESP32 microcontroller, a Python Flask backend, and a web interface hosted on Timeweb Cloud.

## Demo  
- "Web Interface": [https://dmitray27-lednf-9cec.twc1.net/](https://dmitray27-lednf-9cec.twc1.net/)  


## Features  
- Real-time LED control via a web interface.  
- Secure HTTPS connection for command transmission.  
- Backend deployed on "Timeweb Cloud".  
- Simple REST API for integration with other services.  

## Technologies  
- "Backend": Python, Flask  
- "Frontend": HTML, JavaScript  
- "Microcontroller": C++, ESP32  
- "Hosting": Timeweb Cloud  
- "Protocols": HTTP, Wi-Fi  

## Setup  
### Hardware Requirements  
- ESP32 Development Board.  
- LED (any color).  
- 220Ω Resistor.  
- Breadboard and Jumper Wires.  

"Connections":  
- "LED Anode (+) → GPIO2" via 220Ω resistor.  
- "LED Cathode (-) → GND" on ESP32.  

### 3. Backend (Flask)  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/dmitray27/lednf.git  
   python app.py
