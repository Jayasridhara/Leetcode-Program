class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s=0
        t=-99999
        for i in nums:
            s=s+i
            t=max(t,s)
            if(s<0):
                s=0
        return t