class Solution:
    def getCommon(self, n1: List[int], n2: List[int]) -> int:
        n1=set(n1)
        n2=set(n2)
    
        l=[]
        x=n1.intersection(n2)
        
        if len(x)==0:
            return -1
        else:
            return  min(x)
        
                
      