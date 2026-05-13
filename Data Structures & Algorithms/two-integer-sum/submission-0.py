class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]
        lookup = {}
        low_index = 0
        high_index = 1
        for i in range(len(nums)):
            value_needed = target - nums[i]
            if value_needed in lookup:
                low_index = lookup[value_needed]
                high_index = i
            else:
                lookup[nums[i]] = i
        return [low_index, high_index]
