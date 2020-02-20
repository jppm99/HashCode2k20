import statistics

name = 'a_example.txt'
# name of the file to be processed

TotalBooks = 0
TotalLibraries = 0
TotalDays = 0
ScoreCalcDivisions = 1
TopLibraries = []
BookScores = []
ScannedBooks = []

LibList = []

def printArrayInLine(array):
    line = ''
    for i in array:
        line += str(i) + ' '
    print(line)

def getSortedDict(d):
    return {k: v for k, v in reversed(sorted(d.items(), key=lambda item:item[1]))}

class Library(object):

    def __init__(self, count, signup, debit, books, avgScore):
        self.BookCount = count
        self.SignupTime = signup
        self.DebitPerDay = debit
        self.BookList = books
        self.AvgScore = avgScore
        self.ScoreList = []
        self.Processed = False
        self.BooksSent = []

        for i in range(len(self.BookList)):
            self.BookDict.update({i: self.BookList[i]})
        
        {k: v for k, v in sorted(self.BookDict.items(), key=lambda item: item[1]).reverse()} #ordem descendente

        for x in range(ScoreCalcDivisions):
            self.ScoreList.append(calcScore(self, TotalDays-(x*(TotalDays/ScoreCalcDivisions))))

    def chooseBooks(self, time): #time is the day of the signup start (day)
        nBooks = self.DebitPerDay * (TotalDays - (time + self.SignupTime))
        orderedKeysList = self.BookDict.keys()
        nSent = 0
        currBook = 0

        while nSent < nBooks:
            if ScannedBooks[currBook]:
                currBook += 1
            else:
                self.BooksSent.append(currBook)
                currBook += 1
                nSent += 1

        return self.BooksSent
    
    def getBooksSent(self):
        return self.BooksSent

    def calcScore(self, time):
        if self.Processed:
            return 0
        else:
            return min(self.AvgScore * self.DebitPerDay * (time - self.SignupTime), self.AvgScore * self.BookCount)

    def write(self):
        print(self.BookCount, self.SignupTime, self.DebitPerDay)
        printArrayInLine(self.BookList)
    
    def processed(self):
        return self.Processed
    
    def process(self):
        self.Processed = True
    
    def getSignup(self):
        return self.SignupTime

    def getScores(self):
        return self.ScoreList
        

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
                books = {}

                scoreSum = 0

                bookLine = f.readline().split()
                for book in bookLine:
                    books[book] = BookScores[book]
                    scoreSum += BookScores[book]
                scoreAvg = scoreSum / len(books)

                lib = Library(count, signup, debit, books, scoreAvg)
                self.Libraries.append(lib)
            
    def write(self):
        path = 'output/' + self.filename + '.out'
        with open(path, 'w') as f:
            f.write(str(len(self.Libraries)) + '\n')
            #f.write(' '.join([str(el) for el in reversed(self.PizzaIndexes)]))
            for i in range(len(self.Libraries)):
                #bonjour


        return 0

    def solve(self):
        return solve_large(self)

    def solve_small(self):  # exact, slow
        return 0

    def solve_large(self):  # not exact, fast

        def selectBestLib(dic, time):
            bestLib = -1
            bestScore = -1
            for i in range(len(self.Libraries)):
                lib = self.Libraries[i]
                score = lib.calcScore(time)
                if score > bestScore:
                    bestScore = score
                    bestLib = i
            self.Libraries[bestLib].process()

            return self.Libraries[bestLib]

        global TotalBooks, TotalLibraries, TotalDays, ScoreCalcDivisions
        global TopLibraries, BookScores, ScannedBooks, LibList

        DaysPerDiv = TotalDays # equals to 1 division (test run)

        ScoreCalcDivisions = TotalDays / DaysPerDiv

        dicts = []

        for i in range(ScoreCalcDivisions):
            time = i * DaysPerDiv
            divDict = {}
            for ind in range(len(self.Libraries)):
                if len(divDict) < 2 * ScoreCalcDivisions:
                    divDict[ind] = self.Libraries[ind]
                    divDict = {k: v for k, v in sorted(divDict.items(), key=lambda item: item[i])}
                else:
                    avg = self.Libraries[ind].calcScore(time)
                    if divDict[divDict.keys()[-1]] < avg:
                        divDict.popitem()
                        divDict[ind] = self.Libraries[ind]
                        divDict = {k: v for k, v in sorted(divDict.items(), key=lambda item: item[i])}
            dicts.append(divDict)
            
        day = 0    
        while day < TotalDays:
            index = round(day / DaysPerDiv) * DaysPerDiv
            lib = selectBestLib(dicts[ind], time)
            LibList.append(lib)
            day += lib.getSignup()

        return 0


def main():
    solver = Solver(name)
    solver.get_input()

    # solver.solve()
    # print('Total Score:', solver.total_score())

    solver.write()


if __name__ == '__main__':
    main()
