class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        if n == 0:
            return eventTime
        if n == 1:
            d = endTime[0] - startTime[0]
            return eventTime - d if eventTime >= d else 0

        durations = [endTime[i] - startTime[i] for i in range(n)]
        
        initial_gaps = []
        initial_gaps.append(startTime[0])
        for i in range(n - 1):
            initial_gaps.append(startTime[i + 1] - endTime[i])
        initial_gaps.append(eventTime - endTime[n - 1])

        max_ft = 0
        if initial_gaps:
            max_ft = max(initial_gaps)

        m = len(initial_gaps)

        prefix_top2 = [(-1, -1)] * m
        if m > 0:
            prefix_top2[0] = (initial_gaps[0], -1)
            for i in range(1, m):
                g = initial_gaps[i]
                p1, p2 = prefix_top2[i-1]
                if g >= p1: prefix_top2[i] = (g, p1)
                elif g > p2: prefix_top2[i] = (p1, g)
                else: prefix_top2[i] = (p1, p2)

        suffix_top2 = [(-1, -1)] * m
        if m > 0:
            suffix_top2[m-1] = (initial_gaps[m-1], -1)
            for i in range(m - 2, -1, -1):
                g = initial_gaps[i]
                s1, s2 = suffix_top2[i+1]
                if g >= s1: suffix_top2[i] = (g, s1)
                elif g > s2: suffix_top2[i] = (s1, g)
                else: suffix_top2[i] = (s1, s2)

        seg_tree = [[] for _ in range(4 * m)]
        if m > 0:
            self._build_segtree(initial_gaps, seg_tree, 0, 0, m - 1)

        for i in range(n):
            d_i = durations[i]
            
            if i == 0:
                merged_gap_len = startTime[1]
            elif i == n - 1:
                merged_gap_len = eventTime - endTime[n-2]
            else:
                merged_gap_len = startTime[i+1] - endTime[i-1]

            p1, p2 = (-1, -1)
            if i > 0: p1, p2 = prefix_top2[i-1]
            s1, s2 = (-1, -1)
            if i + 2 < m: s1, s2 = suffix_top2[i+2]
            
            all_gaps_top = sorted([p1, p2, s1, s2, merged_gap_len], reverse=True)
            L1, L2 = all_gaps_top[0], all_gaps_top[1]
            
            l_min_sufficient = float('inf')
            if merged_gap_len >= d_i:
                l_min_sufficient = merged_gap_len

            if m > 0:
                if i > 0:
                    res1 = self._query_segtree(seg_tree, 0, 0, m - 1, 0, i - 1, d_i)
                    l_min_sufficient = min(l_min_sufficient, res1)
                
                if i + 2 < m:
                    res2 = self._query_segtree(seg_tree, 0, 0, m - 1, i + 2, m - 1, d_i)
                    l_min_sufficient = min(l_min_sufficient, res2)

            if l_min_sufficient == float('inf'):
                continue
            
            if l_min_sufficient < L1:
                max_ft = max(max_ft, L1)
            else:
                max_ft = max(max_ft, max(L1 - d_i, L2))

        return max_ft

    def _build_segtree(self, arr, tree, node, start, end):
        if start == end:
            tree[node] = [arr[start]]
            return
        mid = (start + end) // 2
        self._build_segtree(arr, tree, 2 * node + 1, start, mid)
        self._build_segtree(arr, tree, 2 * node + 2, mid + 1, end)
        
        left_list, right_list = tree[2 * node + 1], tree[2 * node + 2]
        merged = []
        i, j = 0, 0
        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                merged.append(left_list[i])
                i += 1
            else:
                merged.append(right_list[j])
                j += 1
        merged.extend(left_list[i:])
        merged.extend(right_list[j:])
        tree[node] = merged

    def _query_segtree(self, tree, node, start, end, l, r, val):
        if r < start or end < l or l > r:
            return float('inf')

        if l <= start and end <= r:
            sorted_list = tree[node]
            idx = bisect.bisect_left(sorted_list, val)
            return sorted_list[idx] if idx < len(sorted_list) else float('inf')

        mid = (start + end) // 2
        res_left = self._query_segtree(tree, 2 * node + 1, start, mid, l, r, val)
        res_right = self._query_segtree(tree, 2 * node + 2, mid + 1, end, l, r, val)

        return min(res_left, res_right)
