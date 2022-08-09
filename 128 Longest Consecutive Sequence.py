# https://leetcode.com/problems/longest-consecutive-sequence/submissions/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        long_seq = 1
        start, end = 0, 0
        if len(nums) == 0:
            return 0
        while end < len(nums) - 1: # O(n)
            while end < len(nums) - 1 and nums[end+1] - nums[end] == 1:
                print(end)
                end += 1
            long_seq = max(long_seq, end - start + 1)
            start = end + 1
            end += 1
        return long_seq
        