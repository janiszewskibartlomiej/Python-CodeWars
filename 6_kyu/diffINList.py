# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
# 1-n = [1,2,3,4,5,...,10]
# np. n=10
# wejście: [2,3,7,4,9], 10
# wyjście: [1,5,6,8,10]

def diff_in_list(list, i):
    # lista = []
    # print(lista)
    # generator = [x for x in range(1,i+1)]
    # print(generator)
    # print(len(generator))

    lista1 = [x for x in range(1,i+1) if x not in list]

    # for x  in range(0,len(generator)):
    #     el = generator[x]
    #     print(el)
    #     if el not in list:
    #         lista.append(el)


    return lista1


test = diff_in_list([2,3,7,4,9], 10)
print(test)
