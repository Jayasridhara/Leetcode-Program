class Solution(object):
    def alternateDigitSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=n
        c=0
        s=0
        while(n):
            c+=1
            n=n/10
        while(m):
           r=m%10
           if c%2==0:
               s=s-r
           else:
              s=s+r
           m=m//10
           c-=1
        return s
        
