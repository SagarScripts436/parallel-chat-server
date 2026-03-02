import socket
import threading

# Server configuration
HOST = "0.0.0.0"   # Accept connections from any IP
PORT = 5000

# Store connected clients
clients = []
nicknames = []


def broadcast(message):
    """
    Send message to all connected clients
    """
    for client in clients:
        try:
            client.send(message)
        except:
            client.close()
            remove_client(client)


def remove_client(client):
    """
    Remove client from list if disconnected
    """
    if client in clients:
        index = clients.index(client)
        nickname = nicknames[index]
        clients.remove(client)
        nicknames.remove(nickname)
        broadcast(f"{nickname} left the chat.\n".encode())
        print(f"{nickname} disconnected.")


def handle_client(client):
    """
    Handle messages from a single client
    """
    while True:
        try:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message)
        except:
            remove_client(client)
            break


def receive_connections():
    """
    Accept incoming client connections
    """
    print("🚀 Server is running...")
    print(f"Listening on port {PORT}...\n")

    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Ask for nickname
        client.send("NICK".encode())
        nickname = client.recv(1024).decode()

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname: {nickname}")
        broadcast(f"{nickname} joined the chat!\n".encode())
        client.send("Connected to the server!\n".encode())

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


# Start server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

receive_connections()