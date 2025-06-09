class FenwickTree:
    def __init__(self, size):
        self.actual_size = size 
        self.tree = [0] * (self.actual_size + 1)

    def update(self, index, delta):
        if not (0 <= index < self.actual_size):
            return 

        index += 1
        while index <= self.actual_size: 
            self.tree[index] += delta
            index += index & (-index)

    def query(self, index):
        if not (0 <= index < self.actual_size):
             return 0
        
        s = 0
        index += 1
        while index > 0:
            s += self.tree[index]
            index -= index & (-index)
        return s

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)

        if n == 0:
            return m
        
        all_zeros = True
        for x_val in nums:
            if x_val < 0:
                pass
            if x_val > 0:
                all_zeros = False
                break
        if all_zeros:
            return m

        delta_counts = [0] * (n + 1) 
        for l, r in queries:
            delta_counts[l] += 1
            delta_counts[r + 1] -= 1
        
        current_total_coverage = 0
        for j in range(n):
            current_total_coverage += delta_counts[j]
            if current_total_coverage < nums[j]:
                return -1

        queries_starting_at = [[] for _ in range(n)]
        for l, r in queries:
            queries_starting_at[l].append((r, l))

        bit = FenwickTree(n + 1) 

        active_queries_by_endpoint = []
        chosen_queries_count = 0 

        for j in range(n):
            while active_queries_by_endpoint and (-active_queries_by_endpoint[0][0] < j):
                heapq.heappop(active_queries_by_endpoint)

            for r_val, l_val in queries_starting_at[j]:
                heapq.heappush(active_queries_by_endpoint, (-r_val, l_val))
            
            coverage_at_j = bit.query(j)
            
            if coverage_at_j < nums[j]:
                needed = nums[j] - coverage_at_j
                for _ in range(needed):
                    if not active_queries_by_endpoint:
                        return -1 

                    neg_r_best, l_best = heapq.heappop(active_queries_by_endpoint)
                    r_best = -neg_r_best
                    
                    if r_best < j: return -1

                    chosen_queries_count += 1
                    
                    bit.update(l_best, 1) 
                    bit.update(r_best + 1, -1) 
        
        return m - chosen_queries_count
