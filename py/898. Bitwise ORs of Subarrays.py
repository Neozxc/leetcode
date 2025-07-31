class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        a = set()
        c = set()

        for num in arr:
            n = {p | num for p in c}
            n.add(num)
            a.update(n)
            c = n

        return len(a)
