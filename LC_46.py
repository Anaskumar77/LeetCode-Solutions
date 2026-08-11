# not a efficient approach

def permute( nums) :
    size = len(nums)
    res, perm = [], []

    def BackTracking():
        if len(perm) == size:
            res.append(perm[:])
            return

        for num in nums:
            if num not in perm:
                perm.append(num)
                BackTracking()
                perm.pop()
    BackTracking()
    return res

print(permute([1,2,3,4]))