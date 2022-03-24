from random import randint

from texttable import Texttable


class Board:
    def __init__(self, dim, apl):
        self.__dim = dim
        self.__apples = apl
        self.__data = [[-1 for _ in range(self.__dim + 2)] for _ in range(self.__dim + 2)]
        self.__dir = 1
        for i in range(1, self.__dim + 1):
            for j in range(1, self.__dim + 1):
                self.__data[i][j] = 0
        mid = self.__dim // 2
        self.__data[mid][mid + 1] = 3
        self.__data[mid + 1][mid + 1] = 2
        self.__data[mid + 2][mid + 1] = 2
        self.__body = []
        self.__body.append([mid + 1, mid + 1])
        self.__body.append([mid + 2, mid + 1])
        self.put_apl()

    @property
    def board(self):
        return self.__data

    def set_value(self, row, col, val):
        self.__data[row][col] = val

    @property
    def body(self):
        return self.__body

    @body.setter
    def body(self, value):
        self.__body = value

    @property
    def dir(self):
        return self.__dir

    @dir.setter
    def dir(self, value):
        self.__dir = value

    def put_apl(self):
        for i in range(self.__apples):
            while True:
                row = randint(1, self.__dim)
                col = randint(1, self.__dim)
                if self.__data[row][col] == 0 and \
                        self.__data[row][col + 1] != 1 and self.__data[row][col - 1] != 1 \
                        and self.__data[row - 1][col] != 1 and self.__data[row + 1][col] != 1:
                    self.__data[row][col] = 1
                    break

    def __str__(self):
        t = Texttable()
        for row in range(1, self.__dim + 1):
            data = []
            for el in self.__data[row][1:-1]:
                if el == 3:
                    data.append('*')
                elif el == 2:
                    data.append('+')
                elif el == 1:
                    data.append('.')
                else:
                    data.append(' ')
            t.add_row(data)
        return t.draw()

    def check_if_edge_or_body(self, row, col):
        if self.__data[row][col] == -1 or self.__data[row][col] == 2:
            return True
        return False

    def check_if_apple(self, row, col):
        if self.__data[row][col] == 1:
            return True
        return False
