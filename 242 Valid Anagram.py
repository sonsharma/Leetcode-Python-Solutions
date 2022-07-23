# https://leetcode.com/problems/valid-anagram/

# T: O(n), S: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        d_dict = {}
        if len(s) != len(t):
            return False
        if s==t:
            return True
        else:
            for (i, j) in zip(s, t):
                s_dict[i] = (s_dict.get(i) or 0) + 1
                d_dict[j] = (d_dict.get(j) or 0) + 1
            return s_dict == d_dict

# T: O(n), S: O(1)      
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

    
# T: O(n), S: O(N)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)