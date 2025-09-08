def lengthOfLongestSubstring(s):
    count = set()
    left,right, maxlen = 0,0,0

    while right < (len(s)):
        print(left,right,maxlen)
        if s[right] not in count:
            count.add(s[right])
            maxlen = max(maxlen,right - left + 1)
            right = right + 1


        else:
            count.remove(s[left])
            left = left + 1

    return maxlen
            
            
    
print(lengthOfLongestSubstring("pwwkew"))