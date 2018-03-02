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
            return (current.board, count, 0)
        current = neighbour
        print("")
        count += 1
    print("Solution found")
    return (current.board, count, 1) # 1 indicates solution found

no_of_steps = []
count = 0
for i in range(100):
    count += 1
    problem = Problem()
    result = hill_climbing(problem)
    if result[2] == 1:
        no_of_steps.append(count)
        count = 0

print(no_of_steps)
print(sum(no_of_steps)/len(no_of_steps ))

