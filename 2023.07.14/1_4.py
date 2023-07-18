a1 = input("введи по горизонтали клетку латинскими буквами от ‘a’ до ‘h’: ")
a2 = int(input("вертикали клетка кодируется цифрами от 1 до 8: "))
b1 = input("введи по горизонтали клетку латинскими буквами от ‘a’ до ‘h’: ")
b2 = int(input("вертикали клетка кодируется цифрами от 1 до 8: "))

trans_table = str.maketrans({'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8'})
repA = int(a1.translate(trans_table))
repB = int(b1.translate(trans_table))

if (repA + a2 + repB + b2) % 2 == 0:
    print('да')
else:
    print('нет')