#!/usr/bin/env python

from Matrix import Matrix

def main() :
	A = Matrix(1,2,3,4,5,6,7,8,9)
	B = Matrix(2,3,4,5,6,7,8,9,10)
	print "Macierz A"
	print A
	print "Macierz B"
	print B
	print "Suma macierzy A i B"
	print A+B
	print "Iloczyn macierzy A i B"
	print A*B
	print "Iloczyn macierzy B i A"
	print B*A
	print "Iloczyn macierzy A i 5"
	print A*5


if __name__ == "__main__":
	main()

