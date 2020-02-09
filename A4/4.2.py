from Point import Point

n = int(input('Enter number of ATMs: '))

arr = []

print('Enter coordinates of ATMs: ')
for i in range(n):
    x,y = tuple(map(float,input().split()))
    arr.append(Point(x,y))

min1 = arr[0]
min2 = arr[1]

for i in range(n-1):
    for j in range(i+1,n):
        if arr[i].distance(arr[j]) < min1.distance(min2):
            min1 = arr[i]
            min2 = arr[j]

print('Closest pair: ' + str(min1) + ' ' + str(min2) )
