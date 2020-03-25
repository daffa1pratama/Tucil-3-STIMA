import Puzzle
import time

def main() :
    f = FileHandler()
    # f.writeFileMatrix(bnb, "../doc/matrix.txt")
    puzzle = f.readFileMatrix("../doc/matrix.txt")
    print("===== BOARD =====")
    puzzle.printMatrix()
    print("=================")
    print("=== KURANG(i) ===")
    start = time.time()
    if (puzzle.isSolveable()) :
        puzzle.printInverse()
        print("puzzle is ... SOLVEABLE")
        print("=================")
        puzzle.container.append(puzzle.flattenMatrix(puzzle.matrix))
        # while (not puzzle.isSolution()) :
        for i in range(5) :
            puzzle.solve()
    else :
        puzzle.printInverse()
        print("puzzle is ... UNSOLVEABLE")
        print("=================")
    end = time.time()
    print("Time elapsed : " + str(end-start))
    

if __name__ == "__main__":
    main()