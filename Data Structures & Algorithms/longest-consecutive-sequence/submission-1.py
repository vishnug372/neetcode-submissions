class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hash = set(nums)
        for i in range(len(nums)):
            temp = 1
            if nums[i]-1 in hash:
                continue
            x = nums[i]
            while x+1 in hash:
                temp+=1
                x+=1
            if temp > res:
                res = temp

        return res