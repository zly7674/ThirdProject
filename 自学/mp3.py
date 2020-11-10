from  歌单2 import *
from tkinter import *
import tkinter.messagebox as messagebox
import os
#按钮触发函数
def start_music():
    mixer.music.load('D://音乐//晴天 - 周杰伦.m4a')
    mixer.music.play()
    print("正在播放：晴天-周杰伦")
def start_music1():
    mixer.music.load('D://音乐//爱在西元前-周杰伦.mp3')
    mixer.music.play()
    print("正在播放：爱在西元前-周杰伦")
def start_music2():
    mixer.music.load('D://音乐//七里香-周杰伦.mp3')
    mixer.music.play()
    print("正在播放：七里香-周杰伦")
def start_music3():
    mixer.music.load('D://音乐//一路向北-周杰伦.mp3')
    mixer.music.play()
    print("正在播放：一路向北-周杰伦")
def start_music4():
    mixer.music.load('D://音乐//珊瑚海-周杰伦.mp3')
    mixer.music.play()
    print("正在播放：珊瑚海-周杰伦")
def start_music5():
    mixer.music.load('D://音乐//BIGBANG - 一天一天.mp3')
    mixer.music.play()
    print("正在播放：BIGBANG - 一天一天")
def start_music6():
    mixer.music.load('D://音乐//她的睫毛-周杰伦.mp3')
    mixer.music.play()
    print("正在播放：她的睫毛-周杰伦")
def start_music7():
    mixer.music.load('D://音乐//借口-周杰伦.mp3')
    mixer.music.play()
    print("正在播放：借口-周杰伦")
def start_music8():
    mixer.music.load('D://音乐//断了的弦-周杰伦.mp3')
    mixer.music.play()
    print("正在播放：断了的弦-周杰伦")
def start_music9():
    mixer.music.load('D://音乐//溯-CORSAK.mp3')
    mixer.music.play()
    print("正在播放：溯-CORSAK")
def start_music10():
    mixer.music.load('D://音乐//脚踏车-《不能说的秘密》插曲.mp3')
    mixer.music.play()
    print("正在播放：脚踏车-《不能说的秘密》插曲")
def start_music11():
    mixer.music.load('D://音乐//好想爱这个世界啊-华晨宇.mp3')
    mixer.music.play()
    print("正在播放：好想爱这个世界啊-华晨宇")
def start_music12():
    mixer.music.load('D://音乐//Luh Kel - Pull Up [mqms2].mp3')
    mixer.music.play()
    print("正在播放：Pull Up - Luh Kel")
def start_music13():
    mixer.music.load('D://音乐//Hero-Cash Cash.mp3')
    mixer.music.play()
    print("正在播放：Hero-Cash Cash")
def start_music14():
    mixer.music.load('D://音乐//陈奕迅 - 陪你度过漫长岁月.mp3')
    mixer.music.play()
    print("正在播放：陪你度过漫长岁月")
def start_music15():
    mixer.music.load('D://音乐//Whoa (mind in awe)-XXXTENTACION.mp3')
    mixer.music.play()
    print("正在播放：Whoa (mind in awe)")
def pause_music():
    mixer.music.pause()
#主窗口定义
player=Tk()
player.title("网易云音乐")
player.geometry("500x700")
player.minsize(500,600)

#框架
F1=Frame(player,bg="white")
F2=Frame(player,bg="white")
F3=Frame(player,bg="red")
#加载图标
ph=PhotoImage(file="wangyiyun.gif")
tub=Label(F1,image=ph)
tub.pack()
theLabel=Label(F1,text="欢迎使用网易云音乐播放器",font=("宋体",20),bg="white",fg="black",)
theLabel.pack(side="top")
theLabel1=Label(F1,text="*点击选择歌曲*",font=("宋体",15),bg="white",fg="red")
theLabel1.pack()
#加载背景图
photo=PhotoImage(file="back.gif")
theLabel2=Label(player,text="正在播放",image=photo,compound=CENTER,font=("宋体",15),fg="white")

Button_1=Button(F2,text="晴天 ▶",font=("宋体",15),command=start_music,width=12).grid(row=0,column=1)
Button_2=Button(F2,text="爱在西元前 ▶",font=("宋体",15),command=start_music1).grid(row=1,column=1)
Button_3=Button(F2,text="七里香 ▶",font=("宋体",15),command=start_music2,width=14).grid(row=0,column=2)
Button_4=Button(F2,text="一路向北 ▶",font=("宋体",15),command=start_music3,width=14).grid(row=0,column=3)
Button_5=Button(F2,text="珊瑚海 ▶",font=("宋体",15),command=start_music4,width=12).grid(row=1,column=2)
Button_6=Button(F2,text="一天一天-BIGBANG ▶",font=("宋体",15),command=start_music5,width=18).grid(row=1,column=3)
Button_7=Button(F2,text="她的睫毛 ▶",font=("宋体",15),command=start_music6,width=12).grid(row=2,column=1)
Button_8=Button(F2,text="借口 ▶",font=("宋体",15),command=start_music7,width=14).grid(row=2,column=2)
Button_9=Button(F2,text="断了的弦 ▶",font=("宋体",15),command=start_music8,width=16).grid(row=2,column=3)
Button_10=Button(F2,text="溯 ▶",font=("宋体",15),command=start_music9,width=12).grid(row=3,column=1)
Button_11=Button(F2,text="不能说的秘密 ▶",font=("宋体",15),command=start_music10,width=15).grid(row=3,column=2)
Button_12=Button(F2,text="好想爱这个世界啊 ▶",font=("宋体",15),command=start_music11,width=19).grid(row=3,column=3)
Button_13=Button(F2,text="Pull Up ▶",font=("宋体",15),command=start_music12,width=14).grid(row=4,column=1)
Button_14=Button(F2,text="Hero ▶",font=("宋体",15),command=start_music13,width=14).grid(row=4,column=2)
Button_15=Button(F2,text="陪你度过漫长岁月 ▶",font=("宋体",15),command=start_music14,width=19).grid(row=4,column=3)
Button_16=Button(F2,text="Whoa ▶",font=("宋体",15),command=start_music15,width=14).grid(row=5,column=1)

F1.pack(side="top",expand=NO,fill=X)
F1.pack()
F2.pack(expand=NO)

#执行
player.mainloop()
os.system("pause")
c=input("任意键退出")