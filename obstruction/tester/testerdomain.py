"""
    @author: Teofana Moisi
    @email:  teofana.moisi@gmail.com
    @date:   06/01/2018 14:02
"""
import unittest
from domain.square import Square
from domain.table import Table

class TesterDomain(unittest.TestCase):

    def setUpSquare(self):
        square = Square(1, 2)
        return square



    def test_square(self):
        square = self.setUpSquare()
        x = square.get_x()
        y = square.get_y()

        self.assertEqual(x, 1)
        self.assertEqual(y, 2)

    def setUp(self):
        table = Table()
        return table

    def setUpTable(self):
        tab = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        return tab

    def test_table(self):
        answer = self.setUp()._checkAll()
        self.assertEqual(answer, False)

        answer2 = self.setUp().checkWin()
        self.assertEqual(answer2, False)

        answer3 = self.setUp().checkDraw()
        self.assertEqual(answer3, True)

        answer4 = self.setUp().move(Square(6, 7), 1)
        self.assertEqual(answer4, False)

        answer5 = self.setUp().getValidMoves()
        self.assertNotEqual(answer5, self.setUpTable())
