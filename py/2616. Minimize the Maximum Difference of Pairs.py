class Solution:
  def minimizeMax(self, nums: List[int], p: int) -> int:
    if p == 0:
        return 0

    nums.sort()
    n = len(nums)

    def can_form_p_pairs(max_allowed_diff: int) -> bool:
        count = 0
        i = 0
        while i < n - 1:
            if nums[i+1] - nums[i] <= max_allowed_diff:
                count += 1
                i += 2
                if count >= p:
                    return True
            else:
                i += 1
        return count >= p

    low = 0
    high = nums[n-1] - nums[0]
    min_max_diff_ans = high

    while low <= high:
        mid = low + (high - low) // 2
        if can_form_p_pairs(mid):
            min_max_diff_ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    return min_max_diff_ans
