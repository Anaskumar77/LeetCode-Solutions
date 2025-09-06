def Solution(nums,target):
    right = len(nums) - 1
    left = 0
    mid = 0

    if nums[right] == target:
        return right
    elif nums[left] == target:
        return left
    else:
        while left <= right:
            print(f"left:{left} , right:{right} , mid:{ mid}")



            mid = left + ( ( right - left ) // 2 )
            print(f"mid : {mid}")

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

            if nums[mid] == target:
                return mid
        else:
            return left


        
print(Solution([1,3,5,8,9],3))
    
        
        
        
