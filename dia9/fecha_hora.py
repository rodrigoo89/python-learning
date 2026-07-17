from datetime import datetime

nacimientoLauti = datetime(2023, 5, 2, 10, 45)  # Año, Mes, Día, Hora, Minuto
actual = datetime.now()

diasentoral = actual - nacimientoLauti
print("Tiempo transcurrido desde el nacimiento de Lauti hasta ahora:", diasentoral)




hora_actual= datetime.now()
minutos= hora_actual.minute
print(minutos)

