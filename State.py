import random
import numpy as np


class State:

    def __init__(self, board):
        self.board = board


    def get_value(self):
        value = 0

        # Counts horizontal attacks
        for i in range(len(self.board)):
            count = np.count_nonzero(self.board == i)
            #print(i,count)
            if count > 1:
                #print("count>1")
                value += int(count * (count - 1) / 2)
        #print(value)
        # Counts diagonal attacks
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if j > i:
                    #print(i,j)
                    if abs(i - j) == abs(self.board[i] - self.board[j]):
                        #print(i,j,self.state[i],self.state[j])
                        value += 1

        return value

    def generate_neighbour(self):
        potential_moves = {}
        for col in range(len(self.board)):
            for row in range(len(self.board)):
                if row != self.board[col]:
                    temp_board = np.copy(self.board)
                    temp_board[col] = row
                    #print(temp_board)
                    temp_state = State(temp_board)
                    #print(temp_state.get_value())
                    potential_moves[(col, row)] = temp_state.get_value()

        #print(potential_moves)
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
            self.board[col] = row

        return State(self.board)


