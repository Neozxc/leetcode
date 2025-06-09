def monotic_stack(arr):
    stack = [] # Stores indices or values
    result = [-1] * len(arr) # Default value if no greater element exists

    for i in range(len(arr)):
        # ==================================
        # While stack is not empty AND the current element is greater 
        # than the element at the index on top of the stack.
        while stack and arr[i] > arr[stack[-1]]:
            # We found the next greater element for the index on top of the stack
            top_index = stack.pop()
            result[top_index] = arr[i]
        
        # Push the current index onto the stack
        stack.push(i)
        # ==================================
        
    return result