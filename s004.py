"""
4. A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
def check_palindrom(x):
	x = str(x)
	for i in range(len(x)//2):
		if x[i] != x[-1-i]:
			return False
	return True


def largest_palindrome_3dig_product():
	Max= 999
	Min = 100
	answer = 0
	#l1 = 0
	#l2 = 0
	while(Max >= Min):
		for i in range(Max,Min+1 , -1):
			prod = Max*i
			if check_palindrom(prod):
				if prod > answer:
					answer = prod
					#l1 =  Max
					#l2 = i
					Max = Max-1
					Min = i
		Max = Max-1
	return answer


	
if __name__=="__main__":
	print(largest_palindrome_3dig_product())

