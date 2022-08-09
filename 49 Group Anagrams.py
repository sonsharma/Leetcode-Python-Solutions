# https://leetcode.com/problems/group-anagrams/submissions/

# T: O(NKlogK), S: O(NK)
# KlogK is for sorting
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i, val in enumerate(strs):
            hashmap[''.join(sorted(val))].append(val)
        return hashmap.values()

# T: O(NK), S: O(NK)
# No sorting here
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for i, val in enumerate(strs):
            count = [0]*26
            for i in val:
                count[ord(i) - ord('a')] += 1
            hashmap[tuple(count)].append(val)
        return hashmap.values()

