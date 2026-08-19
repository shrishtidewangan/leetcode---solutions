import heapq
from collections import defaultdict

class Solution:
    def topKFrequent(self,nums,k):

        if k == len(nums):
            return nums 

        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        heap = []
        for n in count:
            heapq.heappush(heap, (count[n],n))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans 
        