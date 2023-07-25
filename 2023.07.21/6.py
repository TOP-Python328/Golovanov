ticket = input("введи номер билета из 6 цифр: ")
first = list(map(int, ticket[:3]))
end = list(map(int, ticket[3:]))
    
if sum(first) == sum(end):
    print("да")
else:
    print("нет")