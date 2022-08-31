Upper_limit = 1000
Sum = 0

for i in range(Upper_limit):
	if i % 3 ==0 or i % 5 == 0:
		Sum += i

print(Sum)