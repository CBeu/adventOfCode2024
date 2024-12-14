import re
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from reader import adventReader

class ceresSearch:
    def __init__(self, filepath):
        self.reader = adventReader(filepath)
    
    def loadMatrix(self):
        self.matrix = []
        for line in self.reader.read():
            self.matrix.append(list(line.strip())) 
        return self.matrix
    
    def searchMatrixFromPos(self, x, y):
        # allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words
        matrixHeight = (len(self.matrix))
        matrixWidth = (len(self.matrix[0]))
        horizontal = self.isMatch(self.retrieveHorizontal(x, y, matrixWidth, matrixHeight),'XMAS')
        vertical = self.isMatch(self.retrieveVerticalDown(x, y, matrixWidth, matrixHeight),'XMAS')
        diagonalDownLeft = self.isMatch(self.retrieveDiagonalDownLeft(x, y, matrixWidth, matrixHeight),'XMAS')
        diagonalDownRight = self.isMatch(self.retrieveDiagonalDownRight(x, y, matrixWidth, matrixHeight),'XMAS')
        return sum([horizontal, vertical, diagonalDownLeft, diagonalDownRight])

    def isMatch(self, word, key):
        if word == key or word == key[::-1]:
            return 1
        return 0

    def retrieveHorizontal(self, x, y, xMax, yMax):
        if x + 3 >= xMax:
            return 'Out of bounds'
        return ''.join(self.matrix[y][x:x+4])
    
    def retrieveVerticalDown(self, x, y, xMax, yMax):
        if y + 3 >= yMax:
            return 'Out of bounds'
        return ''.join([self.matrix[y+i][x] for i in range(4)])
    
    def retrieveDiagonalDownLeft(self, x, y, xMax, yMax):
        if y + 3 >= yMax or x - 3 < 0:
            return 'Out of bounds'
        return ''.join([self.matrix[y+i][x-i] for i in range(4)])
    
    def retrieveDiagonalDownRight(self, x, y, xMax, yMax):
        if y + 3 >= yMax or x + 3 >= xMax:
            return 'Out of bounds'
        return ''.join([self.matrix[y+i][x+i] for i in range(4)])

sample = ceresSearch("day4/input.txt")
sample.loadMatrix()
# go through each position in the matrix and search for the word 'XMAS'
count = 0
for y in range(len(sample.matrix)):
    for x in range(len(sample.matrix[y])):
        count +=(sample.searchMatrixFromPos(x, y))
print(count)