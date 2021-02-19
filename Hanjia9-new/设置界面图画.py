##先设置界面


import pygame
import sys
panel_width = 300
panel_height = 300
pygame.init() 
window = pygame.display.set_mode((panel_width,panel_height))
pygame.display.set_caption('TicTacToe')
window.fill((255,255,255))

logo = pygame.image.load('gameData/Images/logo.png')
buttom1 = pygame.image.load('gameData/Images/button1Img.png')

window.blit(logo,(5,10))
window.blit(buttom1,(50,170))


while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			print(event.key,str(event))
			if event.key == 27:
				pygame.quit()
				sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			print(pygame.mouse.get_pos())
	pygame.display.update()