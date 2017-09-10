def find_diff(a, b):
    x = list(set(a) ^ set(b))
    return x[0]
