def backtracking_template(nums):
    result = []

    def backtrack(current_path, remaining_options):
        # 1. Base Case: a valid solution is found
        if is_a_solution(current_path):
            result.append(list(current_path)) # Add a copy
            return

        # 2. Base Case: prune the search if this path is not promising
        if not is_promising(current_path):
            return

        # 3. Iterate through choices
        for choice in remaining_options:
            # a. Make a choice
            current_path.append(choice)
            
            # b. Recurse
            # The new remaining options might be different based on the problem
            new_remaining_options = calculate_new_options(remaining_options, choice)
            backtrack(current_path, new_remaining_options)

            # c. Backtrack (un-make the choice)
            current_path.pop()

    initial_path = []
    initial_options = nums

    backtrack(initial_path, initial_options)

    return result
