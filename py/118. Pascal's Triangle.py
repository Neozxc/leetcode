class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]

        if numRows == 1:
            return triangle

        for i in range(1, numRows):
            prev = triangle[i - 1]
            curr = [1]

            for j in range(len(prev) - 1):
                curr.append(prev[j] + prev[j + 1])

            curr.append(1)
            triangle.append(curr)

        return triangle
