class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        
        if len(matrix) == 1:
            return matrix[0]

        if len(matrix[0]) == 1:
            return [row[0] for row in matrix]

        M = len(matrix)
        N = len(matrix[0])
        result = matrix[0][:N-1] + \
            [row[-1] for row in matrix[:M-1]] + \
            matrix[-1][-1:-N:-1] + \
            [row[0] for row in matrix[-1:-M:-1]]
        inner_result = []
        if M > 2 and N > 2:
            submatrix = [row[1:N-1] for row in matrix[1:M-1]]
            inner_result = self.spiralOrder(submatrix)

        return result + inner_result