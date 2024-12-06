class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sort = sorted(nums1 + nums2)
        

        
        n = len(sort)
        median = n // 2

        if n % 2 == 1:
            return float(sort[median])
        else:
            return (sort[median - 1] + sort[median]) / 2
