import pygame

#初始化游戏
pygame.init()

#生成游戏窗口
screen=pygame.display.set_mode((500,600))
screen.fill((255,255,255))#RGB

img=pygame.image.load("下载.jpg")
screen.blit(img,(0,0))
pygame.display.flip()
#游戏帧循环
runn=True
while runn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runn=False
#退出游戏
pygame.quit()