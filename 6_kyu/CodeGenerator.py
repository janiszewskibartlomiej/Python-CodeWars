# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi

def code_generator(start, stop):
    start =int(start.replace("-", ""))
    stop = int(stop.replace("-", ""))
    codeList = ["%02d-%03d" % divmod(x, 1000) for x in range(start+1,stop)]
    return codeList
    
if __name__ == '__main__':
    test =code_generator("83-300", "84-330")
    print(test)
