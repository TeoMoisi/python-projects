"""
    @author: Teofana Moisi
    @email:  teofana.moisi@gmail.com
    @date:   05/01/2018 21:50
"""
from domain.square import Square
import tester.texttable as tt

class Table:

    @staticmethod
    def table(l, h):
        tab = tt.Texttable()

        x = [[]]  # The empty row will have the header

        for i in range(1, l):
            x.append([' ', ' ', ' ', ' '])

        tab.add_rows(x)
        for j in range(1, h):
            tab.set_cols_align(['r', 'r', 'r', 'r'])

            # tab.header([' ', ' ', ' ', ' '])
        x = tab.draw()
        return(x)


    def __init__(self, l, h):
        self.__l = l
        self.__h = h
        self._table = [[0 for i in range(l)] for j in range(h)]

    def get_l(self):
        return self.__l

    def get_h(self):
        return self.__h


    def ret_table(self):
        return self._table

    def _checkAll(self):
        m = 0
        """for i in range(0, self.__l):
            for j in range(0, self.__h):
                b = self._table
                if b[i][j] == 0:
                    m += 1"""
        if 0 in self._table:
            m += 1
        if m != 0:
            return True #toate sunt ocupate
        else:
            return False #inca mai sunt locuri libere

    def checkWin(self):
        if self._checkAll() == True:
            return True
        return False


    def checkDraw(self):
        if self.checkWin() is not True:
            for i in self._table:
                if 0 in i:
                    return True
            return False
        return True

    def __str__(self):
        z = ""
        for i in range(self.__l):
            z += " -"
        z += " \n"
        for i in self._table:
            z += "|"
            for j in i:
                if j == 1:
                        z += "X"
                elif j == -1:
                        z += "0"
                elif j == 2:
                        z += "s"
                else:
                    z += " "x
                z += "|"
            z += "\n"
            for i in range(self.__l):
                z += " -"
            z += " \n"
        return z

    def move(self, pos, val):
        if pos.get_x() not in range(self.__l) or pos.get_y() not in range(self.__h):
            return False
        elif self._table[pos.get_x()][pos.get_y()] == 'x' or self._table[pos.get_x()][pos.get_y()] == '0' or self._table[pos.get_x()][pos.get_y()] == 's':
            return False
        else:
            self._table[pos.get_x()][pos.get_y()] = val

    def getValidMoves(self):
        table = self._table
        validMoves = []
        for i in range(0, self.__l):
            for j in range(0, self.__h):
               if table[i][j] == 0:
                   validMoves.append(Square(i, j))
                   return validMoves