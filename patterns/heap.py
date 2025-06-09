# Finding K largest elements using a Min-Heap
def top_k_template(nums, k):
    min_heap = []

    for num in nums:
        # ==================================
        # Push the current number onto the heap.
        heapq.heappush(min_heap, num)

        # If the heap size exceeds K, pop the smallest element.
        if len(min_heap) > k:
            heapq.heappop(min_heap)
        # ==================================
            
    # The heap now contains the K largest elements.
    return min_heap
