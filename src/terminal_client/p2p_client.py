import socket
import threading


def start():
    # Create threads to run the listen and send functions simultaneously
    listen_thread = threading.Thread(target=listen)
    send_thread = threading.Thread(target=send)

    # Start the threads
    listen_thread.start()
    send_thread.start()

    # Wait for the threads to complete
    listen_thread.join()
    send_thread.join()


def listen():
    # Set up the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the IP address and port number to bind to
    ip_address = ''  # listen on all available network interfaces
    port = 55555  # use any available port

    sock.bind((ip_address, port))

    sock.listen(1)

    print(f"Waiting for connection from other client...")

    connection, client_address = sock.accept()

    print(f"Connection from {client_address[0]} received! Waiting...")

    try:
        while True:
            data = connection.recv(1024)
            if data:
                print(f"{client_address[0]}: {data.decode('utf-8')}")
            else:
                break

    finally:
        # Clean up the connection
        connection.close()
        print(f"Connection from {client_address[0]} closed.")


def send():
    # Set up the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the IP address and port number to connect to
    ip_address = input("Enter the ip address of the other client: >>> ")
    port = 55555  # use the same port number as the server

    sock.connect((ip_address, port))
    print(f"Connected to {ip_address}!")

    while True:
        message = input(">>> ")
        if message:
            sock.sendall(message.encode('utf-8'))
        else:
            break

    sock.close()
