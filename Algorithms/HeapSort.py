import heapq

def HeapSort(array):
    heapq.heapify(array)
    ln = len(array)
    sorted = [0] * ln

    for i in range (ln):
        minVal = heapq.heappop(array)
        sorted[i] = minVal
        

    return sorted


arr = [3,4,9,-3,10,-9,5,-2,-7,1]

print(HeapSort(arr))