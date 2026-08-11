class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [0] * 9
        cols = [0] * 9
        boxes = [0] * 9

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue

                bit = 1 << (ord(board[i][j]) - 49)
                box = (i // 3) * 3 + j // 3

                if rows[i] & bit or cols[j] & bit or boxes[box] & bit:
                    return False

                rows[i] |= bit
                cols[j] |= bit
                boxes[box] |= bit

        return True