fecha = input('Introduce la fecha de tu nacimiento en formato dd/mm/aaaa:')
dia = fecha[:fecha.find('/')]
mesaño = fecha[fecha.find('/')+1:]
mes = mesaño[:mesaño.find('/')]
año = mesaño[mesaño.find('/')+1:]
print('Día', fecha[:2])
print('Mes', fecha[3:5])
print('Año', fecha[6:])
