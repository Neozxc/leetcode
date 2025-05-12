class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        res = set()

        for i in range(1, 10):
            for j in range(0, 10):
                for k in range(0, 10):
                    if k % 2 != 0:
                        continue

                    num = 100 * i + 10 * j + k

                    candidate_count = Counter([i, j, k])

                    if all(candidate_count[d] <= count[d] for d in candidate_count):
                        res.add(num)

        return sorted(res)
