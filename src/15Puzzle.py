import random
import copy
import time
from queue import Queue

class Puzzle15 :
    def __init__(self) :
        self.matrix = [[-999 for i in range(4)] for i in range(4)]
        self.inversion = []
        self.container = []
        self.queue = []
        self.depth = 0

    def manualInput(self) :
        for i in range(4) :
            for j in range(4) :
                self.matrix[i][j] = int(input())

    def randomInput(self) :
        for i in range(4) :
            for j in range(4) :  
                value = random.randint(1, 16)
                while any (value in x for x in self.matrix) :
                    value = random.randint(1, 16)
                self.matrix[i][j] = value
    
    def flattenMatrix(self, matrix) :
        _matrix = [-999 for i in range(16)]
        x = 0
        for i in range(4) :
            for j in range(4) :
                _matrix[x] = matrix[i][j]
                x += 1
        return _matrix

    def unflattenMatrix(self, matrix) :
        _matrix = [[-999 for i in range(4)] for i in range(4)]
        x = 0
        for i in range(4) :
            for j in range(4) :
                _matrix[i][j] = matrix[x]
                x += 1
        return _matrix 
        
    def countInverse(self) :
        count = 0
        _matrix = self.flattenMatrix(self.matrix)
        for i in range(16) :
            inverseTile = 0
            for j in range(i+1, 16) :
                if (_matrix[i] > _matrix[j]) :
                    inverseTile += 1
                    count += 1
            self.inversion.append([_matrix[i], inverseTile])
        inversion = self.inversion
        inversion.sort(key = lambda inversion: inversion[0])
        return count
    
    def rowBlankSpace(self) :
        found = False
        i = 0
        while not found :
            j = 0
            while (j < 4 and not found) :
                if (self.matrix[i][j] == 16) :
                    found = True
                j += 1
            i += 1
        return i
    
    def colBlankSpace(self) :
        found = False
        i = 0
        while not found :
            j = 0
            while (j < 4 and not found) :
                if (self.matrix[i][j] == 16) :
                    found = True
                j += 1
            i += 1
        return j

    def findBlankSpace(self) :
        i = self.rowBlankSpace()
        j = self.colBlankSpace()
        if ((i+j) % 2 == 0):
            return 0
        return 1

    def isSolveable(self) :
        if ((self.countInverse() + self.findBlankSpace()) % 2 == 0) :
            return True
        return False

    def isSolution(self) :
        if (self.countPosition(self.matrix) != 16) :
            return False
        return True
    
    def countPosition(self, matrix) :
        count = 0;
        ctr = 1;
        for i in range(4) :
            for j in range(4) :
                if (matrix[i][j] == ctr) :
                    count += 1
                ctr += 1
        return count

    def printMatrix(self) :
        for i in range(4) :
            for j in range(4) :
                if (self.matrix[i][j] < 10) :
                    print(str(self.matrix[i][j]) + " ", end=" ")
                else :
                    if (self.matrix[i][j] == 16) :
                        print("X ", end=" ")
                    else :
                        print(self.matrix[i][j], end=" ")
            print()

    def printInverse(self) :
        for i in range(16) :
            print(str(i+1) + " : " + str(self.inversion[i][1]))
        inverse = self.countInverse()
        print("Total : " + str(inverse))
        print("sigma KURANG(i) + X = " + str(inverse + self.findBlankSpace()))

    
    def isMoveValid(self, matrix) :
        if (matrix[1] == 'up') :
            if (self.rowBlankSpace() == 1) :
                return False
        elif (matrix[1] == 'down') :
            if (self.rowBlankSpace() == 4) :
                return False
        elif (matrix[1] == 'left') :
            if (self.colBlankSpace() == 1) :
                return False
        elif (matrix[1] == 'right') :
            if (self.colBlankSpace() == 4) :
                return False
        return True
         

    def move(self, matrix) :
        i = self.rowBlankSpace() - 1
        j = self.colBlankSpace() - 1
        if (self.isMoveValid(matrix)) :
            if (matrix[1] == "up") :
                matrix[0][i][j] = matrix[0][i-1][j]
                matrix[0][i-1][j] = 16
            elif (matrix[1] == "down") :
                matrix[0][i][j] = matrix[0][i+1][j]
                matrix[0][i+1][j] = 16
            elif (matrix[1] == "left") :
                matrix[0][i][j] = matrix[0][i][j-1]
                matrix[0][i][j-1] = 16
            elif (matrix[1] == "right") :
                matrix[0][i][j] = matrix[0][i][j+1]
                matrix[0][i][j+1] = 16
        return matrix

    def solve(self) :
        posUp = 999
        posDown = 999
        posLeft = 999
        posRight = 999

        up = [copy.deepcopy(self.matrix), 'up']
        down = [copy.deepcopy(self.matrix), 'down']
        left = [copy.deepcopy(self.matrix), 'left']
        right = [copy.deepcopy(self.matrix), 'right']

        self.move(up)
        self.move(down)
        self.move(left)
        self.move(right)

        self.depth += 1
        print("Depth : " + str(self.depth))

        if (self.flattenMatrix(up[0]) not in self.container) :
            posUp = 16 - self.countPosition(up[0]) + self.depth
            self.container.append(self.flattenMatrix(up[0]))
            self.queue.append([posUp, self.depth, self.flattenMatrix(up[0])])

        if (self.flattenMatrix(down[0]) not in self.container) :
            posDown = 16 - self.countPosition(down[0]) + self.depth
            self.container.append(self.flattenMatrix(down[0]))
            self.queue.append([posDown, self.depth, self.flattenMatrix(down[0])])
            
        if (self.flattenMatrix(left[0]) not in self.container) :
            posLeft = 16 - self.countPosition(left[0]) + self.depth
            self.container.append(self.flattenMatrix(left[0]))
            self.queue.append([posLeft, self.depth, self.flattenMatrix(left[0])])

        if (self.flattenMatrix(right[0]) not in self.container) :
            posRight = 16 - self.countPosition(right[0]) + self.depth
            self.container.append(self.flattenMatrix(right[0]))
            self.queue.append([posRight, self.depth, self.flattenMatrix(right[0])])

        self.queue.sort()
        pop = self.queue.pop(0)
        self.matrix = self.unflattenMatrix(pop[2])
        self.depth = pop[1]
        # print(self.matrix)
        # print(self.matrix)
        self.printMatrix()

