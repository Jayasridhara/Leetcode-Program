class Solution:
    def intersect(self, n1: List[int], n2: List[int]) -> List[int]:
        l=[]
        
        for i in n1:
            if i in n2:
                n2.remove(i)
                l.append(i)
        return l


