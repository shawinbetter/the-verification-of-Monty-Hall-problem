"""
@Copyright
author : shawinqiu
last modified dat:2019/1/6 18:55

This program aims to test the monty hall problem and
give a visual chart for better understanding.

First, you will be asked to input 2 positive integers which are 
the time of each trial and the time of total trail. If what you input 
is not a positive integer, the program will ask you to do so again.

Then, a chart will be generated automically by the program.

The probability of choosing the reward when you change you decision is two times
higher than the porbability of choosing the reward when you do not change.
In other words, p1 = 2/3 p2 = 1/3
"""

import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import  MultipleLocator


while True:
    transfer = input("please input the times of each trial:")
    try:
        a = int(transfer)
        break
    except :
        print("you should input a positive integer!")
       
while True:
    if a>0:
        break;
    else:
        while True:
            transfer = input("please input the times of each trial:")
            try:
                a = int(transfer)
                break
            except :
                print("you should input a positive integer!")
                a = input("please input the times of each trial:")
"""
    The two while statement is to judge whether the context which was input by
    the user is a positive integer
"""

while True:
    transfer = input("please input the times of total trial:")
    try:
        b = int(transfer)
        break
    except :
        print("you should input a positive integer!")
       
while True:
    if b>0:
        break;
    else:
        while True:
            transfer = input("please input the times of total trial:")
            try:
                b = int(transfer)
                break
            except :
                print("you should input a positive integer!")
                b = input("please input the times of total trial:")

print()

print('*' * 50)
print('The charting is generating by Python......')  #字体颜色红色反白处理
print('*' * 50)
   

nochange = []  #to store the success_nochange
change = []   #to store the success_change
success_nochange = 0 #count the time of success while nochange
success_change = 0  #count the time of success while change

def no_change ():
    global success_nochange
    list1 = [0, 1, 2]  #assume that 0 is the reward, 1 and 2 are not reward
    random.shuffle(list1)  #reorder it,and assume that only choose the first number
    if list1[0] == 0:  #we choose the reward
        del list1[2] # just delete the last element since it is totally the samce
        success_nochange += 1  #since we make no change
    else:  #we do not choose the reward
        if list1[0] == 1:
            list1.remove(2)  #remove the rest non-reward
        else:
            list1.remove(1)  #remove the rest non-reward
        success_nochange += 0 #since we make no change, we definitely can not get the reward

def yes_change ():
    global success_change
    list1 = [0, 1, 2]  #assume that 0 is the reward, 1 and 2 are not reward
    random.shuffle(list1)  #reorder it,and assume that only choose the first number
    if list1[0] == 0:  #we choose the reward
        del list1[2] # just delete the last element since it is totally the samce
        success_change +=0  #since we make change, we definitely can not get the reward
    else:  #we do not choose the reward
        if list1[0] == 1:
            list1.remove(2)  #remove the rest non-reward
        else:
            list1.remove(1)  #remove the rest non-reward
        success_change += 1 #since we make change, we definitely get the reward

def run(func,times):#func is the name of the function you want to run, and times mean the times you want to run
    for i in range(times):
        func()

for i in range (b):
    run(no_change,a)
    nochange.append(success_nochange/a)
    success_nochange = 0

for i in range(b):
    run(yes_change,a)
    change.append(success_change/a)
    success_change = 0

y = nochange #安排list
z = change #安排list
mean_nochange = np.mean(nochange)#获取平均值
mean_change   = np.mean(change)#获取平均值

plt.figure(figsize=(15,7)) #设置画布大小

l1,=plt.plot(y)
l2,=plt.plot(z)

plt.plot([0,b],[mean_nochange,mean_nochange],color='#000000')#画出平均水平线
plt.plot([0,b],[mean_change,mean_change],color='#000000')#画出平均水平线
         
plt.grid(True) ##增加格点
yminorLocator = MultipleLocator(0.015)#y轴坐标设置为0.015的倍数 
plt.legend(handles = [l1,l2,],labels = ['nochange','change'],loc = 'best')#设置图例
plt.axis('tight') # 坐标轴适应数据量 axis 设置坐标轴
plt.xlabel('each trial of 1000 times')#x轴标签
plt.ylabel('probability of choosing the reward')#y轴标签
plt.title('The data of Monty Hall problem')#标题

plt.show()#画图




