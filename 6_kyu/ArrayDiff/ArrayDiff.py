def array_diff(a, b):
    # nowe =[]
    # for i in a:
    #     if i not in b:
    #         nowe.append(i)
    # return nowe

    new_array = [x for x in a if x not in b]
    return new_array


x = array_diff([1, 2], [1])
print(x)
