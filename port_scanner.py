from argparse import ArgumentParser
import socket
from threading import Thread
from time import time
from colorama import init, Fore, Style

open_ports = []

RESET   = '\033[39m'
YELLOW  = '\033[33m'

banner ='''
          _                                   _                                 
  __ _  _| |__  ___ _ _   ___   _ __  ___ _ _| |_ ___ __ __ _ _ _  _ _  ___ _ _ 
 / _| || | '_ \/ -_) '_| |___| | '_ \/ _ \ '_|  _(_-</ _/ _` | ' \| ' \/ -_) '_|
 \__|\_, |_.__/\___|_|         | .__/\___/_|  \__/__/\__\__,_|_||_|_||_\___|_|  
     |__/                      |_|                                              
'''


def main_args():
    print(banner)
    print('')
    love = ArgumentParser(description='Python Port Scanner....', epilog="Help %(prog)s -p 20 -ep 1000 -t 500 -V 192.168.12.1")
    love.add_argument('-p', '--start-port', type=int, metavar='', dest='start_port', help='Starting port', default=10)
    love.add_argument('-ep', '--end-port', type=int, metavar='', dest='end_port', help='Ending port', default=6000)
    love.add_argument('-t', '--thread', type=int, dest='thread', metavar='', help='Thread amount', default=500)
    love.add_argument('-v', '--verbose', action='store_true', dest='verbose', help='Verbose output')
    love.add_argument(metavar='Target IP', dest='IP', help='Target IP')
    arg = love.parse_args()
    return arg

def make_port(start_port: int, end_port: int):
    for port in range(start_port, end_port + 1):
        yield port

def scan_port():
    while True:
        try:
            s = socket.socket()
            s.settimeout(1)
            port = next(ports)
            s.connect((arguments.IP, port))
            open_ports.append(port)
            if arguments.verbose:
                print()
                print(f'\r{open_ports}', end='')
        except (ConnectionRefusedError, socket.timeout):
            continue
        except StopIteration:
            break
        except socket.gaierror:
            print()
            print('USE domain only')
            break

def make_thread(thread):
    thread_list = []
    for _ in range(thread):
        thread_list.append(Thread(target=scan_port))
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()

arguments = main_args()
start_time = time()
ports = make_port(arguments.start_port, arguments.end_port)
make_thread(arguments.thread)
end_time = time()

if arguments.verbose:
    print()
print()
print()
print(f"Open ports found: {open_ports}")
print(f"Total time taken: {round(end_time - start_time, 2)} seconds")
