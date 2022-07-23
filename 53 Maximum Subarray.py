# brute force
# T: O(n3), S: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                max_sum = max(max_sum, sum(nums[i:j+1]))
        return max_sum

# brute force optimized
# T: O(n2), S: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        for i in range(0, len(nums)):
            current_subarray = 0
            for j in range(i, len(nums)):
                current_subarray = current_subarray + nums[j]
                max_sum = max(max_sum, current_subarray)
        return max_sum

# Kadane's Algorithm
# T: O(n), S: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        current_subarray = 0
        for num in nums:
            current_subarray = max(num + current_subarray, num)
            max_sum = max(current_subarray, max_sum)
        return max_sum
    
