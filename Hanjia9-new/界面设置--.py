##先做一个界面 
##caotion: TieTacToe
## 长度宽度为 300 * 300

import pygame
import sys
pygame.init()

window=pygame.display.set_mode((300,300))
pygame.display.set_caption('')
window.fill((255,255,255))

logo = pygame.image.load(r'gameData\Images\blogo.png')
button_start = (50,140)

button1 = pygame.image.load('gameData/Images/button1Img.png')
a,b = button1.get_size()
button1_rect = button1.get_rect() ##Method 返回一个 200*63的一个矩形 起点是0,0 [0,0,200,63]
##button1_rect rectangle 
window.blit(button1,button_start)
button1_rect.center = (a/2+button_start[0],b/2+button_start[1])
#pygame.draw.rect(window,[0,0,0],button1_rect,0)


window.blit(logo,(7,7))


pygame.display.update()

flag = False
##对窗口用图片进行填充  
##1. 图片 读进来 Object
##2. 对图片进行摆放. 

##bu_rect.collidepoint((x,y)) #判断x,y是否处在bu_Rect这个rectangle里面

while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type==pygame.MOUSEBUTTONDOWN:
			x,y=pygame.mouse.get_pos()
			print(x,y)
			if button1_rect.collidepoint((x,y)):
				flag=True
			# if 50<=x<=250 and 120<=y<=183:
			# 	flag = True
	if flag:
		window.fill((255,255,255))
##点击 那个图标  就要重新填充屏幕 白色
	pygame.display.update()


##作业 
## 把3*3的网格画出来 是在点击游戏图片之后 直接画出网格 