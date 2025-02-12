import numpy as np
from pymdp.utils import initialize_empty_A, initialize_empty_B


class POMDP:
    def __init__(self, O, S, U, environment):
        self._observation_set = O
        self._state_set = S
        self._action_set = U
        self._env = environment

    def make_a(self):
        num_obs = [len(modality) for modality in self._observation_set]
        num_states = [len(factor) for factor in self._state_set]
        A = initialize_empty_A(num_obs, num_states)

        A[0] = np.eye(A[0].shape[0])

        # The agent will be uncertain of what the map looks like, ie how observations map to 'whether the tile is closed or open'
        A[1][:, :] = 1.0
        A[1] /= np.sum(A[1], axis=0)
        return A

    def make_b(self):
        num_states = [len(factor) for factor in self._state_set]
        num_action_controls = [len(control_factor) for control_factor in self._action_set]

        B = initialize_empty_B(num_states, num_action_controls)

        # make transitions based on the map
        for i in range(64):
            curr_row = i // 64
            curr_col = i % 64

            if self._env[curr_row][curr_col] == 'C':
                # if we are in a wall we cannot leave it, nor can we enter it
                B[0][:, i, :] = 0.0
                B[0][i, :, :] = 0.0

                B[0][i, i, :] = 1.0 # still working on transition function.
        return B
