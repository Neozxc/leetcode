class Solution:
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        adj = collections.defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        children = [[] for _ in range(n)]
        q = collections.deque([0])
        visited = {0}
        
        topo_order = [] 
        while q:
            u = q.popleft()
            topo_order.append(u)
            for v in adj[u]:
                if v not in visited:
                    visited.add(v)
                    parent[v] = u
                    children[u].append(v)
                    q.append(v)

        subtree_xor = list(nums)
        for u in reversed(topo_order):
            for v in children[u]:
                subtree_xor[u] ^= subtree_xor[v]
        
        total_xor = subtree_xor[0]

        entry_time = [-1] * n
        exit_time = [-1] * n
        time = 0
        stack = [(0, 0)]
        
        while stack:
            u, state = stack.pop()
            if state == 0:
                entry_time[u] = time
                time += 1
                stack.append((u, 1))
                for v in reversed(children[u]):
                    stack.append((v, 0))
            else:
                exit_time[u] = time
                time += 1

        def is_ancestor(u, v):
            return entry_time[u] < entry_time[v] and exit_time[u] > exit_time[v]

        min_score = float('inf')
        
        for u in range(1, n):
            for v in range(u + 1, n):
                xor1, xor2, xor3 = 0, 0, 0
                
                if is_ancestor(u, v):
                    xor1 = subtree_xor[v]
                    xor2 = subtree_xor[u] ^ xor1
                    xor3 = total_xor ^ subtree_xor[u]
                elif is_ancestor(v, u):
                    xor1 = subtree_xor[u]
                    xor2 = subtree_xor[v] ^ xor1
                    xor3 = total_xor ^ subtree_xor[v]
                else:
                    xor1 = subtree_xor[u]
                    xor2 = subtree_xor[v]
                    xor3 = total_xor ^ xor1 ^ xor2
                
                current_score = max(xor1, xor2, xor3) - min(xor1, xor2, xor3)
                min_score = min(min_score, current_score)

        return min_score
