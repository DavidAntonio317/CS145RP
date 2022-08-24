# CS145RP

David Antonio
2018-00087
CS 145
Lab 1

Replacement Project
Pull-Centric UDP-based Protocol (Replacement
Project)
A.Y. 2021-2022, 2nd Semester
=================================================  README FILE  ========================================================

Instructions on how to run client.py:

1. Open an Amazon EC2 instance. SSH into the instance.
3. Get a copy of client.py via UvLe or via GitHub. Recommended to clone the repository via "sudo git clone https://github.com/DavidAntonio317/CS145RP"
4. Open in your instance the directory which contains client.py. If CS145 repository was cloned to your instance, get in the "CS145RP" directory.
5. Type (with specified values): "python3 client.py -a <IP address of receiver> -s <receiver port> -c <sender port> -i <Unique ID>". Press Enter.
6. Wait for transaction ID to be printed on your console.

**Note**
This implementation (level 1) expects client.py to send an Initiate Packet (to the receiver or test server), and
receive an Accept Packet (from the receiver or test server) which contains the Transction ID.


==============================================  END OF README FILE  ========================================================
