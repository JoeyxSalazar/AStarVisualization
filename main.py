from environment import Environment
from problem import Problem

def main():
    env = Environment(10) #num polygons
    solution = Problem(env)
    path = solution.astar()
    steps = []
    if path:
        print("PRINTING ASTAR SOLUTION PATH: ")
        for n in path:
            steps.append(n)
    else:
        print('No Path')
    print(steps)
    env.display_solution(steps)
    

if __name__ == '__main__':
    main()
