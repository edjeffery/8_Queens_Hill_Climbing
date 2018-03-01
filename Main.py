from Problem import Problem
from State import State


def hill_climbing(problem):
    """ Runs the 8-queens game loop until no better state is found"""

    current = State(problem.initial_state)
    print(current.get_value())
    while current.get_value() != 0:
        neighbour = current.generate_neighbour()
        print(neighbour.board)
        print(neighbour.get_value())
        if neighbour.get_value() >= current.get_value():
            return current.board
        current = neighbour


problem = Problem()
print(problem.initial_state)
print("Final state = " + str(hill_climbing(problem)))