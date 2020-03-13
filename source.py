"""
5.08.2020
TCP&UDP_PortScanner on Python3.8
by Yaroslav Ilyusin
"""
import socket

global choose  # variable for user choose [TCP or UDP protocol scanning]
global ip  # variable for ip of the server whose ports need to be checked
global port1  # variable for the first port in the scan range
global port2  # variable for the end port in the scan range


def data_reader():
    """Void func. Using for reading data from user"""
    global choose
    global ip
    global port1
    global port2

    print("TCP or UDP?")
    choose = input()
    if not choose == 'TCP' and not choose == 'UDP':  # exception for non-existing protocol
        choose = None
        print('Wrong answer, try again')
        return
    print("Input ip: ")
    ip = input()
    try:
        print("Input first: ")
        port1 = int(input())
        print("Input second: ")
        port2 = int(input())
    except:
        choose = None
        print('Wrong port or ports, expected number.')
        return
    if port1 > port2:
        tmp = port2
        port2 = port1
        port1 = tmp
    pass


def scan_port_tcp(ip: int, port: int):
    """
    scan_port_tcp(ip, port)
    ip: IP address of the server whose ports need to be checked.
    port: The port that you want to check.

    Scanning port on server that use the tcp protocol
    """

    my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # creating new socket type of SOCK_STREAM
    my_sock.settimeout(0.5)  # set timeout for waiting connection
    try:  # starting try to connection
        my_sock.connect((ip, port))
        print('Port: ', port, ' open.')  # print 'Open port' if connection success
        my_sock.close()  # and close connection
    except:
        # print('Port: ', port, 'its close.')
        # uncomment upper the line above for debug closed port
        pass


def scan_port_udp(ip: int, port: int):
    """
    scan_port_udp(ip, port)
    ip: IP address of the server whose ports need to be checked.
    port: The port that you want to check.

    Scanning port on server that use the udp protocol
    """

    my_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # creating new socket type of SOCK_DGRAM
    my_sock.settimeout(5)  # set timeout for waiting connection
    my_sock.sendto(b"Are you open?", (ip, port))  # sending message to custom server
    try:  # start of attempt to receive message from custom server
        bytes_address_pair = my_sock.recvfrom(1024)  # receiving message
    except:
        # print('Port: ', port, 'its close.')
        # uncomment upper the line above for debug closed port
        return  # if message cant receive then 'return'
        pass

    print('Port: ', port, 'its open.')  # else print 'Port open'


while True:  # start of program
    data_reader()  # getting user data
    if choose is not None:
        break

print('Scanning...\n')  # information to the user that everything is fine

for i in range(int(port1), int(port2) + 1):  # start of a loop to iterate over a range of ports
    # print(str(i) + "/" + str(port2))
    if choose == "TCP":  # if user wrote TCP
        scan_port_tcp(ip, i)  # start tcp scanning func
    elif choose == "UDP":  # if user wrote UDP
        scan_port_udp(ip, i)  # start udp scanning func
    else:
        print('Unknown protocol, pls try again later')
        break
    if i == (int(port2)):
        print('\nAll ports checked successful\n')  # information to the user that everything done


