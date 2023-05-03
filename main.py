import reader
import sudoku
import sys
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.5f} seconds to execute")
        return result
    return wrapper


@time_it
def bruteForceTest(s, generator = False):
    if generator:
        sol = sudoku.bruteForceGenerator(s)
    else:   
        sol = sudoku.bruteForce(s)
    if sol is None:
        print("No sol found")
    else:
        print("Brute force solution:")
        reader.printSudoku(sol)


@time_it
def heuristicTest(s):
    solution = sudoku.solve(s)
    if solution is None:
        print("No sol found")
    else:
        print("Heuristic Solution:")
        reader.printSudoku(solution)

def main():
    generator = True
    if len(sys.argv) > 3 or len(sys.argv) == 1:
        print(f"Uso: python {sys.argv[0]} [filaname] [(optional) Generator?]")
        exit(1)
    if len(sys.argv) == 2:
        generator = False
    
    s = reader.readSudoku(sys.argv[1])
    print("="*30)
    print("Sudoku original: ")
    reader.printSudoku(s)
    print("="*30)
    try:
        bruteForceTest(s, generator)
    except RecursionError as e:
        print("Out of tries for brute force algorithm")

    print("="*30)
    heuristicTest(s)

    

if __name__ == '__main__':
    main()