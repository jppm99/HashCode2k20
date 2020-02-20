name = 'a_example.txt'
# name of the file to be processed

def printArrayInLine(array):
    line = ''
    for i in array:
        line += str(i) + ' '
    print(line)

class Library(object):

    def __init__(self, count, signup, debit, books):
        self.BookCount = count
        self.SignupTime = signup
        self.DebitPerDay = debit
        self.BookList = books

    def write(self):
        print(self.BookCount, self.SignupTime, self.DebitPerDay)
        printArrayInLine(self.BookList)

class Solver(object):

    def __init__(self, filename):
        self.TotalBooks = 0
        self.TotalLibraries = 0
        self.TotalDays = 0
        self.BookScores = []            # access by book index
        self.Libraries = []             # access by library index (duh)
        self.filename = filename
        self.get_input()

    def total_score(self):
        return 0

    def get_input(self):
        path = 'input/' + self.filename
        with open(path, 'r') as f:
            [self.TotalBooks, self.TotalLibraries, self.TotalDays] = [int(el) for el in f.readline().split()]
            self.BookScores = [int(el) for el in f.readline().split()]
            for i in range(self.TotalLibraries):
                [count, signup, debit] = [int(el) for el in f.readline().split()]
                books = [int(el) for el in f.readline().split()]
                lib = Library(count, signup, debit, books)
                self.Libraries.append(lib)
            
    def write(self):
        print(str(self.TotalBooks), str(self.TotalLibraries), str(self.TotalDays))
        printArrayInLine(self.BookScores)
        for lib in self.Libraries:
            lib.write()
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

    # solver.solve()
    # print('Total Score:', solver.total_score())

    solver.write()


if __name__ == '__main__':
    main()
