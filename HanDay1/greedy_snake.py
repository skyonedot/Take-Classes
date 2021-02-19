# 游戏是基于PyGame框架制作的，程序核心逻辑如下：

# 游戏界面分辨率是640*480，蛇和食物都是由1个或多个20*20像素的正方形块儿（为了方便，下文用点表示20*20像素的正方形块儿）组成，这样共有32*24个点，使用pygame.draw.rect来绘制每一个点；
# 初始化时蛇的长度是3，食物是1个点，蛇初始的移动的方向是右，用一个数组代表蛇，数组的每个元素是蛇每个点的坐标，因此数组的第一个坐标是蛇尾，最后一个坐标是蛇头；
# 游戏开始后，根据蛇的当前移动方向，将蛇运动方向的前方的那个点append到蛇数组的末位，再把蛇尾去掉，蛇的坐标数组就相当于往前挪了一位；
# 如果蛇吃到了食物，即蛇头的坐标等于食物的坐标，那么在第2点中蛇尾就不用去掉，就产生了蛇长度增加的效果；食物被吃掉后，随机在空的位置（不能与蛇的身体重合）再生成一个；
# 通过PyGame的event监控按键，改变蛇的方向，例如当蛇向右时，下一次改变方向只能向上或者向下；
# 当蛇撞上自身或墙壁，游戏结束，蛇头装上自身，那么蛇坐标数组里就有和舌头坐标重复的数据，撞上墙壁则是蛇头坐标超过了边界，都很好判断；
# 其他细节：做了个开始的欢迎界面；食物的颜色随机生成；吃到实物的时候有声音提示等。


import pygame
import sys
from os import path
from sys import exit
from time import sleep
from random import choice
from itertools import product
from pygame.locals import QUIT, KEYDOWN


def direction_check(moving_direction, change_direction):
    directions = [['up', 'down'], ['left', 'right']]
    if moving_direction in directions[0] and change_direction in directions[1]:
        return change_direction
    elif moving_direction in directions[1] and change_direction in directions[0]:
        return change_direction
    return moving_direction


class Snake:

    colors = list(product([0, 64, 128, 192, 255], repeat=3))[1:-1]

    def __init__(self):
        self.map = {(x, y): 0 for x in range(32) for y in range(24)}
        self.body = [[100, 100], [120, 100], [140, 100]]
        self.head = [140, 100]
        self.food = []
        self.food_color = []
        self.moving_direction = 'right'
        self.speed = 4
        self.generate_food()
        self.game_started = False

    def check_game_status(self):
        if self.body.count(self.head) > 1:
            return True
        if self.head[0] < 0 or self.head[0] > 620 or self.head[1] < 0 or self.head[1] > 460:
            return True
        return False

    def move_head(self):
        moves = {
            'right': (20, 0),
            'up': (0, -20),
            'down': (0, 20),
            'left': (-20, 0)
        }
        step = moves[self.moving_direction]
        self.head[0] += step[0]
        self.head[1] += step[1]

    def generate_food(self):
        self.speed = len(self.body) // 16 if len(self.body) // 16 > 4 else self.speed
        for seg in self.body:
            x, y = seg
            self.map[x//20, y//20] = 1
        empty_pos = [pos for pos in self.map.keys() if not self.map[pos]]
        result = choice(empty_pos)
        self.food_color = list(choice(self.colors))
        self.food = [result[0]*20, result[1]*20]

# 画网格
def draw_Grid(screen):
    # 垂直方向
    Window_Width = 640
    Window_Height = 480
    Cell_Size = 20
    for x in range(0, Window_Width, Cell_Size):
        pygame.draw.line(screen, (255,160,122), (x, 0), (x, Window_Height))
    # 水平方向
    for y in range(0, Window_Height, Cell_Size):
        pygame.draw.line(screen, (255,160,122), (0, y), (Window_Width, y))


def main():
    key_direction_dict = {
        119: 'up',  # W
        115: 'down',  # S
        97: 'left',  # A
        100: 'right',  # D
        273: 'up',  # UP
        274: 'down',  # DOWN
        276: 'left',  # LEFT
        275: 'right',  # RIGHT
    }

    fps_clock = pygame.time.Clock()  ##设置游戏帧速
    pygame.init()
    pygame.mixer.init()
    snake = Snake()
    sound = False
    if path.exists('eat.wav'):
        sound_wav = pygame.mixer.Sound("eat.wav")
        sound = True
    title_font = pygame.font.SysFont('arial', 32)
    welcome_words = title_font.render('Welcome to My Snake', True, (0, 0, 0), (255, 255, 255))
    tips_font = pygame.font.SysFont('arial', 24)
    start_game_words = tips_font.render('Click to Start Game', True, (0, 0, 0), (255, 255, 255))
    close_game_words = tips_font.render('Press ESC to Close', True, (0, 0, 0), (255, 255, 255))
    gameover_words = title_font.render('GAME OVER', True, (205, 92, 92), (255, 255, 255))
    win_words = title_font.render('THE SNAKE IS LONG ENOUGH AND YOU WIN!', True, (0, 0, 205), (255, 255, 255))
    screen = pygame.display.set_mode((640, 480), 0, 32)
    pygame.display.set_caption('My Snake')
    new_direction = snake.moving_direction

    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == 27:
                    pygame.quit()
                    sys.exit()
                if snake.game_started and event.key in key_direction_dict:
                    direction = key_direction_dict[event.key]
                    new_direction = direction_check(snake.moving_direction, direction)
            elif (not snake.game_started) and event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 213 <= x <= 422 and 304 <= y <= 342:
                    snake.game_started = True
        screen.fill((255, 255, 255))
        print('Change Screen')
        print('Draw Grid')
        draw_Grid(screen)
        if snake.game_started:
            snake.moving_direction = new_direction  # 在这里赋值，而不是在event事件的循环中赋值，避免按键太快
            snake.move_head()
            snake.body.append(snake.head[:])
            if snake.head == snake.food:
                if sound:
                    sound_wav.play()
                snake.generate_food()
            else:
                snake.body.pop(0)
            for seg in snake.body:
                pygame.draw.rect(screen, [0, 0, 0], [seg[0], seg[1], 20, 20], 0)
            pygame.draw.rect(screen, snake.food_color, [snake.food[0], snake.food[1], 20, 20], 0)
            if snake.check_game_status():
                screen.blit(gameover_words, (241, 310))
                pygame.display.update()
                snake = Snake()
                new_direction = snake.moving_direction
                sleep(3)
            elif len(snake.body) == 512:
                screen.blit(win_words, (33, 210))
                pygame.display.update()
                snake = Snake()
                new_direction = snake.moving_direction
                sleep(3)
        else:
            screen.blit(welcome_words, (188, 100))
            screen.blit(start_game_words, (236, 310))
            screen.blit(close_game_words, (233, 350))
        pygame.display.update()
        fps_clock.tick(snake.speed)


if __name__ == '__main__':
    main()