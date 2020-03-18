import random


def countInverse(matrix) :
    count = 0
    for i in range(16) :
        for j in range(i+1, 16) :
            if (matrix[i] > matrix[j]) :
                count += 1
    return count

def findBlankSpace(matrix) :
    for i in range(16) :
        if (matrix[i] == 0) :
            break
    i += 1
    # print(i)
    if (i % 2 == 0) :
        return 1
    return 0

def isSolveable(matrix) :
    if ((countInverse(matrix) + findBlankSpace(matrix)) % 2 == 0) :
        return True
    return False

def isSolution(matrix) :
    for i in range(16) :
        if (i != matrix[i+1]) :
            return False
    return True

def main() :
    matrix = [-999 for i in range(16)]
    print(matrix)

    for i in range(16) :
        value = random.randint(0, 15)
        while (value in matrix) :
            value = random.randint(0, 16)
        matrix[i] = value
        # print(value)
    print(matrix)

    print(countInverse(matrix))

    print(findBlankSpace(matrix))

    if (isSolveable(matrix)) :
        print("SOLVABLE")
        while (!isSolution(matrix)) :
             
    else :
        print("UNSOLVEABLE")
    


if __name__ == "__main__":
    main()