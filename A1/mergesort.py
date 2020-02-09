def read(i):
    inp = input('Enter the elements of array ' + str(i) + ': ')
    arr = list(map(int,inp.split()))
    return arr

def ordered_merge(a1,a2):
    result = []
    i = 0
    j = 0

    while i<len(a1) and j<len(a2):
        if a1[i]<a2[j]:
            result.append(a1[i])
            i=i + 1
        else:
            result.append(a2[j])
            j=j + 1
    
    if i!=len(a1):
        result  = result + a1[i:]
    elif j != len(a2):
        result = result + a2[j:]
    else:
        pass

    print("Merge sorted (recursive): ",result)

arr1 = read(1)
arr2 = read(2)
ordered_merge(arr1,arr2)
            
