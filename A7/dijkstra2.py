from collections import defaultdict 
import sys 

class Heap(): 

	def __init__(self): 
		self.array = [] 
		self.size = 0
		self.pos = [] 

	def newMinHeapNode(self, v, dist): 
		minHeapNode = [v, dist] 
		return minHeapNode 

	def swapMinHeapNode(self,a, b): 
		t = self.array[a] 
		self.array[a] = self.array[b] 
		self.array[b] = t 

	def minHeapify(self, index): 
		smallest = index 
		left = 2*index + 1
		right = 2*index + 2

		if left < self.size and self.array[left][1] < self.array[smallest][1]: 
			smallest = left 

		if right < self.size and self.array[right][1] < self.array[smallest][1]: 
			smallest = right 

		if smallest != index: 

			self.pos[ self.array[smallest][0] ] = index 
			self.pos[ self.array[index][0] ] = smallest 

			self.swapMinHeapNode(smallest, index) 

			self.minHeapify(smallest) 

	def extractMin(self): 
 
		if self.isEmpty() == True: 
			return

		root = self.array[0] 

		lastNode = self.array[self.size - 1] 
		self.array[0] = lastNode 

		self.pos[lastNode[0]] = 0
		self.pos[root[0]] = self.size - 1

		self.size -= 1
		self.minHeapify(0) 

		return root 

	def isEmpty(self): 
		return True if self.size == 0 else False

	def decreaseKey(self, v, dist): 

		i = self.pos[v] 

		self.array[i][1] = dist 

		while i > 0 and self.array[i][1] < self.array[(i - 1) / 2][1]: 

			self.pos[ self.array[i][0] ] = (i-1)/2
			self.pos[ self.array[(i-1)/2][0] ] = i 
			self.swapMinHeapNode(i, (i - 1)/2 ) 

			i = (i - 1) / 2; 

	def isInMinHeap(self, v): 

		if self.pos[v] < self.size: 
			return True
		return False


def output(dist, n): 
	print "Vertex\tDistance from source"
	for i in Dict: 
		print "%c\t\t%d" % (i,dist[Dict[i]]) 


class Graph(): 

	def __init__(self, V): 
		self.V = V 
		self.graph = defaultdict(list) 

	def addEdge(self, source, dest, weight): 

		newNode = [Dict[dest], weight] 
		self.graph[Dict[source]].insert(0, newNode) 

		
		newNode = [Dict[source], weight] 
		self.graph[Dict[dest]].insert(0, newNode) 

	def dijkstra(self, source): 

		V = self.V 
		dist = []

		minHeap = Heap() 

		for v in range(V): 
			dist.append(sys.maxint) 
			minHeap.array.append( minHeap.newMinHeapNode(v, dist[v]) ) 
			minHeap.pos.append(v) 

		minHeap.pos[Dict[source]] = Dict[source] 
		dist[Dict[source]] = 0
		minHeap.decreaseKey(Dict[source], dist[Dict[source]]) 

		minHeap.size = V; 

		while minHeap.isEmpty() == False: 

			newHeapNode = minHeap.extractMin() 
			u = newHeapNode[0] 

			for pCrawl in self.graph[u]: 

				v = pCrawl[0] 

				
				if minHeap.isInMinHeap(v) and dist[u] != sys.maxint and pCrawl[1] + dist[u] < dist[v]: 
						dist[v] = pCrawl[1] + dist[u] 

						minHeap.decreaseKey(v, dist[v]) 

		output(dist,V) 


graph = Graph(12) 
Dict={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7,'i':8,'j':9,'k':10,'l':11}
graph.addEdge('a', 'b', 3) 
graph.addEdge('a', 'd', 4) 
graph.addEdge('a', 'c', 5)  
graph.addEdge('b', 'e', 3) 
graph.addEdge('b', 'f', 6) 
graph.addEdge('c', 'd', 2) 
graph.addEdge('c', 'g', 4) 
graph.addEdge('d', 'e', 1) 
graph.addEdge('d', 'h', 5) 
graph.addEdge('e', 'f', 2) 
graph.addEdge('e', 'i', 4)
graph.addEdge('f', 'j', 5)
graph.addEdge('g', 'h', 3)
graph.addEdge('g', 'k', 6)
graph.addEdge('h', 'i', 6)
graph.addEdge('h', 'k', 7)
graph.addEdge('i', 'l', 5)
graph.addEdge('i', 'j', 3)
graph.addEdge('k', 'l', 8)
graph.addEdge('j', 'l', 9) 
graph.dijkstra('a') 

