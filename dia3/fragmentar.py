texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

fragmento = texto[2:5]# Devuelve el fragmento de texto desde la posición 2 hasta la posición 4 (excluyendo la posición 5)
fragmento = texto[2:5:3]# Devuelve el fragmento de texto desde la posición 2 hasta la posición 4 (excluyendo la posición 5) con un paso de 3    
fragmento = texto[::3] # Devuelve el fragmento de texto completo con un paso de 3 (es decir, cada tercer carácter del texto)    
print(fragmento)    