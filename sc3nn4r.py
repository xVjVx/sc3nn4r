"""
    Programmer.....: (C) xVjVx
    Date...........: 17/03/2023
    Version........: V1.0.0
    About..........: SC3NN4R
"""

# Importing Libraries
import socket
import sys

# Constant Variables
HOST = str(input("[+] Host: "))
PORTS = str(input("[+] Ports: "))

TIME_OUT = 0.5

def main():

    portsList = list(map(int, PORTS.split()))

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(TIME_OUT)
        print("[-] Testing " + HOST + "...")

        for port in portsList:
            responseCode = client.connect_ex((HOST, port))

            if responseCode == 0:
                print("[-] Port " + str(port) + " is open")
            else:
                print("[-] Port " + str(port) + " is closed")
    except OSError:
        print("[!] Something went wrong")
        sys.exit(0)

if __name__ == '__main__':
    main()