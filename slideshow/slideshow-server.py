#!/usr/bin/python3

import socket
import sys
import os
import random
#from subprocess import call

# Photo directory
##imgDir="/home/gzav/img"
imgDir = "/home/gzav/Documents/xavier/git/rpi-stuff/"

# Display traces if True
debug = False

# Executes system commands (fbi startup / shutdown...) if True
exec_sys_commands = False

def getRandomDir(imgPath):

    # List subdirectories
    photodirs = []
    for dirname in os.listdir(imgPath):
        if os.path.isdir(os.path.join(imgPath, dirname)) and dirname[0]!='.':
            photodirs.append(dirname)

    print(photodirs)
    # find a random photo directory to show
    randDir = photodirs[random.randint(0, len(photodirs)-1)]

    print("Selected random directory: %s" % randDir)
    return randDir


def display(dirpath):

    print("Display slideshow: %s" % dirpath)

    if exec_sys_commands:
        os.system("killall fbi && sleep 5")
        ##os.sleep(5)
        # nohup fbi -T 2 -noverbose --autodown -t 6 $RDMDIR/* > /dev/null
        os.system("nohup fbi -T 2 -noverbose --autodown -t 6 %s/* > /dev/null" % dirpath)
        # other fbi test with os.call
        ##call(["nohup", "fbi", "-T 2", "", "", "", "",])


def displayRandomDir(dirname):
    slideshowDir = getRandomDir(dirname)
    print("Display slideshow: %s" % slideshowDir)
    display(os.path.join(dirname, slideshowDir))
    print("Display slideshow: %s" % slideshowDir)
    return slideshowDir


def main():
    # Display random dir by default
    displayRandomDir(imgDir)

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # handle reusing same address if killed (either socket is left in TIME_WAIT state)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Bind the socket to the port
    server_address = ('localhost', 10003)
    print('starting up on %s port %s' % server_address)
    sock.bind(server_address)

    # Listen for incoming connections
    sock.listen(1)

    while True:
        # Wait for a connection
        print('waiting for a connection')
        connection, client_address = sock.accept()

        try:
            print('Slideshow server - connection from ', client_address)
            connection.sendall(b'Welcome on Slideshow server')
            connection.sendall(b'===========================')
            connection.sendall(b'Here is the command list: rand, list, exit (^C)... or type the name of the directory to display')
            connection.sendall(b'> ')

            # Receive the data in small chunks and retransmit it
            while True:
                data = connection.recv(256)
                # remove trailing \r\n
                data = data[:len(data)-2]

                if debug:
                    print("Received <", data, ">")

                # Ask for a random directory to display
                if data == b"rand":
                    slideshowDir = displayRandomDir(imgDir)
                    connection.sendall(b"Display slideshow: %s\n" % slideshowDir.encode())
                # exit
                elif data == b"exit" or data == b"quit" or data == b"\xff\xf4\xff":
                    connection.sendall(b"Bye-bye ;-)")
                    break
                # ask for a specific folder to display
                elif data:
                    slideshowPath = os.path.join(imgDir, data.decode())
                    if os.path.exists(slideshowPath):
                        display(slideshowPath)
                        connection.sendall(b"Display slideshow: %s\n" % slideshowPath.encode())
                    else:
                        connection.sendall(b"Directory doesn't exist: %s\n" % slideshowPath.encode())
                
        finally:
            # Clean up the connection
            connection.close()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopping smartframe server')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

