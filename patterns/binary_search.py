def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2 # or left + (right - left) // 2 to prevent overflow

        # ==================================
        # Problem-specific logic determines what you do with mid.
        if arr[mid] == target:
            return mid # Found it
        elif arr[mid] < target:
            # Search the right half
            left = mid + 1
        else:
            # Search the left half
            right = mid - 1
        # ==================================
            
    return -1 # Target not found
