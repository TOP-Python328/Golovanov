num = int(input("введи натуральное число: "))
div = 0

for i in range(1, num+1):
    if num % i == 0:
        div += i

print(div)