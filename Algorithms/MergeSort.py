def MergeSort(array):

    def BackTrack(arr):
        n = len(arr)
        if n <= 1:
            return arr
        
        m = n // 2
        return merge(BackTrack(arr[:m]),BackTrack(arr[m:]))

        
    def merge(arr1,arr2):
        i , j = 0 , 0

        merged = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        merged.extend(arr1[i:])
        merged.extend(arr2[j:])
        return merged
    
    return BackTrack(array)


    
sorted_array = MergeSort([7,436,25,74,26,2,146,3,0,3,367])
print(sorted_array)

        
        
