def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    if 5 <= upSpeed <= 100:
        height += upSpeed
    if 2 <= downSpeed < upSpeed:
        height -= downSpeed
    if 4 <= desiredHeight <= 1000:
         suma = desiredHeight / height
    if desiredHeight <= upSpeed:
        suma = 1
    return int(suma), height, suma

if __name__ == '__main__':
    x = growing_plant(100,10,910)
    y = growing_plant(10,9,4)
    z = growing_plant(5,2,0)
    w = growing_plant(5,2,5)
    wz = growing_plant(55,32,72)
    print(x)
    print("-------------------")
    print(y)
    print("-----------")
    print(z)
    print("==============")
    print(w)
    print("=================")
    print(wz)