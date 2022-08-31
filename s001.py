import time


def method1():
	start1 = time.time()
	Upper_limit = 1000
	Sum = 0
	for i in range(Upper_limit):
		if i % 3 ==0 or i % 5 == 0:
			Sum += i
	stop1 = time.time()
	comp_time= stop1 - start1
	return Sum , comp_time



def method2():
	start2 = time.time()
	Sum = sum(i for i in range(1000) if i % 3==0 or i% 5 == 0)
	stop2 = time.time()
	comp_time = stop2-start2
	return Sum , comp_time


def multiples_sum():
	answer = sum(i for i in range(1000) if i % 3==0 or i% 5 == 0)
	return answer


if __name__=="__main__":
	print(multiples_sum())
