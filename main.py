from maze import Maze
from pomdp import POMDP

def main():
    maze = Maze()

    o_location = [i for i in range(64)]
    o_what = ['open', 'closed', 'start', 'goal']
    s_location = [i for i in range(64)]
    u_movement = ['up', 'down', 'left', 'right']

    O = [o_location, o_what]
    S = [s_location]
    U = [u_movement]

    agent = POMDP(O=O, S=S, U=U, environment=maze)
    a_matrix = agent.make_a()
    print(a_matrix)


if __name__ == '__main__':
    main()