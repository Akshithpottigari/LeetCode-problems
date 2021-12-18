from math import sqrt
class Solution:
    def mySqrt(self, x: int) -> int:
        return(sqrt(x).__trunc__())