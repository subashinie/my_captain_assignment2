# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 12:24:41 2021

@author: suba
"""
def fullPyramid():
    for i in range(5):
        for s in range(5, i+1, -1):
            print(end=" ")
        for j in range(i + 1):
            print(end="* ")
        print()
fullPyramid()        
    