class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a=0
        b=1
        while n>0:
            a,b=b,a+b
            n-=1
        return b



