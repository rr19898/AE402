# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 14:03:17 2020

@author: reaga
"""
import random 
n=random.randint(1,10)
for i in range(5):
    a=int(input("請輸入答案:"))
    if a==n:
        print("答對了")
    if a > n:
        print("too big")
    if a < n:
        print("too small")

