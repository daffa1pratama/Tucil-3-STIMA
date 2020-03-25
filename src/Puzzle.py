import random
import copy
import time

# Kelas Puzzle15 Solver
class Puzzle15 :
    # Constructor
    def __init__(self) :
        self.matrix = [[-999 for i in range(4)] for i in range(4)]
        self.inversion = []
        self.container = {}
        self.queue = []
        self.depth = 0
        self.path = ""
    
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
    
    def evalPath(self) :
        currPath = self.path.pop(0)
        if (currPath == 'w') :
            self.move([self.matrix, 'up'])
            print("Up")
        elif (currPath == 's') :
            self.move([self.matrix, 'down'])
            print("Down")
        elif (currPath == 'a') :
            self.move([self.matrix, 'left'])
            print("Left")
        elif (currPath == 'd') :
            self.move([self.matrix, 'right'])
            print("Right")
        else :
            pass

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
        # print("Depth : " + str(self.depth))
        
        if (tuple(self.flattenMatrix(up[0])) not in self.container) :
            posUp = 16 - self.countPosition(up[0]) + self.depth
            self.container[tuple(self.flattenMatrix(up[0]))] = 'up'
            self.queue.append([posUp, self.depth, self.path + 'w ', self.flattenMatrix(up[0])])

        if (tuple(self.flattenMatrix(down[0])) not in self.container) :
            posDown = 16 - self.countPosition(down[0]) + self.depth
            self.container[tuple(self.flattenMatrix(down[0]))] = 'down'
            self.queue.append([posDown, self.depth, self.path + 's ', self.flattenMatrix(down[0])])
            
        if (tuple(self.flattenMatrix(left[0])) not in self.container) :
            posLeft = 16 - self.countPosition(left[0]) + self.depth
            self.container[tuple(self.flattenMatrix(left[0]))] = 'left'
            self.queue.append([posLeft, self.depth, self.path + 'a ', self.flattenMatrix(left[0])])

        if (tuple(self.flattenMatrix(right[0])) not in self.container) :
            posRight = 16 - self.countPosition(right[0]) + self.depth
            self.container[tuple(self.flattenMatrix(right[0]))] = 'right'
            self.queue.append([posRight, self.depth, self.path + 'd ', self.flattenMatrix(right[0])])
            
        self.queue.sort()
        pop = self.queue.pop(0)
        self.matrix = self.unflattenMatrix(pop[3])
        self.depth = pop[1]
        self.path = pop[2]

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

def main() :
    print("=== 15 PUZZLE SOLVER ===")
    dir = input("Masukkan nama file (diakhiri .txt) : ")
    try :
        f = FileHandler()
        puzzle = f.readFileMatrix("../doc/" + dir)
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
            temp = copy.deepcopy(puzzle)
            puzzle.container[tuple(puzzle.flattenMatrix(puzzle.matrix))] = 'none'
            step = 0
            while (not puzzle.isSolution()) :
                puzzle.solve()
                step += 1

            temp.path = puzzle.path.split(" ")
            while (len(temp.path) != 1) :
                temp.evalPath()
                temp.printMatrix()
                print("=================")
            print("=== END SOLVE ===")
            
        else :
            puzzle.printInverse()
            print("puzzle is ... NOT SOLVEABLE")
            print("=================")
        end = time.time()
        print("Elapsed time : " + str(end-start) + " seconds")
    except :
        print("Error expected : File not found")

if __name__ == "__main__":
    main()
