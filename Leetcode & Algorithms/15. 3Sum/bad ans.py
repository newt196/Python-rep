class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not (3 <= len(nums) <= 3000):
            return None  

        for i in nums:
            if not (-100000 <= i <= 100000):
                return None
        nums.sort()  
        triplet_count = 0
        final_temp_list = []
        
        k = 0  
        
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            s = set()
            temp_list = []
            
            temp_list.append(nums[i])
            
            curr_k = k - nums[i]
            
            for j in range(i + 1, len(nums)):
                if (curr_k - nums[j]) in s:
                    triplet_count += 1
                    
                    temp_list.append(nums[j])
                    temp_list.append(curr_k - nums[j])
                    
                    triplet = sorted(temp_list)
                    if triplet not in final_temp_list:
                        final_temp_list.append(triplet)
                    
                    temp_list.pop(2)
                    temp_list.pop(1)
                
                s.add(nums[j])
        
        return final_temp_list
        
       
