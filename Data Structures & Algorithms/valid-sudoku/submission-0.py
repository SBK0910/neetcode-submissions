class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(0, len(board)):
            r_seen = set()
            for c in range(0, len(board[0])):
                if board[r][c] in r_seen and board[r][c] != ".":
                    return False
                r_seen.add(board[r][c])
        for c in range(0, len(board[0])):
            c_seen = set()
            for r in range(0, len(board)):
                if board[r][c] in c_seen and board[r][c] != ".":
                    return False
                c_seen.add(board[r][c])
        for br in range(0, 3):
            for bc in range(0, 3):
                b_seen = set()
                for r in range(0, 3):
                    for c in range(0, 3):
                        cell = board[3 * br + r][3 * bc + c]
                        if  cell in b_seen and cell != ".":
                            return False
                        b_seen.add(cell)
        return True