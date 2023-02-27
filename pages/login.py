#-*- coding:utf-8 -*-
import tkinter as tk
import tkinter.messagebox
import pickle
from pages.send_email import *
from pages.vert import *
def show():
    # 窗口
    window = tk.Tk()
    window.title('欢迎使用邮箱客户端！')
    window.geometry('1000x650')
    # 画布放置图片
    canvas = tk.Canvas(window, height=650, width=1100)
    imagefile = tk.PhotoImage(file='images/deskdop_1.png')
    image = canvas.create_image(0, 0, anchor='nw', image=imagefile)
    canvas.pack(side='top')
    # 标签 用户名密码
    tk.Label(window, text='邮箱号:').place(x=400, y=160)
    tk.Label(window, text='授权码:').place(x=400, y=280)
    tk.Label(window,text='服务器：').place(x=400, y=220)
    # 邮箱号输入框
    var_usr_name = tk.StringVar()
    entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
    entry_usr_name.place(x=470, y=160)
    #邮箱服务器输入框
    var_sever=tk.StringVar()
    entry_sever_name =tk.Entry(window,textvariable=var_sever)
    entry_sever_name.place(x=470,y=220)
    # 授权码输入框
    var_usr_pwd = tk.StringVar()
    entry_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
    entry_usr_pwd.place(x=470, y=280)
    #帮助文档
    def hp():
             subwindow=tk.Toplevel(window)
             subwindow.geometry('550x200')
             subwindow.title('帮助文档！')
             var = tkinter.StringVar()
             var.set("1若点击登录后无响应，表明smtp输入非法，请重新输入！\n2若点击登录后验证失败，表明授权码和、箱号和smtp服务器三者不匹配！"
                     "\n3如果您不知道如何获取smtp授权码，请参考http://t.csdn.cn/MOLzK"
                     "\n4示例：@qq.com,smtp.qq.com,******i,随后您可以用他来给您的QQ邮箱发送消息，当然也可以使用其他邮箱，但无法保障邮件能被收到。"        )
             message = tkinter.Message(subwindow, width=400, textvariable=var)
             message.place(x=20, y=50)
    # 退出的函数
    def usr_sign_quit():
        window.destroy()
    def login():
        def back():
         window_error.destroy()
        uesrname=entry_usr_name.get()
        mailsever=entry_sever_name.get()
        password = entry_usr_pwd.get()
        a=verify(mailsever,uesrname,password)
        if a == 221 :
            window.destroy()
            imshow( mailsever, uesrname, password)
        else:
            window_error = tk.Toplevel(window)
            window_error.geometry('550x200')
            window_error.title('Attention!')
            tk.Label(window_error, text='验证失败',width=10).place(x=100, y=100)
            bb1=tk.Button(window_error,text='返回',font=('黑体'), fg='black', bg='white',command=back).place(x=300,y=150)
    # 登录 注册按钮
    bt_login = tk.Button(window, text='登录', command=login).place(x=460, y=340)
    bt_logup = tk.Button(window, text='帮助文档', command=hp).place(x=530, y=340)
    bt_logquit = tk.Button(window, text='退出', command=usr_sign_quit).place(x=600, y=340)
    # 主循环
    window.mainloop()