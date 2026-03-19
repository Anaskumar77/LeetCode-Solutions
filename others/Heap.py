import heapq
Arr = [3,4,9,-3,10,-9,5,-2,-7,1]

heapq.heapify(Arr)
print(Arr)


heapq.heappush(Arr,35)
print(Arr)

minVal = heapq.heappop(Arr)
print(minVal)
print(Arr)


