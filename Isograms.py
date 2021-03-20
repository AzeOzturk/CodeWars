def is_isogram(string):
    if type(string) is not str:
        return False
    if len(string) == 0:
        return True

    a = []
    for i in string.lower():
        if i in a:
            return False
        else:
            a.append(i)

    return True