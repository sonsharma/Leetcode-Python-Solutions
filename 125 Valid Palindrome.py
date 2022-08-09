# https://leetcode.com/problems/valid-palindrome/submissions/

# T:O(N), S:O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = list(s.lower())
        i = 0
        j = len(s) - 1
        
        while i<j:
            while i<j and not s[i].isalnum():
                i += 1
            while i<j and not s[j].isalnum():
                j -= 1
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True