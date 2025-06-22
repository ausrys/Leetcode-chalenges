from typing import List


def dest_city(paths: List[List[str]]) -> str:
    pset: set[str] = set()
    for d in paths:
        pset.add(d[0])
    for d in paths:
        if d[1] not in pset:
            return d[1]
    return paths[-1][-1]
