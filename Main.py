from Problem import Problem
from State import State


def hill_climbing(problem):
    """ Runs the 8-queens game loop until no better neighbour state is found"""

    current = State(problem.initial_state)
    count = 1
    while current.get_value() != 0:
        print("Iteration = " + str(count))
        neighbour = current.generate_neighbour()
        print("Neighbour board: " + str(neighbour.board))
        print("Neighbour value: " + str(neighbour.get_value()))
        print("Current value: " + str(current.get_value()))
        if neighbour.get_value() >= current.get_value():
            print("No lower valued state")
            return current.board
        current = neighbour
        print("")
    print("Solution found")
    return current.board


problem = Problem()
#print(problem.initial_state)
print("Final state = " + str(hill_climbing(problem)))