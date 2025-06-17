def judge_circle(moves: str) -> bool:
    horizont = 0
    vertical = 0
    for move in moves:
        if move == "U":
            vertical += 1
        elif move == "D":
            vertical -= 1
        elif move == "L":
            horizont -= 1
        else:
            horizont += 1
    return horizont == 0 and vertical == 0
