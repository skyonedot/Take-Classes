##首先响应 点击某个方格 可以实现识别出某个方格来



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
	pygame.draw.rect(window, color, (0, 300, 300, 30))

def Get_pos(window):
	width = 90
	height = 90
	board_pos = [[[5,5,90,90],[105,5,90,90],[205,5,90,90]],
	[[5,105,90,90],[105,105,90,90],[205,105,90,90]],
	[[5,205,90,90],[105,205,90,90],[205,205,90,90]]]
	board_rect = []
	for x in board_pos:
		temp_store = []
		for y in x:
			temp_store.append(pygame.Rect(y))
		board_rect.append(temp_store)
	board = [['','',''],
		['','',''],
		['','','']]
	return board_rect,board


def change(player):
	if player=='x':
		return 'o'
	else:
		return 'x'

#def draw_board(window,board):



panel_width = 300
panel_height = 330
pygame.init() 
window = pygame.display.set_mode((panel_width,panel_height))
pygame.display.set_caption('TicTacToe')
window.fill((255,255,255))

logo = pygame.image.load('gameData/Images/logo.png')
buttom1 = pygame.image.load('gameData/Images/button1Img.png')
a,b = buttom1.get_size()

o_img = pygame.image.load('gameData/Images/circleImg.png')
x_img = pygame.image.load('gameData/Images/crossImg.png')

window.blit(logo,(5,10))
bu_start = (50,170)
window.blit(buttom1,bu_start)
bu_rect = buttom1.get_rect()
bu_rect.center = (a/2+bu_start[0],b/2+bu_start[1])
#pygame.draw.rect(window,[0,0,0],bu_rect,0) 这句话可以画出隐形的梯形来来
flag = False
st = False

board_rect,board = Get_pos(window)

player = 'x'
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == 27:
				pygame.quit()
				sys.exit()
		elif event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			print(x,y)
			if bu_rect.collidepoint((x,y)) and st==False:
				print('Hello,Here I am') ##设置信号量
				flag = True ##防止变回Ture的时候的死循环
				st = True 
			elif st==True and flag==True:
				for i in range(len(board_rect)):
					for j in range(len(board_rect)):
						if board_rect[i][j].collidepoint((x,y)):
							board[i][j] = player
							player = change(player)






	if flag==True:
		window.fill((255,255,255))
		drawGrid(window)


	pygame.display.update()