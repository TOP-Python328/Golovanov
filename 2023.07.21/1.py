num = int(input("введи любое число: "))
numRev = []
while num%7==0: 
    numRev.append(num) 
    num = int(input("Введите число: "))
else: 
    numRev.reverse()
    print(numRev)