board =[
    #the board game
    [0,9,0,0,5,8,6,0,4],
    [0,0,5,7,6,3,0,0,9],
    [6,3,8,0,2,0,0,7,1],
    [0,0,0,4,1,0,7,8,0],
    [0,6,0,0,0,9,0,1,2],
    [0,0,1,3,0,2,9,6,0],
    [0,8,0,0,9,1,0,4,7],
    [3,1,0,6,4,7,2,5,8],
    [7,2,0,0,0,5,1,9,6]

]

def solve_sudoku(board):
    #this finds an empty cell in the board to guess the number
    find = find_empty_cell(board)
    if not find:
        #if it doesn't find any empty cell then that means that the board is filled completly, hence return true for solve sudoku
        return True        
    else:
        #and when it finds an empty cell, it takes it's row and col position to work on it
        row, col = find

    for i in range(1, 10):
        #this will check if the number is possible then place it on the specified position
        if valid_sudoku(board, i, (row, col)):
            board[row][col] = i

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False
#this checks if the number is valid in a specific box
def valid_sudoku(board, num, pos):
    for i in range(len(board[0])):
        #this checks if board's first row's number is equal to the given num
        #and then checks if column number is not the same as the row one
        #so that the two numbers don't intersect with each other
        if board[pos[0]][i] == num and pos[1] != i:

            return False

    for i in range(len(board)):
        #this does the same thing as above code but for rows instead
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    #this will return the multiplier for example
    # 12 // 3 will return 4 because 3 * 4 = 12
    #this is used to limit the search to one of the 9 boxes
    #we know that the max value a pos can store is 8 so
    #this can have a max value of 2( 8 // 3 = 2 (it rounds off)) so 2,2 box will become the bottom right now while the box with 0,0 pos will become the top left one
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    #this code will check if the specified number is in the specific box or not
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True


#self explanatory
def print_sudoku(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j])+" ", end="")

#the code which finds an empty cell with value 0 and returns it's position
def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


print_sudoku(board)
solve_sudoku(board)
print("      ")
print("      ")
print("The solution of the sudoku is")
print("      ")
print_sudoku(board)
