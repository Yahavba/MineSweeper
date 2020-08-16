import random as rn


class Minesweeper(object):
    def __init__(self):
        self.row = 0
        self.col = 0
        self.currentField = []
        self.fullField = []
        self.isMine = False

    def createField(self, rows, cols):
        self.row = rows
        self.col = cols
        fullRow1 = []
        fullRow2 = []

        for i in range(0, self.row):
            for j in range(0, self.col):
                fullRow1 += '.'
                fullRow2 += '.'
            self.currentField += [fullRow1]
            self.fullField += [fullRow2]
            fullRow1 = []
            fullRow2 = []

    def randomMineSpots(self):
        traps = int(self.col * self.row * 0.25)
        for i in range(0, traps):
            col = rn.randrange(self.col - 1)
            row = rn.randrange(self.row - 1)
            if self.fullField[row][col] != '*':
                self.layMine(row, col)

    def layMine(self, row, col):
        self.fullField[row][col] = '*'

        def setField(row, col):
            if 0 <= row < self.row and 0 <= col < self.col:
                if type(self.fullField[row][col]) == type(1):
                    self.fullField[row][col] += 1
                elif self.fullField[row][col] == '.' or self.fullField[row][col] == '+':
                    self.fullField[row][col] = 1
            for i in range(0, self.row):
                for j in range(0, self.col):
                    if self.fullField[i][j] == '.':
                        self.fullField[i][j] = '+'

        setField(row + 1, col)
        setField(row, col + 1)
        setField(row + 1, col + 1)
        setField(row + 1, col - 1)
        setField(row - 1, col)
        setField(row, col - 1)
        setField(row - 1, col - 1)
        setField(row - 1, col + 1)

    def play(self, row, col):
        def floodFill(row, col):
            if 0 <= row < self.row and 0 <= col < self.col:
                if self.fullField[row][col] == '+' and self.currentField[row][col] == '.':
                    self.currentField[row][col] = self.fullField[row][col]
                    floodFill(row + 1, col)
                    floodFill(row - 1, col)
                    floodFill(row, col + 1)
                    floodFill(row, col - 1)
                    floodFill(row + 1, col - 1)
                    floodFill(row - 1, col + 1)
                    floodFill(row + 1, col + 1)
                    floodFill(row - 1, col - 1)
                elif type(self.fullField[row][col]) == type(1):
                    self.currentField[row][col] = self.fullField[row][col]

        if self.fullField[row][col] == '*':
            self.currentField[row][col] = self.fullField[row][col]
            self.isMine = True
        else:
            floodFill(row, col)
        if self.isMine or self.status() == 'WON':
            for i in range(0, self.row):
                for j in range(0, self.col):
                    if self.fullField[i][j] == '*':
                        self.currentField[i][j] = self.fullField[i][j]

    def StartGame(self):
        print("Welcome to Minesweeper!\n\nPlease enter desired grid")
        while True:
            self.row = numericToInt(input("Number of rows (minimum 2): "), "Number of rows (minimum 2): ")
            if self.row > 1:
                break
            else:
                print("Invalid value! try again...\n")
        while True:
            self.col = numericToInt(input("Number of columns (minimum 2): "), "Number of columns (minimum 2): ")
            if self.col > 1:
                break
            else:
                print("Invalid value! try again...\n")
        self.createField(self.row, self.col)
        self.randomMineSpots()
        print("\nAll set!\nLets start the game...\n")
        print("Current Field:")
        self.printField()
        while self.status() == 'PLAYING':
            print("Please pick a spot")
            while True:
                row = numericToInt(input("Row: "), "Row: ")
                if 0 <= row - 1 < self.row:
                    break
                else:
                    print("Invalid value! try again...\n")
            while True:
                col = numericToInt(input("Col: "), "Col: ")
                if 0 <= col - 1 < self.col:
                    break
                else:
                    print("Invalid value! try again...\n")
            row = row - 1
            col = col - 1
            self.play(row, col)
            print("\nCurrent Field:")
            self.printField()
        print("You " + self.status() + "!")

    def status(self):
        if self.isMine:
            return 'LOST'
        else:
            flag = 0
            for i in range(0, self.row):
                for j in range(0, self.col):
                    if self.fullField[i][j] != '*' and self.fullField[i][j] != self.currentField[i][j]:
                        flag = 1
            if flag == 0:
                return 'WON'
            else:
                return 'PLAYING'

    def printField(self):
        for i in range(0, self.row):
            print("\"", end="")
            for j in range(0, self.col):
                print("{0}".format(self.currentField[i][j]), end="")
                if j + 1 != self.col:
                    print(" ", end="")
                else:
                    print("\"")
        print("\n")


def numericToInt(value, typeOfValue):
    while not value.isnumeric():
        print("Invalid value! try again...\n")
        value = input(typeOfValue + ": ")
    return int(value)


if __name__ == "__main__":
    game = Minesweeper()
    game.StartGame()