import random

def countInverse(matrix) :
    count = 0
    _matrix = [-999 for i in range(16)]
    x = 0
    for i in range(4) :
        for j in range(4) :
            _matrix[x] = matrix[i][j]
            x += 1

    for i in range(16) :
        for j in range(i+1, 16) :
            if (_matrix[i] > _matrix[j]) :
                count += 1
    return count

def findBlankSpace(matrix) :
    found = False
    i = 0
    while not found :
        j = 0
        while (j < 4 and not found) :
            if (matrix[i][j] == 16) :
                found = True
            j += 1
        i += 1
    if ((i+j) % 2 == 0):
        return 0
    return 1

def isSolveable(matrix) :
    if ((countInverse(matrix) + findBlankSpace(matrix)) % 2 == 0) :
        return True
    return False

def isSolution(matrix) :
    

def manualInput(matrix) :
    for i in range(4) :
        for j in range(4) :
            matrix[i][j] = int(input())

def randomInput(matrix) :
    for i in range(4) :
        for j in range(4) :  
            value = random.randint(1, 16)
            while any (value in x for x in matrix) :
                value = random.randint(1, 16)
            matrix[i][j] = value
def printMatrix(matrix) :
    for i in range(4) :
        for j in range(4) :
            if (matrix[i][j] < 10) :
                print(str(matrix[i][j]) + " ", end=" ")
            else :
                if (matrix[i][j] == 16) :
                    print(0, end=" ")
                else :
                    print(matrix[i][j], end=" ")
        print()

def main() :
    matrix = [[-999 for i in range(4)] for i in range(4)]

    # manualInput(matrix)
    randomInput(matrix)

    printMatrix(matrix)

    if (isSolveable(matrix)) :
        print("SOLVABLE")
        # while (not isSolution(matrix)) :
    else :
        print("UNSOLVEABLE")
    


if __name__ == "__main__":
    main()