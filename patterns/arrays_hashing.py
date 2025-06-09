def frequency_counter(items):
    # Use a dictionary or defaultdict to store frequencies
    freq_map = defaultdict(int)

    for item in items:
        # ==================================
        # This is where the problem-specific logic goes.
        # Usually, you're just incrementing the count.
        freq_map[item] += 1
        # ==================================
    
    # Now you can iterate through the map to find the answer
    # For example, find the most frequent item:
    # max_freq = 0
    # result = None
    # for item, freq in freq_map.items():
    #     if freq > max_freq:
    #         # your logic here ...
    
    return freq_map
