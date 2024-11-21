class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = []
        for i in nums:
            if i not in l:
                l.append(i)
        nums[:len(l)] = l 
        return len(l)  
