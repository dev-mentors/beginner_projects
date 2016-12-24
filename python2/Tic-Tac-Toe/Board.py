from Cell import Cell


class Board(object):

    def __init__(self):

        self.cells = [
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell()],
            [Cell(), Cell(), Cell()]
        ]

    def __repr__(self):
        return str(self.cells[0]) + "\n" + str(self.cells[1]) + "\n" + str(self.cells[2]) + "\n"

    def is_empty(self, row, column):
        if self.cells[row][column].mark is None:
            return True
        else:
            return False

    def player_mark(self, row, column, mark):
        cell = self.cells[row][column]
        cell.mark_cell(mark)

    def check_won(self, mark):
        # rows
        if self.cells[0][0].mark == self.cells[0][1].mark == self.cells[0][2].mark == mark and self.cells[0][0].mark is not None:
            return True
        elif self.cells[1][0].mark == self.cells[1][1].mark == self.cells[1][2].mark == mark and self.cells[1][0].mark is not None:
            return True
        elif self.cells[2][0].mark == self.cells[2][1].mark == self.cells[2][2].mark == mark and self.cells[2][0].mark is not None:
            return True

        # columns
        elif self.cells[0][0].mark == self.cells[1][0].mark == self.cells[2][0].mark == mark and self.cells[0][0].mark is not None:
            return True
        elif self.cells[0][1].mark == self.cells[1][1].mark == self.cells[2][1].mark == mark and self.cells[0][1].mark is not None:
            return True
        elif self.cells[0][2].mark == self.cells[1][2].mark == self.cells[2][2].mark == mark and self.cells[0][2].mark is not None:
            return True

        # diagonals
        elif self.cells[0][0].mark == self.cells[1][1].mark == self.cells[2][2].mark == mark and self.cells[0][0].mark is not None:
            return True
        elif self.cells[0][2].mark == self.cells[1][1].mark == self.cells[2][0].mark == mark and self.cells[0][2].mark is not None:
            return True
        else:
            return False
