class Solution:
    def maximumNumberOfStringPairs(self, w: List[str]) -> int:
        c=0
        for i in range(len(w)):
            
            for j in range(i+1,len(w)):
                w[j]=w[j][::-1]
                if w[i]==w[j]:
                    c=c+1
        return c
                