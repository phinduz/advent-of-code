import os
from typing import List
import parse

def read_file(filePath) -> List[str]:
    """ Returns all the lines from a file as a list """
    with open(filePath, 'r') as file:    
        lines: List[str] = file.read().strip().split('\n')
        file.close()
    return lines

def problem_1(lines):
    pattern = parse.compile("{opponent} {player}")
    rounds = list()
    for line in lines:
        match = pattern.search(line)
        rounds.append((match.named.get("opponent"), match.named.get("player")))
    score = 0
    for round in rounds:
        if round[0] == 'A':
            if round[1] == 'X':
                score = score + 3 + 1
            elif round[1] == 'Y':
                score = score + 6 + 2
            elif round[1] == 'Z':
                score = score + 0 + 3
        elif round[0] == 'B':
            if round[1] == 'X':
                score = score + 0 + 1
            elif round[1] == 'Y':
                score = score + 3 + 2
            elif round[1] == 'Z':
                score = score + 6 + 3
        elif round[0] == 'C':
            if round[1] == 'X':
                score = score + 6 + 1
            elif round[1] == 'Y':
                score = score + 0 + 2
            elif round[1] == 'Z':
                score = score + 3 + 3
    print(score)
    

def problem_2(lines):
    pattern = parse.compile("{opponent} {player}")
    rounds = list()
    for line in lines:
        match = pattern.search(line)
        rounds.append((match.named.get("opponent"), match.named.get("player")))
    score = 0
    for round in rounds:
        if round[0] == 'A':
            if round[1] == 'X':
                score = score + 0 + 3
            elif round[1] == 'Y':
                score = score + 3 + 1
            elif round[1] == 'Z':
                score = score + 6 + 2
        elif round[0] == 'B':
            if round[1] == 'X':
                score = score + 0 + 1
            elif round[1] == 'Y':
                score = score + 3 + 2
            elif round[1] == 'Z':
                score = score + 6 + 3
        elif round[0] == 'C':
            if round[1] == 'X':
                score = score + 0 + 2
            elif round[1] == 'Y':
                score = score + 3 + 3
            elif round[1] == 'Z':
                score = score + 6 + 1
    print(score)


if __name__ == "__main__":
    path:str = os.path.dirname(os.path.abspath(__file__))
    fileName:str = 'input/dec-2.txt'
    filePath:str = os.path.join(path, fileName)
    lines: List[str] = read_file(filePath)

    problem_1(lines)
    problem_2(lines)