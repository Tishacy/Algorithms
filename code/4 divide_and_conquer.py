"""Divide and Conquer

01 Binary search
02 Calculate the n power of x
03 Fibonacci using matrix tricks
"""
import numpy as np

def binarySeach(x, A):
	if len(A) <= 1:
		# print(x)
		if A[0] == x:
			return print("%.2f exists" %x)
		else:
			return print("%.2f doesn't exist" %x)

	num = int(len(A) / 2)
	if x < A[num]:
		# print(A[:num])
		subarray = binarySeach(x, A[:num])
	else:
		# print(A[num:])
		subarray = binarySeach(x, A[num:])

def power(x, n):
	if n == 1:
		return x

	if n%2 == 0:
		return power(x, n/2) * power(x, n/2)
	else:
		return power(x,(n-1)/2) * power(x, (n-1)/2) * x

def fib(n):
	A = np.array([[1,1],[1,0]])
	# print(A)
	if n == 1 or n == 0:
		return A

	if n%2 == 0:
		return np.dot(fib(n/2), fib(n/2))
	else:
		return np.dot(np.dot(fib((n-1)/2), fib((n-1)/2)), A)

def Fibonacci(n):
	return fib(n)[0][0]

if __name__ == "__main__":
	A = list(range(0, 10000))
	binarySeach(1000, A)
	print(power(10, 20))
	print(Fibonacci(1000))
