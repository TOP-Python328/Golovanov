num = input("введи трехзначное число: ")
num1 = int(num)//100
num2 = int(num)//10%10
num3 = int(num)%10
print(f"cумма цифр = {num1+num2+num3} \n Произведение цифр = {num1*num2*num3}")