#!/usr/bin/python3

import socket
import sys
import os
import smartframe

#from subprocess import call

# Display traces if True
debug = False
# Executes system commands (fbi startup / shutdown...) if True
exec_sys_commands = False

# Photo directory
##imgDir="/home/gzav/img"
imgDir = "/home/gzav/Documents/xavier/git/rpi-stuff/"

def main():

    sf = smartframe.smartframe(exec_sys_commands)

    # Display random dir by default
    sf.displayRandomDir(imgDir)

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
                    slideshowDir = sf.displayRandomDir(imgDir)
                    connection.sendall(b"Display slideshow: %s\n" % slideshowDir.encode())
                # exit
                elif data == b"exit" or data == b"quit" or data == b"\xff\xf4\xff":
                    connection.sendall(b"Bye-bye ;-)")
                    break
                # ask for a specific folder to display
                elif data:
                    slideshowPath = os.path.join(imgDir, data.decode())
                    msg = sf.display(slideshowPath)
                    connection.sendall(msg.encode())
                
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

