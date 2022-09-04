"""
5. 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def Factorize(i , factors):
	for j in factors:
		if i % j == 0:
			i = i/j
	return i

def smallest_multiple(Num):
	Answer = 1
	factors = []
	for i in range(1,Num+1):
		factors.append(Factorize(i , factors))
		Answer *= factors[i-1]
	return int(Answer)


	
if __name__=="__main__":
	Num = 20
	print(smallest_multiple(Num))

