class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPSILON = 1e-6
        numbers = [float(num) for num in cards]

        def solve(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPSILON

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue

                    remaining_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    
                    a, b = nums[i], nums[j]
                    
                    if solve(remaining_nums + [a + b]):
                        return True
                    if solve(remaining_nums + [a - b]):
                        return True
                    if solve(remaining_nums + [a * b]):
                        return True
                    if b != 0 and solve(remaining_nums + [a / b]):
                        return True
            
            return False

        return solve(numbers)
