class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        box=[set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                ch=board[i][j]
                box_id=(i//3)*3+j//3
                if ch=='.':
                    continue
                if ch in rows[i] or ch in cols[j] or ch in box[box_id]:
                    return False
                rows[i].add(ch)
                cols[j].add(ch)
                box[box_id].add(ch)
        return True
        