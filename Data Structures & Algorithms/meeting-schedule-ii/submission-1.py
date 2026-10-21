"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x.start)
        end_times_heap = []
        for interval in intervals:
            if end_times_heap and interval.start >= end_times_heap[0]:
                heapq.heappop(end_times_heap)
            heapq.heappush(end_times_heap, interval.end)

        return len(end_times_heap)
        