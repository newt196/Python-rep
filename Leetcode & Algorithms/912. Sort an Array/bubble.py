class Solution(object):
    def sortArray(self, nums):
        n = len(nums)       
        for i in range(n):  
            for j in range(0, n-i-1):  
                if nums[j] > nums[j+1]:  
                    nums[j], nums[j+1] = nums[j+1], nums[j]  
        return nums # watch where this is placed, will fail if 
                    # not properly set. 

        
