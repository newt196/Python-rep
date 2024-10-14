import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'Nate':
                client.send(name_entry.get().encode('ascii'))
            else:
                chat_area.configure(state='normal')
                chat_area.insert(tk.END, message + '\n')
                chat_area.configure(state='disabled')
                chat_area.yview(tk.END)
        except:
            print("An error occurred!")
            client.close()
            break

def send_message(event=None):
    message = f'{name_entry.get()}: {message_entry.get()}'
    client.send(message.encode('ascii'))
    message_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Chat???")

chat_area = scrolledtext.ScrolledText(window, state='disabled', wrap=tk.WORD)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

name_label = tk.Label(window, text="Name Kudasai:")
name_label.pack(pady=5)

name_entry = tk.Entry(window)
name_entry.pack(pady=5)

message_label = tk.Label(window, text="Enter your message:")
message_label.pack(pady=5)

message_entry = tk.Entry(window)
message_entry.pack(pady=5)
message_entry.bind("<Return>", send_message)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 1234))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

window.mainloop()
