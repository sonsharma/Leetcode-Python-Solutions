# https://leetcode.com/problems/product-of-array-except-self/submissions/

# T:O(N), S:O(1)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = []
        mult = 1
        num_zeros = 0
        for num in nums:
            if num != 0:
                mult *= num
            else:
                num_zeros += 1
        for num in nums:
            if num != 0:
                product.append(mult // num * (num_zeros == 0))
            else:
                product.append(mult * (num_zeros == 1))
        return product