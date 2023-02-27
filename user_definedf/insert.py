import os
import base64
def insert1(filename):
    file_tail = os.path.splitext(filename)[-1]
    # 根据附件文件后缀名判断类型
    if file_tail == '.pdf':
        type = 'application/pdf'
        name = 'test.pdf'
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
    # 一个小小的尝试，但是文件损坏
    elif file_tail == '.kgm':
        type = 'application/' + file_tail
        name = 'test.mp3'
    else:
        type = 'application/' + file_tail
        name = 'test' + file_tail
    # elif file_tail =='.conf':
    # type = 'application/x-conf'
    # name = 'test.conf'
    with open(filename, "rb") as f:
        file_data = base64.b64encode(f.read())
    msg = '------=_NextPart_000_0012345JZ\r\n'.encode()
    msg += ('Content-Type: ' + type + ' ;name=' + name + '\r\n').encode()
    msg += 'Content-Transfer-Encoding: base64\r\n'.encode()
    msg += 'Content-ID: JZJZJZJZJZJZJZJZ'.encode()
    msg += '\r\n'.encode()
    msg += file_data + "\r\n".encode()
    msg += '\r\n'.encode()
    #msg += '------=_NextPart_000_0012345JZ\r\n'.encode()
    return msg
