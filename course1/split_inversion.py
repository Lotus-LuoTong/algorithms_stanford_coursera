#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

def merge_countInv(A, B):
	n = len(A) + len(B)
	A.append(float('inf'))
	B.append(float('inf'))
	i = 0
	j = 0
	countInv = 0
	C = []
	for k in range(n):
		if(A[i] < B[j]):
			C.append(A[i])
			i += 1
		else:
			C.append(B[j])
			countInv += len(A) - i - 1
			j += 1
	A.pop()
	B.pop()
	return countInv, C

def countInv(A):
	n = len(A)
	if n == 1:
		return 0, A
	else:
		n2 = int(n/2)
		left = A[:n2]
		right = A[n2:]
		left_count, left_sort = countInv(left)
		right_count, right_sort = countInv(right)
		A_count, A_sort = merge_countInv(left_sort, right_sort)
		return A_count+left_count+right_count, A_sort


with open('IntegerArray.txt', 'r') as f:
	A = f.read().split('\r\n')
	A.pop()
	A = map(int, A)
	A_inv, A_sort = countInv(A)
	print A_inv



