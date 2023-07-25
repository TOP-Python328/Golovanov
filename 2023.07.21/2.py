ranges = int(input("введи кол-во вводимых цифр: "))
plus = 0

for i in range(ranges):
    num = int(input("введите любое число отрицательное или положительное: "))
    if num > 0:
        plus += num

print(plus)