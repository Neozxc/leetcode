class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        
        occupied_rooms = []
        
        meeting_counts = [0] * n

        for start, end in meetings:
            while occupied_rooms and occupied_rooms[0][0] <= start:
                _end_time, room_id = heapq.heappop(occupied_rooms)
                heapq.heappush(available_rooms, room_id)

            duration = end - start
            
            if available_rooms:
                room_to_book = heapq.heappop(available_rooms)
                heapq.heappush(occupied_rooms, (end, room_to_book))
                meeting_counts[room_to_book] += 1
            else:
                earliest_free_time, room_to_book = heapq.heappop(occupied_rooms)
                new_end_time = earliest_free_time + duration
                heapq.heappush(occupied_rooms, (new_end_time, room_to_book))
                meeting_counts[room_to_book] += 1
        
        return meeting_counts.index(max(meeting_counts))
