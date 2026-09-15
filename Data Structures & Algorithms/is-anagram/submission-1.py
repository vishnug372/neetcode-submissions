class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashS = {}
        hashT = {}
        for char in s:
            if char in hashS:
                hashS[char] += 1
            else:
                hashS[char] = 1
        for char2 in t:
            if char2 in hashT:
                hashT[char2] += 1
            else:
                hashT[char2] = 1
        
        return hashT == hashS


