def to_goat_latin(sentence: str) -> str:
    vovels = {'a', 'e', 'i', 'o', 'u'}
    repeat = 1
    f_list = []
    s = sentence.split()
    for w in s:
        if w[0].lower() in vovels:
            w = w + 'ma' + 'a' * repeat
            repeat += 1
            f_list.append(w)
        else:
            w = w[1:] + w[0] + 'ma' + 'a' * repeat
            repeat += 1
            f_list.append(w)
    return " ".join(f_list)


print(to_goat_latin("I speak Goat Latin"))
