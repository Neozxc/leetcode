class Solution:
  def answerString(self, word: str, numFriends: int) -> str:
    n = len(word)
    max_lex_string = "" 

    max_part_len = n - (numFriends - 1)

    for i in range(n):
      if max_lex_string and word[i] < max_lex_string[0]:
          continue
      
      for j in range(i, n):
        current_part_len = j - i + 1
        
        if current_part_len > max_part_len:
            break 
        
        pref_len = i
        suff_len = n - (j + 1)

        min_pref_parts = 0 if pref_len == 0 else 1
        max_pref_parts = pref_len
        
        min_suff_parts = 0 if suff_len == 0 else 1
        max_suff_parts = suff_len

        parts_to_make_from_others = numFriends - 1

        if (min_pref_parts + min_suff_parts <= parts_to_make_from_others and
            parts_to_make_from_others <= max_pref_parts + max_suff_parts):
          
          current_substring = word[i : j+1]

          if not max_lex_string or current_substring > max_lex_string:
            max_lex_string = current_substring
              
    return max_lex_string
