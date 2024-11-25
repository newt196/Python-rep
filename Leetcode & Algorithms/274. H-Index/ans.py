class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort(reverse=True)   
        print(citations)
        for index, value in enumerate(citations):
            print(index + 1,value)
           
        for index, value in enumerate(citations):
            if value < index + 1:        
                return index
