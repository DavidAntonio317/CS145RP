import hashlib
import socket
import time
import random

HOST = '127.0.0.1'
PORT = 6671
ADDR = (HOST, PORT)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('',9000))

uid = sock.recv(512) # begin transaction
uid = uid.decode()
print(uid)
sock.sendto(uid[8:16].encode(), ADDR) # respond with id

# def checksum(packet):
#     return hashlib.md5(packet.encode('utf-8')).hexdigest()

# i = 0
# while True:
#     time.sleep(.8)
#     data = sock.recv(512)
#     data = data.decode()

#     if int(data[12:19]) < i:
#         print(data)
#         continue

#     if len(data[35:]) > 10:
#         continue

#     print('{} {}'.format(i, data))
    
#     sock.sendto('ACK{}TXN{}MD5{}'.format(str(i).zfill(7), uid, checksum(data)).encode(), ADDR)
#     i+=len(data[35:])

#     if data[34] == '1':
#         break