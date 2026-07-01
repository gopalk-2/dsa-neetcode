class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq=Counter(tasks)
        max_heap=[-i for i in freq.values()]
        heapq.heapify(max_heap)
        time=0
        while max_heap:
            used=[]
            slots=n+1

            while slots>0 and max_heap:
                cnt=-heapq.heappop(max_heap)
                cnt-=1
                if cnt>0:
                    used.append(-cnt)
                time+=1
                slots-=1
            for c in used:
                heapq.heappush(max_heap,c)
            if max_heap and slots>0:
                time+=slots
        return time


        