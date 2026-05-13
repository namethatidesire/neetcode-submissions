class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        charS = {}
        charT = {}
        for char in s:
            if charS.get(char) == None:
                charS[char] = 1
            else:
                charS[char] += 1
        for char in t:
            if charT.get(char) == None:
                charT[char] = 1
            else:
                charT[char] += 1
        return charS == charT
