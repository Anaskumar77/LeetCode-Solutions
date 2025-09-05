
def removeElement( self,nums, val):
    length = 0
    i = 0
    size = len(nums)
    while length != size:
        if nums[i] != val:
            length = length + 1
            i = i + 1
            print("if",i,nums)
        else:
            nums.pop(i)
            length = length + 1
            print("else",i,nums)
    return  i



        


nums = [2,3,3,4,5,6]

print(removeElement(nums,3))