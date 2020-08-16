import sys, io, unittest
from minesweeper import Minesweeper


class TestMinesweeper(unittest.TestCase):
    def setUp(self):
        self.field = Minesweeper()

    def test_create_field(self):
        self.field.createField(2, 2)
        self.assertEqual(self.field.currentField, [['.', '.'], ['.', '.']])

    def test_lay_mine(self):
        self.field.createField(3, 3)
        self.field.layMine(1, 1)
        self.assertEqual(self.field.fullField, [[1, 1, 1], [1, '*', 1], [1, 1, 1]])

    def test_play_number_cell(self):
        self.field.createField(3, 3)
        self.field.layMine(1, 1)
        self.field.play(0, 0)
        self.assertEqual(self.field.currentField, [[1, '.', '.'], ['.', '.', '.'], ['.', '.', '.']])

    def test_play_empty_cell(self):
        self.field.createField(3, 3)
        self.field.layMine(0, 0)
        self.field.layMine(1, 0)
        self.field.play(2, 2)
        self.assertEqual(self.field.currentField, [['.', 2, '+'], ['.', 2, '+'], ['.', 1, '+']])

    def test_play_mine_cell(self):
        self.field.createField(3, 3)
        self.field.layMine(0, 0)
        self.field.layMine(1, 2)
        self.field.layMine(2, 2)
        self.field.play(2, 2)
        self.assertEqual(self.field.currentField, [['*', '.', '.'], ['.', '.', '*'], ['.', '.', '*']])

    def test_random_mine_spots(self):
        self.field.createField(3, 3)
        self.field.randomMineSpots()
        currentMines = list(filter(lambda x: x=='*', [mines for rows in self.field.fullField for mines in rows]))
        expectedMines = []
        for i in range(0, int(3*3*0.25)):
            expectedMines += ['*']
        self.assertEqual(currentMines, expectedMines)

    def test_status_LOST(self):
        self.field.createField(2, 2)
        self.field.layMine(1, 1)
        self.field.play(1, 1)
        self.assertEqual(self.field.status(), 'LOST')

    def test_status_WON(self):
        self.field.createField(2, 2)
        self.field.layMine(1, 1)
        self.field.layMine(0, 0)
        self.field.play(0, 1)
        self.field.play(1, 0)
        self.assertEqual(self.field.status(), 'WON')

    def test_status_PLAYING(self):
        self.field.createField(2, 2)
        self.field.layMine(0, 0)
        self.field.play(0, 1)
        self.assertEqual(self.field.status(), 'PLAYING')

    def test_print_field(self):
        self.field.createField(3, 3)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        self.field.printField()
        self.assertEqual(capturedOutput.getvalue(), "\". . .\"\n\". . .\"\n\". . .\"\n\n\n")


if __name__ == '__main__':
    unittest.main()




