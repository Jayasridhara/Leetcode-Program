class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        s=0
        for i,j in d.items():
            if j==1:
                s+=i
        return s