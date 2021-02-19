##整理蛇的Class
##暂停游戏 按下空格

import sys
from itertools import product
import pygame
from random import choice
import time

class Snake():
	def __init__(self,body,direction,speed):
		self.body = body
		self.direction = direction
		self.speed = speed


	def move(self,cell_size=20):
		x,y = self.body[-1]
		if self.direction == 'right':
			target = [x+self.speed*cell_size,y]
		elif self.direction == 'left':
			target = [x-self.speed*cell_size,y]
		elif self.direction == 'up':
			target = [x,y-self.speed*cell_size]
		elif self.direction == 'down':
			target = [x,y+self.speed*cell_size]
		else:
			print('Direction is Wrong')
		# if eaten==True:
		# 	body.insert(0,tail)
		self.body.append(target)
		return body

	def check_direction(self,new_d,old_d):
		left_right = ['left','right']
		up_down = ['up','down']
		if new_d in left_right and old_d in left_right:
			return False
		elif new_d in up_down and old_d in up_down:
			return False
		else:
			return True 



body = [[100,100],[120,100],[140,100]]
direction = 'right'
speed = 1
snake = Snake(body,direction,speed)


panel_width = 640
panel_height = 480
pygame.init() 
window = pygame.display.set_mode((panel_width,panel_height))
pygame.display.set_caption('This is first')

def draw_Grid(screen,Window_Width,Window_Height,Cell_Size,result):
    # 垂直方向
    for x in range(0, Window_Width, Cell_Size):
         pygame.draw.line(screen, result, (x, 0), (x, Window_Height))
    # 水平方向
    for y in range(0, Window_Height, Cell_Size):
        pygame.draw.line(screen, result, (0, y), (Window_Width, y))


##生成食物
def generate_food(window,body):
	game_map = []
	for x in range(32):
		for y in range(24):
			game_map.append([x,y])
	#game_map = {(x, y): 0 for x in range(32) for y in range(24)}
	while True:
		x,y = choice(game_map)
		x1 = 20*x
		y1 = 20*y
		if [x1,y1] not in body:
			#pygame.draw.rect(window,[255,0,0],[x1,y1,20,20],0)
			return x1,y1
	
def checkeat(body,food_x,food_y):
	if food_x/20==body[-1][0]/20 and food_y/20 == body[-1][1]/20:
		print('Food_x:',food_x,'Body_x',body[-1][0],'Food_y',food_y,'Body_y',body[-1][1])
		print(food_x/20,body[-1][0]/20,food_y/20,body[-1][1]/20)
		return True
	return False



color_list = [0,64,128,192,255]
colors = product(color_list,repeat=3)
colors = list(colors)
result = choice(colors)
flag = False
end = False
grade = 0

title_font = pygame.font.SysFont('arial', 32)
welcome_words = title_font.render('Welcome to My Snake', True, (0, 0, 0), (255, 255, 255))
tips_font = pygame.font.SysFont('arial', 24)
start_game_words = tips_font.render('Click to Start Game', True, (0, 0, 0), (255, 255, 255))
close_game_words = tips_font.render('Press ESC to Close', True, (0, 0, 0), (255, 255, 255))
filled_flag = False



##画蛇

fps_clock = pygame.time.Clock()
##第一次开始 信号量
only_start = True

##游戏暂停信号量
game_pause = False




key_direction_dict = {
	119:'up',
	115:'down',
	97:'left',
	100:'right',
}

while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == 32:
				game_pause = not game_pause
			if flag==True and event.key in key_direction_dict:
				move_direction = key_direction_dict[event.key]
				if snake.check_direction(move_direction,snake.direction):
					snake.direction = move_direction
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
	if flag:
		if game_pause==True:
			window.blit(welcome_words, (188, 100))
		else:
			words_grade = tips_font.render('Grade:'+str(grade), True, (0, 0, 0), (255, 255, 255))

			window.fill((255,255,255))
			draw_Grid(window,640,480,20,result)
			window.blit(words_grade, (188, 100))
			if only_start == True:
				food_x,food_y = generate_food(window,body)
			only_start = False
			for rect in body:
				pygame.draw.rect(window,[0,0,0],[rect[0],rect[1],20,20],0)
			##如果移动到这里? body = move(body,direction)
			eaten = checkeat(body,food_x,food_y)
			#检查是否吃到食物
			if eaten == True:
				food_x,food_y = generate_food(window,body)
				grade += 1
			else:
				snake.body.pop(0)
			pygame.draw.rect(window,[255,0,0],[food_x,food_y,20,20],0)
			snake.body = snake.move()
			if(snake.body[-1][0]<0 or snake.body[-1][0]>640 or snake.body[-1][1]<0 or snake.body[-1][1]>480):
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
	fps_clock.tick(4)