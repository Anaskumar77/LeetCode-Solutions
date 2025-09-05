
def LC_26(nums):
    d = []
    n = 0
    for i in range(len(nums)):
        if nums[n] in d:
            nums.remove(nums[n])
        else:
            d.append(nums[n])
            n += 1
    k = len(nums)
    return k

nums = [1,1,2,2,3,3,4,4,5,5,6,6,6,6,7,7,7]
print(LC_26(nums))

