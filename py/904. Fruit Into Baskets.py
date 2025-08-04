class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_pck = 0
        baskets = defaultdict(int)

        for right, fruit in enumerate(fruits):
            baskets[fruit] += 1

            while len(baskets) > 2:
                left_fruit = fruits[left]
                baskets[left_fruit] -= 1

                if baskets[left_fruit] == 0:
                    del baskets[left_fruit]

                left += 1

            curr = right - left + 1
            max_pck = max(max_pck, curr)

        return max_pck
