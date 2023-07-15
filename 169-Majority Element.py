class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        n=len(nums)//2
        for i,j in d.items():
            if(j>n):
                return i
