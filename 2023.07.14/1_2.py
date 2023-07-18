num1 = int(input("введи первое число: "))
num2 = int(input("введи второе число: "))
if num1%num2==0:
   print(f"{num1} делится на {num2} нацело \n частное:{int(num1/num2)}")
else: print(f"{num1} не делится на {num2} нацело \n неполное частное: {int(num1/num2)} \n остаток: {num1%num2}")