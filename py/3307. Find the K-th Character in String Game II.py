class Solution:
  def kthCharacter(self, k: int, operations: List[int]) -> str:
    num_operations = len(operations)
    shift = 0

    for i in range(num_operations - 1, -1, -1):
      half_len = 1 << i
      
      if k > half_len:
        k -= half_len
        if operations[i] == 1:
          shift += 1

    final_shift = shift % 26
    final_char_code = ord('a') + final_shift
    
    return chr(final_char_code)
