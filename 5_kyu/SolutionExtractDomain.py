def domain_name(url):
    if '/' in url:
        splitUrl = url.split('/')
        stripL = splitUrl[2].lstrip('www.')
        resolutionL = stripL.split('.')
        resolution = resolutionL[0]
    else:
        splitUrl = url.split('.')
        resolution = splitUrl[1]

    return resolution




if __name__ == '__main__':

    test = "http://github.com/carbonfive/raygun"
    test2 = "http://www.zombie-bites.com"
    t1 = test.split('/')
    t11 = t1[2].lstrip('www.')
    t111 = t11.rstrip('.com')

    t2 = test2.split('/')
    t22 = t2[2].lstrip('www.')
    t222 = t22.split('.')
    t2222 = t222[0]
    print(t1)
    print(t2)
    print(t22)
    print(t222)
    print(t2222)

    x = domain_name("www.xakep.ru")
    print(x)