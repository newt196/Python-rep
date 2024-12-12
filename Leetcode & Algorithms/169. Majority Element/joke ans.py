class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = max(nums,key=nums.count)
        return l
