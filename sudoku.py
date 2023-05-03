import itertools
from copy import deepcopy
import math

def checkSudoku(sudoku: list[int]) -> bool:
    #check for null sudoku
    if not sudoku:
        return False

    for row in sudoku:
        for item in row:
            if item == 0:
                return False

    for row in sudoku:
        if (len(set(row)) < len(row)):
            return False

    for index, _ in enumerate(sudoku):
        s = [j[index] for j in sudoku]
        if len(set(s)) < len(row):
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            s = [sudoku[x][y] for x in range(i, i+3) for y in range(j, j+3)]
            if len(set(s)) != 9:
                return False
    
    return True

def replaceSolution(sudoku: list[list[int]], solution: list[list[int]]):
    new_sudoku = deepcopy(sudoku)
    for rowI, row in enumerate(new_sudoku):
        k = 0
        for columnI, item in enumerate(row):
            if item == 0:
                new_sudoku[rowI][columnI] = solution[rowI][k]
                k+=1
    return new_sudoku


def findAllPermutations(sudoku: list[list[int]]):
    reference = list(range(1, 10))
    remaining = []
    for row in sudoku:
        remaining.append([x for x in reference if x not in row])
    perms = [list(map(list, itertools.permutations(subl))) for subl in remaining]
    return list(itertools.product(*perms))


def bruteForce(sudoku: list[list[str]], tries = 1000) -> list[list[str]]:
    t = findAllPermutations(sudoku)
    i = 0
    n = 0
    new_sudoku = []
    while not checkSudoku(new_sudoku) and i != len(t):
        new_sudoku = replaceSolution(sudoku, t[i])
        i+=1
        #para que no toque modificar el código
        n+=1
        if n == tries:
            raise RecursionError("Too many tries for brute force algorithm")
        


    if i == len(t):
        return None
    else:
        return new_sudoku


def findAllPermutationsGenerator(sudoku: list[list[int]]):
    reference = list(range(1, 10))
    remaining = []
    for row in sudoku:
        remaining.append([x for x in reference if x not in row])
    perms = [list(map(list, itertools.permutations(subl))) for subl in remaining]
    for t in itertools.product(*perms):
        yield t


def bruteForceGenerator(sudoku: list[list[str]], tries = 1000) -> list[list[str]]:
    s = []
    n = 0
    for sol in findAllPermutationsGenerator(sudoku):
        s = replaceSolution(sudoku, sol)
        if checkSudoku(s):
            return s
        n+=1
        if n == tries:
            raise RecursionError("Too many tries for brute force algorithm")
    
# solve with heuristic

def mrv_domains(sudoku: list[list[str]]): 
    domains = {}
    # Check for empty cells and asign them in the dict the initial posibilities [1-9]
    for i, _ in enumerate(sudoku):
        for j, _ in enumerate(sudoku):
            if sudoku[i][j] == 0:
                domains[i, j] = set(range(1, 10))
    

    sqrt_n = int(math.sqrt(len(sudoku))) # square len

    #traverse the sudoku 
    for i, _ in enumerate(sudoku):
        for j, _ in enumerate(sudoku):
            #get the square posibilities
            qs = range(sqrt_n) 
            block_i = int(i / sqrt_n)
            block_i_set = {block_i * sqrt_n + q for q in qs}
            block_j = int(j / sqrt_n)
            block_j_set = {block_j * sqrt_n + q for q in qs}
            #traverse the posibilites per cell
            for k in domains.keys():
                #discard the non posible solution, in a row, column or square
                if k[0] == i or k[1] == j or (k[0] in block_i_set and k[1] in block_j_set):
                    domains[k].discard(sudoku[i][j])


    min_remaining_val = None;
    # Check for the cell with min posibilities
    for domain in domains.values():
        if min_remaining_val is not None:
            min_remaining_val = min(min_remaining_val, len(domain))
        else:
            min_remaining_val = len(domain)

    if min_remaining_val == 0:
        return None


    # get the min values for the cells that are empty
    min_domains = {k: domains[k]
                   for k in domains.keys()
                   if len(domains[k]) == min_remaining_val}

    return min_domains


def selector(sudoku: list[list[str]]):
    min_domains = mrv_domains(sudoku)

    if not min_domains:
        return None, None, None
    
    cell = min_domains.popitem()
    # row index, column index, possibilities
    return cell[0][0], cell[0][1], cell[1]



def backtracking(sudoku: list[list[str]]):
    if checkSudoku(sudoku):
        return sudoku
    
    i, j, domain = selector(sudoku)

    if domain is None:
        return None

    for val in domain:
        sudoku[i][j] = val
        result = backtracking(sudoku)
        if result:
            return result
        sudoku[i][j] = 0

def solve(sudoku: list[list[int]]) -> list[list[str]]:
    return backtracking(sudoku)