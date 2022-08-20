import socket
import argparse

# Initialize Variables
parser = argparse.ArgumentParser()
parser.add_argument('-a', default='10.0.5.69')
parser.add_argument('-s', default=9000)
parser.add_argument('-c', default=6671)
parser.add_argument('-i', default='e3e22884')
args = parser.parse_args()

STUDENT_ID = args.i
HOST = args.a
SRC_PORT = args.c
DST_PORT = args.s
ADDR = (HOST, SRC_PORT)
ADDR2 = (HOST, DST_PORT)

TRANSACTION_ID = '12345678' # check if pwede lagyan ng value
TYPE = '8'
PULL_BYTE = '00000'
PULL_SIZE = '00000'
UIN = '0000000'
UIN_ANS = '0'
DATA = '0'

# Initiate UDP connection
UDP_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the UDP scoket to host and port
UDP_SOCKET.bind(ADDR)

def main():
    
    # Send an Initiate Packet
    UDP_SOCKET.sendto(f'{STUDENT_ID}{TRANSACTION_ID}{TYPE}{PULL_BYTE}{PULL_SIZE}{UIN}{UIN_ANS}/{DATA}'.encode(), ADDR2)
    data, addr = UDP_SOCKET.recvfrom(1024)
    transaction = data.decode()
    print(transaction)

if __name__ == "__main__":
    main()