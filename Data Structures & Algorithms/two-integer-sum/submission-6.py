class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            potential_pair = target - num
            if potential_pair in seen:
                return [seen[potential_pair], i]
            else:
                if num not in seen:
                    seen[num] = i
