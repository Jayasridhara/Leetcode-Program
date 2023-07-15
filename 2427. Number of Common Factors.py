class Solution(object):
    def commonFactors(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        l=[]
        f=[]
        c=0
        for i in range(1,a//2+1):
            if a%i==0:
                l.append(i)
        l.append(a)
        print(l)
        for j in range(1,b//2+1):
            if b%j==0:
                f.append(j)
        f.append(b)
        print(f)
        f=set(f)
        l=set(l)
    
        return len(l.intersection(f))