import sys
from itertools import product
import pygame
from random import choice


panel_width = 640
panel_height = 480
pygame.init() #它必须在导入pygame模块之后，且开始使用Pygame提供的任何函数前调用，你不必知道此函数的作用，只需要知道，为了使用pygame函数能正常工作，必须在一开始就调用它。如果你碰到像pygame.error: font not initialized这样的错识，请检查一下是否忘记了在程序前面调用pygame.init()。
window = pygame.display.set_mode((panel_width,panel_height))
pygame.display.set_caption('This is first')

def draw_Grid(screen,Window_Width,Window_Height,Cell_Size,result):
    # 垂直方向
    # Window_Width = 640
    # Window_Height = 480
    # Cell_Size = 20
    for x in range(0, Window_Width, Cell_Size):
        pygame.draw.line(screen, result, (x, 0), (x, Window_Height))
    # 水平方向
    for y in range(0, Window_Height, Cell_Size):
        pygame.draw.line(screen, result, (0, y), (Window_Width, y))

color_list = [0,64,128,192,255]
colors = product(color_list,repeat=3)
colors = list(colors)
#result = choice(colors)
##random.uniform(3,8)

while True:
	
	#print(len(list(pygame.event.get())))
	for event in pygame.event.get():
		print(len(list(pygame.event.get())))
		if event.type == pygame.KEYDOWN:
			print(event.key)
			if event.key == 27:
				pygame.quit()
				sys.exit()
			elif event.key==1073742048:
				result = choice(colors)
				draw_Grid(window,640,480,20,result)
		elif event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		else:
			print('Not key')
	#draw_Grid(window,result)
	pygame.display.update()


	##1.课后作业 