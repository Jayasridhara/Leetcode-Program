class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums=sorted(nums)
        n=len(nums)
        f=n*(n+1)//2-sum(nums)
        return f