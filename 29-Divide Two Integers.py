
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if(dividend/divisor < 2**31-1):
            k=int(dividend/divisor)
            return k
        else:
            return 2**31-1