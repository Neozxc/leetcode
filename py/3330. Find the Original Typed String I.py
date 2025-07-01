class Solution:
    def possibleStringCount(self, word: str) -> int:
        n = len(word)
        total_count = 1
        current_group_length = 1

        for i in range(1, n):
            if word[i] == word[i - 1]:
                current_group_length += 1
            else:
                if current_group_length > 1:
                    total_count += current_group_length - 1
                
                current_group_length = 1
        
        if current_group_length > 1:
            total_count += current_group_length - 1

        return total_count
