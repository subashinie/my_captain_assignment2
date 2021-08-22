# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 19:08:34 2021

@author: suba
"""
print("while with break statement")
a=1
while a<9:
    print(a)
    if a==5:
        break
    a+=1

print("while with continue statement")
a=0
while a<9:
    a+=1
    if a==4:
        continue
    print(a)
    

print("for loop with break statement")

cars=["ford","nano","ferrari","hyundai"]
for x in cars:
    print(x)
    if x=="nano":
        break
    
print("for loop with continue statement")

veg=["cabbage","tomato","potato","ginger"]
for x in veg:
 if x=="potato":
   continue
 print(x)    
     
    