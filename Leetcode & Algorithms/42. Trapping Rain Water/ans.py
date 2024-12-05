from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:  
            return 0

        results = 0
        for i in range(1, n - 1):
            l_max = max(height[:i])

            r_max = max(height[i + 1:])

            results += max(0, min(l_max, r_max) - height[i])

        return results
