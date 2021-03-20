def add_binary(a,b):
    if a == b:
        l = int(a)
        if a != 1:
            a = 1
        k = '%s' % a
        plass = k.ljust(l + len(k), '0')
        plass1 = '%s'%plass
        return plass1

        pass
    else:
        a1 = bin(a)
        b1 = bin(b)
        l1 = []
        l2 = []
        for i in a1:
            l1.append(i)
        for j in b1:
            l2.append(j)
        del l2[:2]
        del l1[:2]
        str = ''
        s1 = str.join(l1)
        s2 = str.join(l2)
        innt1 = int(s1)
        innt2 = int(s2)
        plas = innt2 + innt1
        plass = '% s' % plas
        return  plass
print(add_binary(1,1))