class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        def gain(p, t):
            if p == t:
                return 0
            return (t - p) / (t * (t + 1))

        max_heap = [(-gain(p, t), p, t) for p, t in classes]
        heapq.heapify(max_heap)

        for _ in range(extraStudents):
            _, p, t = heapq.heappop(max_heap)

            p_new, t_new = p + 1, t + 1
            new_gain = gain(p_new, t_new)
            
            heapq.heappush(max_heap, (-new_gain, p_new, t_new))

        total_ratio_sum = sum(p / t for _, p, t in max_heap)

        return total_ratio_sum / len(classes)
