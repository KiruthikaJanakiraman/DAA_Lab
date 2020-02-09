import time
import random
import math

def max_sub_cubic(arr):
      n = len(arr)
      thisSum=0
      maxSum=0
      for i in range(n):
          for j in range(n):
              thisSum=0;
              for k in range (i,j+1):
                    thisSum+=arr[k]
              if thisSum > maxSum:
                    maxSum=thisSum
      return maxSum    



for i in range(10):

    n=int(input("Enter array size: "))
    total=0
    avg=0

    for j in range (10):
        arr=[]

        for k in range(n):
          arr.append(random.randint(-100,100))

        start=time.time()
        maxSum = max_sub_cubic(arr)
        end=time.time()
        total+=end-start
         
        print('Array: ', arr)
        print('Maximum subarray sum: ' ,maxSum)
        print('Execution time: ' ,end-start)

    avg=total/10

    print(' \nAverage time : ', avg)
    print(' \nlog(n)       : ', avg/math.log(n))
    print(' \nn            :', avg/n)
    print(' \nn^2          :', avg/(n*n))
    print(' \nn^3          :', avg/(n*n*n))
    print(' \n2^n          :', avg/(2**n))




  
 
