# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 14:42:27 2022

@author: 21A-003-SE
"""

class QuadraticEquation:
     
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        
    def get_a(self):
        return self.__a
    
    def get_b(self):
        return self.__b
    
    def get_c(self):
        return self.__c
    
    def getDiscriminant(self):
        d = (self.__b**2)-(4*self.__a*self.__c)
        return d
    
    def get_root1(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            c = -(self.__b)+(self.getDiscriminant()**0.5)/2*self.__a
            return c
        
    def get_root2(self):
        if self.getDiscriminant() < 0:
            return 0
        else:
            e = -(self.__b)-(self.getDiscriminant()**0.5)/2*self.__a
            return e
        
def main(a,b,c):
    f = QuadraticEquation(a,b,c)
    g = f.getDiscriminant()
    if g>0:
        print(f.get_root1(),f.get_root2())
    elif g==0:
        print(f.get_root1())
    else:
        print("The equation has no roots")
a = eval(input("enter value of a : "))
b = eval(input("enter value of b : "))
c = eval(input("enter value of c : "))
main(a,b,c)