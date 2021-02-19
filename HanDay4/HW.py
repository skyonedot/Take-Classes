# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 13:59:18 2021

@author: win10
"""

##作业: 需要你  当蛇已经撞墙之后  结束游戏 并出现GameOver的字样
##x,y = body[-1] if x<0 or x>640 or y<0 or y>480: 都是已经撞墙了  
##window.fill()##再填充一层墨水 画一层网格.
##我还你显示字体. 指明字体大小  设置内容 最后blit

## 
import pygame
import sys
from itertools import product
import numpy as np
from random import choice

#画网格
def draw_grid(window,panel_width,panel_hight,cell_size,color):
    for a in range(0,panel_width,cell_size):
        pygame.draw.line(window,color, (a,0), (a,panel_hight))
    for b in range(0,panel_hight,cell_size):
        pygame.draw.line(window,color, (0,b), (panel_width,b))
    pygame.display.update()
    


#RGB组合
def random_choice_color(color_list):
    color_list=list(product(color_list,repeat=3))
    return color_list


#创建界面
pygame.init()
panel_width = 640
panel_hight = 480
window=pygame.display.set_mode((panel_width,panel_hight))
pygame.display.set_caption("Pygame")


#设置字体，标题
title_font=pygame.font.SysFont('arial', 40)
Welcome_words=title_font.render('Welcome to Greedy Snake', True, (255,255,0))
Start_words=title_font.render('start',True,(100,255,255))
Exit_words=title_font.render('exit',True,(255,0,255))
Game_over_words=title_font.render('Game Over',True,(100,255,100))

#选颜色
color_list=random_choice_color([0,50,100,200])
m =np.random.randint(0,len(color_list))

flag = False



body = [[200,200],[220,200],[240,200]] ##一条蛇 初始长度为3


#蛇的移动
def move(body,direction,speed,cell_size):
    if direction == 'right':
        new_head = [body[-1][0]+speed*cell_size,body[-1][1]]
    elif direction == 'left':
        new_head = [body[-1][0]-speed*cell_size,body[-1][1]]
        
    elif direction == 'up':
        new_head = [body[-1][0],body[-1][1]-speed*cell_size]
    elif direction == 'down':
        new_head = [body[-1][0],body[-1][1]+speed*cell_size]
    else:
        print('Direction is Wrong')
    body.append(new_head)
    body.pop(0)
    return body

speed = 1
direction = 'left'



###刷新的作用
fps_clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y=event.pos
            print('x={},y={}'.format(x,y))
            if(283<=x<=353 and 210<=y<=240):
                flag = True
                # ##重新覆盖掉原来的字体 然后再画网格
                # #window.fill((255,255,255))
                # #color_list=random_choice_color([0,50,100,200])
                # #m =np.random.randint(0,len(color_list))
                # #draw_grid(window,panel_width,panel_hight,20,color_list[m])
                # for x in body:
                #     pygame.draw.rect(window,(0,0,0),[x[0],x[1],20,20],0)
    
                # # pygame.draw.rect(window,(0,0,0),[200,200,20,20],0) ##[x,y,x_width,y_width]
                # # pygame.draw.rect(window,(0,0,0),[220,200,20,20],0) 
                # # pygame.draw.rect(window,(0,0,0),[240,200,20,20],0) 
                # ##蛇吃东西 蛇每次碰到一个方框 就要长一个给子.
            elif (291<=x<=347 and 307<=y<=342):
                pygame.quit()
                sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == 27:
                pygame.quit()
                sys.exit()
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()



    if flag==False: 
        window.blit(Welcome_words, (124,100))
        window.blit(Start_words,(286,200))
        window.blit(Exit_words,(293,300))
        pygame.display.update()  


    ##代表 点击了start  也就是开始了游戏
    elif flag == True:
        window.fill((255,255,255))
        draw_grid(window,panel_width,panel_hight,20,color_list[m])
        for x in body:
            pygame.draw.rect(window,(0,0,0),[x[0],x[1],20,20],0)
        body = move(body,direction,speed,cell_size=20)
        a,b=body[-1]
        if a<0 or a>640 or b<0 or b>480:
            window.fill((0,0,0))
            window.blit(Game_over_words, (230,100))



        
        
    pygame.display.update()
    fps_clock.tick(speed)  #设置刷新的帧率  