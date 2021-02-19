##跳转界面 重新填充白色及网格


import pygame
import sys

def drawGrid(window):
	width = 10
	color = dark_grey = (85, 85, 85)
	pygame.draw.line(window, color, (100, 0), (100, 300), width)
	pygame.draw.line(window, color, (200, 0), (200, 300), width)
	pygame.draw.line(window, color, (0, 100), (300, 100), width)
	pygame.draw.line(window, color, (0, 200), (300, 200), width)
	pygame.draw.rect(window, color, (0, 0, 5, 300))
	pygame.draw.rect(window, color, (0, 0, 300, 5))
	pygame.draw.rect(window, color, (295, 0, 5, 300))


panel_width = 300
panel_height = 300
pygame.init() 
window = pygame.display.set_mode((panel_width,panel_height))
pygame.display.set_caption('TicTacToe')
window.fill((255,255,255))

logo = pygame.image.load('gameData/Images/logo.png')
buttom1 = pygame.image.load('gameData/Images/button1Img.png')
a,b = buttom1.get_size()

window.blit(logo,(5,10))
bu_start = (50,170)
window.blit(buttom1,bu_start)
bu_rect = buttom1.get_rect()
bu_rect.center = (a/2+bu_start[0],b/2+bu_start[1])
#pygame.draw.rect(window,[0,0,0],bu_rect,0) 这句话可以画出隐形的梯形来来
flag = False

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			print(event.key,str(event))
			if event.key == 27:
				pygame.quit()
				sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			if bu_rect.collidepoint((x,y)):
				print('Hello,Here I am') ##设置信号量
				flag = True

	if flag==True:
		window.fill((255,255,255))
		drawGrid(window)
	pygame.display.update()