class FileHandler :
    def __init__(self):
        pass

    def readFileMatrix(self, fileName) :
        f = open(fileName, "r")
        temp = f.readlines()
        matrix = []
        for item in temp:
            a = item.strip("\n").split(" ")
            matrix.append(a)
        for i in range(4) :
            for j in range(4) :
                if matrix[i][j] == 'X' :
                    matrix[i][j] = 16
                else :
                    matrix[i][j] = int(matrix[i][j])
        puzzle = Puzzle15()
        puzzle.matrix = matrix
        return puzzle

    def writeFileMatrix(self, puzzle, fileName) :
        f = open(fileName, "w")
        temp = ""
        for i in range(4) :
            for j in range(4) :
                if (puzzle.matrix[i][j] == 16) :
                    temp += "X  "
                else :
                    temp += str(puzzle.matrix[i][j])
            temp += "\n"
        if (puzzle.isSolveable()) :
            temp += "\nSOLVEABLE\n"
        else :
            temp += "\nUNSOLVABLE\n"
        f.write(temp)
        f.close()

def main() :

    f = FileHandler()
    # f.writeFileMatrix(bnb, "../doc/matrix.txt")
    puzzle = f.readFileMatrix("../doc/matrix.txt")
    start = time.time()
    print("===== BOARD =====")
    puzzle.printMatrix()
    print("=================")
    print("=== KURANG(i) ===")
    if (puzzle.isSolveable()) :
        puzzle.printInverse()
        print("puzzle is ... SOLVEABLE")
        print("=================")
        print("===== SOLVE =====")
        puzzle.container.append(puzzle.flattenMatrix(puzzle.matrix))
        step = 0
        while (not puzzle.isSolution()) :
        # for i in range(20) :
            puzzle.solve()
            step += 1
            print("=================")
        print(step)
        print("=== END SOLVE ===")
        
    else :
        puzzle.printInverse()
        print("puzzle is ... UNSOLVEABLE")
        print("=================")
    end = time.time()
    print("Elapsed time : " + str(end-start))

if __name__ == "__main__":
    main()