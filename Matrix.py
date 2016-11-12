#!/usr/bin/env python

from math import sqrt
from copy import deepcopy
import numbers

class Matrix(object) :
	def __init__(self, *vector) :
		size = sqrt(len(vector))
		if(size == int(size)) :
			self.__size = int(size)
			self.__matrix = []
			temp_list = []
			for i in range(len(vector)) :
				temp_list.append(vector[i])
				if not (i+1) % self.__size :
					self.__matrix.append(temp_list[:])
					del temp_list[:]
		else :
			raise Exception("Wrong number of elements - this class represents a square matrix.")

	def __str__(self) :
		temp_string = ""
		for row in self.__matrix :
			temp_string+=str(row) + '\n'
		return temp_string
	def __add__(self,matrix_to_add):
		return self.__add(matrix_to_add)
			
	def __radd__(self,matrix_to_add):
		return self.__add(matrix_to_add)
			
	def __mul__(self,to_multiply_by):
		return self.__multiply(to_multiply_by);
		
	def __rmul__(self,to_multiply_by) :
		result = 0
		if isinstance(to_multiply_by,Matrix) :
			result = to_multiply_by.__multiply(self)
		else :
			result = self.__multiply(to_multiply_by)
		return result
		
	def __len__(self) :
		return self.__size
		
	def __iter__(self) :
		for row in self.__matrix :
			yield row
			
	def __add(self,matrix_to_add):
		if isinstance(matrix_to_add,Matrix) :
			if len(self) == len(matrix_to_add) :
				result_matrix = deepcopy(self)
				for i in range(len(result_matrix)) :
					for j in range(len(result_matrix)) :
						result_matrix[i][j] += matrix_to_add[i][j]
				return result_matrix
			else :
				raise ValueError("Wrong matrix size - you can only add matrices of the same size")
		else :
			raise TypeError("Wrong argument type - you can only add a matrix to a matrix")

	def __multiply(self,to_multiply_by) :
		if isinstance(to_multiply_by,Matrix) :
			if len(self) == len(to_multiply_by) :
				result_matrix = deepcopy(self)
				for i in range(len(self)) :
					for j in range(len(to_multiply_by)) :
						result_matrix[i][j]=0
						for k in range(len(result_matrix)):
							result_matrix[i][j] += self[i][k] * to_multiply_by[k][j]
				return result_matrix
			else :
				raise ValueError("Wrong value type - you can only multiply matrices of the same size")
		elif isinstance(to_multiply_by,numbers.Real) :
			result_matrix = deepcopy(self)
			result_matrix.__matrix = map(lambda x: map(lambda y: y* to_multiply_by,x),result_matrix.__matrix)
			return result_matrix
		else :
			raise TypeError("Wrong argument type - you can only multiply a matrix by a matrix or a number")
			
	def __getitem__(self,i) :
		if i < self.__size :
			return self.__matrix[i]
		else :
			raise IndexError("Row index out of range")
