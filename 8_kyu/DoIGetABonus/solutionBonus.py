def bonus_time(salary, bonus):
    if bonus:
        salary = salary*10
    return "$"+str(salary)
    #your code here

if __name__ == '__main__':
    x = bonus_time(25000, True)
    print(x)