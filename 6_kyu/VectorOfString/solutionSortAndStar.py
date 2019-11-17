def two_sort(array):
    x = [x[0] for x in sorted(array)]
    print(x)
    for el in x:
        many = x.count(el)
        if many > 1:
            print(x.count(el), "litera:", el)
            # c x[el]
            for i in range(many):
                x.remove(el)
            # print(x.count(el), "litera:", el)
    #print(len(x))
    print(x)
    nowalista = []
    for i in range(len(x)-1):
        nowalista.append(x[i]+'***')
    nowalista.append(x[-1])
    fullStr = ''.join(nowalista)
    print(fullStr)
    return fullStr

    #print(x)
    #print(nowalista)
    # result = print(*x, sep="***")
    # print(type(result))
    # return result


test = two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"])

# test2 = two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"])
