class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        count = 0
        for int in nums:
            if (target - int) in hash:
                return [hash[target-int], count]
            hash[int] = count
            count = count+1
        
            

