#!/usr/bin/env python

class Matrix:
	
	def __init__(self,elem11,elem12,elem21,elem22):
		self.__M11 = elem11
		self.__M12 = elem12
		self.__M21 = elem21
		self.__M22 = elem22

	def __str__(self):
		return str(self.__M11) + ' ' + str(self.__M12) + '\n' + str(self.__M21) + ' ' + str(self.__M22)

	def add(self,matrix2):
		return Matrix(self.__M11+matrix2.__M11,self.__M12+matrix2.__M12,self.__M21+matrix2.__M21,self.__M22+matrix2.__M22)

	def multiply(self,matrix2):
		return Matrix(self.__M11*matrix2.__M11 + self.__M12*matrix2.__M21,self.__M11*matrix2.__M12+self.__M12*matrix2.__M22,self.__M21*matrix2.__M11+self.__M22*matrix2.__M21,self.__M21*matrix2.__M12+self.__M22*matrix2.__M22)
		




m=Matrix(1,2,3,4)
print m
n = Matrix(2,3,4,5)
print
print m.add(n)
print
print m.multiply(n)
