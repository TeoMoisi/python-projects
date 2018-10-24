"""
    @author: Teofana Moisi
    @email:  teofana.moisi@gmail.com
    @date:   05/01/2018 22:02
"""
from domain.table import Table
from domain.square import Square
import random

class GamePlay:
    def __init__(self, l, h):
        self.boardControl = Table(l, h)

    def moveUser(self, pos):
        if self.boardControl.move(pos, 1) == False:
            print("Already taken or outside the board!")
        else:
            self.boardControl.move(pos, 1)

    def moveComputer(self):
        validMoves = self.boardControl.getValidMoves()
        pos = random.randint(0,len(validMoves)-1)
        mov = validMoves[pos]
        return mov

    def moveAround(self, pos):
        self.boardControl.move(pos, 2)