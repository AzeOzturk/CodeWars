def array_diff(a,b):
    for i in b:
        while i in a:
            try:
                a.remove(i)
            except ValueError:
                return []
    return a
print(array_diff([1,2],[1]))