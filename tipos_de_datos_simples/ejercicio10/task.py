payasos = int(input("Introduce el número de payasos a enviar:"))
muñecas = int(input("Introduce el número de muñecas a enviar:"))
pesoTotalPayasos = payasos * 112
pesoTotalMuñecas = muñecas * 75
resultado = pesoTotalMuñecas + pesoTotalPayasos
print("El peso total del paquete es "+str(resultado))