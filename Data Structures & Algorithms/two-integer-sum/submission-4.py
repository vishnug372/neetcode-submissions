class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = 0
        dict = {}
        for int in nums:
            if target - int in dict:
                return [dict[target-int], count]
            else:
                dict[int] = count
            count += 1
        