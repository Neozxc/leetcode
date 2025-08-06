class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        capacity_to_indices = defaultdict(list)

        for i, b in enumerate(baskets):
            capacity_to_indices[b].append(i)
        
        sorted_caps = sorted(capacity_to_indices.keys())
        k = len(sorted_caps)
        infinity = float('inf')

        tree = [infinity] * (4 * k)

        def build(node, start, end):
            if start == end:
                tree[node] = capacity_to_indices[sorted_caps[start]][0]
                return
            mid = (start + end) // 2
            build(2 * node, start, mid)
            build(2 * node + 1, mid + 1, end)
            tree[node] = min(tree[2 * node], tree[2 * node + 1])

        def update(node, start, end, idx_to_update, new_val):
            if start == end:
                tree[node] = new_val
                return
            mid = (start + end) // 2
            if start <= idx_to_update <= mid:
                update(2 * node, start, mid, idx_to_update, new_val)
            else:
                update(2 * node + 1, mid + 1, end, idx_to_update, new_val)
            tree[node] = min(tree[2 * node], tree[2 * node + 1])

        def query(node, start, end, l, r):
            if r < start or end < l:
                return infinity
            if l <= start and end <= r:
                return tree[node]
            mid = (start + end) // 2
            p1 = query(2 * node, start, mid, l, r)
            p2 = query(2 * node + 1, mid + 1, end, l, r)
            return min(p1, p2)

        if k > 0:
            build(1, 0, k - 1)
        
        index_to_cap_idx = {}
        for i, cap in enumerate(sorted_caps):
            for original_idx in capacity_to_indices[cap]:
                index_to_cap_idx[original_idx] = i

        unplaced_count = 0
        
        for fruit_quantity in fruits:
            start_idx = bisect.bisect_left(sorted_caps, fruit_quantity)
            
            if start_idx == k:
                unplaced_count += 1
                continue

            min_original_idx = query(1, 0, k - 1, start_idx, k - 1)
            
            if min_original_idx == infinity:
                unplaced_count += 1
            else:
                cap_idx = index_to_cap_idx[min_original_idx]
                capacity = sorted_caps[cap_idx]
                
                capacity_to_indices[capacity].pop(0)
                
                new_min_for_cap = capacity_to_indices[capacity][0] if capacity_to_indices[capacity] else infinity
                
                update(1, 0, k - 1, cap_idx, new_min_for_cap)

        return unplaced_count
