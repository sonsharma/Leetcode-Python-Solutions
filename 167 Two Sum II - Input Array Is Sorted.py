# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/solution/

# T:O(n), S:O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict = {}
        for i, val in enumerate(numbers):
            if target - val in dict.keys():
                return [dict[target - val] + 1, i + 1]
            else:
                dict[val] = i

# # T:O(n), S:O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum_nums = numbers[left] + numbers[right]
            if sum_nums > target:
                right -= 1
            elif sum_nums < target:
                left += 1
            else:
                return [left + 1, right + 1]