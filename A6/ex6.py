class node:
    def __init__(self,prob,symbol,l,r):
        self.prob=prob
        self.symbol=symbol
        self.l=l
        self.r=r
        self.bs=""

def insert(h,x):
    h1=h+[node(0,'','','')]
    size=len(h)+1
    i=size-1
    while(h1[i//2].prob>x.prob and i>0):
        h1[i]=h1[i//2]
        i=i//2
    h1[i]=x
    return h1

def buildHeap(lst):
    h=[node(-999,'','','')]
    for x in lst:
        h=insert(h,x)
    return h

def deleteMin(h):
    if(len(h)==1):
        print("Empty heap\n")
        return
    size=len(h)-1
    min=h[1]
    last=h[size]
    i=1
    while(i*2<=size):

        child=i*2
        if(child!=size and h[child+1].prob<h[child].prob):
            child=child+1
        if(last.prob > h[child].prob):
            h[i]=h[child]
        else:
            break;

        i=child

    h[i]=last
    h=h[:-1]
    return h,min


def tree(arr,symbol):
    tree_list=[]
    
    for i in range(len(arr)):
        tree_list+=[node(arr[i],symbol[i],'none','none')]
    
    return tree_list

def traverse(heap,bs):
    if(heap!='none'):
        traverse(heap.l,'0'+bs)
        if(heap.l=='none'and heap.r=='none'):
            heap.bs=bs[::-1]
        traverse(heap.r,'1'+bs)

arr=[0.54,0.23,0.18,0.03,0.41]
symbol=['a','b','c','d','e']
tree_list=tree(arr,symbol)

heap=buildHeap(tree_list)

while(len(heap)!=2):
    heap,l=deleteMin(heap)
    heap,r=deleteMin(heap)

    prob=l.prob+r.prob
    l.bs='0'+l.bs
    r.bs='1'+r.bs
        
    res=node(prob,'',l,r)
    heap=insert(heap,res)

traverse(heap[1],'')

avg=0
print("Symbol\tProbability\tBinary code\n")
for i in tree_list:
    print(i.symbol,"\t",i.prob,"\t\t",i.bs)
    avg+=i.prob*len(i.bs)
print("\nAverage Symbol length: %.2f"%avg)