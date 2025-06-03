

def is_valid(arr):

	for i in range(len(arr) - 1):
		if arr[i] > arr[i + 1]:
			if max(arr[i:]) > arr[i]:
				return False
		else:
			if min(arr[i:]) < arr[i]:
				return False
	return True


print(is_valid([500,300,100,10,400]))