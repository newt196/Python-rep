class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = []
        for i in nums:
            if l.count(i) < 2:
                l.append(i)
        nums[:len(l)] = l 
        return len(l)  
