from flask import Flask, request, jsonify, redirect, send_from_directory
import paramiko
import subprocess
import time
import pyautogui
from flask_cors import CORS
app = Flask(__name__)


def close_terminal_session(hostname, username, password):
    # Establish SSH connection
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)

    # Close terminal session
    stdin, stdout, stderr = client.exec_command('pkill -f terminal')

    # Print the output of the command
    output = stdout.read().decode('utf-8')

    # Close the SSH connection
    client.close()
    return output

def reboot_remote_raspberry_pi(hostname, username, password):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(hostname, username=username, password=password)

        stdin, stdout, stderr = client.exec_command('sudo reboot')
        output = stdout.read().decode('utf-8')

        client.close()
        return jsonify({'message': 'Raspberry Pi is rebooting.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def connect_to_raspberry_pi(pi_ip):
    realvnc_path = "C:\\Program Files\\RealVNC\\VNC Viewer\\vncviewer.exe"
    try:
        subprocess.Popen([realvnc_path, f"{pi_ip}::5900"])
        time.sleep(5)
        pyautogui.typewrite("pi")
        pyautogui.press("tab")
        
        pyautogui.typewrite("pi")
        pyautogui.press("enter")

        # time.sleep(5)
        # pyautogui.hotkey('ctrl', 'alt', 't')
        return jsonify({'message': 'Connected to Raspberry Pi.'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/execute_script', methods=['POST'])
def execute_script():
    data = request.get_json()
    action = data.get('action')
    hostname = "192.168.2.194"
    username = "pi"
    password = "pi"  

    if action == 'schedule':
        redirect_url = 'https://docs.google.com/spreadsheets/d/13W2KsylmaPssAKXmk0_eo51duvMMiNubFihqrLqLxmE/edit#gid=0'  # Modify this with your desired redirect URL
        return jsonify({'redirect_url': redirect_url})
    elif action == 'restart':
        return reboot_remote_raspberry_pi(hostname, username, password)
    elif action == 'status':
        return connect_to_raspberry_pi(hostname)
    elif action == 'close_terminal':
        return close_terminal_session(hostname, username, password)
    else:
        return jsonify({'error': 'Invalid action'}), 400
    

def redirect_new_tab(url):
    return redirect(url)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)
