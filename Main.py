from Problem import Problem
from State import State


problem = Problem()
print(problem.initial_state)

def hill_climbing(problem):

    current = State(problem.initial_state)
    print(current.get_value())
    while current.get_value() != 0:
        neighbour = current.generate_neighbour()
        print(neighbour.board)
        print(neighbour.get_value())
        #if neighbour.get_value() >= current.get_value():
        #    return current.board
        current = neighbour
    print("Solution = " + str(current.board))

hill_climbing(problem)
#print("Solution = " + str(hill_climbing(problem)))
