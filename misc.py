# of a given list of ints, return the smallest
def smallest(num_list):
    smallest = num_list[0]
    for i in num_list:
        if smallest > i:
            smallest = i
    return smallest
	
# of two given int return the larger
def larger(num1, num2):
	if num1 > num2:
		return num1
	else:
		return num2
