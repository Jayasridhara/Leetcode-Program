class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        c=0
        l=[]
        if target not in nums:
           return [-1,-1]
        ele1=nums.index(target)
        for i in range(ele1+1,len(nums)):
            if nums[i]==target:
                c=c+1
        l.append(ele1)
        l.append(ele1+c)
        return l


        