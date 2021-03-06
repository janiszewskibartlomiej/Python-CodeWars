# ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.


def list_decimal(start=2, stop=5.5, step=0.5):
    start = int(start / step)
    stop = int(stop / step)
    solution_list = [round((x * step), 2) for x in range(start, stop)]
    return solution_list


if __name__ == '__main__':
    test = list_decimal()
    print(test)

    test2 = list_decimal(1, 10, 0.1)
    print(test2)
