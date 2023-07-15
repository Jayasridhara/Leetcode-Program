import sys
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s=0
        for i in num:
            s=s*10+i
        s=s+k
        l=[]
        while s!=0:
            l.append(s%10)
            s=s//10
        return l[::-1]


        
