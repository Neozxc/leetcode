class Solution:
  def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
    n = len(edges1) + 1
    m = len(edges2) + 1

    adj1 = defaultdict(list)
    for u_node, v_node in edges1:
        adj1[u_node].append(v_node)
        adj1[v_node].append(u_node)

    adj2 = defaultdict(list)
    for u_node, v_node in edges2:
        adj2[u_node].append(v_node)
        adj2[v_node].append(u_node)

    def bfs(start_node, num_total_nodes, adj):
        distances = [-1] * num_total_nodes
        distances[start_node] = 0
        
        q = collections.deque([(start_node, 0)])
        visited_bfs = [False] * num_total_nodes
        visited_bfs[start_node] = True

        while q:
            curr, dist = q.popleft()
            for neighbor in adj[curr]:
                if not visited_bfs[neighbor]:
                    visited_bfs[neighbor] = True
                    distances[neighbor] = dist + 1
                    q.append((neighbor, dist + 1))
        return distances

    d1 = [[-1]*n for _ in range(n)]
    for i in range(n):
        d1[i] = bfs(i, n, adj1)

    d2 = [[-1]*m for _ in range(m)]
    for i in range(m):
        d2[i] = bfs(i, m, adj2)
        
    num_reachable1 = [[0]*(k + 1) for _ in range(n)]
    for i in range(n):
        dist_counts = [0] * n
        for j in range(n):
            dist_ij = d1[i][j]
            if dist_ij < n:
                 dist_counts[dist_ij] += 1
        
        current_sum = 0
        for r_val in range(k + 1):
            if r_val < n:
                current_sum += dist_counts[r_val]
            num_reachable1[i][r_val] = current_sum
    
    num_reachable2 = [[0]*(k + 1) for _ in range(m)]
    for i in range(m):
        dist_counts = [0] * m
        for j in range(m):
            dist_ij = d2[i][j]
            if dist_ij < m:
                dist_counts[dist_ij] += 1
        
        current_sum = 0
        for r_val in range(k + 1):
            if r_val < m:
                current_sum += dist_counts[r_val]
            num_reachable2[i][r_val] = current_sum

    max_coverage_tree2 = [0] * k
    if k > 0:
        for r_idx in range(k):
            max_val_for_this_radius = 0
            for v_tree2_node in range(m):
                max_val_for_this_radius = max(max_val_for_this_radius, num_reachable2[v_tree2_node][r_idx])
            max_coverage_tree2[r_idx] = max_val_for_this_radius

    answer = [0] * n
    for i_query_node in range(n):
        contrib1 = num_reachable1[i_query_node][k]
        
        max_contrib2_for_i = 0
        if k > 0: 
            for u_conn_tree1 in range(n):
                dist_i_to_u = d1[i_query_node][u_conn_tree1]
                
                radius_for_tree2 = k - 1 - dist_i_to_u
                
                if radius_for_tree2 >= 0:
                    current_contrib2 = max_coverage_tree2[radius_for_tree2]
                    max_contrib2_for_i = max(max_contrib2_for_i, current_contrib2)
        
        answer[i_query_node] = contrib1 + max_contrib2_for_i
            
    return answer
