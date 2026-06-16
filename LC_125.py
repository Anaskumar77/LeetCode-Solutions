class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_list = [ch for ch in s if ch.isalnum() or ch.isdigit()]
        s = "".join(s_list).lower()
        if s == s[::-1]:
            return True
        else:
            return False