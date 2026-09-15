class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = {}
        for char in s:
            if char in temp:
                temp[char] = temp[char] + 1
            else:
                temp[char] = 1
        
        for char in t:
            if char not in temp:
                return False
            else:
                temp[char] = temp[char]-1
                if temp[char] == 0:
                    del temp[char]
        return len(temp) == 0
        
