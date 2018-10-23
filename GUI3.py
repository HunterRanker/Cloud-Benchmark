# encoding: utf-8
import Get_mysql
import Get_info
import tkinter as tk
from tkinter import messagebox
import time

window = tk.Tk()
window.title('EPYC Benchmark SoftwareV3.0')
# window.geometry('900x500')
sw = window.winfo_screenwidth()
#得到屏幕宽度
sh = window.winfo_screenheight()
#得到屏幕高度
ww = 900
wh = 500
#窗口宽高为900*500
x = (sw-ww) / 2
y = (sh-wh) / 2
window.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
window.resizable(width=False, height=False)
window.overrideredirect(True)

# window.attributes("-alpha", 1)#窗口透明度0 %


canvas = tk.Canvas(window,bg='white',height=1920,width=1080)
image_file = tk.PhotoImage(file='背景图片机器人.gif')
image = canvas.create_image(0,0,anchor='nw',image=image_file)
canvas.pack()


info = Get_info.Get_Info()
sql = Get_mysql.Get_mysql(host="123.207.6.194")

cpu = info.get_info_cpu()
video = info.get_info_video()
hard = info.get_info_hard()
bank = info.get_info_bank()
sql_video = sql.get_video(video)
sql_cpu = sql.get_cpu(cpu)
sql_hard = sql.get_hard(hard)
sql_bank = sql.get_bank(bank)

mess='CPU ---- '+cpu['cpu_name']\
        +'\n'+'显示卡 ---- '+video['video_name']\
        +'\n'+'硬盘 ---- '+hard['hard_name'][0]\
        +'\n'+'内存 ---- '+bank['bank_name'][0]#本机信息

def local_infomation():
    global mess
    tk.messagebox.showinfo(
        title='本机信息',
        message=mess)


def close():
    window.destroy()

    
b2 = tk.Button(window,text='本机信息',width=20,height=1,command=local_infomation,font=('腾祥智黑简-W5'),bg='orangered2') #按钮
b2.place(x=350,y=445)
b2 = tk.Button()

cpu = tk.Label(window,text='请点击一键测速进行跑分',font=('腾祥智黑简-W5',23))
cpu.place(x=270,y=65)
#明文文本框

cpu = tk.Label(window,text='CPU',font=('腾祥智黑简-W5',14),bg='mediumturquoise')
cpu.place(x=100,y=210)


var0 = tk.StringVar()
on_hit = False
def cpu_paofen():
    if b1['text'] =='一键测速':
        b1['text']='测速成功'
        time.sleep(3)
    else:
        b1['text'] ='请稍等'
    global on_hit
    global sql_cpu
    if on_hit == False:
        on_hit = True
        cpu_marks = sql_cpu['cpu_marks']
        var.set(cpu_marks)
        gpu_marks = sql_video['G3D_Mark']
        var2.set(gpu_marks)
        disk_marks = sql_hard['Disk_Rating'][0]
        var3.set(disk_marks)
        var4.set(str(cpu_marks+gpu_marks+disk_marks))

        var5.set('总分')
    else:
        on_hit = False
        pass


var = tk.StringVar()
cpumark = tk.Label(window,textvariable=var,font=('Charlemagne Std',30,'bold'),bg='#f1b219')
time.sleep(1)
cpumark.place(x=110,y=242)

gpu = tk.Label(window,text='显卡',bg='mediumturquoise',font=('腾祥智黑简-W5',14))
gpu.place(x=118,y=316)

var2 = tk.StringVar()
gpumark = tk.Label(window,textvariable=var2,bg='#f1b219',font=('Charlemagne Std',20,'bold'))
gpumark.place(x=170,y=310)

disk = tk.Label(window,text='硬盘',bg='mediumturquoise',font=('腾祥智黑简-W5',14))
disk.place(x=680,y=210)

var3 = tk.StringVar()
diskmark = tk.Label(window,textvariable=var3,bg='#f1b219',font=('Charlemagne Std',20,'bold'))
diskmark.place(x=670,y=235)

var4 = tk.StringVar()
totalmark = tk.Label(window,textvariable=var4,bg='#f1b219',font=('腾祥智黑简-W5',30,'bold'))
totalmark.place(x=498,y=198)

var5 = tk.StringVar()
totalmark = tk.Label(window,textvariable=var5,bg='#f1b219',font=('腾祥智黑简-W5',26,'bold'))
totalmark.place(x=300,y=200)

b0 = tk.Button(window,text='O',width=4,height=0,command=close,font=('腾祥智黑简-W5'),bg='mediumturquoise') #按钮
b0.place(x=830,y=0)

b1 = tk.Button(window,text='一键测速',width=8,height=1,command=cpu_paofen,font=('腾祥智黑简-W5')) #按钮
b1.place(x=403,y=315)



window.mainloop()
#不停刷新窗口 