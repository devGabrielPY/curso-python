def factorial(n):
    """Función que calcula el factorial de un número entero positivo.
    Parámetros
    n: Es un entero positivo.
    Devuelve el factorial de n.
    """
    # TODO

    resultado = 1
    for i in range(int(n)):
        resultado *= i + 1
        #print(resultado)
    return resultado

print(factorial(4))