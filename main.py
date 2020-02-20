name = 'a_example'
# name of the file to be processed


class Solver(object):

    def __init__(self, filename):
        self.TotalBooks = 0
        self.TotalLibraries = 0
        self.TotalDays = 0
        self.bookScores = []            # access by book index
        self.LibraryBookCount = []      # access by library index
        self.LibrarySignupTime = []     # access by library index
        self.LibraryDebitPerDay = []    # access by library index
        self.LibraryBookList = []       # [n][m] -> n is library index, m is book index (inside library)
        self.filename = filename
        self.get_input()

    def total_score(self):
        return 0

    def get_input(self):
        path = 'input/' + self.filename + '.txt'
        with open(path, 'r') as f:
            [self.TotalBooks, self.TotalLibraries, self.TotalDays] = [int(el) for el in f.readline().split()]
            self.bookScores = [int(el) for el in f.readline().split()]
            for i in range(self.TotalLibraries):
                [bookCount, signup, debit] = [int(el) for el in f.readline().split()]
                self.LibraryBookCount.append(bookCount)
                self.LibrarySignupTime.append(signup)
                self.LibraryDebitPerDay.append(debit)
                self.LibraryBookList.append([int(el) for el in f.readline().split()])
            
    def write(self):
        print(str(self.TotalBooks), str(self.TotalLibraries), str(self.TotalDays))
        print(self.bookScores)
        for i in range(self.TotalLibraries):
            print(str(self.LibraryBookCount[i]), str(self.LibrarySignupTime[i]), str(self.LibraryDebitPerDay[i]))
            print(self.LibraryBookList[i])
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
