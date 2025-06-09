def dp_template(n, ...other_params):
    # 1. DP State: dp[i] represents the answer for the subproblem of size i.
    dp = [0] * (n + 1)
    
    # 2. Base Cases
    dp[0] = ... # some initial value
    dp[1] = ... # some initial value
    
    # 3. Recurrence Relation (Transition) in a loop
    for i in range(2, n + 1):
        # ==================================
        # The core logic of the problem.
        # dp[i] is calculated based on previous dp values.
        dp[i] = dp[i-1] + dp[i-2] # e.g., Fibonacci-style
        # or dp[i] = max(dp[i-1], dp[i-2] + value[i]) # e.g., House Robber-style
        # ==================================
        
    # 4. Final Answer
    return dp[n]
