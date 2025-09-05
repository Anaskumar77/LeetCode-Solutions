def canJump(nums):
    lastIndex = len(nums) - 1
    print(lastIndex)
    if lastIndex == 0:
        return True
    else:
        def recurtion(index):
            if (lastIndex == index):
                return True
            for i in range(1,nums[index]):
                print(i)
                if i > lastIndex:
                    break
                result = recurtion(index+i)
                if result == True:
                    return result
            return False
        return recurtion(0)



print(canJump([2,1,1,3]))
# canJump([3,2,1,0,4])