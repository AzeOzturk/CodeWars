def generate_hashtag(s):

    if s == "":
        return False
    elif len(s)>140:
        return False
    else:
        k = s.title()
        l = []
        for i in k:
            l.append(i)
            if i == ' ':
                l.remove(i)
        z = ''.join(l)
        return '#' + z