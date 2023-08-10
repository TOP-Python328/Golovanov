num = int(input("введи натуральное число: "))

# ПЕРЕИМЕНОВАТЬ: div вводит в заблуждение относительно значения, ассоциированного с данным именем, здесь подойдёт что-нибудь вроде num_divs_sum
div = 0
# ПЕРЕИМЕНОВАТЬ: имена переменных i, j, k традиционно используются только для индексов, а здесь вы перебираете делители — всегда предпочтительнее называть вещи своими именами: делитель — divisor, div
# ИСПРАВИТЬ: единица и само число всегда являются делителями, для них не нужно выполнять все проверки ниже — оптимизируйте
# ИСПРАВИТЬ: подумайте о том, при каких значениях делителя остаток от деления никогда не будет равным нулю — это лишние итерации, от которых надо избавиться
for i in range(1, num+1):
    if num % i == 0:
        div += i

print(div)


# ДОБАВИТЬ: результат выполнения программы с собственными данными


# ИТОГ: нужно лучше, доработать — 3/6
