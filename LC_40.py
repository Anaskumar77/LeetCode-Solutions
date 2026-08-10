def combinationSum2(candidates,target):
    arr = sorted(candidates)
    res , comb = [] , []

    def BackTrack(i,total):
        if total > target:
            return 

        if total == target:
            if comb[:] not in res:
                res.append(comb[:])
        
        for j in range(i,len(arr)):
            comb.append(arr[j])
            BackTrack(j+1,total + arr[j])
            comb.pop()
    BackTrack(0,0)
    return res

print(combinationSum2([10,1,2,7,6,1,5],8))