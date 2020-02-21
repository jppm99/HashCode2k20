import statistics

name = '.txt'
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

    def __init__(self, id, count, signup, debit, books, avgScore):

        global BookScores

        self.id = id
        self.BookCount = count
        self.SignupTime = signup
        self.DebitPerDay = debit
        self.BookList = books
        self.AvgScore = avgScore
        self.ScoreList = []
        self.Processed = False
        self.BooksSent = []
        
        self.BookList = {k: v for k, v in reversed(sorted(self.BookList.items(), key=lambda item: item[1]))} #ordem descendente

        for x in range(int(ScoreCalcDivisions)):
            self.ScoreList.append(self.calcScore(TotalDays-(x*(TotalDays/ScoreCalcDivisions))))


        #print("Id: " + str(id) + ", score: " + str(self.ScoreList) + ", books: " + str(books))

    def chooseBooks(self, time): #time is the day of the signup start (day)

        global ScannedBooks

        nBooks = self.DebitPerDay * (TotalDays - (time + self.SignupTime))
        orderedKeysList = self.BookList.keys()
        nSent = 0
        currBook = 0

        for key in orderedKeysList:
            if not ScannedBooks[key]:
                self.BooksSent.append(key)
                nSent += 1
            if nSent >= nBooks:
                break
            
    def getBooksSent(self):
        return self.BooksSent

    def calcScore(self, time):

        global TotalDays

        if self.Processed:
            return -1000
        else:
            return min(int(self.AvgScore) * int(self.DebitPerDay) * ((int(TotalDays) - int(time)) - int(self.SignupTime)), self.AvgScore * self.BookCount)

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
            for i in range(TotalLibraries):
                [count, signup, debit] = [int(el) for el in f.readline().split()]
                books = {}

                scoreSum = 0

                bookLine = [int(el) for el in f.readline().split()]
                for book in bookLine:
                    books.update({book: BookScores[book]})
                    scoreSum += BookScores[book]
                scoreAvg = scoreSum / len(books)

                lib = Library(len(self.Libraries), count, signup, debit, books, scoreAvg)
                self.Libraries.append(lib)
            
    def write(self, LibList):
        path = 'output/' + self.filename
        with open(path, 'w') as f:
            f.write(str(len(LibList)) + '\n')
            for i in range(len(LibList)):
                BookList = self.Libraries[LibList[i]].getBooksSent()
                f.write(str(LibList[i]) + " " + str(len(BookList)) + '\n')
                for b in BookList:
                    f.write(str(b) + " ")
                f.write('\n')

        return 0

    def solve(self):

        global TotalBooks, TotalLibraries, TotalDays, ScoreCalcDivisions
        global TopLibraries, BookScores, ScannedBooks, LibList

        def selectBestLib(dic, time):
            bestLib = -1
            bestScore = -1
            for i in range(len(self.Libraries)):
                lib = self.Libraries[i]
                score = lib.calcScore(time)
                if score > bestScore:
                    bestScore = score
                    bestLib = i
            
            if bestScore > -1:
                self.Libraries[bestLib].process()
                return self.Libraries[bestLib]

            return None
            
        DaysPerDiv = TotalDays # equals to 1 division (test run)

        ScoreCalcDivisions = TotalDays / DaysPerDiv

        dicts = []

        for i in range(int(ScoreCalcDivisions)):
            time = i * DaysPerDiv
            divDict = {}
            for ind in range(len(self.Libraries)):
                if len(divDict) < 2 * ScoreCalcDivisions:
                    divDict[ind] = self.Libraries[ind]
                    divDict = {k: v for k, v in sorted(divDict.items(), key=lambda item: item[i])}
                else:
                    avg = self.Libraries[ind].calcScore(time)
                    if divDict.get(list(divDict.keys())[-1]).calcScore(time) < avg:
                        divDict.popitem()
                        divDict[ind] = self.Libraries[ind]
                        divDict = {k: v for k, v in sorted(divDict.items(), key=lambda item: item[i])}
            dicts.append(divDict)
            
        day = 0    
        while day < TotalDays:
            index = round(day // DaysPerDiv) * DaysPerDiv
            lib = selectBestLib(dicts[index], time)
            if lib is None:
                break
            LibList.append(lib.id)
            lib.chooseBooks(day)
            if len(lib.BooksSent) == 0:
                LibList.remove(lib.id)
            day += lib.getSignup()
                

        return 0
    
    def solve_b(self):
        libraryScores = {}

        for i in range(len(self.Libraries)):
            score = 1000 - self.Libraries[i].SignupTime

            for book in self.Libraries[i].BookList:
                if ScannedBooks.count(book) == 1:
                    score -= 1
                else:
                    ScannedBooks.append(book)

            libraryScores[i] = score

        ret = sorted(libraryScores.values())
        ret.reverse()

        return ret

    def solve_d(self):
        libraryNBooks = {}

        for i in range(len(self.Libraries)):
            bookCount = self.Libraries[i].BookCount

            for book in self.Libraries[i].BookList:
                if ScannedBooks.count(book) == 1:
                    bookCount -= 1
                else:
                    ScannedBooks.append(book)
        
            libraryNBooks[i] = bookCount

        ret = sorted(libraryNBooks.values())
        ret.reverse()

        return ret


def main():
    solver = Solver(name)

    print("inputing")
    solver.get_input()

    print("solving")
    solver.solve()

    print("writing")
    solver.write(LibList)


if __name__ == '__main__':
    main()
