class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo= {0:0,1:1}

        def f(num):
            if num in memo:
                return memo[num]
            else:
                memo[num] =  f(num-1) + f(num - 2)
                return memo[num]

        return f(n)

        