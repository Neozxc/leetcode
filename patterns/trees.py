# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Tree BFS (Level Order Traversal)
def tree_bfs_template(root):
    if not root:
        return []
        
    queue = deque([root])
    result = []

    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            
            # ==================================
            # Problem-specific logic goes here.
            # e.g., add the node's value to the current level's list
            current_level.append(node.val)

            # Add children to the queue for the next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            # ==================================
        
        result.append(current_level)
            
    return result
