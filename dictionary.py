# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 12:48:38 2021

@author: suba
"""
car={"brand":"ferrari",
     "horsepower":"812",
     "torque":"718Nm",
     "year":"2021"}
a=car.copy()
print(a)


x=('Ford','BMW','RR')
y='5'
cars=dict.fromkeys(x,y)
print(cars)


X=car.get("torque")
print(X)


Y=car.items()
print(Y)

m=car.keys()
print(m)


car.pop("year")
print(car)

car.popitem()
print(car)

M=car.setdefault("oil","petrol")
print(M)
print(car)

car.update({"clutch":"auto"})
print(car)

N=car.values()
print(N)

car.clear()
print(car)