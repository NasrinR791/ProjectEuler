"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

"""
def sqrt(x):

	To be done later

"""
import math

def smallest_prime_factor(Num):
	for i in range(2,int(math.sqrt(Num)+1)):
		if Num % i == 0:
			return i
	return Num


def largest_prime_factor(Num):
	while True:
		spf = smallest_prime_factor(Num)
		if spf < Num:
			Num = Num // spf
		else:
			return Num


if __name__=="__main__":
	Num = 600851475143
	print(largest_prime_factor(Num))
