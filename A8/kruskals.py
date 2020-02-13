from collections import defaultdict

class Graph:
	
	def __init__(self,n):
		self.v = n;
		self.graph = []

	def add(self,a,b,c):
		self.graph.append([b,c,a]);

	def find(self,parent,i):
		if(parent[i]==i):
			return i

		else:
			return self.find(parent,parent[i])

	def union(self,parent,rank,x,y):
		xroot = self.find(parent,x)
		yroot = self.find(parent,y)

		if (rank[xroot] < rank[yroot]):
			parent[xroot] = yroot
		elif (rank[xroot] > rank[yroot]):
			parent[yroot] = xroot

		else:
			parent[xroot] = yroot
			rank[xroot] += 1

	def MST(self):

		res = []
		i = 0
		e = 0
		
		self.graph = sorted(self.graph, key=lambda item: item[2])

		parent = []
		rank = []
		
		for node in range(self.v):
			parent.append(node)
			rank.append(0)
		
		while (e < self.v - 1):

			a,b,c = self.graph[i]
			i += 1
			x = self.find(parent,a)
			y = self.find(parent,b)

			if (x!=y):
				e += 1
				res.append([a,b,c])
				self.union(parent,rank,x,y)

		print("Following are the edges in the constructed MST")

		print("\nSource    Dest    Weight")
		for u,v,weight in res:
			print("%d     --   %d   ==   %d" % (u,v,weight))


g = Graph(9) 
g.add(1,7,6)
g.add(2,8,2)
g.add(2,6,5)
g.add(4,0,1)
g.add(4,2,5)
g.add(6,8,6)
g.add(7,2,3)
g.add(7,7,8)
g.add(8,0,7)
g.add(8,1,2)
g.add(9,3,4)
g.add(10,5,4)
g.add(11,1,7)
g.add(14,3,5)
  
g.MST() 