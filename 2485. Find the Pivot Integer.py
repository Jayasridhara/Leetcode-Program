class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = sum(range(n+1))
        s= 0
        
        for i in range(n, -1, -1):
            s += i
            if s == total:
                return i

            total -= i
            
        return -1
