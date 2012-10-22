#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sympy

pi=3.14159265358979324

class Ellipsoide:
    def __init__(self,a = [0.75,1.,0.5],point = [0.,0.,-1.]):
        self.__point = point # координаты центра эллипсоида в глобальной системе
        self.__a = a
        self.__computeAxesReverse = False
        self.__axesReverse = []
        self.__toGlobalCoordinates = [[1.0,0.,0.],[0.,1.,0.],[0.,0.,0.]] # alpgl -  матрица переходо от координат эллипсоида к глобальной системе координат
    def setAxes(self,a):
        self.__a = a
    def getAxes(self):
        return self.__a
    def getAxesReverse(self):
        if not self.__computeAxesReverse:
            for x in self.__a:
                self.__axesReverse.append(1./x)
            self.__computeAxesReverse = True
        return self.__axesReverse

class CoordinateSystem:
    pass

class Sampling:
    def __init__(self,model = "ellipsoide"):
        self.__model = model
        self.__radiusHat = 2.0
        self.__lengthMinimumsMax = 5
        self.__neighborsMax = 50
        self.__roughNumberPoints = 25

class Environment:
    def __init__(self,ρ = 20,ν = 0.33,λ = 2.,μ = 1.):
        self.__ρ = ρ
        self.__ν = ν
        self.__λ = λ
        self.__μ = μ
    def ρGet(self):
        return self.__ρ

class ProfileControl:
    def __init__(self,d = 19):
        self.__d = d
        self.__points = [[0. for i in range(3)] for j in range(d)]
        self.__shifts = [[0. for i in range(3)] for j in range(d)]         
        
        for i in range(0,d,1):
            self.__points[i][0] = -0.45
            self.__points[i][1] = -0.45 + 0.05 * i
            self.__points[i][2] = -0.75
            
            self.__shifts[i][0] = 0.05
            self.__shifts[i][1] = 0.
            self.__shifts[i][2] = 0.


class SourceWave:
    def __init__(self,coordinates = [0.,0.,-2 * pi],model = "dotty",power = 1,ω = 1.):
        # self.__point = point # 
        self.__model = model # тип источника
        self.__power = power # мощность источника
        self.__coordinates = coordinates # координаты источника
        self.__ω = ω # круговая частота колебаний

s = SourceWave()

e = Ellipsoide()

p = ProfileControl()

Ω_e = Environment()
Ω_i = Environment(ρ = 4.)

print(e.getAxesReverse())
print(Ω_e.ρGet())
print(Ω_i.ρGet())
α = sympy.Symbol('α')
print(sympy.diff(α**2,α))
