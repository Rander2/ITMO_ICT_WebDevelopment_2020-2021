import socket

if __name__ == '__main__':
    sock = socket.socket()
    sock.connect(('localhost', 9090))
    data = input('enter base length and height separated by a space\n')
    sock.send(data.encode("utf-8"))
    data = sock.recv(1024)
    sock.close()

    print(data.decode("utf-8"))
