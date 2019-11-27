def growing_plant(upSpeed, downSpeed, desiredHeight):
    height = 0
    if 5 <= upSpeed <= 100:
        height -= downSpeed
    if 2 <= downSpeed < upSpeed:
        height += upSpeed
    if 4 <= desiredHeight <= 1000:
         suma = height / desiredHeight
    return round(suma)


x = growing_plant(100,10,910)
print(x)