
def even_fib_sum():
	fib = [1,2]

	new_fib = fib[-1]+fib[-2]

	while new_fib <= 4000000:
		fib.append(new_fib)
		new_fib = fib[-1]+fib[-2]
	answer = sum(i for i in fib if i % 2==0)
	return answer


if __name__=="__main__":
	print(even_fib_sum())
