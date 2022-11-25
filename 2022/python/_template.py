import os
from typing import List

def read_file(filePath) -> List[str]:
    """ Returns all the lines from a file as a list """
    with open(filePath, 'r') as file:    
        lines: List[str] = file.read().strip().split('\n')
        file.close()
    return lines

def problem_1(lines):
    pass

def problem_2(lines):
    pass

if __name__ == "__main__":
    path:str = os.path.dirname(os.path.abspath(__file__))
    fileName:str = 'input/template.txt'
    filePath:str = os.path.join(path, fileName)
    lines: List[str] = read_file(filePath)

    problem_1(lines)
    problem_2(lines)