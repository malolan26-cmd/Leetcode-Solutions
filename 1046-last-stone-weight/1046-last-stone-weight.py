class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        heapq.heapify_max(stones)
        
        while len(stones) > 1:
            y = heapq.heappop_max(stones)
            x = heapq.heappop_max(stones)
            if x == y:
                continue
            else:
                y = y - x
                heapq.heappush_max(stones, y)

        if len(stones) == 1:
            return stones[0]
        else:
            return 0
