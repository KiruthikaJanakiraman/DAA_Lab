b = [1,5,4,2,3]
a  = [2,4,3,5,1]

def partition(arr,pivot):
	left = []
	right = []
	for i in arr:
		if i < pivot:
			left.append(i)
		elif i > pivot:
			right.append(i)
	index = len(left)
	left.extend([pivot])
	left.extend(right)
	
	return left,index

res_a = []
res_b = []

def solve(a,b):
	global res_a
	global res_b
	if len(a) == 0:
		return
	if len(a) == 1:
		res_a.extend(a)
		res_b.extend(b)
		return	

	pivot = a[ len(a) // 2 ]
	b,index  = partition(b,pivot)
	a,index = partition(a,b[index])
	solve(a[:index],b[:index])
	res_a.append(pivot)
	res_b.append(pivot)
	solve(a[index+1:],b[index+1:])


solve(a,b)
print(res_a)
print(res_b)

