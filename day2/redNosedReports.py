import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from reader import adventReader

class redNosedReports:
    def __init__(self, filepath):
        self.reader = adventReader(filepath)
    
    def generateReportArrays(self):
        self.reportArrays = []
        for line in self.reader.read():
            self.reportArrays.append(line.split())
        return self.reportArrays
    
    def determineSafe(self):
        safeReports = 0
        validChange = [1, 2, 3]
        for array in self.reportArrays:
            increasingFlag = None
            isSafe = True
            for i in range(len(array) - 1):
                change = int(array[i+1]) - int(array[i])
                if abs(change) not in validChange:
                    isSafe = False
                    break
                if increasingFlag is None:
                    increasingFlag = change > 0
                elif (increasingFlag and change < 0) or (not increasingFlag and change > 0):
                    isSafe = False
                    break
            if isSafe:
                safeReports += 1
        print(safeReports)
    
    def determineSafeSecond(self):
        validChange = [1, 2, 3]
        updatedSafeCount = 0
        for array in self.reportArrays:
            increasingFlag = None
            unSafeChangeCount = 0
            for i in range(len(array) - 1):
                unSafeChange = False
                change = int(array[i+1]) - int(array[i])
                if abs(change) not in validChange:
                    unSafeChange = True
                if increasingFlag is None:
                    increasingFlag = change > 0
                elif (increasingFlag and change < 0) or (not increasingFlag and change > 0):
                    unSafeChange = True
                if unSafeChange:
                    unSafeChangeCount += 1
                if unSafeChangeCount > 1:
                    break
                
            if unSafeChangeCount <= 1:
                updatedSafeCount += 1
        print(updatedSafeCount)
                    



sample = redNosedReports("day2/input.txt")
sample.generateReportArrays()
sample.determineSafe()
sample.determineSafeSecond()
