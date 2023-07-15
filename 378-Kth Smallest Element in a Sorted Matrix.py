class Solution:
    def kthSmallest(self, m: List[List[int]], k: int) -> int:
        f=sum(m,[])
        return sorted(f)[k-1]
