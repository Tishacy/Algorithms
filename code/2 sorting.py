# -*- coding: utf-8 -*-
"""Commen sorting algorithms

01 Insertion sort
02 Merge sort
03 Quick sort
04 Counting sort
"""
import numpy as np
import matplotlib.pyplot as plt
import time

def InsertionSort(A, n):
	"""Insertion sort"""
	for j in range(1, n):
		key = A[j]
		i = j-1
		while i>=0 and A[i]>key:
			A[i+1] = A[i]
			i = i-1
		A[i+1] = key

def MergeSort(A):
	"""Merge sort"""
	if len(A) <= 1:
		return A
	num = int(len(A) / 2)
	left = MergeSort(A[:num])
	right = MergeSort(A[num:])
	return Merge(left, right)

def Merge(left, right):
	temp = []
	l, r = 0, 0
	while l < len(left) and r <len(right):
		if left[l] < right[r]:
			temp.append(left[l])
			l += 1
		else:
			temp.append(right[r])
			r += 1
	temp += list(left[l:])
	temp += list(right[r:])
	return temp

def QuickSort(A, low, high):
	"""Quick sort"""
	if low < high:
		pivot_index = Partition(A, low, high)
		QuickSort(A, low, pivot_index)
		QuickSort(A, pivot_index+1, high)

def Partition(A, low, high):
	# swap(A, low, np.random.randint(low, high)) # Choose the pivot randomly
	pivot = A[low]
	i = low
	for j in range(low+1, high):
		if A[j] <= pivot:
			i += 1
			swap(A, i, j)
	swap(A, low, i)
	return i

def swap(A, i, j):
	A[i], A[j] = A[j], A[i]

def CountingSort(A):
	"""Counting sort
	This algorithm requires that elements in A are integers.
	"""
	# initialization
	k = max(A) # k is the range of A
	C = np.zeros(k+1)
	B = np.zeros(len(A))

	for i in range(len(A)):
		C[A[i]] += 1

	for i in np.arange(1, len(C)):
		C[i] += C[i-1]

	for i in np.arange(len(A)-1, 0, -1):
		B[int(C[A[i]])-1] = A[i]
		C[A[i]] -= 1
	print(C)
	return B


if __name__ == "__main__":
	SEED = 2
	N = 10000
	rdm = np.random.RandomState(SEED)
	x = np.arange(0, N)

	plt.rc('text', usetex=True)
	plt.rc('font', family='serif')
	plt.figure(figsize=(6, 5))
	A = rdm.randint(0, 100, size=N)
	plt.plot(x, A, '.', color='r', alpha=0.5, label='unsorted')

	t1 = time.time()
	# A = MergeSort(A)
	# InsertionSort(A, len(A))
	QuickSort(A, 0, len(A))
	# A = CountingSort(A)
	dt = time.time() - t1
	print("This sorting algorithm costs %.4f seconds" %dt)

	plt.plot(x, A, '.', color='k', alpha=0.5, label='sorted')

	plt.legend()
	plt.show()
