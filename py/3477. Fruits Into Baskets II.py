class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        bsk = [False] * n
        count = 0

        for fruit_quantity in fruits:
            found_basket = False

            for j in range(n):
                if not bsk[j] and baskets[j] >= fruit_quantity:
                    bsk[j] = True
                    found_basket = True

                    break

            if not found_basket:
                count += 1

        return count
