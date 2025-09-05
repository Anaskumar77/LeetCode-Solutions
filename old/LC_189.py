def hello(nums,k):
    for i in range(k):
        pop = nums.pop()
        nums.append(pop)

    return nums


n = [1,2,3,4,5,6,7,8]
k = 3
print(hello(n,k))