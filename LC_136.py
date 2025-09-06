list = [4,3,3,4,5]

def Solution(nums):
    
    drop = set()

    for i in nums:
        if i in drop:
            drop.remove(i)
        else:
            drop.add(i)
    return drop.pop()



print(Solution(list))

        
    