import random
import numpy as np


class State:
    """ Class defines the state of an 8-queens board

    Attributes:
        board (np array): Represents the locations of the queens on the board. Col = index. Row = array element

    """

    def __init__(self, board):
        self.board = board


    def get_value(self):
        """ Calculates the number of queens attacking each other """

        value = 0

        # Counts horizontal attacks
        for i in range(len(self.board)):
            count = np.count_nonzero(self.board == i)
            if count > 1:
                value += int(count * (count - 1) / 2)

        # Counts diagonal attacks
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if j > i:
                    if abs(i - j) == abs(self.board[i] - self.board[j]):
                        value += 1

        return value

    def generate_neighbour(self):
        """ Generates the best available next state.
        If multiple states have equal value, a random state is selected. """

        potential_moves = {}
        for col in range(len(self.board)):
            for row in range(len(self.board)):
                if row != self.board[col]:
                    temp_board = np.copy(self.board)
                    temp_board[col] = row
                    temp_state = State(temp_board)
                    potential_moves[(col, row)] = temp_state.get_value()

        best_moves = []
        lowest_value = self.get_value()
        for key, value in potential_moves.items():
            if value < lowest_value:
                lowest_value = value

        for key, value in potential_moves.items():
            if value == lowest_value:
                best_moves.append(key)

        if len(best_moves) > 0:
            pick = random.randint(0, len(best_moves) - 1)
            col = best_moves[pick][0]
            row = best_moves[pick][1]
            new_board = np.copy(self.board)
            new_board[col] = row

        return State(new_board)


