n=int(input("Enter n: "))
num = n
s=""
while(n>0):
	binary=n%2
	s=s+str(binary)
	n=n/2
print(s)

M=[[1,1],[1,0]]
term=M
if(s[0]=='1'):
	result=M
else:
	result=[[1,0],[0,1]]

def mult(a,b):
	res=[[0,0],[0,0]]
	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(b)):
				res[i][j]+=a[i][k] * b[k][j]
	return res

for b in s[1:len(s)]:
	term=mult(term,term)
	if(b=='1'):
		result=mult(result,term)

for i in result:
	print(i)

print"The",num,"th fibonacci term is ",result[0][0]
