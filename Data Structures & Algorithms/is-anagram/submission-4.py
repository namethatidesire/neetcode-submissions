class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        available = {}
        for char in s:
            if char in available:
                available[char] += 1
            else:
                available[char] = 1
        for char in t:
            if char not in available:
                return False
            if available[char] == 0:
                return False
            available[char] -= 1
        for char in available:
            if available[char] != 0:
                return False
        return True