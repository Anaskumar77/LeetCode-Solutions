class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1 or x == 2:
            return 1
        i = 1 
        while (i**2) <= x:
            i += 1

        return i - 1

        