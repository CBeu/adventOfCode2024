import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from reader import adventReader

class historianHysteria:
    def __init__(self, filepath):
        self.reader = adventReader(filepath)
    
    def createLists(self):
        self.leftData = []
        self.rightData = []
        for line in self.reader.read():
            line = line.split()
            self.leftData.append(line[0])
            self.rightData.append(line[1])
        return self.leftData, self.rightData
    
    def sortLists(self):
        self.leftData.sort()
        self.rightData.sort()
        return self.leftData, self.rightData
    
    def findDistances(self):
        distances = 0
        for i in range(len(self.leftData)):
            distances += abs(int(self.leftData[i]) - int(self.rightData[i]))
        return distances
    
    def similarityScore(self):
        score = 0
        for i in range(len(self.leftData)):
            occurance = self.rightData.count(self.leftData[i])
            score += (int(self.leftData[i]) * occurance)
        return score

sample = historianHysteria("day1/input.txt")
sample.createLists()
sample.sortLists()
print(sample.findDistances())
print(sample.similarityScore())