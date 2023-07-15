class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=9999999
        op=0
        for i in prices:
            if(i<l):
                l=i
            p=i-l
        
            if op<p:
                op=p
        return op