# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:15:12 2019

@author: joema
"""
import math
class vector(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def __str__(self):
        return "({},{})".format(round(self.x , 2), round(self.y , 2))
    def __repr__(self):
        return "({},{})".format(round(self.x , 2), round(self.y , 2))
    def __add__(self, vectorin):
        new = vector()
        new.x = self.x + vectorin.x 
        new.y = self.y + vectorin.y
        return new
    def __sub__(self, vectorin):
        new = vector()
        new.x = self.x + (vectorin.x * -1)
        new.y = self.y + (vectorin.y * -1)
        return new
    def __mul__(self, vectorin):
        if isinstance(vectorin, int):
            new = vector()
            new.x = self.x * vectorin
            new.y = self.y * vectorin
            return new
        else:
            new = vector()
            new.x = self.x * vectorin.x
            new.y = self.y * vectorin.y
            return new
    def __rmul__(self, vectorin):
        if isinstance(vectorin, int):
            new = vector()
            new.x = self.x * vectorin
            new.y = self.y * vectorin
            return new
        else:
            new = vector()
            new.x = self.x * vectorin.x
            new.y = self.y * vectorin.y
            return new
    def magnitude(self):
        return math.sqrt((self.x**2 + self.y**2))
    def unit(self):
        try:
            scale = 1 / self.magnitude()
            self.x = self.x * scale
            self.y = self.y * scale
        except ZeroDivisionError:
            print( "Cannot convert zero vector to a unit vector")
            raise(ValueError)
            
            