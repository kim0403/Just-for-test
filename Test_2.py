# BMR
weight = float(input("输入体重（公斤）"))
height = float(input("输入身高（公分）"))
age = float(input("输入年龄"))
gender = input("性别")
if gender == "男":
    BMR = (13.7 * weight) + (5.0 * height) - (6.8 * age) + 66
else:
    BMR = (9.6 * weight) + (1.8 * height) - (4.7 * age) + 65
print(BMR)
