a = [1,5,4,2,3]
b  = [2,4,3,5,1]


for i in range(len(b) - 1):
	for j in range(i,len(a)):
		if a[j] == b[i]:
			a[j],a[i] = a[i],a[j]
			break
		
print(a)
print(a)
