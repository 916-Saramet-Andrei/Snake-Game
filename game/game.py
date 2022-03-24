import random

from board.board import Board


class GameOverException(Exception):
    def __init__(self):
        self._msg = "Game over!"


class ImpossibleDirectionException(Exception):
    def __init__(self):
        self._msg = ""


class Game:
    def __init__(self, dim, apl):
        self._dim = dim
        self.__board = Board(dim, apl)

    def display_board(self):
        print(self.__board)

    def find_head(self):
        for i in range(1, self._dim + 1):
            for j in range(1, self._dim + 1):
                if self.__board.board[i][j] == 3:
                    return i, j

    def find_last_body(self):
        return self.__board.body[-1][0], self.__board.body[-1][1]

    def move_more(self, arg):
        for i in range(arg):
            self.move_one()

    def left(self):
        dir = self.__board.dir
        if dir == 3:
            return
        if dir == 4:
            raise ImpossibleDirectionException
        self.__board.dir = 3
        self.move_one()

    def right(self):
        dir = self.__board.dir
        if dir == 4:
            return
        if dir == 3:
            raise ImpossibleDirectionException
        self.__board.dir = 4
        self.move_one()

    def up(self):
        dir = self.__board.dir
        if dir == 1:
            return
        if dir == 2:
            raise ImpossibleDirectionException
        self.__board.dir = 1
        self.move_one()

    def down(self):
        dir = self.__board.dir
        if dir == 2:
            return
        if dir == 1:
            raise ImpossibleDirectionException
        self.__board.dir = 2
        self.move_one()

    def empty_pos(self):
        l = []
        for i in range(1, self._dim + 1):
            for j in range(1, self._dim + 1):
                if self.__board.board[i][j] == 0 and self.__board.board[i + 1][j] != 1 \
                        and self.__board.board[i - 1][j] != 1 and self.__board.board[i][j + 1] != 1 \
                        and self.__board.board[i][j - 1] != 1:
                    l.append([i, j])
        return l

    def add_apple(self):
        l = self.empty_pos()
        if l == []:
            raise GameOverException
        l1 = random.choice(l)
        self.__board.set_value(l1[0], l1[1], 1)

    def move_one(self):
        row, col = self.find_head()
        dir = self.__board.dir
        if dir == 1:
            if self.__board.check_if_edge_or_body(row - 1, col):
                raise GameOverException
            val = self.__board.check_if_apple(row - 1, col)
            self.__board.set_value(row - 1, col, 3)
            self.__board.set_value(row, col, 2)
            body = self.__board.body
            body.insert(0, [row, col])
            self.__board.body = body
            if not val:
                row, col = self.find_last_body()
                self.__board.set_value(row, col, 0)
                body = self.__board.body
                body.pop()
                self.__board.body = body
            else:
                self.add_apple()
        elif dir == 2:
            if self.__board.check_if_edge_or_body(row + 1, col):
                raise GameOverException
            val = self.__board.check_if_apple(row + 1, col)
            self.__board.set_value(row + 1, col, 3)
            self.__board.set_value(row, col, 2)
            body = self.__board.body
            body.insert(0, [row, col])
            self.__board.body = body
            if not val:
                row, col = self.find_last_body()
                self.__board.set_value(row, col, 0)
                body = self.__board.body
                body.pop()
                self.__board.body = body
            else:
                self.add_apple()
        elif dir == 3:
            if self.__board.check_if_edge_or_body(row, col - 1):
                raise GameOverException
            val = self.__board.check_if_apple(row, col - 1)
            self.__board.set_value(row, col - 1, 3)
            self.__board.set_value(row, col, 2)
            body = self.__board.body
            body.insert(0, [row, col])
            self.__board.body = body
            if not val:
                row, col = self.find_last_body()
                self.__board.set_value(row, col, 0)
                body = self.__board.body
                body.pop()
                self.__board.body = body
            else:
                self.add_apple()
        else:
            if self.__board.check_if_edge_or_body(row, col + 1):
                raise GameOverException
            val = self.__board.check_if_apple(row, col + 1)
            self.__board.set_value(row, col + 1, 3)
            self.__board.set_value(row, col, 2)
            body = self.__board.body
            body.insert(0, [row, col])
            self.__board.body = body
            if not val:
                row, col = self.find_last_body()
                self.__board.set_value(row, col, 0)
                body = self.__board.body
                body.pop()
                self.__board.body = body
            else:
                self.add_apple()
