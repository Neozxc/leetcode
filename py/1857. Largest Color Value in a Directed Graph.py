class Solution:
    def largestPathValue(self, colors: str, edges: list[list[int]]) -> int:
        n = len(colors)
        
        adj = collections.defaultdict(list)
        in_degree = [0] * n
        
        for u, v in edges:
            adj[u].append(v)
            in_degree[v] += 1
            
        dp = [[0] * 26 for _ in range(n)]
        
        queue = collections.deque()
        for i in range(n):
            if in_degree[i] == 0:
                queue.append(i)
                
        max_overall_color_value = 0
        nodes_processed = 0
        
        while queue:
            u = queue.popleft()
            nodes_processed += 1
            
            color_u_code = ord(colors[u]) - ord('a')
            dp[u][color_u_code] += 1 
            
            max_overall_color_value = max(max_overall_color_value, dp[u][color_u_code])
            current_path_value_ending_at_u = 0

            for count_for_color_c in dp[u]:
                 current_path_value_ending_at_u = max(current_path_value_ending_at_u, count_for_color_c)
            max_overall_color_value = max(max_overall_color_value, current_path_value_ending_at_u)

            for v in adj[u]:
                for c_idx in range(26):
                    dp[v][c_idx] = max(dp[v][c_idx], dp[u][c_idx])
                
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)

        if nodes_processed < n:
            return -1
        else:
            return max_overall_color_value
