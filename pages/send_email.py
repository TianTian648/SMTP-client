#-*- coding:utf-8 -*-
import tkinter as tk
import tkinter.messagebox
import pickle
import tkinter.filedialog
from pages.Pic_preview import *
from inline_pic.pic import *
from attachments.attachments_n import *
from user_definedf.insert import *
from user_definedf.makemessages import *
def  imshow(SMTP_host, from_account, from_password):
    # 窗口
    global filename1,filename2,filename3,msg
    msg = '\r\n'.encode()
    filename1=filename2=filename3=' '
    window = tk.Tk()
    window.title('TCP-Socket 邮件发送！')
    window.geometry('1000x650')
    # 画布放置图片
    canvas = tk.Canvas(window, height=1200, width=1100)
    imagefile = tk.PhotoImage(file='images/ye.png')
    image = canvas.create_image(0, 0, anchor='nw', image=imagefile)
    canvas.pack(side='top')
    # 收件人，主题和内容
    tk.Label(window, text='收件人:').place(x=200, y=60)
    tk.Label(window, text='主题:').place(x=200, y=120)
    tk.Label(window, text='内容：').place(x=200, y=180)
    # 收件人输入框
    var_rec_name = tk.StringVar()
    entry_rec_name = tk.Entry(window, textvariable=var_rec_name,width=75)
    entry_rec_name.place(x=270, y=60)
    # 主题输入框
    var_subject = tk.StringVar()
    entry_sub_name = tk.Entry(window, textvariable=var_subject, width=75)
    entry_sub_name.place(x=270, y=120)
    # 内容输入框
    content_text = tk.Text(window, width=75, height=12, font=('黑体', 13))
    content_text.place(x=270, y=180)
    #退出函数
    def usr_sign_quit():
        window.destroy()
    def hpp():
        subwindow = tk.Toplevel(window)
        subwindow.geometry('550x200')
        subwindow.title('帮助文档！')
        var = tkinter.StringVar()
        var.set("可以发送纯文字/html/和大部分类型的附件，此文档其实没什么用")
        message = tkinter.Message(subwindow, width=400, textvariable=var)
        message.place(x=20, y=50)
    def pic_inline():
        def back1():
            window_ack.destroy()
        def back2():
            window_error.destroy()
        global filename1
        global filename2
        global filename3
        reca = entry_rec_name.get()
        rec = str(reca)
        subject1 = entry_sub_name.get()
        subject = str(subject1)
        content_1 = content_text.get("0.0", "end")
        content = str(content_1)
        b=send_email_img_inline(SMTP_host,from_account,from_password, rec, subject, content,filename1,filename2,filename3)
        if b == 221 :
            window_ack = tk.Toplevel(window)
            window_ack.geometry('550x200')
            window_ack.title('Attention!')
            tk.Label(window_ack, text='发送成功！', width=10).place(x=100, y=100)
            bb1 = tk.Button(window_ack, text='返回', font=('黑体'), fg='black', bg='white', command=back1).place(x=300,
                                                                                                                 y=150)
        else :
            window_error = tk.Toplevel(window)
            window_error.geometry('550x200')
            window_error.title('Attention!')
            tk.Label(window_error, text='发送失败', width=10).place(x=100, y=100)
            bb1 = tk.Button(window_error, text='返回', font=('黑体'), fg='black', bg='white', command=back2).place(x=300,
                                                                                                                  y=150)
    def add1():
        global filename1
        filename1 = tkinter.filedialog.askopenfilename()
        print(filename1)
    def add2():
        global filename2
        filename2 = tkinter.filedialog.askopenfilename()

        print(filename2)
    def add3():
        global filename3
        filename3 = tkinter.filedialog.askopenfilename()
        print(filename3)
    def add4():
        def back1():
            window_ack.destroy()
        def back2():
            window_error.destroy()
        reca = entry_rec_name.get()
        rec = str(reca)
        subject1 = entry_sub_name.get()
        subject = str(subject1)
        content_1 = content_text.get("0.0", "end")
        content = str(content_1)
        b = send_email_attn(SMTP_host, from_account, from_password, rec, subject, content, filename1,filename2,filename3)
        if b == 221:
            window_ack = tk.Toplevel(window)
            window_ack.geometry('550x200')
            window_ack.title('Attention!')
            tk.Label(window_ack, text='发送成功！', width=10).place(x=100, y=100)
            bb1 = tk.Button(window_ack, text='返回', font=('黑体'), fg='black', bg='white', command=back1).place(x=300,
                                                                                                                 y=150)
        else:
            window_error = tk.Toplevel(window)
            window_error.geometry('550x200')
            window_error.title('Attention!')
            tk.Label(window_error, text='发送失败', width=10).place(x=100, y=100)
            bb1 = tk.Button(window_error, text='返回', font=('黑体'), fg='black', bg='white', command=back2).place(
                x=300,
                y=150)
    def insert():
        global msg
        def back1():
            global msg
            filename = tkinter.filedialog.askopenfilename()
            msg+=insert1(filename)
            window_1.destroy()
        def back2():
            def back0():
                window_ack.destroy()
            global msg
            msg += '------=_NextPart_000_0012345JZ--\r\n'.encode()
            reca = entry_rec_name.get()
            rec = str(reca)
            subject1 = entry_sub_name.get()
            subject = str(subject1)
            content_1 = content_text.get("0.0", "end")
            content = str(content_1)
            b=makemessages(SMTP_host, from_account, from_password, reca, subject, content,msg)
            if b == 221:
                window_ack = tk.Toplevel(window)
                window_ack.geometry('550x200')
                window_ack.title('Attention!')
                tk.Label(window_ack, text='发送成功！', width=10).place(x=100, y=100)
                bb1 = tk.Button(window_ack, text='返回', font=('黑体'), fg='black', bg='white', command=back0).place(
                    x=300,
                    y=150)
            else:
                window_error = tk.Toplevel(window)
                window_error.geometry('550x200')
                window_error.title('Attention!')
                tk.Label(window_error, text='发送失败', width=10).place(x=100, y=100)
                bb1 = tk.Button(window_error, text='返回', font=('黑体'), fg='black', bg='white', command=back0).place(
                    x=300,
                    y=150)
            window_1.destroy()
        window_1=tk.Toplevel(window)
        window_1.geometry('550x200')
        window_1.title('是否添加!')
        bb1 = tk.Button(window_1, text='是', font=('黑体'), fg='black', bg='white', command=back1).place(x=150,
                                                                                                             y=150)
        bb2 = tk.Button(window_1, text='直接发送', font=('黑体'), fg='black', bg='white', command=back2).place(x=300,
                                                                                                             y=150)
        reca = entry_rec_name.get()
        rec = str(reca)
        subject1 = entry_sub_name.get()
        subject = str(subject1)
        content_1 = content_text.get("0.0", "end")
        content = str(content_1)






    #确认发送与文件选择
    bt_user=tk.Button(window, text='选择附件', font=('黑体', 13), fg='black', bg='white',command=insert,
    width=10, height=2).place(x=300, y=400)
    check_button = tk.Button(window, text='发送', font=('黑体', 13), fg='black', bg='white',command=add4,
    width=10, height=2).place(x=460, y=400)
    bt_login = tk.Button(window, text='图片预览',  font=('黑体', 13),fg='black', bg='white',command= pic_show,
                         width=10, height=2).place(x=600, y=400)
    pic_inline=tk.Button(window, text='html',  font=('黑体', 13),fg='black', bg='white',command= pic_inline,
                         width=10, height=2).place(x=660, y=450)
    sk_button=tk.Button(window, text='退出',  font=('黑体', 13),fg='black', bg='white',command=usr_sign_quit,
                         width=10, height=2).place(x=760, y=400)
    sk1_button = tk.Button(window, text='帮助文档', font=('黑体', 13), fg='black', bg='white', command=hpp,
                          width=10, height=2).place(x=550, y=450)
    add1_button=tk.Button(window, text='附件1', font=('黑体', 13), fg='black', bg='white', command=add1,
                          width=10, height=2).place(x=460, y=550)
    add2_button = tk.Button(window, text='附件2', font=('黑体', 13), fg='black', bg='white', command=add2,
                            width=10, height=2).place(x=600,y=550)
    add3_button = tk.Button(window, text='附件3', font=('黑体', 13), fg='black', bg='white', command=add3,
                            width=10, height=2).place(x=760, y=550)
    # 主循环
    window.mainloop()

