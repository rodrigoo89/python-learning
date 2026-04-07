mi_bool = 4< 5 < 6
print(mi_bool)  # Esto imprimirá True, ya que 4 es menor que 5 y 5 es menor que 6


mi_bool = 4 < 5 > 6 
print(mi_bool)  # Esto imprimirá False, ya que 5 no es mayor que 6  

mi_bool = 4 < 5 and 5 > 6
print(mi_bool)  # Esto imprimirá False, ya que 5 no es mayor que 6

mi_bool = 4 < 5 or 5 > 6
print(mi_bool)  # Esto imprimirá True, ya que 4 es menor que 5, aunque 5 no es mayor que 6, el operador OR solo requiere que una de las condiciones sea verdadera para que el resultado sea verdadero.

texto = "esta frase es breve"
mi_bool = "breve" in texto or "frase" in texto
print(mi_bool) # Esto imprimirá True, ya que la palabra "breve" está presente en el texto, aunque la palabra "frase" también está presente, el operador OR solo requiere que una de las condiciones sea verdadera para que el resultado sea verdadero.

mi_bool = not ("a" == "a")
print(mi_bool)  # Esto imprimirá False, ya que "a" es igual a "a", por lo tanto la expresión dentro del paréntesis es verdadera, y el operador NOT invierte ese valor a falso.

mi_bool = not ("a" != "a")
print(mi_bool)  # Esto imprimirá True, ya que "a" no es diferente de "a", por lo tanto la expresión dentro del paréntesis es falsa, y el operador NOT invierte ese valor a verdadero.