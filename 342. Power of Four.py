
    
class Solution:
    def fun(self,n):
        while(n!=0):
            r=n%4
            n=n//4
            if r!=0:
               return False
            if n==1 and r==0:
                return True
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        return self.fun(n)