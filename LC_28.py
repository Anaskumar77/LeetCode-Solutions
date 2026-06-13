def strStr( haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    len1 = len(haystack)
    len2 = len(needle)
    for i in range(len1 - len2 + 1):
        if haystack[i] == needle[0]:
            j = 0
            while j < len2:
                if haystack[i + j] != needle[j]:
                    break
                j += 1
            if j == len2:
                return i
            
    return -1
        

            


print(strStr("aaabaaabbbabaa","babb"))