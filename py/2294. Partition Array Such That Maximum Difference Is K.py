class Solution:
  def partitionArray(self, nums: List[int], k: int) -> int:
    nums.sort()
    num_subsequences = 1
    current_subsequence_min = nums[0]
    
    for i in range(1, len(nums)):
      current_num = nums[i]
      
      if current_num - current_subsequence_min > k:
        num_subsequences += 1
        current_subsequence_min = current_num

    return num_subsequences
