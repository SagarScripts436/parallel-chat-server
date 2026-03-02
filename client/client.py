import socket
import threading

# ===============================
# Configuration
# ===============================

HOST = "127.0.0.1"   # Change to server IP if running on another machine
PORT = 5000
BUFFER_SIZE = 1024

# ===============================
# Connect to Server
# ===============================

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


# ===============================
# Receive Messages from Server
# ===============================

def receive_messages():
    while True:
        try:
            message = client.recv(BUFFER_SIZE).decode()

            if message == "NICK":
                client.send(nickname.encode())
            else:
                print(message)
        except:
            print("❌ Disconnected from server.")
            client.close()
            break


# ===============================
# Send Messages to Server
# ===============================

def send_messages():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode())


# ===============================
# Start Threads
# ===============================

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()