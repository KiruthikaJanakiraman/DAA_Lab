def read():
    a = input('Enter elements: ')
    array = list(map(int,a.split()))
    return array  

def heap_sort(arr):
    i = 0
    while 2 ** (i + 1) < len(arr):
        if arr[2 ** i] > arr[2 ** (i + 1)]:
            arr[2 ** i],arr[2 ** ( i + 1)] = arr[2 ** (i + 1)],arr[2 ** i]
            i = i + 1
        else: 
            break
    return arr

arr = read()
print('The input array is:',arr)
print('The Sorted Array is:',heap_sort(arr))