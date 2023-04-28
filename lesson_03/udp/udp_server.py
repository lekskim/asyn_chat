from socket import socket, AF_INET, SOCK_DGRAM, SOL_SOCKET, SO_REUSEADDR, SO_BROADCAST

SERV_SOCK = socket(AF_INET, SOCK_DGRAM)
SERV_SOCK.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
SERV_SOCK.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
SERV_SOCK.bind(('', 8080))

try:
    while True:
        MSG, ADDR = SERV_SOCK.recvfrom(1024)
        print(ADDR)
        print(MSG.decode('utf-8'))
        ANS = 'Привет, клиент'
        SERV_SOCK.sendto(ANS.encode('utf-8'), ADDR)
finally:
    SERV_SOCK.close()
