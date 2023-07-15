class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        else:
            nums.remove(max(nums))
            nums.remove(min(nums))
            return nums[0]