def BinarySearch(arr,target):
    l = len(arr)
    L = 0
    R = l-0

    while L <= R:
        M = L + ((R - L )// 2)
        # print(M)
        if arr[M] == target:
            return M
        elif target < arr[M]:
             R = M - 1
        else:
            L = M + 1


    return False

arr1 =[1, 3, 5, 7, 9, 11]
arr2 = [2, 4, 6, 8, 10]
arr3 = [10, 20, 30, 40, 50]

print(BinarySearch(arr1,9))
print(BinarySearch(arr1,2))