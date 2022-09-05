"""
7. By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""


import math

def smallest_prime_factor(Num):
	for i in range(2,int(math.sqrt(Num)+1)):
		if Num % i == 0:
			return i
	return Num

def nth_prime(N):
	prime_list = []
	n = 2
	while len(prime_list) != N:
		spf = smallest_prime_factor(n)
		if spf == n:
			prime_list.append(n)
		n += 1
	return prime_list[-1]


	


	
if __name__=="__main__":
	N = 10001
	print(nth_prime(N))

