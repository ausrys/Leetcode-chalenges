from typing import List


def cal_points(operations: List[str]) -> int:
    opers = {"C", "D", "+"}
    points = []
    for op in operations:
        if op not in opers:
            points.append(int(op))
        elif op == "C":
            points.pop()
        elif op == "D":
            points.append(2*points[-1])
        elif op == "+":
            points.append(points[-1] + points[-2])
    return sum(points)


print(cal_points(["5", "2", "C", "D", "+"]))
