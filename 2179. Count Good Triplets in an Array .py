class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 1)

    def update(self, i, delta):
        i += 1

        while i < len(self.tree):
            self.tree[i] += delta
            i += i & - i

    def query(self, i):
        i += 1
        result = 0

        while i > 0:
            result += self.tree[i]
            i -= i & - i 

        return result

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = {val: idx for idx, val in enumerate(nums2)}
        mapped = [pos2[val] for val in nums1]

        right_bit = FenwickTree(n)
        total_right = [0] * n

        for val in mapped:
            total_right[val] += 1

        for val in range(n):
            right_bit.update(val, total_right[val])

        result = 0
        left_bit = FenwickTree(n)

        for val in mapped:
            right_bit.update(val, - 1)

            left_smaller = left_bit.query(val - 1)
            right_larger = right_bit.query(n - 1) - right_bit.query(val)

            result += left_smaller * right_larger
            left_bit.update(val, 1)

        return result
