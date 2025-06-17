def defang_ip_addr(address: str) -> str:
    result = ""
    for c in address:
        if c == ".":
            result += "[.]"
        else:
            result += c
    return result
