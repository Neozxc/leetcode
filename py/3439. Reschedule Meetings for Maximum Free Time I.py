class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        
        num_gaps = n + 1
        gaps = [0] * num_gaps
        
        gaps[0] = startTime[0]
        
        for i in range(n - 1):
            gaps[i + 1] = startTime[i + 1] - endTime[i]
            
        gaps[n] = eventTime - endTime[n - 1]
        
        prefix_sums = [0] * (num_gaps + 1)
        for i in range(num_gaps):
            prefix_sums[i + 1] = prefix_sums[i] + gaps[i]
            
        max_freetime = 0
        
        dq = collections.deque()
        dq.append(0)
        
        for R in range(1, num_gaps + 1):
            if dq and dq[0] < R - (k + 1):
                dq.popleft()
            
            max_freetime = max(max_freetime, prefix_sums[R] - prefix_sums[dq[0]])
            
            while dq and prefix_sums[dq[-1]] >= prefix_sums[R]:
                dq.pop()
            dq.append(R)
                
        return max_freetime
