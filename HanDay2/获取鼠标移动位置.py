##得到鼠标位置
##Lesson1
##按键教程
##即键盘上的某些键输入到控制台中 对应哪些数值?
## 重点  w s a d esc即可 还有 event.type == pygame.QUIT: 即点击 × 号
import pygame
import sys
panel_width = 640
panel_height = 480
pygame.init() #它必须在导入pygame模块之后，且开始使用Pygame提供的任何函数前调用，你不必知道此函数的作用，只需要知道，为了使用pygame函数能正常工作，必须在一开始就调用它。如果你碰到像pygame.error: font not initialized这样的错识，请检查一下是否忘记了在程序前面调用pygame.init()。
window = pygame.display.set_mode((panel_width,panel_height))
pygame.display.set_caption('This is first')
while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			print(event.key,str(event))
			if event.key == 27:
				pygame.quit()
				sys.exit()
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			print(x,y)
			print('Mouse Down')
		elif event.type == pygame.MOUSEBUTTONUP:
			print("Mouse Up")
		elif event.type == pygame.MOUSEMOTION:
			print('Mouse Move',event.pos)
		else:
			print(str(event))
			print('Not key')
	pygame.display.update()

##再符加 空格键暂停?




# 有游戏均具有while True循环，并注明“main game loop”字样的注释。一个游戏循环主要做以下三件事情：

# 1.        处理事件

# 2.        更新游戏状态

# 3.        在屏幕上绘图