'''

'''

board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]

def isSafe(row, col, digit) :
    for i in range(9) :
        if board[i][col] == digit :
            return False
        if board[row][i] == digit :
            return False
    
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3) :
        for c in range(start_col, start_col + 3) :
            if board[r][c] == digit :
                return False
    return True

def backtrack(row, col) :
    if row == 9 :
        return True
    nextrow, nextcol = row, col + 1
    if col == 8 :
        nextrow = row + 1
        nextcol = 0
    
    if board[row][col] != "." :
        return backtrack(nextrow, nextcol) 
    
    for digit in map(str, range(1,10)) :
        if isSafe(row,col, digit) :
            board[row][col] = digit 
        #foward function
            if backtrack(nextrow, nextcol) :
                return True 
        #exclude 
            board[row][col] = "."

print(backtrack(0, 0))
for i in board :
    for j in i :
        print(j, end = "" )
    print()