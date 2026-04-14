palabra = "Python"
lista = []

for letra in palabra:
    lista.append(letra)
print(lista)    

# o tenemos una forma mas corta de escribirlo, con comprension de listas    

palabra = "Python"
lista = [letra for letra in palabra]    
print(lista)
# o tambien podemos hacer operaciones con las letras, por ejemplo convertirlas a mayusculas 
palabra = "Python"
lista = [letra.upper() for letra in palabra]    
print(lista)
# o tambien podemos hacer operaciones con las letras, por ejemplo convertirlas a mayusculas y agregar un guion entre cada letra
palabra = "Python"
lista = [letra.upper() + "-" for letra in palabra]
print(lista)


lista = [ n for n in range (0,21,2)]
print(lista)

lista = [ n*2 for n in range (0,21,2)]
print(lista)

lista = [ n if n*2 > 10 else "No" for n in range (0,21,2)]
print(lista)

pies = [10, 20, 30, 40, 50]
metros = [pie * 0.3048 for pie in pies]
print(metros)