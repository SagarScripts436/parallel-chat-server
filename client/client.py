import socket
import threading
import tkinter as tk
from tkinter import simpledialog
from tkinter import scrolledtext
from tkinter import messagebox

# ===============================
# Configuration
# ===============================
HOST = "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1024

# ===============================
# Connect to Server
# ===============================
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))


class ChatClient:
    def __init__(self, root):
        self.root = root
        self.root.title("Parallel Chat Client")

        # Ask nickname
        self.nickname = simpledialog.askstring("Nickname", "Choose a nickname:", parent=root)

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(root)
        self.chat_area.pack(padx=10, pady=10)
        self.chat_area.config(state='disabled')

        # Message entry
        self.msg_entry = tk.Entry(root)
        self.msg_entry.pack(padx=10, pady=5, fill=tk.X)
        self.msg_entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=5)

        # Start receive thread
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

    def receive_messages(self):
        while True:
            try:
                message = client.recv(BUFFER_SIZE).decode()
                if message == "NICK":
                    client.send(self.nickname.encode())
                else:
                    self.chat_area.config(state='normal')
                    self.chat_area.insert(tk.END, message + "\n")
                    self.chat_area.yview(tk.END)
                    self.chat_area.config(state='disabled')
            except:
                messagebox.showerror("Error", "Connection lost!")
                client.close()
                break

    def send_message(self, event=None):
        message = f"{self.nickname}: {self.msg_entry.get()}"
        client.send(message.encode())
        self.msg_entry.delete(0, tk.END)


# ===============================
# Run GUI
# ===============================
root = tk.Tk()
app = ChatClient(root)
root.mainloop()