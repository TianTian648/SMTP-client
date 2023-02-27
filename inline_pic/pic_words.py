#改为Python3格式
from socket import *
import base64
import ssl
import os
import time
def send_email_jinx(SMTP_host, from_account, from_password, to_account, subject, words,filename):

    # Choose a mail server (e.g. Google mail server) and call it mailserver
    mailserver = SMTP_host
    mailUser = from_account
    mailFromAddress = from_account
    mailPassWord = from_password
    mailToAddress = to_account
    file_tail=os.path.splitext(filename)[-1]
    #根据附件文件后缀名判断类型
    if file_tail == '.pdf':
        type='application/pdf'
        name='test.doc'
    elif file_tail == '.doc':
        type = 'application/msword'
        name = 'test.word'
    elif file_tail == '.rar':
        type = 'application/x-rar'
        name = 'test.rar'
    elif file_tail == '.txt':
        type = 'application/x-txt'
        name = 'test.txt'
    elif file_tail == '.jpg':
        type = 'image/jpg'
        name = 'test.jpg'
    elif file_tail == '.png':
        type = 'image/png'
        name = 'test.png'
    elif file_tail == '.mp4':
        type = 'vedio/mp4'
        name = 'test.mp4'
    #一个小小的尝试，但是文件损坏
    elif file_tail == '.kgm':
        type ='application/'+file_tail
        name = 'test.mp3'
    else:
        type ='application/'+file_tail
        name='test'+file_tail
    #elif file_tail =='.conf':
        #type = 'application/x-conf'
        #name = 'test.conf'
    with open(filename,"rb") as f:
        file_data = base64.b64encode(f.read())
    temp_b =words.encode("utf-8")  # 将字符串转换为二进制
    content_b = base64.b64encode(temp_b)
    # 构造邮件正文
    msg = 'FROM: ' + mailFromAddress + '\r\n'
    msg += 'TO: ' + mailToAddress +  '\r\n'
    msg += 'Subject: ' + subject +  '\r\n'
    msg += 'Content-Type:multipart/related; boundary="----=_NextPart_000_0012345JZ"\r\n'
    msg += 'MIME-Version: 1.0\r\n'
    msg += '\r\n'
    msg = msg.encode()
    msg += '------=_NextPart_000_0012345JZ\r\n'.encode()
    msg += 'Content-Type: text/plain;\r\n'.encode()# charset=UTF-8
    msg += 'Content-Transfer-Encoding: base64\r\n'.encode()
    msg += '\r\n'.encode()
    msg +=content_b +'\r\n'.encode()
    msg += '\r\n'.encode()
    msg += '\r\n'.encode()
    msg += '------=_NextPart_000_0012345JZ\r\n'.encode()
    #msg += 'Content-Type:application/pdf; name=1234.pdf\r\n'.encode()
    msg += ('Content-Type: '+type+' ;name='+name+'\r\n').encode()
    msg += 'Content-Transfer-Encoding: base64\r\n'.encode()
    msg += 'Content-ID: JZJZJZJZJZJZJZJZ'.encode()
    msg += '\r\n'.encode()
    msg += file_data + "\r\n".encode()
    msg += '\r\n'.encode()
    msg += '------=_NextPart_000_0012345JZ--\r\n'.encode()
    endmsg = "\r\n.\r\n"
    # Create socket called clientSocket and establish a TCP connection with mailserver
    context = ssl.create_default_context()
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, 465))
    clientSocketSSL = context.wrap_socket(clientSocket, server_hostname=mailserver)
    #quit()
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
    MFCommand = 'MAIL FROM: <'+ mailFromAddress + '>\r\n'
    while True:
        clientSocketSSL.send(MFCommand.encode())
        recv = clientSocketSSL.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '250':
            break

    # Send RCPT TO command and print server response.
    RTCommand = 'RCPT TO: <'+ mailToAddress + '>\r\n'
    while True:
        clientSocketSSL.send(RTCommand.encode())
        time.sleep(0.9)
        recv = clientSocketSSL.recv(1024)
        recv = recv.decode()
        print(recv)
        if recv[:3] == '250':
             break
        else :
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


