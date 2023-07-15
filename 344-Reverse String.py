class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st=[]
        for i in reversed(s):
            st.append(i)
        s[:] = st
        return s

        
       

