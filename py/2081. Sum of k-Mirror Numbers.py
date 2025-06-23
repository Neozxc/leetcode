class Solution:
    def kMirror(self, k: int, n: int) -> int:
        found_count = 0
        total_sum = 0
        length = 1

        while found_count < n:
            half_len = (length + 1) // 2
            start_num = k**(half_len - 1)
            end_num = k**half_len

            for i in range(start_num, end_num):
                s_half = self.to_base_k_string(i, k)
                
                if length % 2 == 1:
                    full_palindrome_k = s_half + s_half[:-1][::-1]
                else:
                    full_palindrome_k = s_half + s_half[::-1]

                val_base10 = int(full_palindrome_k, k)

                if str(val_base10) == str(val_base10)[::-1]:
                    total_sum += val_base10
                    found_count += 1
                    if found_count == n:
                        return total_sum
            
            length += 1
            
        return total_sum

    def to_base_k_string(self, n: int, k: int) -> str:
        if n == 0:
            return "0"
        res = ""
        while n > 0:
            res = str(n % k) + res
            n //= k
        return res
