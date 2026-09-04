class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        
        min_heap = list(count.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]
            
            if count[first] == 0:
                heapq.heappop(min_heap)
                continue
            
            num_groups = count[first]
            
            for i in range(first, first + groupSize):
                if count[i] < num_groups:
                    return False
                count[i] -= num_groups
                
        return True
        