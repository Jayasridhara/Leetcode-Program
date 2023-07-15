class Solution:
    def largestGoodInteger(self, nums: str) -> str:
        d={}
        l=[]
        for i in nums:
            d[i] = d.get(i,0) + 1
        for i,j in d.items():
            if j >= 3:
                l.append(i)
        if len(l) == 0:
            return ''
        print(l)
        l.sort(reverse=True)
        for k in l:

            for i in range(len(nums)-2):
                if nums[i] == k and nums[i+1] == k and nums[i+2] == k :
                    return k*3
        return ''


        



            