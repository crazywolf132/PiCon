import socket


print("RUNNING")
s = socket.socket()
print("> Socket created")
host = socket.gethostname()
print("> IP: " + host)
port = 4416
print("> Host: " + str(host) + " Port: " + str(port))

try:
    s.bind((host, port))
except socket.error as msg:
    print("> Bind failed. Error Code : " + str(msg[0]) + " Message " + msg[1])
    exit()

print("> Socket bind complete.")

_ls = [] ## For debugging only.

s.listen(5)
print("> Socket now listening")
while True:
    c, addr = s.accept()

    data = c.recv(1024)
    ## These strip everything from the message.
    _in = data.strip("\x00")
    _in = _in.strip("\x06")
    _in = _in.strip("\t")
    _in = _in.strip("\x08")
    _in = _in.strip("\x0e")
    _in = _in.strip("\n")
    _in = _in.strip("\x0c")

    ### STATUS
    print("GOT - " + _in)
