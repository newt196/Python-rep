from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        added_arrays = sorted(nums1 + nums2)
        
        n = len(added_arrays)
        mid = n // 2  

        if n % 2 == 1:
            return float(added_arrays[mid])  
        else:
            return (added_arrays[mid - 1] + added_arrays[mid]) / 2.0

solution = Solution()

result = solution.findMedianSortedArrays([1, 2], [3])
print(result)  
