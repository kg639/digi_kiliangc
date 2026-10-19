textdna = "atggatcattta"
contador=0
for i, letra in enumerate(textdna):
    if letra == "a":
        contador +=1
print(f"La cadena {textdna} contiene {contador} 'a'")