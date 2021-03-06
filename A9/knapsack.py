import numpy as np

n = int(input())

Weights = [-1]
Values = [-1]

for i in range(n):
    ip = input().split(' ')
    Weights.append(int(ip[0]))
    Values.append(int(ip[1]))

W = int(input())

l = [[ -1 for i in range(W+1)] for j in range(n+1)]
chosen = np.array([False for i in range(n+1)])
array = np.array(l)

for i in range(n+1):
    for j in range(W+1):
        if i == 0 or j == 0:
            array[i][j] = 0

def knapsack(i,j):
    global array
    global Weights
    global Values
    global chosen

    value = 0
    if array[i][j] < 0:
        if j < Weights[i]:
            array[i][j] = knapsack(i-1,j)
        else:
            array[i][j] = knapsack(i-1,j)
            chosen[i] = False
            if Values[i] + knapsack(i-1,j-Weights[i]) > array[i][j]:
                array[i][j] = Values[i] + knapsack(i-1,j-Weights[i])
                chosen[i] = True
    return array[i][j]

print('Max Value: ',knapsack(n,W))
print(chosen[1:])