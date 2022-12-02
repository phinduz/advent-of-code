import os
from typing import List

def read_file(filePath) -> List[str]:
    """ Returns all the lines from a file as a list """
    with open(filePath, 'r') as file:    
        lines: List[str] = file.read().strip().split('\n')
        file.close()
    return lines

def problem_1(lines):
    calories: int = 0
    max_calories: int = 0
    for line in lines:
        #print(max_calories)
        if len(line) == 0:
            if calories > max_calories:
                max_calories = calories
            calories = 0
        else:
            calories = calories + int(line)
    if calories > max_calories:
                max_calories = calories
    print(max_calories)

def problem_2(lines):
    calories: int = 0
    max_calories: List[int] = [0, 0, 0]
    for line in lines:
        #print(max_calories)
        if len(line) == 0:
            if calories > min(max_calories):
                max_calories[max_calories.index(min(max_calories))] = calories
            calories = 0
        else:
            calories = calories + int(line)
    if calories > min(max_calories):
        max_calories[max_calories.index(min(max_calories))] = calories
    print(sum(max_calories))

if __name__ == "__main__":
    path:str = os.path.dirname(os.path.abspath(__file__))
    fileName:str = 'input/dec-1.txt'
    filePath:str = os.path.join(path, fileName)
    lines: List[str] = read_file(filePath)

    problem_1(lines)
    problem_2(lines)