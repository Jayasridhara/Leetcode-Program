from itertools import permutations
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        l=[]
        for i in range(1,n+1):
            l.append(i)
        l=list(permutations(l))
        l=list(l[k-1])
        s=''
        for i in l:
            s+=str(i)
        
        return s

