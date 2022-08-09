# https://leetcode.com/problems/arithmetic-subarrays/

# T: O(nm), S:O(n)
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = [True]*len(l)
        ind_answer = 0
        for i in range(len(l)): # O(m) to traverse l, r
            sub_array = sorted(nums[l[i]: r[i]+1]) # O(n) for sorting nums
            diff = sub_array[1] - sub_array[0]
            for j in range(2, len(sub_array)): # O(n) for traversing sorted nums
                if diff != (sub_array[j] - sub_array[j-1]):
                    answer[ind_answer] = False
                    break
            ind_answer += 1
        return answer