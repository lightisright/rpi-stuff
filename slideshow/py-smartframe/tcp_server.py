import socket
import sys
import os
import smartframe


class TcpServer:

    def __init__(self, ip, port, smartframe: smartframe.SmartFrame, debug: bool):

        self.ip = ip
        self.port = port
        self.sf = smartframe
        self.debug = debug


    def start(self):

        # Display random dir by default
        self.sf.displayRandomDir()

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # handle reusing same address if killed (either socket is left in TIME_WAIT state)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # Bind the socket to the port
        server_address = (self.ip, self.port)
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

                    if self.debug:
                        print("Received <", data, ">")

                    # Ask for a random directory to display
                    if data == b"rand":
                        slideshowDir = self.sf.displayRandomDir()
                        connection.sendall(b"Display slideshow: %s\n" % slideshowDir.encode())
                    # exit
                    elif data == b"exit" or data == b"quit" or data == b"\xff\xf4\xff":
                        connection.sendall(b"Bye-bye ;-)")
                        break
                    # ask for a specific folder to display
                    elif data:
                        msg = self.sf.display(data.decode())
                        connection.sendall(msg.encode())
                    
            finally:
                # Clean up the connection
                connection.close()

