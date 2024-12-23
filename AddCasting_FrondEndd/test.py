import vncdotool.api

# IP address and port number of the VNC server
vnc_server_ip = "192.168.2.194"
vnc_server_port = 5900  # Default VNC port is 5900

# Connect to VNC server
client = vncdotool.api.connect(vnc_server_ip)
try:
    # Perform actions on the VNC server
    client.keyPress("control")
    client.keyPress("alt")
    client.keyPress("t")
    # Add more actions as needed
finally:
    # Close the connection
    client.close()
