import statistics

name = 'a_example.txt'
# name of the file to be processed

TotalBooks = 0
TotalLibraries = 0
TotalDays = 0
ScoreCalcDivisions = 0
BookScores = []
ScannedBooks = []

def printArrayInLine(array):
    line = ''
    for i in array:
        line += str(i) + ' '
    print(line)

class Library(object):

    def __init__(self, count, signup, debit, books, avgScore):
        self.BookCount = count
        self.SignupTime = signup
        self.DebitPerDay = debit
        self.BookList = books
        self.AvgScore = avgScore
        self.Processed = False

    def calcScore(self, time):
        return self.AvgScore * self.DebitPerDay * (time - self.SignupTime)

    def write(self):
        print(self.BookCount, self.SignupTime, self.DebitPerDay)
        printArrayInLine(self.BookList)
    
    def processed(self):
        return self.Processed
        

class Solver(object):

    def __init__(self, filename):
        self.Libraries = []             # access by library index (duh)
        self.filename = filename
        self.get_input()

    def total_score(self):
        return 0

    def get_input(self):

        global TotalBooks, TotalLibraries, TotalDays
        global ScoreCalcDivisions, BookScores, ScannedBooks

        path = 'input/' + self.filename
        with open(path, 'r') as f:
            [TotalBooks, TotalLibraries, TotalDays] = [int(el) for el in f.readline().split()]
            ScoreCalcDivisions = TotalDays / 3
            scoresLine = f.readline().split()
            for el in scoresLine:
                BookScores.append(int(el))
                ScannedBooks.append(False)
            BookScores = [int(el) for el in f.readline().split()]
            for i in range(TotalLibraries):
                [count, signup, debit] = [int(el) for el in f.readline().split()]
                books = []

                scoreSum = 0

                bookLine = f.readline().split()
                for book in bookLine:
                    books.append(book)
                    scoreSum += BookScores[book]
                scoreAvg = scoreSum / len(books)

                lib = Library(count, signup, debit, books, scoreAvg)
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
