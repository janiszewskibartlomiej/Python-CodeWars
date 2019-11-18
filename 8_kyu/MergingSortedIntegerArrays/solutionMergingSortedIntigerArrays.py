def merge_arrays(first, second):
    x = set(first + second)
    x = list(x)
    return sorted(x)