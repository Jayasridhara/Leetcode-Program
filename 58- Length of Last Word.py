class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans=[]
        s=s.strip()
        ans=s.split(' ')
        n=len(ans)-1
        return len(ans[n])
        