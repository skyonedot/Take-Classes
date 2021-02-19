#----------------------------------------
##Lesson2

#图形教程
##itertools对象迭代
import sys
from itertools import product
import pygame
from random import choice



color_list = [0,64,128,192,255]
colors = product(color_list,repeat=3)
#for c in colors:
#	print(c)  ##不可再现性
colors = list(colors)
##补充 统计list中某个元素方法

result = choice(colors)


##1. 颜色的RGB
##1.笛卡尔积


##小知识
aList = [123, 'xyz', 'zara', 'abc', 123];
print ("Count for 123 : ", aList.count(123));
print ("Count for zara : ", aList.count('zara'));