a = [11,33,24,78,90,10,14,55,60]
def bubble_sort(a):
	for pass_number in range(len(a) - 1,0,-1):
		for i in range(pass_number):
			if a[i] > a[i+1]:
				number = a[i]
				a[i] = a[i+1]
				a[i+1] = number	
			
bubble_sort(a)
print (a)


