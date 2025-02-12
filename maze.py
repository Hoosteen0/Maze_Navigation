import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
"""
File to make the maze environment the agent needs to navigate through
"""


class Maze:
    def __init__(self, env_size: tuple[int, int] = (4, 4)):
        self._env_size = env_size
        self._maze = self.generate_maze()

    def generate_maze(self):
        return ['OOCOOOOC',
                'OCCOCCOG',
                'OOOOCCCC',
                'OCCOOCCO',
                'OOCCOOOO',
                'COOCCCOC',
                'CCOCOCOC',
                'SOOOOOOC']

    def test_maze(self):
        char_to_num = {'O':0, 'C': 1, 'S': 0.5, 'G': 0.75}
        plottable_maze = np.zeros((8, 8))
        for i in range(8):
            for j in range(8):
                plottable_maze[i, j] = char_to_num.get(self._maze[i][j], -1.0)
        sns.heatmap(plottable_maze, cmap='Greys')

        plt.title('Maze')
        plt.xlabel('Columns')
        plt.ylabel('Rows')
        plt.savefig('maze.png')
        plt.show()
