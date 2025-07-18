class Solution:
  def minimumDifference(self, nums: List[int]) -> int:
    N = len(nums)
    n = N // 3

    prefix_min_sum = [0] * N
    max_h = []
    current_sum = 0
    for i in range(N):
        val = nums[i]
        heapq.heappush(max_h, -val)
        current_sum += val
        
        if len(max_h) > n:
            removed_val = -heapq.heappop(max_h)
            current_sum -= removed_val

        if len(max_h) == n:
            prefix_min_sum[i] = current_sum

    suffix_max_sum = [0] * N
    min_h = []
    current_sum = 0
    for i in range(N - 1, -1, -1):
        val = nums[i]
        heapq.heappush(min_h, val)
        current_sum += val

        if len(min_h) > n:
            removed_val = heapq.heappop(min_h)
            current_sum -= removed_val
        
        if len(min_h) == n:
            suffix_max_sum[i] = current_sum

    min_diff = float('inf')
    
    for i in range(n - 1, 2 * n):
        s1 = prefix_min_sum[i]
        s2 = suffix_max_sum[i + 1]
        min_diff = min(min_diff, s1 - s2)
        
    return min_diff
