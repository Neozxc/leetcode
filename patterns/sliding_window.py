def sliding_window(arr):
    left = 0
    result = 0 # Or float('inf') for minimums
    current_sum = 0 # e.g, a hash map, etc.

    for right in range(len(arr)):
        # 1. ADD the right element to the window
        # Update current_sum with arr[right]

        # 2. SHRINK the window from the left if it's no longer valid
        while window_is_invalid(current_sum):
            # Remove arr[left] from current_sum
            left += 1
        
        # 3. UPDATE the result
        # At this point, the window is valid.
        # Calculate the answer (e.g., max_length = max(max_length, right - left + 1))
        
    return result
