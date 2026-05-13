class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabet = {}
        for char in s:
            if char not in alphabet:
                alphabet[char] = 1
            else:
                alphabet[char] += 1
        
        for char in t:
            if char not in alphabet or alphabet[char] == 0:
                return False
            alphabet[char] -= 1
            if alphabet[char] == 0:
                alphabet.pop(char, None)
        return len(alphabet) == 0
