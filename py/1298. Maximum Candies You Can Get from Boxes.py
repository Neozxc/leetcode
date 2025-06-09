class Solution:
    def maxCandies(self, status: list[int], candies: list[int], keys: list[list[int]], containedBoxes: list[list[int]], initialBoxes: list[int]) -> int:
        n = len(status)
        
        have_box = [False] * n
        processed_box = [False] * n
        
        q = deque()
        
        for box_idx in initialBoxes:
            have_box[box_idx] = True
            if status[box_idx] == 1 and not processed_box[box_idx]:
                q.append(box_idx)
                processed_box[box_idx] = True 

        total_candies_collected = 0
        
        while q:
            current_box_idx = q.popleft()
            
            total_candies_collected += candies[current_box_idx]
            
            for key_for_box_idx in keys[current_box_idx]:
                if status[key_for_box_idx] == 0: 
                    status[key_for_box_idx] = 1 
                    if have_box[key_for_box_idx] and not processed_box[key_for_box_idx]:
                        q.append(key_for_box_idx)
                        processed_box[key_for_box_idx] = True
                
            for new_box_idx in containedBoxes[current_box_idx]:
                have_box[new_box_idx] = True 
                if status[new_box_idx] == 1 and not processed_box[new_box_idx]:
                    q.append(new_box_idx)
                    processed_box[new_box_idx] = True
                    
        return total_candies_collected
