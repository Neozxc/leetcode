class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        n = len(edges1) + 1
        m = len(edges2) + 1

        def get_depths_and_parity_counts(num_nodes: int, edges: List[List[int]]):
            adj = collections.defaultdict(list)
            for u_node, v_node in edges:
                adj[u_node].append(v_node)
                adj[v_node].append(u_node)

            depths = [-1] * num_nodes
            q = collections.deque()
            visited_bfs = [False] * num_nodes
            
            depths[0] = 0
            q.append((0, 0))
            visited_bfs[0] = True
            
            count_even_depth_nodes = 0
            count_odd_depth_nodes = 0

            while q:
                curr, d = q.popleft()
                if d % 2 == 0:
                    count_even_depth_nodes += 1
                else:
                    count_odd_depth_nodes += 1
                
                for neighbor in adj[curr]:
                    if not visited_bfs[neighbor]:
                        visited_bfs[neighbor] = True
                        depths[neighbor] = d + 1
                        q.append((neighbor, d + 1))
            
            return depths, count_even_depth_nodes, count_odd_depth_nodes

        depths1, count1_even, count1_odd = get_depths_and_parity_counts(n, edges1)
        
        _, count2_even, count2_odd = get_depths_and_parity_counts(m, edges2)

        max_contrib_from_tree2 = max(count2_even, count2_odd)
        
        answer = [0] * n
        for i_query_node in range(n):
            contrib1 = 0
            if depths1[i_query_node] % 2 == 0:
                contrib1 = count1_even
            else:
                contrib1 = count1_odd
            
            answer[i_query_node] = contrib1 + max_contrib_from_tree2
            
        return answer
