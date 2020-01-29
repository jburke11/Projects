# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 16:26:23 2019

@author: joema
"""

class Time(object):
    def __init__(self,hour = 0, minute = 0, seconds = 0 ):
        # initialize instance
        # hours, minutes, and seconds
        self.hours = hour
        self.minute = minute
        self.seconds = seconds
    def __repr__(self):
        return ("Class Time: {:02d}:{:02d}:{:02d}".format(self.hours, self.minute, self.seconds))
    def __str__(self):
        return ("{:02d}:{:02d}:{:02d}".format(self.hours, self.minute, self.seconds))
    def from_str(self, time):
        num = time.split(":")
        self.hours = int(num[0])
        self.minute = int(num[1])
        self.seconds = int(num[2])


#import clock

A = Time( 12, 25, 30 )

print( A )
print( repr( A ) )
print( str( A ) )
print()

B = Time( 2, 25, 3 )

print( B )
print( repr( B ) )
print( str( B ) )
print()

C = Time( 2, 25 )

print( C )
print( repr( C ) )
print( str( C ) )
print()

D = Time()

print( D )
print( repr( D ) )
print( str( D ) )
print()

D.from_str( "03:09:19" )

print( D )
print( repr( D ) )
print( str( D ) )


