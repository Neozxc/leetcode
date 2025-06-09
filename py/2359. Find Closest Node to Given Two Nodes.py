class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def path_distance(node_val: int) -> list[int]:
            distance = [-1] * n
            current_distance = 0
            current_node_idx = node_val

            while current_node_idx != -1 and distance[current_node_idx] == -1:
                distance[current_node_idx] = current_distance
                current_node_idx = edges[current_node_idx]
                current_distance += 1

            return distance
        
        dist_map1 = path_distance(node1)
        dist_map2 = path_distance(node2)

        overall_max_distance = float('inf')
        result_node = -1

        for candidate_node_idx in range(n):
            dist_from_n1 = dist_map1[candidate_node_idx]
            dist_from_n2 = dist_map2[candidate_node_idx]

            if dist_from_n1 != -1 and dist_from_n2 != -1:
                current_node_max_dist = max(dist_from_n1, dist_from_n2)

                if current_node_max_dist < overall_max_distance:
                    overall_max_distance = current_node_max_dist
                    result_node = candidate_node_idx
                elif current_node_max_dist == overall_max_distance:
                    if candidate_node_idx < result_node:
                        result_node = candidate_node_idx

        return result_node
