#改为Python3格式
import time
from socket import *
import base64
# Choose a mail server (e.g. Google mail server) and call it mailserver
def verify(mailsever,mailUser,mailPassWord):

    msg = 'FROM: ' + mailUser + '\r\n'
    msg += 'TO: ' + '\r\n'
    msg += 'Subject: ' + 'test' +  '\r\n'
    endmsg = "\r\n.\r\n"
    # Create socket called clientSocket and establish a TCP connection with mailserver
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailsever, 25))
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO mailserver\r\n'
    while True:
        clientSocket.send(heloCommand.encode())
        recv = clientSocket.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '250':
            break
        else :
            clientSocket.close()
            return 0


    # 登录过程
    loginCommand = 'auth login\r\n'
    while True:
        clientSocket.send(loginCommand.encode())
        recv = clientSocket.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '334':
            break
        else :
            clientSocket.close()
            return 0

    # 邮箱账户经过base64编码
    userCommand = base64.b64encode(mailUser.encode()) + b'\r\n'
    while True:
        clientSocket.send(userCommand)
        recv = clientSocket.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '334':
            break
        else :
            clientSocket.close()
            return 0

    # 邮箱密码经过base64编码 这里不展示密码了
    passCommand = base64.b64encode(mailPassWord.encode()) + b'\r\n'
    while True:
        clientSocket.send(passCommand)
        time.sleep(1)
        recv = clientSocket.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '235':
            break
        else :
            clientSocket.close()
            return 0
    # Send QUIT command and get server response.
    QUITCommand = 'QUIT\r\n'
    while True:
        clientSocket.send(QUITCommand.encode())
        time.sleep(1)
        recv = clientSocket.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '221':
            clientSocket.close()
            return 221


