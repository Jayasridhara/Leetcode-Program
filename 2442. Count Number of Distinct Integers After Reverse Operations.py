class Solution:
    def countDistinctIntegers(self, n: List[int]) -> int:
        l=[]
        for i in n:
            l.append(int(str(i)[::-1]))
        l.extend(n)
        l=list(set(l))
        return len(l)

            

            
        
        
        
        