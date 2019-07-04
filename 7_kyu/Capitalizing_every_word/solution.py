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
    quote = "How can mirrors be real if our eyes aren't real"
    text = toJadenCase(quote)
    print(text)
