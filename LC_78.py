
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        size = len(nums)
        outs, sol = [], []

        def backTracking(index):
            
            # boundry condition
            if index == size:
                outs.append(sol[:])
                return

            # if not added 
            backTracking(index + 1)


            # if added 
            sol.append(nums[index])
            backTracking(index + 1)
            sol.pop()     

        backTracking(0)
        return outs  
