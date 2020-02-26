# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n. NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
# 1-n = [1,2,3,4,5,...,10]
# np. n=10
# wejście: [2,3,7,4,9], 10
# wyjście: [1,5,6,8,10]

def diff_in_list(list, i):
    solution_list = [x for x in range(1, i + 1) if x not in list]
    return solution_list


if __name__ == '__main__':
    test = diff_in_list([2, 3, 7, 4, 9], 10)
    print(test)
