import socket
import argparse

# Parse Arguments
parser = argparse.ArgumentParser()
parser.add_argument('-a', default='10.0.5.69')
parser.add_argument('-s', default=9000)
parser.add_argument('-c', default=6671)
parser.add_argument('-i', default='e3e22884')
args = parser.parse_args()
STUDENT_ID = args.i
HOST = args.a
SRC_PORT = int(args.c)
DST_PORT = int(args.s)

# Initialize Variables
ADDR = (HOST, int(DST_PORT))
TRANSACTION_ID = '12345678' 
TYPE = int(0b1000)
PULL_BYTE = '00000'
PULL_SIZE = '00000'
UIN = '0000000'
UIN_ANS = '0'
DATA = '0'

# Initiate UDP connection
UDP_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the UDP socket to host and port
UDP_SOCKET.bind(('', SRC_PORT))

# Send an Initiate Packet
UDP_SOCKET.sendto(f'{STUDENT_ID}{TRANSACTION_ID}{TYPE}{PULL_BYTE}{PULL_SIZE}{UIN}{UIN_ANS}/{DATA}'.encode(), ADDR)

# Receive Accept Packet
data, addr = UDP_SOCKET.recvfrom(1024)
transaction = data.decode()
print(transaction)