from socket import socket, AF_INET, SOCK_STREAM

try:
    while True:
        CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)
        CLIENT_SOCK.connect(('localhost', 8080))
        TIME_BYTES = CLIENT_SOCK.recv(1024)
        CLIENT_SOCK.close()
        print(f"Текущее время: {TIME_BYTES.decode('utf-8')}")
finally:
    CLIENT_SOCK.close()
