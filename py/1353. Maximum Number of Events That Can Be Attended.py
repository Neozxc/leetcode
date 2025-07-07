class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()

        min_heap = []
        attended_count = 0
        event_idx = 0
        num_events = len(events)

        for d in range(1, 100001):
            if event_idx >= num_events and not min_heap:
                break

            while event_idx < num_events and events[event_idx][0] == d:
                heapq.heappush(min_heap, events[event_idx][1])
                event_idx += 1

            while min_heap and min_heap[0] < d:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                attended_count += 1
        
        return attended_count
