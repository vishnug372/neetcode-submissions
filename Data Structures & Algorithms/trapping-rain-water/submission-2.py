class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        
        result = 0;
        preMax = 0
        postMax = 0
        while l < r:
            if height[l] < height[r]:
                preMax = max(preMax, height[l])
                result += preMax - height[l]
                l+=1
            else:
                postMax = max(postMax, height[r])
                result += postMax-height[r]
                r-=1
        return result





        return result
        





