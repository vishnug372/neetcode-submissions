class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        preArr = [0] * len(height)
        result = 0;
        preMax = 0
        postMax = 0
        for i in range(len(height)-1):
            preArr[i] = preMax
            if height[i] > preMax:
                preMax = height[i]
        for i in range(len(height)-1, -1, -1):
            if min(postMax, preArr[i]) > height[i]:
                result += min(postMax, preArr[i]) - height[i]
            if height[i] > postMax:
                postMax = height[i]



        return result
        





