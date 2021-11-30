#Server Program
import socket

HOST = 'localhost' # This machine is the server
PORT = 50007 # Random port for communication

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen()
print('Listen..')
conn, addr = s.accept()
print('Connected with', addr)

def server():
    number_msg = conn.recv(1024).decode('UTF-8')
    number_msg = int(number_msg)
    i = 0
    while i < number_msg:
        print('Waiting for msgs...')
        data = conn.recv(1024)
        str_data = data.decode('UTF-8')
        print('Messages in str: ', str_data)
        i += 1
        conn.sendall(data)

    fin_rest = conn.recv(1024).decode('UTF-8')
    if fin_rest == 'yes':
        print("Finished him!")
        conn.close()
    else:
        print("Restarting transmission...")
        server()
server()