def readSudoku(filename: str) -> list:
    s = []
    with open(filename, "r") as file:
        for line in file:
            s.append([int(c) for c in line.replace("X", "0").removesuffix("\n")])
    return s

def printSudoku(sudoku: list):
    for i, row in enumerate(sudoku):
        for j, item in enumerate(row):
            print(f" {item if item != 0 else ' '} ", end="")
            if j in [2, 5]:
                print("|" ,end="")
        print()
        if i in [2,5]:
            print("---------|---------|---------")
        
