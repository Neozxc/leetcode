class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        current_node = 1
        k_steps_remaining = k - 1

        while k_steps_remaining > 0:
            steps_in_group = self.calculate(n, current_node, current_node + 1)

            if steps_in_group <= k_steps_remaining:
                k_steps_remaining -= steps_in_group
                current_node += 1
            else:
                k_steps_remaining -= 1
                current_node *= 10
        
        return current_node

    def calculate(self, n_max: int, n1: int, n2: int) -> int:
        steps = 0
        curr_n1 = n1
        curr_n2 = n2

        while curr_n1 <= n_max:
            steps += min(n_max + 1, curr_n2) - curr_n1

            curr_n1 *= 10
            curr_n2 *= 10

        return steps
