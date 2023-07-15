class Solution:
    def findFinalValue(self, n: List[int], o: int) -> int:
        f=0
        while f==0:
            if o in n:
                o=o*2
            elif o not in n:
                f=1
                
        return o
        
    
            
            

        


            
        
    


    

