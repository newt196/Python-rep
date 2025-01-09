class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        n = abs(x)  

        while n > 0:
            r = r * 10 + n % 10
            n //= 10
        r = r if x > 0 else -r
        if r < -2**31 or r > 2**31 - 1:
            return 0  
        return r


solution = Solution()

