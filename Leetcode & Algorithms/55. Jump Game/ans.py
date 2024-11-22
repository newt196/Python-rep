class Solution:
    def canJump(self, nums: List[int]) -> bool:
        element = 0  
        
        for i in range(len(nums)):
            if i > element:
                return False 
            element = max(element, i + nums[i])  
            
            if element >= len(nums) - 1:
                return True  
        
        return False  
