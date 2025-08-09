'''
Given n for n x n matrix

intution :

Each Queen is placed in seperate row
Create isSafe() function to check every new queen position
isSafe() will each upper diagonals and upper column
'''

n = 4

#intilize 
result = []
board = [['.'] * n for _ in range(n)]

def isSafe(row, col) :
    for i in range(row) :
        if board[i][col] == 'Q' :
            return False
        
    r, c = row - 1, col - 1
    while r > - 1 and c > -1 :
        if board[r][c] == 'Q' :
            return False
        r -= 1
        c -= 1

    r, c = row - 1 , col + 1
    while r > - 1 and c < n :
        if board[r][c] == 'Q' :
            return False
        r -= 1
        c += 1

    return True

def backtrack(row) :
    if row == n :
        solution = [''.join(r) for r in board]
        result.append(solution)
        return 
    
    for col in range(n) :
        if isSafe(row, col) :
            # Marking Q
            board[row][col] = 'Q'
            backtrack(row + 1)
            board[row][col] = '.'

backtrack(0)
        
print(result)