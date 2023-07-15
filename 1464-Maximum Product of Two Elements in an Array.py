class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=max(nums)
        nums.remove(n)
        n1=max(nums)
        nums.remove(n1)
        return (n1-1)*(n-1)