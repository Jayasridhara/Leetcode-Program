import sys
class Solution:
    def largestOddNumber(self, num: str) -> str:
        s=""
        sys.set_int_max_str_digits(100000)
        num=int(num)
        while(num!=0):
            r=num%10
            if(r%2!=0):
              return str(num)
            else:
                if(r%2!=0):
                    s+=str(r)
                num=num//10
        return s