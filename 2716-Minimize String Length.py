class Solution:
    def minimizedStringLength(self, s: str) -> int:
        d={}
        for i in s:
            d[i]=d.get(i,0)+1
        return len(d)
