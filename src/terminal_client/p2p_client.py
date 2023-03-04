import os
import socket
import threading

messages = []


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

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((ip_address, port))

    sock.listen(1)

    connection, client_address = sock.accept()

    try:
        while True:
            data = connection.recv(1024)
            if data:
                messages.append({
                    "sender": client_address[0],
                    "message": data.decode('utf-8')
                })
                draw()
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

    while True:
        message = input()
        if message:
            sock.sendall(message.encode('utf-8'))
            messages.append({
                "sender": 'You',
                "message": message
            })
            draw()
        else:
            break

    sock.close()


def draw():
    global messages

    os.system('clear')

    for message in messages[-30:]:
        print(f"{message['sender']}: {message['message']}")
