def toJadenCase(string):
    string = string.split()
    print(string)
    string_list = []
    for i in string:
        i = i.replace(i[0], i[0].upper())
        i = i.replace(i[1:], i[1:].lower())
        string_list.append(i)
    xx = ''
    for word in string_list:
        xx += word + ' '
    return xx.strip()

if __name__ == '__main__':
    text = toJadenCase(Not_Jaden_Cased)
    print(text)
