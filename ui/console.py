import configparser

from game.game import Game, GameOverException, ImpossibleDirectionException


class Console:
    def __init__(self, file_name):
        self._file_name = file_name
        self._dim = 0
        self._apple = 0
        self.read_from_file()
        self._game = Game(self._dim, self._apple)

    def read_from_file(self):
        config = configparser.ConfigParser()
        config.read(self._file_name)
        self._dim = int(config.get("Settings", "dim"))
        self._apple = int(config.get("Settings", "apples"))

    def get_command_args(self, cmd_line):
        pos = cmd_line.find(" ")
        if pos == -1:
            return cmd_line, None
        cmd = cmd_line[:pos]
        args = int(cmd_line[pos:])
        return cmd, args

    def display_board(self):
        self._game.display_board()

    def left(self, args):
        if args is not None:
            raise OptionException
        self._game.left()

    def right(self, args):
        if args is not None:
            raise OptionException
        self._game.right()

    def up(self, args):
        if args is not None:
            raise OptionException
        self._game.up()

    def down(self, args):
        if args is not None:
            raise OptionException
        self._game.down()

    def move_more(self, arg):
        self._game.move_more(arg)

    def move_one(self):
        self._game.move_one()

    def move(self, arg):
        if arg is None:
            self.move_one()
        else:
            self.move_more(arg)

    def read_cmd(self):
        commands = {"move": self.move, "left": self.left, "right": self.right, "up": self.up, "down": self.down}

        while True:
            cmd_line = input("cmd = ")
            try:
                cmd, args = self.get_command_args(cmd_line)
                try:
                    commands[cmd](args)
                    self.display_board()
                except KeyError:
                    print("You introduced an invalid option.\n Try again!")
                except OptionException:
                    print("You introduced an invalid option.\n Try again!")
                except ImpossibleDirectionException:
                    print("The snake cannot go in the opposite direction.")
                except GameOverException:
                    print("Game over!")
                    break
            except ValueError:
                print("You introduced an invalid option.\n Try again!")

    def start(self):
        self.display_board()
        self.read_cmd()


class OptionException(Exception):
    def __init__(self):
        self._msg = ""
