class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while(l < r):
                sum = nums[l] + nums[r] + nums[i]
                if sum == 0:
                    result.append([nums[l], nums[r], nums[i]])
                    l+=1
                    while(l < r and nums[l] == nums[l-1]):
                        l+=1
                if sum < 0:
                    l+=1
                else:
                    r-=1
                
            
        return result

