class Solution:
    def isPalindrome(self, s: str) -> bool:
        str = ""
        for char in s:
            if char.isalnum():
                str = str + char
        return str.lower() == str[::-1].lower()
        






