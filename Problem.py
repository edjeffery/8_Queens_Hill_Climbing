import numpy as np


class Problem:

    def __init__(self):
        self.initial_state = np.array([7,5,3,1,6,3,0,3])

        # [7,6,5,4,3,2,1,0]
        # [7,5,3,1,6,3,0,3]
        # [0, 5, 3, 1, 6, 3, 0, 3]