# https://leetcode.com/problems/top-k-frequent-elements/submissions/

# T: O(NlogN), S:O(N)
# Heap creation: NlogN
# Heap: Klog(N) - Create a frequency map and then add every tuple (frequency, item) to a max heap. Then extract the top k elements.

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        result = []
        for num in nums:
            hashmap[num] += 1
        for key in hashmap:
            heapq.heappush(result, (-hashmap[key], key))
        return [heappop(result)[1] for i in range(k)]

# T: O(N), S:O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums) # O(N)
        return [c[0] for c in count.most_common(k)]

# T: O(NlogN), S:O(N)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        result = set()
        for num in nums:
            hashmap[num] += 1
        return list(sorted(hashmap, key=hashmap.get, reverse=True))[0:k]