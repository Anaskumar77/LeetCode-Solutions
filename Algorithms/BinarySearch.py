def BinarySearch(arr,target):
    l = len(arr)
    L = 0
    R = l-0

    while L <= R:
        M = L + ((R - L )// 2)
        if arr[M] == target:
            return M
        elif target < arr[M]:
             R = M - 1
        else:
            L = M + 1
    return False



def lower_bound(arr, target):
    L, R = 0, len(arr)

    while L < R:
        M = (L + R) // 2
        if arr[M] < target:
            L = M + 1
        else:
            R = M

    return L


lower_bound([1,2,7],9)



    

arr1 =[1, 3, 5, 7, 9, 11]
arr2 = [2, 4, 6, 8, 10]
arr3 = [10, 20, 30, 40, 50]

print(BinarySearch(arr1,9))
print(BinarySearch(arr1,2))
