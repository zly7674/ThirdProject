print('正在加载。。。。。。。')
from   pygame import *
import winsound
import os
import random
import time
import sys
i = os.system('cls')
str1=['晴天-周杰伦','陪你度过漫长岁月-陈奕迅','一天一天-BigBang','Hero-Cash Cash',
      '断线-Shang','好想爱这个世界啊-华晨宇','演员-薛之谦','sunflower feelings-Kuzu mellow',
      'My Heart Still Goes On-MuSik I','So Cute-Lopu$','高尚-薛之谦','病态-薛之谦','最佳歌手-许嵩',
      'Listen-Said The Sky','爱在西元前-周杰伦','七里香-周杰伦','一路向北-周杰伦','她的睫毛-周杰伦',
      '珊瑚海-周杰伦','断了的弦-周杰伦','借口-周杰伦','彩虹-周杰伦','How to love-Cash Cash',
      '不要说话-陈奕迅','溯-CORSAK','青春纪念册-可米小子','Pull Up-Luh Kel',
      'Whoa (mind in awe)-XXXTENTACION','Jocelyn Flores-XXXTentacion',
      'Black Sheep-OmenXIII&ʎpoqou','脚踏车-《不能说的秘密》插曲','Back In Black-AC/DC',
      'It\'s a Long Way to the Top-AC/DC','You Shook Me All Night Long-AC/DC',
      '感谢你曾来过-Ayo97','双笙 - 心做し（Cover GUMI）',
      'Lost In The Stars - 张杰 ']
def menu():

        print('\n-------------------赵凌宇的歌单-----------------------')
        for i in range(len(str1)):
              print(i+1,'~',str1[i])
        print('--------------------------------------------------')


mixer.init()
global g
def option(n):
      if n==1:
               mixer.music.load('D://音乐//晴天 - 周杰伦.m4a')
      elif n==2:
               mixer.music.load('D://音乐//陈奕迅 - 陪你度过漫长岁月.mp3')
      elif n==3:
               mixer.music.load('D://音乐//BIGBANG - 一天一天.mp3')
      elif n==4:
               mixer.music.load('D://音乐//Hero-Cash Cash.mp3')
      elif n==5:
               mixer.music.load('D://音乐//断线-Shang.mp3')
      elif n==6:
               mixer.music.load('D://音乐//好想爱这个世界啊-华晨宇.mp3')
      elif n==7:
               mixer.music.load('D://音乐//演员-薛之谦.mp3')
      elif n==8:
               mixer.music.load('D://音乐//sunflower feelings-Kuzu mellow.mp3')
      elif n==9:
               mixer.music.load('D://音乐//My Heart Still Goes On-MuSik I&廖伟珊.mp3')
      elif n==10:
               mixer.music.load('D://音乐//So Cute-Lopu$.mp3')
      elif n==11:
               mixer.music.load('D://音乐//高尚-薛之谦.mp3')
      elif n==12:
               mixer.music.load('D://音乐//病态-薛之谦.mp3')
      elif n==13:
               mixer.music.load('D://音乐//最佳歌手-许嵩.mp3')
      elif n==14:
               mixer.music.load('D://音乐//Listen-Said The Sky.mp3')
      elif n==15:
               mixer.music.load('D://音乐//爱在西元前-周杰伦.mp3')
      elif n==16:
               mixer.music.load('D://音乐//七里香-周杰伦.mp3')
      elif n==17:
               mixer.music.load('D://音乐//一路向北-周杰伦.mp3')
      elif n==18:
               mixer.music.load('D://音乐//她的睫毛-周杰伦.mp3')
      elif n==19:
               mixer.music.load('D://音乐//珊瑚海-周杰伦.mp3')
      elif n==20:
               mixer.music.load('D://音乐//断了的弦-周杰伦.mp3')
      elif n==21:
               mixer.music.load('D://音乐//借口-周杰伦.mp3')
      elif n==22:
               mixer.music.load('D://音乐//彩虹-周杰伦.mp3')
      elif n==23:
               mixer.music.load('D://音乐//How to love-Cash Cash.mp3')
      elif n==24:
               mixer.music.load('D://音乐//不要说话-陈奕迅.mp3')
      elif n==25:
               mixer.music.load('D://音乐//溯-CORSAK.mp3')
      elif n==26:
               mixer.music.load('D://音乐//青春纪念册-可米小子.mp3')
      elif n==27:
               mixer.music.load('D://音乐//Luh Kel - Pull Up [mqms2].mp3')
      elif n==28:
               mixer.music.load('D://音乐//Whoa (mind in awe)-XXXTENTACION.mp3')
      elif n==29:
               mixer.music.load('D://音乐//Jocelyn Flores-XXXTentacion.mp3')
      elif n==30:
               mixer.music.load('D://音乐//Black Sheep-OmenXIII&ʎpoqou.mp3')
      elif n==31:
               mixer.music.load('D://音乐//脚踏车-《不能说的秘密》插曲.mp3')
      elif n==32:
               mixer.music.load('D://音乐//Back In Black-ACDC.mp3')
      elif n==33:
               mixer.music.load('D://音乐//ACDC - It\'s a Long Way to the Top (If You Wanna R.mp3')
      elif n==34:
               mixer.music.load('D://音乐//ACDC - You Shook Me All Night Long [mqms2].mp3')
      elif n==35:
               mixer.music.load('D://音乐//感谢你曾来过.mp3')
      elif n==36:
               mixer.music.load('D://音乐//双笙 - 心做し（Cover GUMI）.mp3')
      elif n==37:
               mixer.music.load('D://音乐//张杰 - Lost In The Stars [mqms2].mp3')

      else:
             print('歌曲不存在')
             error=input()
             return 0
def confirm():
      #c=input("确认播放吗？\n1.播放  2.退出\n输入:")
      #if c=='2':
      #        print('退出')
      #else:
          mixer.music.play()


while True:
           i=os.system('cls')
           menu()
           b=mixer.music.get_busy()
           if b==1:
                   print('正在播放:\n               ',str1[g-1],'\n')
                   
           a=input('1.选择歌曲   2.随机播放   3.暂停/继续    4.退出程序\n输入:')
           if a=='1':
                    N=input('请选择歌曲(编号):')
                    if N!='':
                            n=int(N)
                            a=option(n)
                            g=n
                            if a!=0:
                               confirm()
                               f1=True
                               f2=False
                  
           elif a=='2':
                    n=random.randint(0,len(str1))
                    a=option(n)
                    g=n
                    if a!=0:
                          confirm()
                          f1=True
                          f2=False
           elif a=='3':
                   if b!=0:
                     #if f1 is True and f2 is False:
                      if f2 is False:
                             mixer.music.pause()
                             f2=True
                     #elif f1 is True and f2 is True:
                      elif f2 is True:
                             mixer.music.unpause()
                             f2 = False
           elif a=='4':
                    print('退出')
                    exit()
           else:
                 print('输入选项有误')
                 w=input()
           
          
