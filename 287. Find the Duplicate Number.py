class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        for i,j in d.items():
            if j>1:
                return i