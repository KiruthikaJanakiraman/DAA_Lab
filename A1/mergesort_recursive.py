def read(i):
    inp = input('Enter elements of array ' + str(i) + ': ')
    arr = list(map(int,inp.split()))
    return arr  

def merge(arr1,arr2,result):
    if len(arr1) and len(arr2):
        if arr1[0] < arr2[0]:
            result.append(arr1[0])
            return merge(arr1[1:],arr2,result)
        else:
            result.append(arr2[0])
            return merge(arr1,arr2[1:],result)

    elif len(arr1):
        result += arr1
        return result
    elif len(arr2):
        result += arr2
        return result
    else:
        return result


arr1 = read(1)
arr2 = read(2)

result = []

result = merge(arr1,arr2,result)

print("Merge sorted: ",result)