def camel_case(string):
    l = []
    for i in string.title():
        l.append(i)
        if i == ' ':
            l.remove(i)
    return ''.join(l)
