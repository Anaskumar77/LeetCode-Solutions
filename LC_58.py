class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        s_list = s.split(" ")
        return len(s_list[-1])
        
        
