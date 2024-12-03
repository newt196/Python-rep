class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list = len(nums)
        result = [1] * list  
        
        prefix = 1
        for i in range(list):
            result[i] = prefix
            prefix *= nums[i]  
        
        suffix = 1
        for i in range(list - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]  
        
        return result
