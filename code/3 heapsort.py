# -*- coding: utf-8 -*-
"""Heap sort
"""
import time

def left(i):
	return 2*(i+1)-1

def right(i):
	return 2*(i+1)

def parent(i):
	return (i-1)//2

def max_heapify(A, i):
	l, r = left(i), right(i)
	largest = i
	if l < len(A) and A[l] >= A[largest]:
		largest = l
	if r < len(A) and A[r] >= A[largest]:
		largest = r
	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		max_heapify(A, largest)

def build_max_heap(A):
	i = parent(A[-1])
	while i >= 0:
		max_heapify(A, i)
		i -= 1
	# print("heap:\n", A)

def heapsort(A):
	result = []
	build_max_heap(A)
	while len(A) > 1:
		result.append(A[0])
		A[0], A[-1] = A[-1], A[0]
		A = A[:-1]
		max_heapify(A, 0)
	result.append(A[0])
	return result


if __name__=="__main__":
	N = 1000
	A = list(range(0, N))
	t1 = time.time()
	A = heapsort(A)
	print(A)
	print("cost %.4fs" %(time.time()-t1))
