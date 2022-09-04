"""
6. Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""



def squared_sum_sum_squared_difference(Num):
	Sum = 0
	S_Sum = 0
	for i in range(1,Num+1):
		Sum += i
		S_Sum += (i*i)
	return int((Sum*Sum)-S_Sum)


	
if __name__=="__main__":
	Num = 100
	print(squared_sum_sum_squared_difference(Num))

