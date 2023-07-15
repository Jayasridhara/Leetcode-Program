class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
       
    	s, q = 0, num**.5
    	for i in range(2,1+int(q)):
    		if num%i == 0: s += i + num//i
    	if int(q) == q: 
            s -= int(q)
    	return s == num - 1
            
