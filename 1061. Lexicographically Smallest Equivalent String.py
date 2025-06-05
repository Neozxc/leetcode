class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])

            return parent[i]


        def union(i: int, j: int) -> None:
            root_i = find(i)
            root_j = find(j)

            if root_i != root_j:
                if root_i < root_j:
                    parent[root_j] = root_i
                else:
                    parent[root_i] = root_j

        for k in range(len(s1)):
            char1_val = ord(s1[k]) - ord('a')
            char2_val = ord(s2[k]) - ord('a')
            union(char1_val, char2_val)

        result = []

        for char_b in baseStr:
            char_b_val = ord(char_b) - ord('a')
            smallest_eq_val = find(char_b_val)
            result.append(chr(smallest_eq_val + ord('a')))

        return "".join(result)
