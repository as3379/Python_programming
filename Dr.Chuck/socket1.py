import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('www.pythonlearn.com', 80))
cmd = 'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.1\r\nHost: www.pythonlearn.com\r\n\r\n'.encode
mysocket.send()

while True:
    data = mysocket.recv(512)
    if (len(data) < 1):
        break
    print(data)

mysocket.close()
