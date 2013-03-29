import math
def median(list_num):
	list_num.sort()
	first_index = 0
	sec_index = 0
	median = 0.0
	print len(list_num)
	if len(list_num)%2==0:
		first_index = len(list_num)/2
		second_index = first_index + 1
		median = float(list_num[first_index-1] + list_num[second_index-1])/2.0
		#median = 5.0/2.0
		print median
		return median
	else:
		first_index = int(math.ceil(len(list_num)/2))
		median = list_num[first_index-1]
		return median

print median([1,2,3,4])

