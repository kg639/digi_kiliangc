list_num = [2, 7, 4, 5, 1, 8, 3, 9, 6, 10]
max = None
min = None
for i, num in enumerate(list_num):
    if i == 0:
        min = num
        max = num
    elif num < min:
        min=num
    elif num > max:
        max=num
print(f"maximo: {max}, mínimo: {min}")