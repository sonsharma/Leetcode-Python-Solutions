# https://leetcode.com/problems/valid-sudoku/

# T(N): O(n^2), S(N): O(N^2)
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9
        row = [set() for _ in range(N)]
        column = [set() for _ in range(N)]
        box = [set() for _ in range(N)]

        for r in range(N):
            for c in range(N):
                val = board[r][c]
                if val == ".":
                    continue
                    
                if val in row[r]:
                    return False
                row[r].add(val)
                
                if val in column[c]:
                    return False
                column[c].add(val)
                
                idx = (r//3) * 3 + c//3
                if val in box[idx]:
                    return False
                box[idx].add(val)
                
        return True
            
            