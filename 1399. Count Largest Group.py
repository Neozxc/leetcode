class Solution:
    def countLargestGroup(self, n: int) -> int:
        group_counts = defaultdict(int)

        def digit_sum(x):
            return sum(int(c) for c in str(x))

        for number in range(1, n + 1):
            s = digit_sum(number)
            group_counts[s] += 1

        max_size = max(group_counts.values())

        return sum(1 for count in group_counts.values() if count == max_size)
