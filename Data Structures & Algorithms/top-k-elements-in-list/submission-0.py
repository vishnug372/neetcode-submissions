class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] = dict[num]+1
            else:
                dict[num] = 1
        newList = []
        for i in range(k):
            highest = next(iter(dict))
            for key in dict:
                if dict[key] > dict[highest]:
                    highest = key
            dict.pop(highest)
            newList.append(highest)
        
       
        
        
        return newList