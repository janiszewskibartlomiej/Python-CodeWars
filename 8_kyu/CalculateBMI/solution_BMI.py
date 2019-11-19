def bmi(weight, height):
    bmi_ex = weight / (height ** 2)
    info = ["Underweight", "Normal", "Overweight", "Obese"]
    if 0 < bmi_ex <= 18.5:
        info = info[0]
    elif 18.5 < bmi_ex <= 25.0:
        info = info[1]
    elif 25.0 < bmi_ex <= 30.0:
        info = info[2]
    elif bmi_ex > 30.0:
        info = info[3]
    return info

if __name__ == '__main__':
    x = bmi(50, 1.80)
    print(x)
