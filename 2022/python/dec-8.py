import os
from typing import List
import parse
import numpy as np
import matplotlib.pyplot as plt



def read_file(filePath) -> List[str]:
    """ Returns all the lines from a file as a list """
    with open(filePath, 'r') as file:    
        lines: List[str] = file.read().strip().split('\n')
        file.close()
    return lines

def problem_1(lines):
    rows = len(lines)
    columns = len(lines[0])

    matrix = np.zeros(shape=(rows, columns))
    
    for idx in range(rows):
        for i,digit in enumerate(lines[idx]):
            matrix[idx][i] = digit
    
    visible_set = set()
   
    for r in range(rows):
        for c in range(0,columns-1):
            if (r,c) in visible_set:
                continue
            elif all(matrix[r,c] > matrix[r,:c]):
                visible_set.add((r,c))

    for r in range(rows):
        for c in range(columns-1,0,-1):
            if (r,c) in visible_set:
                continue
            elif all(matrix[r,c] > matrix[r,c+1:]):
                visible_set.add((r,c))
         
    for r in range(0,rows-1):
        for c in range(columns):
            if (r,c) in visible_set:
                continue
            elif all(matrix[r,c] > matrix[:r,c]):
                visible_set.add((r,c))

    for r in range(rows-1,0,-1):
        for c in range(columns):
            if (r,c) in visible_set:
                continue
            elif all(matrix[r,c] > matrix[r+1:,c]):
                visible_set.add((r,c))

    print(len(visible_set))
    

    debug = False
    if debug:
        matrix_visible = np.zeros(shape=(rows, columns))
        for coordinate in visible_set:
            matrix_visible[coordinate[0], coordinate[1]] = -1
        plt.imshow(matrix_visible, interpolation='nearest')
        plt.colorbar()
        plt.show()

    
def problem_2(lines):
    rows = len(lines)
    columns = len(lines[0])

    matrix = np.zeros(shape=(rows, columns))
    
    for idx in range(rows):
        for i,digit in enumerate(lines[idx]):
            matrix[idx][i] = digit
    
    matrix_score = np.zeros(shape=(rows, columns))
   
    for r in range(rows):
        for c in range(0,columns-1):

            left = np.flip(matrix[r,c] > matrix[r,:c])
            right = (matrix[r,c] > matrix[r,c+1:])
            up = np.flip(matrix[r,c] > matrix[:r,c])
            down = (matrix[r,c] > matrix[r+1:,c])

            count_left = 0
            for i in left:
                count_left = count_left + 1
                if i:
                    continue
                else:
                    break
            count_right = 0
            for i in right:
                count_right = count_right + 1
                if i:
                    continue
                else:
                    break
            count_up = 0
            for i in up:
                count_up = count_up + 1
                if i:
                    continue
                else:
                    break

            count_down = 0
            for i in down:
                count_down = count_down + 1
                if i:
                    continue
                else:
                    break

            matrix_score[r,c] = count_left*count_right*count_up*count_down

    print(int(matrix_score.max()))
    
    debug = False
    if debug:
        plt.imshow(matrix_score, interpolation='nearest')
        plt.colorbar()
        plt.show()


if __name__ == "__main__":
    path:str = os.path.dirname(os.path.abspath(__file__))
    fileName:str = 'input/dec-8.txt'
    filePath:str = os.path.join(path, fileName)
    lines: List[str] = read_file(filePath)

    problem_1(lines)
    problem_2(lines)
