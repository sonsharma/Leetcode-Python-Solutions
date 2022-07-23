# https://leetcode.com/problems/two-sum/

# Brute force
# T:O(N^2), S: O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            sub_num = target - nums[i]
            if sub_num in nums[i+1:]:
                return [i, nums[i+1:].index(sub_num)+i+1]

# T:O(N), S: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i in range(0, len(nums)):
            num_dict[nums[i]] = i
        for i in range(0, len(nums)):
            sub_num = target - nums[i]
            if sub_num in num_dict and num_dict[sub_num] != i:
                return [i, num_dict[sub_num]]

# T:O(N), S: O(N)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for i, num in enumerate(nums):
            sub_num = target - num
            if sub_num in num_dict:
                return [num_dict[sub_num], i]
            num_dict[num] = i
