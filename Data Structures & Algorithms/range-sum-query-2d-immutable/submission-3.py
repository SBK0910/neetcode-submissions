class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.store = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for r in range(0,len(matrix)):
            for c in range(0, len(matrix[0])):
                self.store[r][c] = matrix[r][c]
                if r > 0:
                    self.store[r][c] += self.store[r-1][c]
                if c > 0:
                    self.store[r][c] += self.store[r][c-1]
                if r > 0 and c > 0:
                    self.store[r][c] -= self.store[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.store[row2][col2]
        if row1 > 0:
            total -= self.store[row1-1][col2]
        if col1 > 0:
            total -= self.store[row2][col1-1]
        if row1 > 0 and col1 > 0:
            total += self.store[row1-1][col1-1]
        return total
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)