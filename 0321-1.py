# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 15:13:35 2020

@author: reaga
"""

# traveling
#‌ ‌traveling‌ ‌
"""‌ ‌
穿‌越‌時‌空‌ ‌ ‌
"""‌ ‌
import‌ ‌pygame‌ ‌
import‌ ‌random‌ ‌
 ‌ ‌
#‌ ‌根‌據‌count‌決‌定‌採‌用‌的‌圖‌像‌ ‌
def‌ ‌move(image1,‌ ‌image2):‌ ‌
    ‌global‌ ‌count‌ ‌
    ‌if‌ ‌count‌ ‌<‌ ‌5:‌ ‌
        ‌image‌ ‌=‌ ‌image1‌ ‌
    ‌elif‌ ‌count‌ ‌>=‌ ‌5:‌ ‌
        ‌image‌ ‌=‌ ‌image2‌ ‌
 ‌
    ‌if‌ ‌count‌ ‌>=‌ ‌10:‌ ‌
        ‌count‌ ‌=‌ ‌0‌ ‌
    ‌else:‌ ‌
        ‌count‌ ‌+=‌ ‌1‌ ‌
    ‌return‌ ‌image‌ ‌
 ‌
BLACK‌    ‌=‌ ‌(‌   ‌0,‌   ‌0,‌   ‌0)‌ ‌
WHITE‌    ‌=‌ ‌(‌ ‌255,‌ ‌255,‌ ‌255)‌ ‌
GREEN‌    ‌=‌ ‌(‌   ‌0,‌ ‌255,‌   ‌0)‌ ‌
RED‌      ‌=‌ ‌(‌ ‌255,‌   ‌0,‌   ‌0)‌ ‌
 ‌
pygame.init()‌ ‌
 ‌
size‌ ‌=‌ ‌(400,‌ ‌300)‌ ‌
screen‌ ‌=‌ ‌pygame.display.set_mode(size)‌ ‌
 ‌
pygame.display.set_caption("‌走‌動‌的‌方‌塊‌")‌ ‌
 ‌
done‌ ‌=‌ ‌False‌ ‌
 ‌
clock‌ ‌=‌ ‌pygame.time.Clock()‌ ‌
 ‌
 ‌
#‌ ‌--------‌ ‌主‌要‌的‌程‌式‌迴‌圈‌ ‌-----------‌ ‌
#‌ ‌方‌塊‌初‌始‌位‌置‌ ‌
x‌ ‌=‌ ‌0‌ ‌
y‌ ‌=‌ ‌0‌ ‌
count‌ ‌=‌ ‌0‌ ‌#‌ ‌延‌緩‌時‌間‌ ‌
locked‌ ‌=‌ ‌False‌ ‌#‌ ‌穿‌越‌模‌式‌ ‌
while‌ ‌not‌ ‌done:‌ ‌
    ‌#‌ ‌---‌ ‌事‌件‌迴‌圈‌ ‌event‌ ‌loop‌ ‌
    ‌for‌ ‌event‌ ‌in‌ ‌pygame.event.get():‌ ‌ ‌
        ‌if‌ ‌event.type‌ ‌==‌ ‌pygame.QUIT:‌ ‌ ‌
            ‌done‌ ‌=‌ ‌True‌ ‌ ‌
 ‌
    ‌keys‌ ‌=‌ ‌pygame.key.get_pressed()‌ ‌
 ‌
    ‌if‌ ‌not‌ ‌locked:‌ ‌#‌不‌在‌穿‌越‌模‌式‌ ‌
        ‌if‌ ‌keys[pygame.K_LEFT]:‌ ‌
            ‌x‌ ‌-=‌ ‌1‌ ‌ ‌
        ‌elif‌ ‌keys[pygame.K_RIGHT]:‌ ‌
            ‌x‌ ‌+=‌ ‌1‌ ‌
        ‌elif‌ ‌keys[pygame.K_UP]:‌ ‌
            ‌y‌ ‌-=‌ ‌1‌ ‌
        ‌elif‌ ‌keys[pygame.K_DOWN]:‌ ‌
            ‌y‌ ‌+=‌ ‌1‌ ‌
        ‌elif‌ ‌keys[pygame.K_SPACE]:‌ ‌
            ‌locked‌ ‌=‌ ‌True‌ ‌#‌ ‌進‌入‌穿‌越‌模‌式‌ ‌
        ‌else:‌ ‌
            ‌pass‌ ‌
    ‌else:‌ ‌#‌ ‌穿‌越‌模‌式‌ ‌
        ‌if‌ ‌count<10:‌ ‌
            ‌count‌ ‌+=‌ ‌1‌ ‌
        ‌else:‌ ‌
            ‌x‌ ‌=‌ ‌random.randrange(0,‌ ‌size[0])‌ ‌
            ‌y‌ ‌=‌ ‌random.randrange(0,‌ ‌size[1])‌ ‌
            ‌locked‌ ‌=‌ ‌False‌ ‌
            ‌count‌ ‌=‌ ‌0‌ ‌
 ‌
    ‌screen.fill(WHITE)‌ ‌
    ‌pygame.draw.rect(screen,‌ ‌RED,‌ ‌[x‌ ‌+‌ ‌10,‌ ‌y‌ ‌+‌ ‌10,‌ ‌10,‌ ‌10])‌ ‌
 ‌ ‌
    ‌pygame.display.flip()‌ ‌
 ‌
    ‌clock.tick(60)‌ ‌
 ‌
pygame.quit()‌ ‌
 ‌
