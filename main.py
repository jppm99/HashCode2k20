name = ''
# name of the file to be processed


class Solver(object):

    def __init__(self, filename):
        self.filename = filename
        self.get_input()

    def total_score(self):
        return 0

    def get_input(self):
        return 0

    def write(self):
        return 0

    def solve(self):
        return 0

    def solve_small(self):  # exact, slow
        return 0

    def solve_large(self):  # not exact, fast
        return 0


def main():
    solver = Solver(name)
    solver.get_input()

    solver.solve()
    print('Total Score:', solver.total_score())

    solver.write()


if __name__ == '__main__':
    main()
