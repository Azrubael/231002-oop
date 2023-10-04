#!/usr/bin/python3

class Money:
    def __init__(self, money):
        self.money = money
        
        
class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color
        

mmm = Money(1000)
MMM = Money(10000)
print(f"mmm money = {mmm.money}\t\tMMM money = {MMM.money}")

points_list = []
j = 1
for i in range(999):
    if i == 1:
        points_list.append(Point(j,j,"yellow"))
    else:
        points_list.append(Point(j,j))
    j = j + 2


for i in points_list:
    print(f"{i.x}  {i.y}  {i.color}", end="\t")


        