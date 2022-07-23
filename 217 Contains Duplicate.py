# https://leetcode.com/problems/contains-duplicate/submissions/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # T: O(N)
        # S: O(N)
        return len(nums) != len(set(nums))
      
# Another solution
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool: 
        # T: O(N)
        # S: O(N)
        d = {}
        for num in nums:
            if num in d:
                return True
            else:
                d[num] = 1
        return False