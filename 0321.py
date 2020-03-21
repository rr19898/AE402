# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 14:20:36 2020

@author: reaga
"""

import pygame
# 定義一些會用到的顏色
# 常數使用大寫
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (  46, 126, 196)
PINK     = (  255,228, 225)
# 初始化pygame
pygame.init()

# 創造一個pygame視窗並設定大小及標題
size = (700, 500)
screen = pygame.display.set_mode(size)



pygame.display.set_caption("我的遊戲")

# 設定一個開關供迴圈使用
done = False

# 創造一個clock控制畫面更新速度
clock = pygame.time.Clock()

x=0
y=0

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 1
    elif keys[pygame.K_RIGHT]:
        x += 1
    elif keys[pygame.K_UP]:
        y -= 1
    elif keys[pygame.K_DOWN]:
        y += 1
    else:
        pass
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [x + 10, y + 10, 10 , 10])
    
    pygame.display.flip()

    clock.tick(60)
game.quit