# ИСПРАВИТЬ: вам не нужен объект str, возвращаемый функцией input(): вместо того, чтобы сохранять его в переменную num, следует возвращаемое значение input() сразу преобразовать в объект int и уже этот объект сохранить в num — тогда бы и не пришлось ниже несколько раз повторять одинаковое действие — преобразование в int одного и того же объекта
num = input("введи число:")
# ИСПРАВИТЬ: вывод не соответствует требуемому формату (см. тест)
print(f"Следующее за числом {num} число: {int(num)+1} \n Для числа {num} предыдущее число: {int(num)-1}")


# введи число:35
# Следующее за числом 35 число: 36
# КОММЕНТАРИЙ: в случае если вы будете генерировать строку не для чтения человеком, а для другой функции/класса/программы — лишний пробел может стоить вам неработающего приложения
#  Для числа 35 предыдущее число: 34

# ДОБАВИТЬ: результат выполнения программы с собственными данными


# ИТОГ: немного доработать — 2/4
