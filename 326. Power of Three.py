class Solution:
    def fun(self,n):
        while(n!=0):
            r=n%3
            n=n//3
            if r!=0:
               return False
            if n==1 and r==0:
                return True
    def isPowerOfThree(self, n: int) -> bool:
        if n==1:
            return True
        return self.fun(n)