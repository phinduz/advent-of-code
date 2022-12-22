import os
from typing import List
import parse


def read_file(filePath) -> List[str]:
    """ Returns all the lines from a file as a list """
    with open(filePath, 'r') as file:    
        lines: List[str] = file.read().strip().split('\n')
        file.close()
    return lines

def problem_1(lines, window=4):

    start_token = 0

    line = lines[0]
    for i in range(len(line)-window):
        if len(set(line[i:i+window])) == window:
            start_token = i + window
            break
    print(start_token)
    
def problem_2(lines):
    problem_1(lines, 14)


if __name__ == "__main__":
    path:str = os.path.dirname(os.path.abspath(__file__))
    fileName:str = 'input/dec-6.txt'
    filePath:str = os.path.join(path, fileName)
    lines: List[str] = read_file(filePath)

    problem_1(lines)
    problem_2(lines)
