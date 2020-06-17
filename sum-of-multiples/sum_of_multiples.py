def sum_of_multiples(n, numeros=[3, 5]):
    resultado = 0
    for i in range(1, n):
        for f in numeros:
            if f != 0 and i % f == 0:
                resultado += i
                break

    return resultado
