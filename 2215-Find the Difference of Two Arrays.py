class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1=(set(nums1))
        nums2=(set(nums2))
        f=[]
        l=[]
        k=[]
        '''
        for i in nums1:
            if i not in nums2:
                l.append(i)
        for i in nums2:
            if i not in nums1:
                k.append(i)
        
        return [l,k]
        '''
        f=nums1.difference(nums2)
        l=nums2.difference(nums1)
        return [f,l]


