class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        char_count: dict[str, int] = defaultdict(int)
        for right in range(len(s)):
            char_count[s[right]] += 1 #char at string index r
            while char_count[s[right]] > 1: #re-validate window
                char_count[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest
