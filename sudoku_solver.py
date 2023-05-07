class Board:
    def __init__(self):
        # self.board = list([0]*9 for _ in range(9))
        # for i in range(9):
        #     self.board[i] = list(map(int, input().split()))
        self.board = [
            [7,8,0,4,0,0,1,2,0],
            [6,0,0,0,7,5,0,0,9],
            [0,0,0,6,0,1,0,7,8],
            [0,0,7,0,4,0,2,6,0],
            [0,0,1,0,5,0,9,3,0],
            [9,0,4,0,6,0,0,0,5],
            [0,7,0,3,0,0,0,1,2],
            [1,2,0,0,0,7,4,0,0],
            [0,4,9,2,0,6,0,0,7]
        ]

    def print_board(self):
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print('----------------------')
            
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    print('| ', end = '')

                if j == 8:
                    print(self.board[i][j])
                else:
                    print(self.board[i][j] , end = ' ')

    def valid(self, row, col, num):
        # Check row and column
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False

        # Check in the box
        box_x = row//3 * 3
        box_y = col//3 * 3

        for i in range(box_x, box_x+3):
            for j in range(box_y, box_y+3):
                if self.board[i][j] == num:
                    return False

        return True

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    for num in range(1, 10):
                        if self.valid(i, j, num):
                            self.board[i][j] = num
                            if self.solve():
                                return True
                            self.board[i][j] = 0

                    return False

        return True
        


if __name__ == "__main__":
    start = Board()
    start.print_board()
    start.solve()
    print('\n Solution:')
    start.print_board()

