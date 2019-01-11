import socket
import sys
import os
import random
#from subprocess import call

# Photo directory
##imgDir="/home/gzav/img"
imgDir = "/home/gzav/Documents/xavier/git/rpi-stuff/"


def getRandomDir(imgPath):

    # List subdirectories
    photodirs = []
    for dirname in os.listdir(imgPath):
        if os.path.isdir(os.path.join(imgPath, dirname)) and dirname[0]<>'.':
            photodirs.append(dirname)

    print(photodirs)
    # find a random photo directory to show
    randDir = photodirs[random.randint(0, len(photodirs)-1)]

    print "Selected random directory: %s" % randDir
    return randDir


def display(dirpath):

    print "Display slideshow: %s" % dirpath

    ##os.system("killall fbi")
    ##sleep(5)

    # nohup fbi -T 2 -noverbose --autodown -t 6 $RDMDIR/* > /dev/null
    ##os.system("nohup fbi -T 2 -noverbose --autodown -t 6 %s/* > /dev/null" % dirpath)
    
    # other fbi test with os.call
    #call(["nohup", "fbi", "-T 2", "", "", "", "",])


def displayRandomDir(dirname):

    slideshowDir = getRandomDir(dirname)
    print "Display slideshow: %s" % slideshowDir
    display(os.path.join(dirname, slideshowDir))
    print "Display slideshow: %s" % slideshowDir



# Display random dir by default
displayRandomDir(imgDir)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# handle reusing same address if killed (either socket is left in TIME_WAIT state)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to the port
server_address = ('localhost', 10003)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()

    try:
        print >>sys.stderr, 'Slideshow server - connection from ', client_address
        connection.sendall('Welcome on Slideshow server')
        connection.sendall('===========================')
        connection.sendall('Here is the command list: rand, list... or type the name of the directory to display')
        connection.sendall('> ')

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            # remove trailing \n
            data = data[:len(data)-1]
            print >>sys.stderr, 'received "%s"' % data
            # Ask for a random directory to display
            if data == "rand":
                displayRandomDir(imgDir)
                connection.sendall("Display slideshow: %s" % slideshowDir)
            # ask for a specific folder to display
            elif data:
                slideshowPath = os.path.join(imgDir, data)
                if os.path.exists(slideshowPath):
                    display(slideshowPath)
                    connection.sendall("Display slideshow: %s" % slideshowPath)
                else:
                    connection.sendall("Directory doesn't exist: %s" % slideshowPath)
            else:
                print >>sys.stderr, 'no more data from', client_address
                break
            
    finally:
        # Clean up the connection
        connection.close()


