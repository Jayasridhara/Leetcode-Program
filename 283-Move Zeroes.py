class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        p=0
        for i in range(n):
            if(nums[i]!=0):
                nums[p],nums[i]=nums[i],nums[p]
                p+=1
        return nums
        
       
        

            
           
            