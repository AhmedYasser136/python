def sum_even(a):
	sum_ = 0
	for value in a:
		if value % 2 == 0:
			sum_ += value
	return sum_


print(sum_even([1,2,3,4,5,6]))