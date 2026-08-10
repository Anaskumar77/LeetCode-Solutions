def combinationSum(candidates, target):
    res , comb = [], []

    def BackTrack(i,comb_sum):
        if comb_sum == target:
            res.append(comb[:])
        
        if comb_sum > target:
            return 
        
        for j in range(i, len(candidates)):
            comb.append(candidates[j])
            BackTrack(j, comb_sum + candidates[j])
            comb.pop()
    
    BackTrack(0,0)
    return res
    
print(combinationSum([2,3,6,1],7))