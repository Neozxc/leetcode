class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        res = []

        for num in nums:
            current_num = num

            while res and math.gcd(res[-1], current_num) > 1:
                last_in_res = res.pop()
                current_num = (last_in_res * current_num) // math.gcd(last_in_res, current_num)

            res.append(current_num)

        return res
