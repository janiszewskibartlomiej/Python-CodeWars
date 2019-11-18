def filter_list(l):
    x = [x for x in l if type(x) == type(1)]
    print(x)
    return x

filter_list([1,2,'a','b',123])

def filter_1(l):
    x = [x for x in l if isinstance(x, int)]
    print(x)
    return x

filter_1([1,2,'aasf','1','123',123])

def filter_2(l):
    x = list(filter(lambda x: isinstance(x, int),l))
    print(x)
    return x

filter_2([1,2,'a','b',3232])
