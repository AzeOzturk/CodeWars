def duplicate_count(text):
    s = set()
    for i in text.lower():
        if text.lower().count(i) > 1:
            s.add(i)
    return len(s)