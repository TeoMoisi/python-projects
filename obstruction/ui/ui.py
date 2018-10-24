"""
    @author: Teofana Moisi
    @email:  teofana.moisi@gmail.com
    @date:   05/01/2018 22:03
"""
from domain.table import Table
from domain.square import Square
import random
from ctrl.moves import GamePlay

class UI:
    def __init__(self):
        l = UI.lenght()
        h = UI.height()
        if type(l) != int or type(h) != int:
            print("The dimensions have to be integer")
        self._play = GamePlay(l, h)
        self._board = Table(l, h)


    def around(self, x, y):
        if x == 0:
            self._play.moveAround(Square(x + 1, y))
            if y <= self._play.boardControl.get_h():
                self._play.moveAround(Square(x + 1, y + 1))
                self._play.moveAround(Square(x, y + 1))
            if y >= 1:
                self._play.moveAround(Square(x + 1, y - 1))
                self._play.moveAround(Square(x, y - 1))
        if x >= 1:
            self._play.moveAround(Square(x - 1, y))
            if y >= 1:
                self._play.moveAround(Square(x - 1, y - 1))
                self._play.moveAround(Square(x, y - 1))
            if y < self._play.boardControl.get_l():
                self._play.moveAround(Square(x - 1, y + 1))
                self._play.moveAround(Square(x, y + 1))
        if x < self._play.boardControl.get_h():
            self._play.moveAround(Square(x + 1, y))
            if y < self._play.boardControl.get_l():
                self._play.moveAround(Square(x + 1, y + 1))
            if y >= 1:
                self._play.moveAround(Square(x + 1, y - 1))

    @staticmethod
    def readFirstCoord():
        '''

        :return:
        '''
        try:
            x = int(input("Enter the first cooordinate: "))
            return x
        except ValueError:
            raise Exception("The coordinate has has to be an integer")

    @staticmethod
    def readSecondCoord():
        '''

        :return:
        '''
        try:
            x = int(input("Enter the second cooordinate: "))
            return x
        except ValueError:
            raise Exception("The coordinate has has to be an integer")

    @staticmethod
    def lenght():
        try:
            x = int(input("Enter the lenght: "))
            return x
        except ValueError:
            raise Exception("The lenght has has to be an integer")

    @staticmethod
    def height():
        try:
            x = int(input("Enter the height: "))
            return x
        except ValueError:
            raise Exception("The height has has to be an integer")

    def startUI(self):
        uname = input("Hello, what is your username?")
        print("Hello,", uname + ".")
        answer = input("Would you like to begin first?")
        while answer != "yes" and answer != "no":
            answer = input("yes / no")
        if answer == "yes":
            turn = 0
        else:
            turn = 1
        while not (self._play.boardControl.checkWin()) and (self._play.boardControl.checkDraw()):
            if turn % 2 == 0:
               try:
                   x = UI.readFirstCoord()
                   y = UI.readSecondCoord()
                   print(x)
                   print(y)
               except Exception as ex:
                   print(*ex.args)
                   continue

               mov = Square(x, y)
               my_moves = []
               my_moves.append([x, y])
               print(my_moves[0][0])
               print(len(my_moves))
               table = self._play.boardControl.ret_table()
               if table[x][y] != 0:
                   print("already taken!")
               else:
                   print(self._play.boardControl.get_h())
                   self._play.moveUser(mov)
                   self.around(x, y)


            else:
                table = self._play.boardControl.ret_table()
                if answer == "yes" or turn != 1:
                    if my_moves[0][0] != 0:
                        print("jnjnj")
                        if self._play.boardControl.get_l() == self._play.boardControl.get_h() and self._play.boardControl.get_h() % 2 != 0:
                            print("jnjj")
                            print(self._play.boardControl.get_l() - my_moves[0][0])
                            if self._play.boardControl.get_l() - 1 -my_moves[0][0] < self._play.boardControl.get_l() and self._play.boardControl.get_h() - 1 - my_moves[0][1] < self._play.boardControl.get_h():
                                print("mjj")
                                if table[self._play.boardControl.get_l() - 1 - my_moves[0][0]][self._play.boardControl.get_h() - 1 - my_moves[0][1]] == 0:
                                    mov = Square(self._play.boardControl.get_l() - 1 - my_moves[0][0], self._play.boardControl.get_h() - 1 - my_moves[0][1])
                                    self._play.boardControl.move(mov, -1)
                                else:
                                    mov = self._play.moveComputer()
                                    self._play.boardControl.move(mov, -1)

                            else:
                                print("aici")
                                mov = self._play.moveComputer()
                                self._play.boardControl.move(mov, -1)
                        else:
                            mov = self._play.moveComputer()
                            self._play.boardControl.move(mov, -1)
                    elif my_moves[0][0] == 0 and my_moves[0][1] < self._play.boardControl.get_h():
                        if table[self._play.boardControl.get_l() - 1][my_moves[0][1]] == 0:
                            mov = Square(self._play.boardControl.get_l() - 1, my_moves[0][1])
                            self._play.boardControl.move(mov, -1)
                        else:
                                mov = self._play.moveComputer()
                                self._play.boardControl.move(mov, -1)
                    elif my_moves[0][1] == self._play.boardControl.get_h():
                        if table[0][my_moves[0][1]] == 0:
                            if my_moves[0][0] == self._play.boardControl.get_l():
                                mov = Square(0, my_moves[0][1])
                                self._play.boardControl.move(mov, -1)
                            else:
                                mov = self._play.moveComputer()
                                self._play.boardControl.move(mov, -1)
                        else:
                            if table[self._play.boardControl.get_l()][my_moves[0][1]] == 0:
                                mov = Square(self._play.boardControl.get_l(), my_moves[0][1])
                                self._play.boardControl.move(mov, -1)
                            else:
                                mov = self._play.moveComputer()
                                self._play.boardControl.move(mov, -1)
                    else:
                        mov = self._play.moveComputer()
                        self._play.boardControl.move(mov, -1)
                else:
                    mov = self._play.moveComputer()
                    self._play.boardControl.move(mov, -1)
                x = mov.get_x()
                y = mov.get_y()
                print(x)
                print(y)
                self.around(x, y)

            turn += 1
            print(str(self._play.boardControl))
        if turn % 2 == 1:
            print("You are the winner!")
        else:
            print("The computer won! Keep trying!")
        print("Game over!")


play = UI()
play.startUI()