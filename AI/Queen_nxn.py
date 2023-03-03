def n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    best_solution = []
    min_conflicts = float('inf')
    
    def is_safe(row, col):
        for i in range(row):
            if board[i][col]:
                return False
            if 0 <= row-i+col < n and board[i][row-i+col]:
                return False
            if 0 <= col-row+i < n and board[i][col-row+i]:
                return False
        return True
    
    def backtrack(row):
        nonlocal min_conflicts, best_solution
        if row == n:
            conflicts = sum(board[i][j] for i in range(n) for j in range(n) if board[i][j])
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                best_solution = [row[:] for row in board]
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row][col] = 1
                backtrack(row+1)
                board[row][col] = 0
                
                if min_conflicts == 0:
                    return
                
                if sum(board[i][j] for i in range(n) for j in range(n) if board[i][j]) >= min_conflicts:
                    return
    
    backtrack(0)
    return best_solution

# Example input
n = int(input("Enter the size of the board (n x n :)"))
solution = n_queens(n)
print(solution)
