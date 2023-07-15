class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=s.split(' ')
        s=sorted(s,key=lambda x: x[-1])
        s=[i[:-1] for i in s]
        return ' '.join(s)
        
      

