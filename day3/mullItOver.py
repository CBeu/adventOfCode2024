import re
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from reader import adventReader

class mullItOver:
    def __init__(self, filepath):
        self.reader = adventReader(filepath)
        self.regexPattern = r"mul\(\d{1,3},\d{1,3}\)"
    
    def parseLines(self):
        self.matches = []
        for line in self.reader.read():
            matches = re.findall(self.regexPattern, line)
            self.matches.append(matches)
        self.matches = [match for sublist in self.matches for match in sublist]
        return self.matches

    def calculateMul(self, match):
        match = match[4:-1]
        match = match.split(",")
        return int(match[0]) * int(match[1])
    
    def calculateMatches(self):
        if len(self.matches) > 0:
            return sum([self.calculateMul(match) for match in self.matches])
        return 0
    
sample = mullItOver("day3/input.txt")
sample.parseLines()
print(sample.calculateMatches())