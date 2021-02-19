## 当蛇头超出位置时 刷新界面 显示GameOver

##画出小蛇来


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
    for x in range(0, Window_Width, Cell_Size):
        pygame.draw.line(screen, result, (x, 0), (x, Window_Height))
    # 水平方向
    for y in range(0, Window_Height, Cell_Size):
        pygame.draw.line(screen, result, (0, y), (Window_Width, y))

def move(body,direction,speed,cell_size):
	x,y = body[-1]
	if direction == 'right':
		target = [x+speed*cell_size,y]
	elif direction == 'left':
		target = [x-speed*cell_size,y]
	elif direction == 'up':
		target = [x,y-speed*cell_size]
	elif direction == 'down':
		target = [x,y+speed*cell_size]
	else:
		print('Direction is Wrong')
	body.pop(0)
	body.append(target)
	print(body)
	return body


color_list = [0,64,128,192,255]
colors = product(color_list,repeat=3)
colors = list(colors)
result = choice(colors)
flag = False
end = False

title_font = pygame.font.SysFont('arial', 32)
welcome_words = title_font.render('Welcome to My Snake', True, (0, 0, 0), (255, 255, 255))
tips_font = pygame.font.SysFont('arial', 24)
start_game_words = tips_font.render('Click to Start Game', True, (0, 0, 0), (255, 255, 255))
close_game_words = tips_font.render('Press ESC to Close', True, (0, 0, 0), (255, 255, 255))
filled_flag = False


##画蛇
body = [[100,100],[120,100],[140,100]]
move_direction = 'right'
speed = 1

###
fps_clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			print(event.key)
			if event.key == 27:
				pygame.quit()
				sys.exit()
			elif event.key == 1073742048:
				flag = True
		elif event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			print(x,y)
		else:
			print('Not key')
	#window.fill((255,255,255)) ##重点  但是 会重复执行这句话 怎么只让他执行一次?
	if flag:
		window.fill((255,255,255))
		draw_Grid(window,640,480,20,result)
		for rect in body:
			pygame.draw.rect(window,[0,0,0],[rect[0],rect[1],20,20],0)
		body = move(body,'up',speed,20)
		if(body[-1][0]<0 or body[-1][0]>640 or body[-1][1]<0 or body[-1][1]>480):
			flag = False
			end = True
	elif flag==False and end == True:
		window.fill((255,255,255))
		draw_Grid(window,640,480,20,result)
		window.blit(welcome_words, (188, 100))
	else:
		window.blit(welcome_words, (188, 100))
		window.blit(start_game_words, (236, 310))
		window.blit(close_game_words, (233, 350))		

	pygame.display.update()
	fps_clock.tick(speed)



## 课后作业 : 实现 1.