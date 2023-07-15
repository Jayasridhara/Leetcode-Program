class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1
        
        lst = [(x, d[x]) for x in d]
        lst.sort(reverse=True, key=lambda t:t[1])
        return dict(lst[:k]).keys()


        





