class Solution:
    def fun(self,n):
        while(n!=0):
            r=n%2
            n=n//2
            if r!=0:
               return False
            if n==1 and r==0:
                return True
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        return self.fun(n)