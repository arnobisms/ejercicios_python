def factors(valor):

    factores = []
    i = 2

    while valor > 1:

        if valor % i == 0:
            factores.append(i)
            valor /= i
        else:
            i += 1

    return factores
