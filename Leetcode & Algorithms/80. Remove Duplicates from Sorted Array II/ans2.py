class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        
        rem = 2  

        for i in range(2, len(nums)):
            if nums[i] != nums[rem - 2]:
                nums[rem] = nums[i]
                rem += 1

        return rem
