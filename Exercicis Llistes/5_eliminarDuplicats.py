list_num = [2, 7, 4, 2, 1, 6, 3, 7, 6, 10]
lista = []
for num in list_num:
    if num not in lista:
        lista.append(num)
print(lista)