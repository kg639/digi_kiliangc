lista=["primero", "medio", "ultimo"]
for i in range(len(lista)):
    if i == 0 or i == len(lista)-1:
        print(lista[i])