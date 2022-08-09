# https://leetcode.com/problems/subsets/

# T:O(N*(2^N)), S:O(N*(2^N))
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for i, num in enumerate(nums):
            result += [ prev + [num] for prev in result]
        return result
