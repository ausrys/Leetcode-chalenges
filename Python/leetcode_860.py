from typing import List


def lemonade_change(bills: List[int]) -> bool:
    c = {5: 0, 10: 0, 20: 0}
    for bill in bills:
        if bill == 5:
            c[bill] += 1
        elif bill == 10:
            c[bill] += 1
            c[5] -= 1
        else:
            if c[10] >= 1 and c[5] >= 1:
                c[10] -= 1
                c[5] -= 1
            else:
                c[5] -= 3
        if c[5] < 0:
            return False

    return True
