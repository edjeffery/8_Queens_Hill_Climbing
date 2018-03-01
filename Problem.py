import numpy as np


class Problem:
    """ Initialises the problem

    Attributes:
        initial_state (np array): Starting board for the 8-queens problem

    """

    def __init__(self):
        """ Initialises the starting board """
        self.initial_state = np.array([0,0,0,0,0,0,0,0])

        # [7,6,5,4,3,2,1,0]
        # [7,5,3,1,6,3,0,3]
        # [0, 5, 3, 1, 6, 3, 0, 3]