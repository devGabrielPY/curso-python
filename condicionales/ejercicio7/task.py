bonificacion = 2400
inaceptable = 0.0
aceptable = 0.4
meritorio = 0.6
puntos = float(input("Introduce tu puntuación:"))
if puntos == inaceptable:
    nivel = "inaceptable"
elif puntos == aceptable:
    nivel = "aceptable"
elif puntos == meritorio:
    nivel = "meritorio"
else:
    nivel = ""

if nivel == "":
    print("Esta puntuación no es válida")
else:
    print("Tu nivel de rendimiento es",  nivel)
    print("Te corresponde cobrar", str((puntos * bonificacion)), "colones")
