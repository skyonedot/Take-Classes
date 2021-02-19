## 1. 
##利用board实现输赢判断
##无法实现重复点击

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

def draw_board(window,board,board_rect):
	for i in range(len(board)):
		for j in range(len(board)):
			pos = (board_rect[i][j][0],board_rect[i][j][1])
			if board[i][j] == 'x':
				window.blit(x_img,pos)
			elif board[i][j] == 'o':
				window.blit(o_img,pos)

# Verify if the current player is the winner
def isWinner(player):
	return ((board[0][0] == player and board[0][1] == player and board[0][2] == player) or
			(board[1][0] == player and board[1][1] == player and board[1][2] == player) or
			(board[2][0] == player and board[2][1] == player and board[2][2] == player) or
			(board[0][0] == player and board[1][0] == player and board[2][0] == player) or
			(board[0][1] == player and board[1][1] == player and board[2][1] == player) or
			(board[0][2] == player and board[1][2] == player and board[2][2] == player) or
			(board[0][0] == player and board[1][1] == player and board[2][2] == player) or
			(board[0][2] == player and board[1][1] == player and board[2][0] == player))


def verifyWinner(player):
	if isWinner(player):
		#playSound('gameData/Sounds/resetSound.wav')
		score[player] += 1
		pygame.time.wait(500)
		print('输赢出')

score = {'x':0,'o':0}


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
							if board[i][j] == '':
								board[i][j] = player
								verifyWinner(player)
								print('score:',score)
								player = change(player)






	if flag==True:
		window.fill((255,255,255))
		drawGrid(window)
		draw_board(window,board,board_rect)


	pygame.display.update()