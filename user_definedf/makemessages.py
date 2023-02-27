from socket import *
import base64
import ssl
import time
from user_definedf.send import *
def makemessages(SMTP_host, from_account, from_password, to_account, subject, words,fmsg):

    # Choose a mail server (e.g. Google mail server) and call it mailserver
    mailserver = SMTP_host
    mailUser = from_account
    mailFromAddress = from_account
    mailPassWord = from_password
    mailToAddress = to_account
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
    #msg += '\r\n'.encode()
    #msg += '------=_NextPart_000_0012345JZ\r\n'.encode()
    msg+=fmsg
    return send(SMTP_host, from_account, from_password, to_account,msg)
