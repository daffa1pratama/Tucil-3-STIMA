import random
import copy

class Puzzle15 :
    def __init__(self) :
        self.matrix = [[-999 for i in range(4)] for i in range(4)]
        self.status = "none"
        self.container = []
    
    def getMatrix(self) :
        return self.matrix
    
    def getStatus(self) :
        return self.status

    def setStatus(self, status) :
        self.status = status

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
        
    def countInverse(self) :
        count = 0
        _matrix = [-999 for i in range(16)]
        x = 0
        for i in range(4) :
            for j in range(4) :
                _matrix[x] = self.matrix[i][j]
                x += 1

        for i in range(16) :
            for j in range(i+1, 16) :
                if (_matrix[i] > _matrix[j]) :
                    count += 1
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
        if (self.countPosition() != 16) :
            return False
        return True
    
    def countPosition(self) :
        count = 0;
        ctr = 1;
        for i in range(4) :
            for j in range(4) :
                if (self.matrix[i][j] == ctr) :
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
                        print(str(0) + " ", end=" ")
                    else :
                        print(self.matrix[i][j], end=" ")
            print()
    
    def isMoveValid(self) :
        if (self.getStatus() == "up") :
            if (self.rowBlankSpace() == 1) :
                return False
        elif (self.getStatus() == "down") :
            if (self.rowBlankSpace() == 4) :
                return False
        elif (self.getStatus() == "left") :
            if (self.colBlankSpace() == 1) :
                return False
        elif (self.getStatus() == "right") :
            if (self.colBlankSpace() == 4) :
                return False
        return True
        

    def move(self) :
        if (self.isMoveValid()) :
            i = self.rowBlankSpace() - 1
            j = self.colBlankSpace() - 1
            if (self.status == "up") :
                self.matrix[i][j] = self.matrix[i-1][j]
                self.matrix[i-1][j] = 16
            elif (self.status == "down") :
                self.matrix[i][j] = self.matrix[i+1][j]
                self.matrix[i+1][j] = 16
            elif (self.status == "left") :
                self.matrix[i][j] = self.matrix[i][j-1]
                self.matrix[i][j-1] = 16
            elif (self.status == "right") :
                self.matrix[i][j] = self.matrix[i][j+1]
                self.matrix[i][j+1] = 16
    
    def matrixCopy(self, status) :
        res = copy.deepcopy(self)
        res.setStatus(status)
        return res

    def isMatrixElm(self, matrix) :
        for i in range(len(self.container)) :
            if (matrix == self.container[i]) :
                return True
        return False

    def solve(self) :
        if (self.getStatus() == "none") :
            self.container += [self.matrix]

        up = self.matrixCopy("up")
        down = self.matrixCopy("down")
        left = self.matrixCopy("left")
        right = self.matrixCopy("right")

        countPosUp = 999
        countPosDown = 999
        countPosLeft = 999
        countPosRight = 999
        
        if (up.isMoveValid()) :
            up.move()
            print("UP")
            up.printMatrix()
            if not self.isMatrixElm(up.matrix) :
                countPosUp = 15 - up.countPosition()
            self.container += [up.matrix]
        if (down.isMoveValid()) :
            down.move()
            print("DOWN")
            down.printMatrix()
            if not self.isMatrixElm(down.matrix) :
                countPosDown = 15 - down.countPosition()
            self.container += [down.matrix]
        if (left.isMoveValid()) :
            left.move()
            print("LEFT")
            left.printMatrix()
            if not self.isMatrixElm(left.matrix) :
                countPosLeft = 15 - left.countPosition()
            self.container += [left.matrix]
        if (right.isMoveValid()) :
            right.move()
            print("RIGHT")
            right.printMatrix()
            if not self.isMatrixElm(right.matrix) :
                countPosRight = 15 - right.countPosition()
            self.container += [right.matrix]

        posContainer = [countPosUp, countPosDown, countPosLeft, countPosRight]
        print(posContainer)
        minPos = min(posContainer)
        print(minPos)
        i = 0
        found = False
        while (i < 4 and not found) :
            if (posContainer[i] == minPos) :
                found = True
            else :
                i += 1
        print(i)
        if i == 0 :
            self.matrix = copy.deepcopy(up.matrix)
            self.status = up.status
        elif i == 1 : 
            self.matrix = copy.deepcopy(down.matrix)
            self.status = down.status
        elif i == 2 :
            self.matrix = copy.deepcopy(left.matrix)
            self.status = left.status
        else :
            self.matrix = copy.deepcopy(right.matrix)
            self.status = right.status

        # print(self.container)
        # print(self.matrix)
        print(self.status)
        self.printMatrix()

class FileHandler :
    def __init__(self):
        pass

    def writeFileMatrix(self, puzzle, fileName) :
        f = open(fileName, "w")
        temp = ""
        for i in range(4) :
            for j in range(4) :
                if (puzzle.getMatrix()[i][j] < 10) :
                    temp += str(puzzle.getMatrix()[i][j]) + "  "
                else :
                    if (puzzle.getMatrix()[i][j] == 16) :
                        temp += str(0) + "  "
                    else :
                        temp += str(puzzle.getMatrix()[i][j]) + " "
            temp += "\n"
        if (puzzle.isSolveable()) :
            temp += "\nSOLVEABLE\n"
            # puzzle.solve()
        else :
            temp += "\nUNSOLVABLE\n"
        f.write(temp)
        f.close()

def main() :
    
    bnb = Puzzle15()
    bnb.manualInput()
    # bnb.randomInput()
    bnb.printMatrix()

    f = FileHandler()
    f.writeFileMatrix(bnb, "matrix.txt")

    if (bnb.isSolveable()) :
        print("SOLVEABLE")
        while (not bnb.isSolution()) :
        # for i in range(3) :
            bnb.solve()
            print("====================")
        bnb.printMatrix()
    else :
        print("UNSOLVEABLE")

if __name__ == "__main__":
    main()