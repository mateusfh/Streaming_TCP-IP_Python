# Client program
import socket

#HOST = '192.168.0.108'    # The remote host (INSERT IP FROM SERVER)
HOST = '127.0.0.1'    # This is local IP. Change for IPV4 from server!
PORT = 50007          # The same port as used by the server!
data = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while 1:
    try:
        s.connect((HOST, PORT))
    except:
        continue
    else:
        break

def client():
    msgs =  input('How many msgs do you like send? ')
    if msgs.isnumeric():
        s.sendall(str.encode(msgs))
        msgs = int(msgs)
    else:
        print("Enter a positive integer for the qty of messages!")
        return client()
    for i in range(msgs):
        s.sendall(str.encode(input('What is the msg? ')))

    data = s.recv(1024)
    if data:
        print('Good job! All msgs arrived! ', data.decode)

    fin_rest = input("Do you need finished transmission? (Say yes for accept) ")
    if fin_rest == 'yes':
        print("Finished him!")
        s.sendall(str.encode(fin_rest))
        s.close()
    else:
        s.sendall(str.encode(fin_rest))
        return client()

client()