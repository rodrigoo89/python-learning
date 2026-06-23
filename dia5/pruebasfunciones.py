def multiplicar(nu1,num2):
    return nu1*num2
resultado = multiplicar(5,6)
print(resultado)    


def potencia(num1, num2):
    return num1 ** num2

resolver = potencia(3,4)
print(resolver)



def usd_a_eur(num1):
    return num1 * 0.9

dolares = 1
resultado = usd_a_eur(dolares)
print(resultado)

def invertir_palabra(palabra):
    return palabra[::-1].upper()

palabra = "Python"
print(invertir_palabra(palabra))  # imprime: NOHTYP