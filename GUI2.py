# encoding: utf-8
import Get_mysql
import Get_info
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('霄龙跑分软件V2.0')
# window.geometry('900x500')
sw = window.winfo_screenwidth()
#得到屏幕宽度
sh = window.winfo_screenheight()
#得到屏幕高度
ww = 900
wh = 500
#窗口宽高为900*500
x = (sw-ww) / 2
y = (sh-wh) / 2 - 50
window.geometry("%dx%d+%d+%d"%(ww,wh,x,y))

canvas = tk.Canvas(window,bg='white',height=1920,width=1080)
image_file = tk.PhotoImage(file='背景图片机器人.gif')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack()


get_info = Get_info.Get_Info()
get_mysql = Get_mysql.Get_mysql(host="123.207.6.194")


def local_infomation(get_info):
    tk.messagebox.showinfo(
        title='本机信息',
        message='CPU ---- '+get_info.get_info_cpu()['cpu_name']\
        +'\n'+'显示卡 ---- '+get_info.get_info_video()['video_name']\
        +'\n'+'硬盘 ---- '+get_info.get_info_hard()['hard_name'][0]\
        +'\n'+'内存 ---- '+get_info.get_info_bank()['bank_name'][0])#本机信息

# def yun_mark():
    
b2 = tk.Button(window,text='本机信息',width=20,height=1,command=lambda:local_infomation(get_info),font=('腾祥智黑简-W5'),bg='orangered2') #按钮
b2.place(x=350,y=445)
b2 = tk.Button()

cpu = tk.Label(window,text='请点击一键测速进行跑分',font=('腾祥智黑简-W5',23))
cpu.place(x=270,y=65)
#明文文本框

cpu = tk.Label(window,text='CPU',font=('腾祥智黑简-W5',14),bg='mediumturquoise')
cpu.place(x=100,y=210)

on_hit = False
def cpu_paofen(get_mysql):
    global on_hit
    if on_hit == False:
        on_hit = True
        cpu_marks = str(get_mysql.get_cpu(get_info.get_info_cpu())['cpu_marks'])
        var.set(cpu_marks)
    else:
        on_hit = False
        var.set('')

var = tk.StringVar()
cpumark = tk.Label(window,textvariable=var,font=('腾祥智黑简-W5',14),bg='mediumturquoise')
cpumark.place(x=100,y=260)

gpu = tk.Label(window,text='显卡',bg='mediumturquoise',font=('腾祥智黑简-W5',14))
gpu.place(x=118,y=316)

disk = tk.Label(window,text='硬盘',bg='mediumturquoise',font=('腾祥智黑简-W5',14))
disk.place(x=680,y=210)

b1 = tk.Button(window,text='一键测速',width=8,height=1,command=lambda:cpu_paofen(get_mysql),font=('腾祥智黑简-W5')) #按钮
b1.place(x=403,y=315)
b1 = tk.Button()


window.mainloop()
#不停刷新窗口 