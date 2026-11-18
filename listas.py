lista=[4,5,77]
print(lista[1])
for i in range(len(lista)):
    print(f"Posicion: {i}, elemento: {lista[i]}")

lista.append(11)
lista.insert(1, 900)
del lista[2]
lista[0]=32
print(lista)
