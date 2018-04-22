#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import math

def karatsuba(A, B):
	A = str(A)
	B = str(B)
	#assert len(A) == len(B)
	n = max(len(A), len(B))
	if(n<=3):
		return int(A) * int(B)
	else:
		n2 = int(math.ceil(n / 2.0))
		n3 = n - n2
		#print(n, n2)
		a = int(A[:(len(A) - n2)])
		b = int(A[(len(A) - n2):])
		c = int(B[:(len(B) - n2)])
		d = int(B[(len(B) - n2):])
		ac = karatsuba(a, c)
		if not ac == a * c:
			print 'ac',a,b,c,d
		bd = karatsuba(b, d)
		if not bd == b * d:
			print 'bd',a,b,c,d
		ad_bc = karatsuba((a+b), (c+d)) - ac - bd
		if not ad_bc == a * d + b * c:
			print 'ad_bc',a,b,c,d
		#ad = karatsuba(a, d)
		#bc = karatsuba(b, c)
		return int((10 ** (2 * n2)) * ac + (10 ** n2) * (ad_bc) + bd)


A = input('Input the first number:')
B = input('Input the second number:')
#A = '3141592653589793238462643383279502884197169399375105820974944592'
#B = '2718281828459045235360287471352662497757247093699959574966967627'
#ans = 8539734222673567065463550869546574495034888535765114961879601127067743044893204848617875072216249073013374895871952806582723184
res = karatsuba(A, B)
#print(ans == res)
print('the Karatsuba multiplication of the two number is {}'.format(karatsuba(A, B)))


