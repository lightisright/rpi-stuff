#!/usr/bin/python3

import sys
import os
import smartframe
from tcp_server import TcpServer
import http_server
import threading

# Indicates if script are running on RPI or not (for debug purpose, PIR & FBI management should not be enables)
real_rpi_install = False

debug = False                                           # Display traces if True
imgDir = "/home/gzav/Documents/xavier/git/rpi-stuff/"   # Photo directory (/home/gzav/img)

# HTTP server options
http_hostname = "localhost" # IP or server name
http_port = 8080            # port as integer

# TCP server options
tcp_hostname = "localhost"  # IP or server name
tcp_port = 10003            # port as integer

# PIR management options
shutoff_delay = 300         # seconds
pir_pin = 17                # 11 on the board

# instanciate sf API
sf = smartframe.SmartFrame(imgDir, real_rpi_install)


def start_pir():
    from pir_manager import PirManager
    pm = PirManager(17, 300)
    pm.start()

def start_tcp_server():
    tcps = TcpServer(tcp_hostname, tcp_port, sf, debug)
    tcps.start()

def start_http_server():
    https = http_server.HttpServer(http_hostname, http_port, sf, debug)
    https.start()

def main():

    # enable PIR only if working with real RPI
    t1 = threading.Thread(target=start_pir, args=[])
    if real_rpi_install:
        t1.start()

    # enable TCP server
    t2 = threading.Thread(target=start_tcp_server, args=[])
    t2.start()

    # enable HTTP server
    t3 = threading.Thread(target=start_http_server, args=[])
    t3.start()


    # waiting for thread terminating
    if real_rpi_install:
        t1.join()

    t2.join()
    t3.join()
    print('Exiting...')



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Stopping py-smartframe')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

