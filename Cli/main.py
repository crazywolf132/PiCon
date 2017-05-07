import socket

def _main():
    _addr = raw_input("Address: ")
    _port = raw_input("PORT: ")


    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((_addr, _port))
    while True:
        _in = raw_input("> ")
        if _in == "end" or _in == "exit" or _in == "quit":
            break
        else:
            clientsocket.send(_in)
