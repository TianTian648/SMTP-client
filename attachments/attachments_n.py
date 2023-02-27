#改为Python3格式
from socket import *
import base64
import ssl
import os
import time
def send_email_attn(SMTP_host, from_account, from_password, to_account, subject, words,filename1,filename2,filename3):

    # Choose a mail server (e.g. Google mail server) and call it mailserver
    mailserver = SMTP_host
    mailUser = from_account
    mailFromAddress = from_account
    mailPassWord = from_password
    mailToAddress = to_account
    file_tail=os.path.splitext(filename1)[-1]
    file_tail2 = os.path.splitext(filename2)[-1]
    file_tail3 = os.path.splitext(filename3)[-1]
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
    if(filename1!=' '):
        # 根据附件文件后缀名判断类型
        if file_tail == '.pdf':
            file1_type = 'application/pdf'
            file1_name = 'test.pdf'
        elif file_tail == '.doc':
            file1_type = 'application/msword'
            file1_name = 'test.word'
        elif file_tail == '.rar':
            file1_type = 'application/x-rar'
            file1_name = 'test.rar'
        elif file_tail == '.txt':
            file1_type = 'application/x-txt'
            file1_name = 'test.txt'
        elif file_tail == '.jpg':
            file1_type = 'image/jpg'
            file1_name = 'test.jpg'
        elif file_tail == '.png':
            file1_type = 'image/png'
            file1_name = 'test.png'
        elif file_tail == '.mp4':
            file1_type = 'vedio/mp4'
            file1_name = 'test.mp4'
        # 一个小小的尝试，但是文件损坏
        elif file_tail == '.kgm':
            file1_type = 'application/' + file_tail
            file1_name = 'test.mp3'
        else:
            file1_type = 'application/' + file_tail
            file1_name = 'test' + file_tail
        with open(filename1, "rb") as f:
            file_data = base64.b64encode(f.read())
        # elif file_tail =='.conf':
        # type = 'application/x-conf'
        # name = 'test.conf'
        with open(filename1, "rb") as f:
            file_data = base64.b64encode(f.read())
        msg += ('Content-Type: '+file1_type+' ;name='+file1_name+'\r\n').encode()
        msg += 'Content-Transfer-Encoding: base64\r\n'.encode()
        msg += 'Content-ID: JZJZJZJZJZJZJZJZ'.encode()
        msg += '\r\n'.encode()
        msg += file_data + "\r\n".encode()
        msg += '\r\n'.encode()
        msg += '------=_NextPart_000_0012345JZ\r\n'.encode()
    if(filename2!=' '):
        # 根据附件文件后缀名判断类型
        if file_tail2== '.pdf':
            file2_type = 'application/pdf'
            file2_name = 'test.pdf'
        elif file_tail2 == '.doc':
            file2_type = 'application/msword'
            file2_name = 'test.word'
        elif file_tail2 == '.rar':
            file2_type = 'application/x-rar'
            file2_name = 'test.rar'
        elif file_tail2 == '.txt':
            file2_type = 'application/x-txt'
            file2_name = 'test.txt'
        elif file_tail2 == '.jpg':
            file2_type = 'image/jpg'
            file2_name = 'test.jpg'
        elif file_tail2 == '.png':
            file2_type= 'image/png'
            file2_name = 'test.png'
        elif file_tail2 == '.mp4':
            file2_type = 'vedio/mp4'
            file2_name = 'test.mp4'
        else:
            file2_type = 'application/' + file_tail2
            file2_name= 'test' + file_tail2
        with open(filename2, "rb") as f:
            file2_data = base64.b64encode(f.read())
        msg += ('Content-Type: ' + file2_type + ' ;name=' +file2_name + '\r\n').encode()
        msg += 'Content-Transfer-Encoding: base64\r\n'.encode()
        msg += 'Content-ID: JZJZJZJZJZJZJZJZ'.encode()
        msg += '\r\n'.encode()
        msg += file2_data + "\r\n".encode()
        msg += '\r\n'.encode()
        msg += '------=_NextPart_000_0012345JZ\r\n'.encode()
    if(filename3!=' '):
        # 根据附件文件后缀名判断类型
        if file_tail3 == '.pdf':
            file3_type = 'application/pdf'
            file3_name = 'test.pdf'
        elif file_tail3 == '.doc':
            file3_type = 'application/msword'
            file3_name = 'test.word'
        elif file_tail3 == '.rar':
            file3_type = 'application/x-rar'
            file3_name = 'test.rar'
        elif file_tail3 == '.txt':
            file3_type = 'application/x-txt'
            file3_name = 'test.txt'
        elif file_tail3 == '.jpg':
            file3_type = 'image/jpg'
            file3_name = 'test.jpg'
        elif file_tail3 == '.png':
            file3_type = 'image/png'
            file3_name = 'test.png'
        elif file_tail3 == '.mp4':
            file3_type = 'vedio/mp4'
            file3_name= 'test.mp4'
        else:
            file3_type = 'application/' + file_tail3
            file3_name = 'test' + file_tail3
        with open(filename3, "rb") as f:
            file3_data = base64.b64encode(f.read())
        msg += ('Content-Type: ' + file3_type + ' ;name=' +file3_name + '\r\n').encode()
        msg += 'Content-Transfer-Encoding: base64\r\n'.encode()
        msg += 'Content-ID: JZJZJZJZJZJZJZJZ'.encode()
        msg += '\r\n'.encode()
        msg += file3_data + "\r\n".encode()
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
        time.sleep(1.2)
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


