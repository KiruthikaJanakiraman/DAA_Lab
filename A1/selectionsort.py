def print_array(a,low,high):
	return a[low:high]

def read_array():
	a=input("Enter list: ")
	l=list(map(int,a.split()))
	return l

def minimum(a,low,high):
	l=print_array(a,low,high)
	min=0
	for i in range(1,len(l)):
		if(l[min]>l[i]):
			min=i
	return (min + low)

def selectionsort(arr):
	for i in range(len(arr)-2):
		arr[minimum(arr,i,len(arr))],arr[i]=arr[i],arr[minimum(arr,i,len(arr))]
	return arr

for i in range(3):
	arr=read_array()
	print("Sorted array:",selectionsort(arr))

