class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in range(len(strs)):
            encoded += str(len(strs[i])) + "#"
            encoded += strs[i]
        return encoded


    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            wordLength = int(s[i:j])
            word = s[j+1:j+1+wordLength]
            result.append(word)
            i = j+1+wordLength
        return result

