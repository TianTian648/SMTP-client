import webbrowser
from inline_pic.geturl import geturl
def gethtml(words1,filename1,filename2,filename3):

    # 命名生成的html
    GEN_HTML = "test.html"

    # 打开文件，准备写入
    f = open(GEN_HTML, 'w')

    # 准备相关变量
    str1 = geturl(filename1)
    if(filename2!=' '):
       str2 = geturl(filename2)
    elif(filename2==' '):
        str2=' '
    if(filename3!=' '):
     str3= geturl(filename3)
    elif(filename3==' '):
        str3=' '
    # 写入HTML界面中
    message = """
 <!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Title</title>
</head>
<body>
<h1>%s</h1>
<img src=%s>
<img src=%s>

<img src=%s>
</body>
</html>
    """ % (words1,str1,str2,str3)

    # 写入文件
    f.write(message)

    # 关闭文件
    f.close()
    return GEN_HTML




