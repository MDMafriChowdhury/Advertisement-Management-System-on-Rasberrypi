import socket

def start_listener(host, port):
    # Create a socket object
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to the host and port
        listener.bind((host, port))

        # Listen for incoming connections
        listener.listen(1)
        print(f"Listening on {host}:{port}...")

        # Accept incoming connections
        client_socket, client_address = listener.accept()
        print(f"Accepted connection from {client_address}")

        # Start receiving data
        while True:
            data = client_socket.recv(1024)  # Receive data in 1KB chunks
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the listener and client socket when done
        listener.close()
        client_socket.close()

if __name__ == "__main__":
    host = "SERVER_IP_ADDRESS"  # Replace with the server's IP address or hostname
    port = 8080  # Choose an available port

    start_listener(host, port)
