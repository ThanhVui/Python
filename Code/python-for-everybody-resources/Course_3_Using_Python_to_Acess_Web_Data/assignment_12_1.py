#Exploring the HyperText Transport Protocol

#You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.

#http://data.pr4e.org/intro-short.txt
#There are three ways that you might retrieve this web page and look at the response headers:

#Preferred: Modify the socket1.py program to retrieve the above URL and print out the headers and data.
#Make sure to change the code to retrieve the above URL - the values are different for each URL.
#Open the URL in a web browser with a developer console or FireBug and manually examine the headers that are returned.
#Use the telnet program as shown in lecture to retrieve the headers and content.
#Enter the header values in each of the fields below and press "Submit".

import socket
## Use the socket module to create a socket and connect to the server
## on port 80.
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))## Create a socket object
## Connect to the server on port 80 (HTTP)
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)## Send the command to the server

while True:
    data = mysock.recv(512)## Receive up to 512 bytes of data from the socket
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()


def getSocket():
    host = 'data.pr4e.org'
    port = 80
    url = 'http://data.pr4e.org/intro-short.txt'

    # Create and connect socket
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, port))

    # Send HTTP GET request
    request = f'GET {url} HTTP/1.0\r\nHost: {host}\r\n\r\n'
    mysock.send(request.encode())

    # Receive full response
    full_response = b""
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        full_response += data

    mysock.close()
    return full_response.decode()

# Example usage:
response = getSocket()
print(response)