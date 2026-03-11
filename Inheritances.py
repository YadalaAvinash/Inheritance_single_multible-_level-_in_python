# 9.10 PM
# 11-03-2026
"""
Inheritance in Python
1.They are 5 type Inheritance in Python
!. single Inheritance in Python
2.multiblelevel Inheritance in Python
3. multilevel
4.Hybrid
5.

"""
'''
class parsent:                                          # parsent class
    def __init__(self,home,land):
        self.home=home
        self.land=land
    def printparsent(self):
        print(self.home)
        print(self.land)

class son1(parsent):                                    # child class 
    def __init__(self,home,land,car,bike):
        parsent.__init__(self,home,land)
        self.car=car
        self.bike=bike
    def printson1(self):
        print(self.car)
        print(self.bike)

child=son1("Somala","2 arcland","R R","R E")
child.printson1()
child.printparsent()
'''
class grandparsent1:
    def __init__(self,home):
        self.home=home
    def printgrand(self):
        print(self.home)
class parsent:
    def __init__(self,money,gold):
        self.money=money
        self.gold=gold
    def parsent1(self):
        print(self.money)
        print(self.gold)
class child(grandparsent1,parsent):
    def __init__(self,home,money,gold,car):
        grandparsent1.__init__(self,home)
        parsent.__init__(self,money,gold)
        self.car=car
    def printchild(self):
        print(self.car)
human=child("Somala","1crore","20kgms","R R")
human.printgrand()
human.parsent1()
human.printchild()

