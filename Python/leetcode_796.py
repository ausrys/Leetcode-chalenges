def rotate_string(s: str, goal: str) -> bool:
    new_s = s
    for i in s:
        new_s = new_s[1:] + i
        if new_s == goal:
            return True
    return False


print(rotate_string("a", "a"))
