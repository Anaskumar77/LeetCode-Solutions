def hello(nums , target):
    d = {}
    d[nums[0]] = 0
    for i in range(len(nums)):
        i += 1
        h = target-nums[i]
        if h in d:
            return [d[h],i]
        else:
            d[nums[i]] = i


nums = [5,4,3,2,1]
target = 3
print(hello(nums,target))