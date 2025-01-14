from typing import Self
from math import sin, cos, asin, acos, degrees, radians

class Vector():
    def __init__(self, x: float, y: float, h: float):
        '''
        Using flat coordinates because DCS world is flat and not spherical.
        flatmodulus is the modulus of the vector projected over the xy plane.
        modulus is the actual full modulus of the vector.
        Phi is the angle between y and x, the bearing so to speak.
        Theta is the angle between the point's vector and it's projection over the xy plane.
        '''
        self.x = x
        self.y = y
        self.h = h

        self.flatModulus = pow(x,2) + pow(y,2)
        self.Modulus = self.flatModulus + pow(h,2)
        self.phi = degrees(acos(y/x))
        self.theta = degrees(asin(h/self.Modulus))

    def fromPolar(modulus, phi, theta) -> Self:
        x = modulus*cos(radians(theta))*cos(radians(phi))
        y = modulus+cos(radians(theta))*sin(radians(phi))
        h = modulus*sin(radians(theta))
        return Vector(x, y, h)

    def vectorBetweenPoints(endPoint: Self, startPoint: Self) -> Self:
        return Vector(endPoint.x-startPoint.x,
                     endPoint.y-startPoint.y,
                     endPoint.h-startPoint.h)
    
    def addVectors(vector1: Self, vector2: Self) -> Self:
        return Vector(vector1.x+vector2.x,
                      vector1.y+vector2.y,
                      vector1.h+vector2.h)
    
    def __sub__(self, startPoint: Self, /) -> Self:
        return self.vectorBetweenPoints(self, startPoint)
    
    def __add__(self, vector: Self, /) -> Self:
        return self.addVectors(self, vector)
