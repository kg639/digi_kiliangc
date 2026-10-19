text =  "Hello World"
text2 = "Hola mon!!!" 
lista = []
for i, letra in enumerate(text):
    if letra == text2[i]:
        lista.append(letra)

print(f"Las palabras {text} y {text2} contienen {len(lista)} letras iguales, {lista}")