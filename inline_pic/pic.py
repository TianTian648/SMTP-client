#改为Python3格式
from socket import *
import base64
import ssl
import os
import time
from inline_pic.gethtml  import *
def send_email_img_inline(SMTP_host, from_account, from_password, to_account, subject, words,filename1,filename2,filename3):

    # Choose a mail server (e.g. Google mail server) and call it mailserver
    mailserver = SMTP_host
    mailUser = from_account
    mailFromAddress = from_account
    mailPassWord = from_password
    mailToAddress = to_account
    # transfer image and html
    with open(gethtml(words,filename1,filename2,filename3),"rb") as f:
        html_data = base64.b64encode(f.read())
    with open(filename1,"rb") as f:
        image_data=base64.b64encode(f.read())
    temp_b = words.encode("utf-8")  # 将字符串转换为二进制
    content_b = base64.b64encode(temp_b)
    # 构造邮件正文C:\Users\xietian\Desktop\UI\images/nilu.gif
    msg = 'FROM: ' + mailFromAddress + '\r\n'
    msg += 'TO: ' + mailToAddress +  '\r\n'
    msg += 'Subject: ' + subject +  '\r\n'
    msg += 'Content-Type:multipart/related; boundary="----=_NextPart_000_0012345JZ"\r\n'
    msg += 'MIME-Version: 1.0\r\n'
    msg += '\r\n'
    msg = msg.encode()
    msg += '------=_NextPart_000_0012345JZ\r\n'.encode()
    '''
    msg += 'Content-Type: text/plain;\r\n'.encode()  # charset=UTF-8
    msg += 'Content-Transfer-Encoding: base64\r\n'.encode()
    msg += '\r\n'.encode()
    msg += content_b + '\r\n'.encode()
    msg += '\r\n'.encode()
    msg += '\r\n'.encode()
    msg += '------=_NextPart_000_0012345JZ\r\n'.encode()
    '''
    msg += 'Content-Type: text/html; charset=UTF-8\r\n'.encode()
    msg += 'Content-Transfer-Encoding: base64\r\n'.encode()
    msg += '\r\n'.encode()
    msg += html_data
    msg += '\r\n'.encode()
    msg += '\r\n'.encode()
    msg += '------=_NextPart_000_0012345JZ\r\n'.encode()
    msg += 'Content-Type: img/jpg; name=test.jpg\r\n'.encode()
    msg += 'Content-Transfer-Encoding: base64\r\n'.encode()
    msg += 'Content-ID: JZJZJZJZJZJZJZJZ'.encode()
    msg += '\r\n'.encode()
    msg += image_data + "\r\n".encode()
    msg += '\r\n'.encode()
    msg += '------=_NextPart_000_0012345JZ--\r\n'.encode()
    endmsg = "\r\n.\r\n"

    # Create socket called clientSocket and establish a TCP connection with mailserver
    context = ssl.create_default_context()
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, 465))
    clientSocketSSL = context.wrap_socket(clientSocket, server_hostname=mailserver)
    # quit()
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] != '220':
        print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO mailserver\r\n'
    while True:
        clientSocketSSL.send(heloCommand.encode())
        recv = clientSocketSSL.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '250':
            break

    # 登录过程
    loginCommand = 'auth login\r\n'
    while True:
        clientSocketSSL.send(loginCommand.encode())
        recv = clientSocketSSL.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '334':
            break

    # 邮箱账户经过base64编码
    userCommand = base64.b64encode(mailUser.encode()) + b'\r\n'
    while True:
        clientSocketSSL.send(userCommand)
        recv = clientSocketSSL.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '334':
            break

    # 邮箱密码经过base64编码 这里不展示密码了
    passCommand = base64.b64encode(mailPassWord.encode()) + b'\r\n'
    while True:
        clientSocketSSL.send(passCommand)
        recv = clientSocketSSL.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '235':
            break

    # Send MAIL FROM command and print server response.
    MFCommand = 'MAIL FROM: <' + mailFromAddress + '>\r\n'
    while True:
        clientSocketSSL.send(MFCommand.encode())
        recv = clientSocketSSL.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '250':
            break

    # Send RCPT TO command and print server response.
    RTCommand = 'RCPT TO: <' + mailToAddress + '>\r\n'
    while True:
        clientSocketSSL.send(RTCommand.encode())
        time.sleep(0.9)
        recv = clientSocketSSL.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '250':
            break
        else:
            clientSocket.close()
            return 0

    # Send DATA command and print server response.
    DATACommand = 'DATA\r\n'
    while True:
        clientSocketSSL.send(DATACommand.encode())
        recv = clientSocketSSL.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '354':
            break

    # Send message data.
    clientSocketSSL.send(msg)

    # Message ends with a single period.
    while True:
        clientSocketSSL.send(endmsg.encode())
        time.sleep(0.9)
        recv = clientSocketSSL.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '250':
            break
        else:
            clientSocket.close()
            return 0

    # Send QUIT command and get server response.
    QUITCommand = 'QUIT\r\n'
    while True:
        clientSocketSSL.send(QUITCommand.encode())
        recv = clientSocketSSL.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '221':
            clientSocketSSL.close()
            return 221
        else:
            clientSocket.close()
            return 0