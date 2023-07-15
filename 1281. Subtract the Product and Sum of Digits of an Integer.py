class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        f=1
        m=n
        while(n!=0):
            r=n%10
            f*=r
            n=n//10
        print(f)
        s=0
        while(m!=0):
            t=m%10
            s+=t
            m=m//10
        print(s)
        return f-s

        
        